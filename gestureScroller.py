# Importing the libraries
import cv2
import pyautogui, sys
import keyboard

# Loading the cascades
palm_cascade = cv2.CascadeClassifier('open_palm.xml')
closed_palm_cascade = cv2.CascadeClassifier('closed_palm.xml')

# Defining a function that will do the detections
def detect(gray, frame):
    palm = palm_cascade.detectMultiScale(gray, 1.3, 5)
    close = closed_palm_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in close:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        pyautogui.scroll(-50)

    for (x, y, w, h) in palm:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        pyautogui.scroll(50) 
        
    return frame

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
option = input("Would you like to see your video (y/n): \n")
print("Make a fist to scroll down (works well with right hand)\n")
print("Show your palm to scroll up\n")
print("Press Q to exit\n")
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    if(option == 'y'):
        cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        break
video_capture.release()
cv2.destroyAllWindows()
