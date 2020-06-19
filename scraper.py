from datetime import date
from url import Url
from iconfinder import IconFinder


class Scraper:
    def __init__(self, url):
        self.orig_url = url
        self.date_checked = date.today()

        url = Url(self.orig_url)
        self.clean_url = url.get_clean_url()
        self.orig_url = url.get_url()
        self.icon_finder = IconFinder(self.clean_url, self.orig_url)
