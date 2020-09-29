from bs4 import BeautifulSoup
import requests
import re
import os
from urllib.parse import urlparse
import time

pcbee = 'https://pcbee.gr'


# # Scrapes the links of a specific page
# def scrape_links(page_url):
#     links = []
#     if page_url == '':
#         print('Empty url')
#         return links
#     page = requests.get(page_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     for link in soup.find_all('a', attrs={'href': re.compile("^http?s://")}):
#         link2append = link.get('href')
#         links.append(link2append)
#     return links


# Creates the data directory
def create_directory(directory_name="Data"):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print(f'Directory {directory_name} already exist.')


# Create the queue and crawled files
def create_data_files(STARTING_URL="https://pcbee.gr"):
    queue = "Data" + "/queue.txt"
    crawled = "Data" + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, STARTING_URL)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# Write data to a file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")


# Delete the contents of a file
def delete_data(path):
    with open(path, "w"):
        pass


# # Initialize the crawler
# def initialize(url, delete):
#     if delete:
#         if not os.path.exists("Data"):
#             create_directory()
#             create_data_files(url)
#         delete_data("Data/queue.txt")
#         delete_data("Data/crawled.txt")
#         write_file("Data/queue.txt", url)


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, "rt") as file:
        for line in file:
            results.add(line.replace("\n", ""))
    return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    # delete_data(file)  ############# to do ###########
    for link in sorted(links):
        append_to_file(file, link)
