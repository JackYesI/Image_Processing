import cv2
import sys

img_grayscale = cv2.imread('test_pict.jpg', 0)
if img_grayscale is None:
    sys.exit("Could not read the image.")

cv2.imwrite('grayscale.jpg', img_grayscale)
cv2.namedWindow("Grayscale image", cv2.WINDOW_NORMAL)

cv2.imshow('Grayscale image', img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()


