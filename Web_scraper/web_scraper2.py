import requests
from bs4 import BeautifulSoup
from sys import argv, exit
from urllib.parse import urlparse
import urllib.robotparser
import time 
import random

#TODO: implementera json lagring
            
usage = "="*40+"\nUsage: python3 <script path> <url>\n"+"="*40
try: url_inp = argv[1] 
except IndexError: print(usage); exit(2)

agent = "MyWebScraper1.0 (learning project using python; non-commerical use)"

def robots(url: str, agent: str):
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    robot_parser = urllib.robotparser.RobotFileParser()
    robot_parser.set_url(robots_url)
    robot_parser.read()
    if robot_parser.can_fetch(agent, url):
        return True 
    else:
        return False

def soup(url: str, agent: str):
    if robots(url, agent):
        print("hej soup")
        headers = {"User-Agent": agent}
        response = requests.get(url_inp, headers=headers)
        error_code = range(400, 600)
        if response.status_code not in error_code:
            soup = BeautifulSoup(response.text, "lxml")
            return soup
        else:
            return -1
    else:
        return -1

def main():
    html = soup(url_inp, agent)
    if html != -1:
        print(html.prettify)
    else:
        print("hej main")
    #TODO: ta fram en massa tags

    
if __name__ == "__main__":
    main()