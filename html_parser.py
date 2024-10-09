import threading
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, html_contents):
        self.html_contents = html_contents


    def parse_html(self, html_content, results, index):
        soup = BeautifulSoup(html_content, 'html.parser')
        # extracting all the links 
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        results[index] = links

    # Function to parse HTML content using multiple threads
    def parse_all(self):
        threads = []
        results = [None] * len(self.html_contents)
        
        for i, content in enumerate(self.html_contents):
            thread = threading.Thread(target=self.parse_html, args=(content, results, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results
