<h1>SpanishDict to Quizlet Set Helper</h1>
Scrapes word,translation pairing from saved SpanishDict list<br>
Copies pairing to clipbord and .txt file to be used to import into Quizlet as a set of flashcards
<br><br>

<h2>Technologies Used</h2>
<strong>bs4 import BeautifulSoup</strong> - used to parse through HTML data from SpanishDict<br>
<strong>json</strong> - used to parse translations JSON data<br>
<strong>pyperclip</strong> - used to copy onto the clipboard<br>
<strong>requests</strong> - used to retrieve data from SpanishDict<br>
<strong>sys</strong> - used to retrieve URL from argument passed<br>
<strong>urllib.parse import urlparse, parse_qs</strong> - used to parse URL within JSON translation data
<br><br>

<h2>Future Plans</h2>
<ol>
<li>Improve method of removing trailing semicolon in order to create JSON</li>
<li>GUI to take in URl argument</li>
<li>Option in GUI to switch order of translation (ie Spanish > English, vs English > Spanish)</li>
<li>Option to name file</li>
</ol>
<br>

<h1>How to Install and Run the Project</h1>
See <em><strong>Technologies Used</strong></em> section for dependencies
<br><br><br>

<h1>How to Use <em>SpanishDict to Quizlet Set Helper</em></h1>
python scrape-spanishdict.py <em>URL-to-SpanishDict-List</em><br>
Example: python scrape-spanishdict.py https://www.spanishdict.com/lists/5980437/mayo-2023
<br><br>
<h2>In clipboard and text file</h2>
Word and translation separated by tab<br>
Pairings (of word and translation) separated by new line<br><br>

<a href="https://www.spanishdict.com/lists/5980437/mayo-2023">Example of SpanishDict URL to use as argument</a><br>
<a href="https://www.awesomescreenshot.com/image/40409517?key=e348f797b7cff82eb24fdc61c08d695b">Example of pasted data into Quizlet</a><br>
<br>
<em>Note: no username or authentication is required, but the SpanishDict list needs to be public.</em>