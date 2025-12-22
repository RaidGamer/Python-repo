import requests
from bs4 import BeautifulSoup
from sys import argv
from urllib.parse import urlparse


url_inp = argv[1]
filter_inp = argv[2:]

def soup(url): #gives soup object (html and css) to scrape info from
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def check_robots():#satte in vilken web-url som helst, går tillbaka till root, kollar robots, och checkar url_inp
    parsed = urlparse(url_inp)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots = f"{base_url}/robots.txt"
    guidelines = soup(robots)
    list = guidelines.__str__().split("\n")
    #filter for dissallowed directories
    list_filtered = [x for x in list if x.__contains__("Disallow")]
    disallow_list = []
    for x in list_filtered:
        disallow_list.append(f"{base_url}/{x[11:]}")
    return disallow_list




def scrape():
    if check_robots().__contains__(url_inp):
        print("Given url is not accessible for scraping according to robots.txt")
    else:
        #TODO: scrape my ass
        print("")
    

if __name__ == "__main__": 
    scrape()

