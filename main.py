# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import time

from image_pairing import ImagePairing
from image_viewer import ImageViewer
from juxtaposition import Juxtaposition

if __name__ == '__main__':
    pairing: ImagePairing = ImagePairing()
    juxtaposition: Juxtaposition = pairing.pair()
    ImageViewer().view(juxtaposition)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
