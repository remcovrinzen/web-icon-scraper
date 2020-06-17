from multiprocessing import Pool
import os
from os import path
from scraper import Scraper

NUMBER_OF_PROCESSES = 4
INPUT_FILE_PATH = "/input/test.txt"


def process_url(url):
    result = Scraper(url)


if __name__ == "__main__":
    if not path.exists(os.getcwd() + '/output/icons'):
        os.makedirs(os.getcwd() + '/output/icons')

    pool = Pool(NUMBER_OF_PROCESSES)

    with open(os.getcwd() + INPUT_FILE_PATH) as input_file:
        results = pool.map(process_url, input_file, 1)
