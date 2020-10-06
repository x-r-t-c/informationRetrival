from functions import *
import os
from bs4 import BeautifulSoup
import requests


class MyCrawler:
    # class variables
    queue = set()
    crawled = set()
    counter = 0

    # locks for multithreading
    lock_queue = False
    lock_crawled = False

    def __init__(self, url, num_of_pages, delete_data, num_of_threads,
                 data_directory="Data", queue_file="/queue.txt", crawled_file="/crawled.txt"):
        self.url = url
        self.num_of_pages = num_of_pages
        self.delete_data = delete_data
        self.num_of_threads = num_of_threads
        # Initializes the paths of Data file and queue,crawled files
        self.data_directory = data_directory
        self.queue_file = queue_file
        self.crawled_file = crawled_file

    @staticmethod
    def scrape_links(url):
        """
        Finds all links inside the specific url
        """
        links = set()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", attrs={'href': re.compile("^http?s://")}):
            links.add(link.get("href"))
        return links

    @staticmethod
    def scrape_data(url):
        scraped_text = []
        # my_dict[url] = ["a", "b", "c"]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for text in soup.find_all("p"):
            replaced = re.sub("<[^>]*>", "", str(text))
            scraped_text.append(replaced)
        return scraped_text

    def boot(self):
        # if data_directory does not exists, creates the file
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
            # creates queue_file
            if not os.path.isfile(self.queue_file):
                file = open(self.queue_file, 'w')
                file.write(self.url)
                file.close()
            # creates crawled_file
            if not os.path.isfile(self.crawled_file):
                file = open(self.crawled_file, 'w')
                file.write("")
                file.close()
        # if data_directory exists
        else:
            # if delete_data is 1, deletes the previous data
            if self.delete_data:
                # deletes the data of queue_file
                queue_path = self.data_directory + self.queue_file
                with open(queue_path, "w"):
                    pass
                # append the starting url
                file = open(queue_path, "w")
                file.write(self.url)
                file.close()
                # deletes the data of crawled_file
                crawled_path = self.data_directory + self.crawled_file
                with open(crawled_path, "w"):
                    pass

    def print_crawler(self):
        print(f' url: {self.url}\n'
              f' num_of_pages: {self.num_of_pages}\n'
              f' delete_data: {self.delete_data}\n'
              f' num_of_threads: {self.num_of_threads}')
        print("\nQueued links: ")
        for link in MyCrawler.queue:
            print(link)
        print("\nCrawled links: ")
        for link in MyCrawler.crawled:
            print(link)

    def queue_to_set(self):
        path = self.data_directory + self.queue_file
        with open(path, "rt") as file:
            for line in file:
                MyCrawler.queue.add(line.replace("\n", ""))

    def crawled_to_set(self):
        path = self.data_directory + self.crawled_file
        with open(path, "rt") as file:
            for line in file:
                MyCrawler.crawled.add(line.replace("\n", ""))

    @staticmethod
    def queue_to_file(path, data):
        with open(path, 'a') as file:
            while not MyCrawler.lock_queue:
                # for concurrency control
                MyCrawler.lock_queue = True
                file.write(data)
                file.close()
                MyCrawler.lock_queue = False

    @staticmethod
    def crawled_to_file(path, data):
        with open(path, 'a') as file:
            while not MyCrawler.lock_crawled:
                # for concurrency control
                MyCrawler.lock_crawled = True
                file.write(data)
                file.close()
                MyCrawler.lock_crawled = False
