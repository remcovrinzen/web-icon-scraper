import requests
from icon import Icon
import favicon


class IconFinder:

    def __init__(self, url, orig_url):
        self.orig_url = orig_url
        self.url_to_search = url
        self.found = False

        icons = self.find_icons_at_url()
        icon = self.get_largest_icon_from_list(icons)

        if self.found:
            icon = Icon(icon, orig_url)
            self.found = icon.valid
            self.icon = icon

    def find_icons_at_url(self):
        icons = favicon.get(self.url_to_search,  allow_redirects=True)

        return icons

    def get_largest_icon_from_list(self, icons):
        if len(icons) > 0:
            self.found = True
            return icons[0]

        return None
