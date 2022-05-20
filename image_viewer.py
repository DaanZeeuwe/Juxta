import matplotlib.pyplot as plt
from matplotlib import image as mpimg

from juxtaposition import Juxtaposition


class ImageViewer:

    def __init__(self):
        pass

    def view(self, juxta: Juxtaposition):
        f, axarr = plt.subplots(1, 2)
        axarr[0].imshow(mpimg.imread(juxta.image1))
        axarr[0].axis('off')
        axarr[1].imshow(mpimg.imread(juxta.image2))
        axarr[1].axis('off')
        plt.draw()
        plt.waitforbuttonpress(0)  # this will wait for indefinite time
        plt.close(f)
