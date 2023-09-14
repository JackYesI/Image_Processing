import cv2 as cv
import sys

class Image:

    def __init__(self, file):
        self.image = cv.imread(file, 0)
        if self.image is None:
            sys.exit("Could not read the image.")

    def write(self, file_write):
        cv.imwrite(file_write, self.image)

    def show(self, caption):
        cv.namedWindow(caption, cv.WINDOW_NORMAL)
        cv.imshow(caption, self.image)

    def __del__(self):
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    image_file = 'test_pict.jpg'
    image_write = 'grayscale.jpg'
    name_window = "Grayscale image"
    image_grayscale = Image(image_file)
    image_grayscale.write(image_write)
    image_grayscale.show(name_window)
    del image_grayscale




