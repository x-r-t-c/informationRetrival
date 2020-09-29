from functions import *
import os
from bs4 import BeautifulSoup
import requests


class MyCrawler:
    # Μεταβλητές κλάσης
    queue = set()
    crawled = set()
    counter = 0

    def __init__(self, url, num_of_pages, delete_data, num_of_threads,
                 data_directory="Data", queue_file="/queue.txt", crawled_file="/crawled.txt"):
        self.url = url
        self.num_of_pages = num_of_pages
        self.delete_data = delete_data
        self.num_of_threads = num_of_threads
        # Αρχικοποιεί τα paths του φακέλου Data και των αρχείων queue και crawled
        self.data_directory = data_directory
        self.queue_file = queue_file
        self.crawled_file = crawled_file

    @staticmethod
    def scrape_links(url):
        """
        Βρίσκει και επιστρέφει όλα τα links που βρίσκονται στο συγκεκριμένο url
        """
        links = set()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", attrs={'href': re.compile("^http?s://")}):
            links.append(link.get("href"))
        return links

    def boot(self):
        # Αν δεν υπάρχει data_directory, το δημιουργεί
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
            # Δημιουργεί το queue_file
            if not os.path.isfile(self.queue_file):
                file = open(self.queue_file, 'w')
                file.write(self.url)
                file.close()
            # Δημιουργεί το crawled_file
            if not os.path.isfile(self.crawled_file):
                file = open(self.crawled_file, 'w')
                file.write("")
                file.close()
        # Αν υπάρχει το data_directory
        else:
            # Αν το delete_data είναι 1, διαγράφει τα προηγούμενα δεδομένα
            if self.delete_data:
                # Διαγράφει τα δεδομένα του αρχείου queue_file
                queue_path = self.data_directory + self.queue_file
                with open(queue_path, "w"):
                    pass
                # Και κάνει append το starting url
                file = open(queue_path, "w")
                file.write(self.url)
                file.close()
                # Διαγράφει τα δεδομένα του αρχείου crawled_file
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

