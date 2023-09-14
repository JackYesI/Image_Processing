import cv2 as cv
import sys

class Video:
    
    def __init__(self, fps):
      self.vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
      if self.vid_capture is None:
            sys.exit("Could not connect of camera.")
      self.frame_size = (int(self.vid_capture.get(3)), int(self.vid_capture.get(4)))
      self.fps = fps

    def output(self, path):
        self.output = cv.VideoWriter(path, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), self.fps, self.frame_size)

    def write(self, time_recording):
        time = 0
        while(self.vid_capture.isOpened()):
            time = time + 1
            ret, frame = self.vid_capture.read()
            print(time)
            if time == time_recording:
                break
            if ret == True:
                self.output.write(frame)
            else:
                print('Stream disconnected')
                break

    def __del__(self):
        self.vid_capture.release()
        self.output.release()
        print("end")


if __name__ == "__main__":
    file_write = 'D:\Procesing_image\Image_Processing\Lab_2\output.avi'
    fps_ = 20
    time_recording_ = 100
    video_grayscale = Video(fps_)
    video_grayscale.output(file_write)
    video_grayscale.write(time_recording_)
    del video_grayscale