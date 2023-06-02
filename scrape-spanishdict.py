from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, parse_qs
import pyperclip
import sys

with sync_playwright() as playwright:
        #launch(headless=False) for visualization (ie opens Chromium)
        browser = playwright.chromium.launch()
        context = browser.new_context()

        page = browser.new_page()

        # TODO: Get teh URL from the GUI
        # Check if the URL argument is provided
        if len(sys.argv) < 2:
                print("Please provide the URL as an argument.")
                sys.exit(1)

        # Get the URL from the command-line argument
        spanishdict_url = sys.argv[1]

        page.goto(spanishdict_url)

        data = page.evaluate('() => window.SD_COMPONENT_DATA.translations')

        translations = []

        for item in data:
                # Get the value of the 'text' parameter from URL 
                text_param = parse_qs(urlparse(item['headwordAudioUrl']).query).get('text')

                # Format the word-translation pairing
                if text_param:
                        formatted_translation = item['translation']
                        if item['contextEn']:
                                formatted_translation += f" ({item['contextEn']})"
                        formatted_translation += f"\t{text_param[0].replace('-', ' ')}"

                        # Add to the translations list
                        translations.append(formatted_translation)


        # Join the translations with a semicolon
        formatted_output = '\n'.join(translations)

        pyperclip.copy(formatted_output)

        # Name of file will be the Name of the List in Spanish Dict
        file_name = spanishdict_url.split("/")[-1].replace("-", " ")

        # TODO: Export CSV file instead of text file
        # Save the translations to a file
        with open(file_name+'.txt', 'w') as file:
                file.write(formatted_output)

        browser.close()
