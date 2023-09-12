import cv2 as cv
import sys

class Image:

    def __init__(self, path):
        self.image = cv.imread('test_pict.jpg', 0)
        if self.image is None:
            sys.exit("Could not read the image.")

    def write(self, path):
        cv.imwrite('grayscale.jpg', self.image)

    def show(self, caption):
        cv.namedWindow(caption, cv.WINDOW_NORMAL)
        cv.imshow(caption, self.image)

    def __del__(self):
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    image_grayscale = Image("image.webp")
    image_grayscale.write("image_grayscale.webp")
    image_grayscale.show("Grayscale image")
    del image_grayscale


