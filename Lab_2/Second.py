import cv2 as cv
import sys

vid_capture = cv.VideoCapture('D:\Procesing_image\Image_Processing\Lab_2\output_7.avi')

if (vid_capture.isOpened() == False):
  print("Error opening the video file")
else:
  fps = int(vid_capture.get(5))
  print("Frame Rate : " , fps, "frames per second") 
  frame_count = vid_capture.get(7)
  print("Frame count : ", frame_count)

while(vid_capture.isOpened()):
  ret, frame = vid_capture.read()
  if ret == True:
    cv.imshow('Frame', frame)
    k = cv.waitKey(20)
    if k == 613:
      break
  else:
    break
# vid_capturel = cv2.VideoCapture('test%02d.jpg')
vid_capture.release()
# cv2.destroyAllWindows()


  

