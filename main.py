from multiprocessing import Pool
import os
from os import path
from scraper import Scraper
import pandas as pd
import shutil
import time


INPUT_FILE_PATH = "/input/test.txt"
OUTPUT_FILE_PATH = "/output/result.csv"


def process_url(url):
    scraper = Scraper(url)
    result = {'domain': scraper.orig_url, 'date_checked': scraper.date_checked,
              'found': scraper.icon_finder.found}

    if scraper.icon_finder.found:
        result['width'] = scraper.icon_finder.icon.width
        result['height'] = scraper.icon_finder.icon.height
        result['colors'] = scraper.icon_finder.icon.colors

    return result


def prepare_wd():
    # Clean previous results
    if path.exists(os.getcwd() + '/output'):
        shutil.rmtree(os.getcwd() + "/output")

    if not path.exists(os.getcwd() + '/output/icons'):
        os.makedirs(os.getcwd() + '/output/icons')


if __name__ == "__main__":
    start_time = time.time()
    prepare_wd()

    pool = Pool()

    with open(os.getcwd() + INPUT_FILE_PATH) as input_file:
        results = pool.map(process_url, input_file, 1)

    df = pd.DataFrame(data=results, columns=[
                      'domain', 'date_checked', 'found', 'width', 'height', 'colors'])
    df.to_csv(os.getcwd() + OUTPUT_FILE_PATH)
    print("--- %s seconds ---" % (time.time() - start_time))
