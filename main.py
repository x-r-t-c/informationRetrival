import concurrent.futures
import time
from bs4 import BeautifulSoup
import requests
import re
from MyCrawler import *


links = set()

myCrawler = MyCrawler('https://pcbee.gr', 200, 0, 8)
myCrawler.boot()
myCrawler.queue_to_set()
myCrawler.print_crawler()




