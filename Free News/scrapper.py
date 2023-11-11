import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y')


def get_news_link(url):
   
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', id='footable_35632')
    table = table.find_all('td')
    table = [x.text for x in table]



    link = None
    if table[0] == str(today):
        link = table[1]

    return link






if __name__ == '__main__':
     
     businessStandard = 'https://www.careerswave.in/business-standard-newspaper-free-download/'

     path = '/Users/sneiden/github/100toPython/Free News/' + str(today) + '.pdf'

     
     link = get_news_link(businessStandard)

     print(link)

   