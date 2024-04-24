from urllib.request import urlopen

def webscraper(page):
    page = urlopen(page)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def main():
    url = input('Indsæt Url:') 
    html = webscraper(url)
    print(html)
    title_index = html.find("<title>")
    print(title_index)
    
if __name__ == "__main__":
    main()
    
