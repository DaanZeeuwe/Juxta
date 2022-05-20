from image_files import ImageFiles
from juxtaposition import Juxtaposition


class ImagePairing:

    def __init__(self):
        self.imagefiles = ImageFiles()

    def pair(self):
        image1 = self.imagefiles.next()
        image2 = self.imagefiles.next()

        if image1 is None or image2 is None:
            return None

        return Juxtaposition(image1, image2)
