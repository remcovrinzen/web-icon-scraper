import os
import requests
from PIL import Image
import base64
import io
import numpy as np
from colorthief import ColorThief


class Icon:
    COLOR_PALETTE = 5

    def __init__(self, icon, orig_url):
        self.icon = icon
        self.orig_url = orig_url
        self.valid = True
        self.width = icon.width
        self.height = icon.height
        self.format = icon.format

        try:
            self.icon_string = requests.get(self.icon.url, timeout=5).content
        except Exception as e:
            self.valid = False

        if self.valid:
            self.colors = self.get_most_used_colors()
            self.colors = self.convert_rgb_array_to_hex(self.colors)
            self.save_to_disk()

    def save_to_disk(self):
        image_buffer = self.convert_string_to_image_buffer(
            self.icon_string)

        try:
            image = Image.open(image_buffer)
            file_path = os.getcwd() + '/output/icons/' + \
                self.orig_url + '.png'
            image.save(file_path)
        except Exception as e:
            self.valid = False

    def convert_string_to_image_buffer(self, base64_string):
        try:
            return io.BytesIO(base64_string)
        except OSError as e:
            self.valid = False

    def get_most_used_colors(self, number_of_colors=COLOR_PALETTE):
        image_buffer = self.convert_string_to_image_buffer(self.icon_string)

        try:
            colorthief = ColorThief(image_buffer)
            return colorthief.get_palette(number_of_colors)
        except Exception as e:
            return None

    def convert_rgb_array_to_hex(self, rgb_array):
        if not rgb_array:
            return None

        hex_array = []

        for rgb_tuple in rgb_array:
            hex_array.append(self.convert_rgb_to_hex(rgb_tuple))

        return hex_array

    def convert_rgb_to_hex(self, rgb_tuple):
        return "#{0:02x}{1:02x}{2:02x}".format(self.clamp(rgb_tuple[0]), self.clamp(rgb_tuple[1]), self.clamp(rgb_tuple[2]))

    def clamp(self, x):
        return max(0, min(x, 255))
