import os


class Icon:
    def __init__(self, icon, orig_url, save=True):
        self.icon = icon
        self.orig_url = orig_url

        if save:
            self.save_to_disk()

    def save_to_disk(self):
        file_path = os.getcwd() + '/output/icons/' + self.orig_url + '.png'

        with open(file_path, 'wb') as f:
            f.write(self.icon)
