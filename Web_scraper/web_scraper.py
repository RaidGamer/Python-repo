import requests
from bs4 import BeautifulSoup
from sys import argv, exit
from urllib.parse import urlparse

try: url_inp = argv[1] 
except IndexError: print("="*40+"\nUsage: python3 <script path> <url> <scrape type>\nScrape types:\n'-a' => all\n"+"="*40); exit(2)
try: filter_inp = argv[2]
except IndexError: print("="*40+"\nUsage: python3 <script path> <url> <scrape type>\nScrape types:\n'-a' => all\n"+"="*40); exit(2)
# rest_inp = argv[3:]

def soup(url: str): #gives soup object (html and css) to scrape info from
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

def scrape(type: str):
    scraped = soup(url_inp) 
    match type:
        case e if e=="-a": 
            return scraped.prettify()




def main():
    if check_robots().__contains__(url_inp):
        print("Given url is not accessible for scraping according to robots.txt")
    else:
        #TODO: scrape my ass
        result = scrape(filter_inp)
        print(result)
    

if __name__ == "__main__": 
    main()

