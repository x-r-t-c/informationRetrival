import concurrent.futures
import time
from bs4 import BeautifulSoup
import requests
import re
from MyCrawler import *

counter = 0
links = set()
data = {}

myCrawler = MyCrawler('https://pcbee.gr/', 200, 0, 8)
myCrawler.boot()
myCrawler.queue_to_set()
myCrawler.print_crawler()

while counter < 200:
    if MyCrawler.queue:
        link = MyCrawler.queue.pop()
    else:
        print("Empty queue.")
        break

    if link not in MyCrawler.crawled:
        links = myCrawler.scrape_links(link)
        print("new links: ", links)
        print("Queue after pop: ", MyCrawler.queue)

        for page_link in links:
            if page_link not in MyCrawler.crawled:
                MyCrawler.queue.add(page_link)

        data[link] = MyCrawler.scrape_data(link)
        MyCrawler.crawled.add(link)
        counter = counter + 1
        print("Queue after append: ", MyCrawler.queue)
        print("Crawled after append: ", MyCrawler.crawled)

    print(counter)

for link in data:
    print(link, data[link])



