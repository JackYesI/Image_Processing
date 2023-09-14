import cv2 as cv
import sys

class Video:
    
    def __init__(self, path):
      self.vid_capture = cv.VideoCapture(path)
      if self.vid_capture is None:
            sys.exit("Could not read the image.")

    def read(self):
        while(self.vid_capture.isOpened()):
            ret, frame = self.vid_capture.read()
            if ret == True:
                cv.imshow('Frame', frame)
                k = cv.waitKey(20)
                if k == 613:
                    break
            else:
                break

    def frame(self):
        fps = int(self.vid_capture.get(5))
        print("Frame Rate : " , fps, "frames per second") 
        frame_count = self.vid_capture.get(7)
        print("Frame count : ", frame_count)

    def __del__(self):
        self.vid_capture.release()
        cv.destroyAllWindows()
        print("end")


if __name__ == "__main__":
    file_read = 'D:\Procesing_image\Image_Processing\Lab_2\output.avi'
    video_grayscale = Video(file_read)
    video_grayscale.frame()
    video_grayscale.read()
    del video_grayscale