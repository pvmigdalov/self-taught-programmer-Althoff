import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site


    def scrape(self, parser='html.parser', f_out='out.txt'):
        r = requests.get(self.site)
        html = r.text
        urls = []

        soup = BeautifulSoup(html, parser)
        for link in soup.find_all('a'):
            url = link.get('href')
            if url is None:
                continue
            if ('./topics' in url) or ('./articles' in url) or ('./publications' in url):
                urls.append(self.site + url[2:])

        with open(f_out, 'w') as f:
            for url in urls:
                f.write(url + '\n')
        
        print('Parsing is finished')
                



if __name__ == '__main__':
    news = 'https://news.google.ru/'
    scraper = Scraper(news)
    scraper.scrape()