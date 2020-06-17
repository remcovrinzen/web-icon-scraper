import validators


class Url:
    def __init__(self, url):
        self.url = url
        self.cleaned_url = None

    def clean_url(self, url):
        url = url.rstrip()
        self.url = url

        if not url.startswith('http://') or url.startswith('https://'):
            url = 'https://' + url

        return url

    def get_clean_url(self):
        if not self.clean_url_is_set():
            self.set_clean_url()

        return self.cleaned_url

    def set_clean_url(self):
        if not validators.url(self.url):
            url = self.clean_url(self.url)

        self.cleaned_url = url

    def clean_url_is_set(self):
        if self.cleaned_url != None:
            return True

        return False

    def get_url(self):
        return self.url
