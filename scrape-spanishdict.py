from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, parse_qs
from plyer import notification
import pyperclip
import sys

class Play:
        def do_everything(self):
                with sync_playwright() as playwright:
                        browser = playwright.chromium.launch(headless=False)
                        context = browser.new_context()

                        page = browser.new_page()

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
                                word_en = item['translation']
                                context_en = item['contextEn']
                                headwordAudioUrl = item['headwordAudioUrl']

                                # Parse the URL
                                parsed_url = urlparse(headwordAudioUrl)

                                # Get the value of the 'text' parameter
                                text_param = parse_qs(parsed_url.query).get('text')

                                if text_param:
                                        # Extract the text value
                                        word_es = text_param[0]

                                        # Replace dashes with spaces
                                        word_es = word_es.replace('-', ' ')

                                        # Format the translation
                                        formatted_translation = word_en
                                        context_en = context_en.replace(',', ' or')
                                        if context_en:
                                                formatted_translation += f" ({context_en})"
                                        formatted_translation += f",{word_es}"

                                        # Add to the translations list
                                        translations.append(formatted_translation)


                        # Join the translations with a semicolon
                        formatted_output = ';'.join(translations)

                        print(formatted_output)

                        pyperclip.copy(formatted_output)
                        self.show_notficiation("Success", "Text for Quizlet from SpanishDict successfully copied to clipboard.")

                        # Name of file will be the Name of the List in Spanish Dict
                        last_part = spanishdict_url.split("/")[-1]
                        file_name = last_part.replace("-", " ")

                        # Save the translations to a file
                        with open(file_name+'.txt', 'w') as file:
                                file.write(formatted_output)
                        browser.close()

        def show_notification(self, title, message):
                notification.notify(
                title=title,
                message=message,
                timeout=15  # Duration in seconds before the notification automatically closes
                )

interesting = Play()
interesting.do_everything()