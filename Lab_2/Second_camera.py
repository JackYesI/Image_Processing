import cv2 as cv
import sys

vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width, frame_height)
fps = 20

output = cv.VideoWriter('D:\Procesing_image\Image_Processing\Lab_2\output_7.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)

time = 0

while(vid_capture.isOpened()):
    
    time = time + 1
    ret, frame = vid_capture.read()
    print(time)
    if time == 100:
         break
    if ret == True:
           #Write the frame to the output files.
           output.write(frame)
    else:
         print('Stream disconnected')
         break

vid_capture.release()
output.release()


