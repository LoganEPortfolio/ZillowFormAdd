import os
from bs4 import BeautifulSoup
from pprint import pprint
import requests

class ZillowScrape():
    def __init__(self):
        self.zillow_response = requests.get(url=os.environ.get("ZILLOW_CLONE_LINK"))
        self.zillow_response_text = self.zillow_response.text

        self.soup = BeautifulSoup(self.zillow_response_text, "html.parser")

    
    def get_links(self):
        list_of_links = self.soup.select('.property-card-link')
        links = [href.get('href') for href in list_of_links]
        
        pprint(links)
        return links

    def get_prices(self):
        list_of_prices = self.soup.select('.PropertyCardWrapper__StyledPriceLine')
        prices = [int(price.getText().split('/')[0].split('+')[0].split('$')[1].replace(",", "").replace('+', "")) for price in list_of_prices]
        pprint(prices)
        return prices

    def get_address(self):
        list_of_addresses = self.soup.select('address')
        addresses = [address.getText().replace('\n', "").strip() for address in list_of_addresses]
        pprint(addresses)
        return addresses

    def build_data(self):
        links = self.get_links()
        prices = self.get_prices()
        addresses = self.get_address()

        data = {}

        for _ in range(len(links)):
            data[_] = {
                "Link": links[_],
                "Price": prices[_],
                'Address': addresses[_]
            }
        
        pprint(data)
        return data


zillow = ZillowScrape()


zillow.build_data()