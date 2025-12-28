import requests
from bs4 import BeautifulSoup
from sys import argv, exit
from urllib.parse import urlparse
import time 
import random

#TODO: implementera json lagring
            
usage = "="*40+"\nUsage: python3 <script path> <url>\n"+"="*40
try: url_inp = argv[1] 
except IndexError: print(usage); exit(2)

agent = "MyWebScraper1.0 (learning project using python; non-commerical use)"

def soup(url: str): #TODO: hantera error http error codes som 429 403
    headers = {"User-Agent": agent}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def delay_timer(): 
    return random.randint(3,5)

def robots(url: str):
    time.sleep(delay_timer())
    robot_content = soup(url_inp).get_text
    #TODO: kolla efter #strings som säger vad som tillåts resp. inte


def main():
    html = soup(url_inp)
    #TODO: ta fram en massa tags

    
    

if __name__ == "__main__":
    main()