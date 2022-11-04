from bs4 import BeautifulSoup
import requests


def parse(url: str):
    url = requests.get(URL)
    soup = BeautifulSoup(url.content, 'html.parser')
    div = soup.find_all('div', {'class': 'additional-details'})
    
    span = div[0].find_all('span')
    data = span[1].text, span[2].text, span[3].text, span[5].text
    
    with open('result.txt', 'w') as result:
        print(*map(str.strip, data), sep='\n', file=result)
        result.close()
        return True
        
  
if __name__ == "__main__":
    URL = 'https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE'
    parse(URL)

