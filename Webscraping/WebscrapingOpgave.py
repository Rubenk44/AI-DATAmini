from urllib.request import urlopen
import re
def webscraper(page):
    page = urlopen(page)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def findtitle(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    print(title)

def main():
    url = input('Indsæt Url:') 
    html = webscraper(url)
    print(html)
    title_index = html.find("<title>")
    print(title_index)
    findtitle(url)
    
    
if __name__ == "__main__":
    main()
    
