from urllib.parse import urlparse, parse_qs
import pyperclip
import sys
import requests
import re
import json
from bs4 import BeautifulSoup

# EXAMPLE URL: 'https://www.spanishdict.com/lists/5980437/mayo-2023'

# TODO: Get the URL from the GUI
# Check if the URL argument is provided
if len(sys.argv) < 2:
        print("Please provide the URL as an argument.")
        sys.exit(1)

# Get the URL from the command-line argument
spanishdict_url = sys.argv[1]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

response = requests.get(spanishdict_url, headers=headers)
html_data = response.content

soup = BeautifulSoup(html_data, 'html.parser')

script_tags = soup.findAll('script')
#vocab_translations_tag = None

for tag in script_tags:
    if tag.string and 'vocabTranslations' in tag.string:
        vocab_translations_tag = tag
        break

if vocab_translations_tag:        
        window_script = vocab_translations_tag.string
        
#        data_dict = json.loads(vocab_translations_tag.string)
        
        # Find the index of the first occurrence of "w"
        # Remove everything before the first "w" (inclusive)
        trimmed_string = window_script[window_script.index("{"):]        

        #TODO: Find a better way to remove the trailing semicolon
        data_dict = json.loads(trimmed_string[:-14])['translations']

        translations = []

        for item in data_dict:
                # Get the value of the 'text' parameter from URL 
                text_param = item['headwordAudioUrl']

                # Format the word-translation pairing
                if text_param:
                        formatted_translation = item['translation']
                        if item['contextEn']:
                                formatted_translation += f" ({item['contextEn']})"

                        # Parse the URL, Extract the value of the "text" attribute, and Remove dashes from the text value
                        text_value = parse_qs(urlparse(text_param).query).get("text", [""])[0].replace("-", " ")
                        formatted_translation += f"\t{text_value}"

                        # Add to the translations list
                        translations.append(formatted_translation)


        # Join the translations with a tab
        formatted_output = '\n'.join(translations)

        pyperclip.copy(formatted_output)

        # Name of file will be the Name of the List in Spanish Dict
        file_name = spanishdict_url.split("/")[-1].replace("-", " ")

        # TODO: Export CSV file instead of text file
        # Save the translations to a file
        with open(file_name+'.txt', 'w') as file:
                file.write(formatted_output)