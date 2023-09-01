import requests
import time
from bs4 import BeautifulSoup as bs
from pync import Notifier

def get_btc_price():
    # Specify url
    URL = 'https://www.coindesk.com/price/bitcoin/'

    # Request
    response = requests.get(URL)

    # Obtaining HTML in text form 
    html = response.text

    # Initiating bs4 to parse through the text
    soup = bs(html,'lxml')


    # Getting the current price of btc according to coindesk
    btc_price = soup.find(class_='currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP').text

    time.sleep(2)

    return str(btc_price)


def notification():
    # Create a notification
    title = "Bitcoin Price"
    message = get_btc_price()
    icon_path = '/Users/sneiden/github/100toPython/Bitcoin Notification/btc.png'

    Notifier.notify(
        title=title,
        message= f"\n{message}",
        appIcon=icon_path,  
        timeout=10,                    
    )

    
   
if __name__ == '__main__':

    notification()





