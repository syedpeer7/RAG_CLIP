import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
    image_urls = [urljoin(url, img['src']) for img in soup.find_all('img') if 'src' in img.attrs]

    return text_content, image_urls
