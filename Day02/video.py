import os
import cv2

# Use absolute path
abs_path = os.path.dirname(__file__)
video_path = 'D:/python/opencv-learning-journey/assets/video.mp4'
# video_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'video.mp4'))
# print(f"Trying to open video at: {video_path}")


# print(video_path2)
if not os.path.exists(video_path):
    print("Error: Video file does not exist at the specified path.")
else:
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
    else:
        while True:
            ret, frame = video.read()
            if not ret:
                print("End of video or can't read the frame.")
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(40) & 0xFF == 27:
                break
        video.release()
        cv2.destroyAllWindows()