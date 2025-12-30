import requests
from bs4 import BeautifulSoup
from sys import argv, exit
from urllib.parse import urlparse
import urllib.robotparser
import time 
import random

#TODO: implementera json lagring
            
usage = "="*60+"\nUsage: python3 <script path> <url> <dump to json (y/n)>\n"+"="*60
try: url_inp = argv[1] 
except IndexError: print(usage); exit(2)
try: json_inp = argv[2] 
except IndexError: print(usage); exit(2)

def dumpJson(dict: dict):
    import json
    if json_inp == "y":
        with open("/home/alexo/Desktop/ws_data.json", "x",encoding="utf-8") as jdump:
            json.dumps(dict, ensure_ascii=False, indent=4)
        

agent = "MyWebScraper1.0 (learning project using python; non-commerical use)"

def robots(url: str, agent: str): 
    #hantera urllib.error.URLError
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
        response = requests.get(url, headers=headers)
        error_codes = range(400, 600)
        status_code = response.status_code
        reason = response.reason
        if status_code not in error_codes:
            soup = BeautifulSoup(response.text, "lxml")
            return soup
        else:
            print(f"HTTP {status_code} {reason} while fetching {url}")
            return -1
    else:
        print(f"Blocked by robots.txt: {url}")
        return -1

def main():
    html = soup(url_inp, agent)
    if html == -1:
        exit(1)
    else:
        #SPECIFY DATA TO BE SCRAPED HERE
        print(html.prettify)
        # dumpJson(arg)

    
if __name__ == "__main__":
    main()