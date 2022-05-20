import random
from os import listdir

from os.path import isfile, join


class ImageFiles:

    def __init__(self):
        path = "images"
        self.files = [path + "/" + f for f in listdir(path) if isfile(join(path, f))]
        random.shuffle(self.files)

    def next(self):
        return self.files.pop()

