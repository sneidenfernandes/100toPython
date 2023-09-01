import requests
import time
from bs4 import BeautifulSoup as bs
import notify2


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

    return btc_price


def notification():

    # Specifying icon image path
    icon_path = 'btc_image.avif'

    # Getting the price of bitcoin using the predefined function 
    btc_price = get_btc_price()

    # Initiaing the d-bus connection
    notify2.init('Bitcoin Price')

    # Create Notification Object

    n = notify2.Notification(None, icon=icon_path)

    # Set Urgency Level

    n.set_urgency(notify2.URGENCY_NORMAL)

    # set timeout for a notification

    n.set_timeout(10000)


    n.update(btc_price)


    # Show notification on desktop
    n.show()

    # Short Delay between notifications
    time.sleep(15)




if __name__ == '__main__':

    notification()





