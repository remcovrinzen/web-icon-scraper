import requests
from icon import Icon


class IconFinder:
    MAX_RETRY = 3
    MOST_COMMON_LOCATION = '/favicon.ico'

    def __init__(self, url, orig_url):
        self.orig_url = orig_url
        self.url_to_search = url
        self.session = requests.Session()
        self.found = False

        icon = self.find_icon_in_web_content()

        if self.found:
            icon = Icon(icon, orig_url)

    def find_icon_in_web_content(self):
        result = self.check_most_common_location()

        if result != None and result.status_code == 200:
            self.found = True
            return result.content

    def check_most_common_location(self):
        try:
            request_result = self.session.get(
                self.url_to_search + self.MOST_COMMON_LOCATION)
        except requests.exceptions.RequestException as e:
            request_result = None

        return request_result
