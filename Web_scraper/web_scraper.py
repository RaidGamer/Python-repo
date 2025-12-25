import requests
from bs4 import BeautifulSoup, Comment
from bs4.element import Tag
from sys import argv, exit
from urllib.parse import urlparse
import time 
import random

usage = "="*40+"\nUsage: python3 <script path> <url> <scrape type> <user-agent>\nScrape types:\n'-a' => all html\n\nUser Agent:\n"+"="*40

user_agents = ["Mozilla/5.0 (Linux; Android 9; Redmi 8 Build/PKQ1.190319.001; ru-ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP",
"Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-T860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1"]


try: url_inp = argv[1] 
except IndexError: print(usage); exit(2)
try: filter_inp = argv[2]
except IndexError: print(usage); exit(2)
# try: user_agent = argv[3]
# except IndexError: print(usage); exit(2) #för user-agent implementation senare 

def soup(url: str): #gives soup object (html and css) to scrape info from
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
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
    time.sleep(2)
    scraped = soup(url_inp)
    comments = []
    headers = []
    links = []
    text = []
    output = []
    while scraped:
        if isinstance(scraped, Comment):
            output.append(f"[Comment]: {scraped.strip()}")
            comments.append(f"[Comment]: {scraped.strip()}")
        elif isinstance(scraped, Tag):
            if scraped.name == "title":
                output.append(f"[Title]: {scraped.get_text(strip=True)}")
                headers.append(f"[Title]: {scraped.get_text(strip=True)}")
            elif scraped.name == "p":
                output.append(f"[Text]: {scraped.get_text(strip=True)}")
                text.append(f"[Text]: {scraped.get_text(strip=True)}")
            elif scraped.name == "a":
                linkName = scraped.get_text(strip=True)
                href = scraped.get("href","")
                output.append(f"[Link]: {linkName.strip()} -> {href}")
                links.append(f"[Link]: {linkName.strip()} -> {href}")
        scraped = scraped.next_element    

    match type:
        case e if e=="-a": 
            return scraped
        case e if e=="-p":
            return scraped.prettify()
        case e if e=="-t":
            return "\n".join(output)
        case e if e=="-w":
            return "\n".join(text)
        case e if e=="-c":
            return "\n".join(comments)
        case e if e=="-l":
            return "\n".join(links)
        case e if e=="-h":
            return "\n".join(headers)

        




def main():
    if check_robots().__contains__(url_inp):
        print("Given url is not accessible for scraping according to robots.txt")
    else:
        result = scrape(filter_inp)
        print(result)
    

if __name__ == "__main__": 
    main()

