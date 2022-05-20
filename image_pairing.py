from image_files import ImageFiles
from juxtaposition import Juxtaposition


class ImagePairing:

    def __init__(self):
        self.imagefiles = ImageFiles()

    def pair(self):
        image1 = self.imagefiles.next()
        image2 = self.imagefiles.next()

        return Juxtaposition(image1, image2)
