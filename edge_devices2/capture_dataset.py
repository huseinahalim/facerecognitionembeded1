import cv2
import os
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i1", "--input1", type=str, default="test_video.mp4",
    help="path to input video file")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
print("input : ",args["input1"])
inputss= args["input1"]
if inputss == "0":
    webcam = int(args["input1"])
    cam = cv2.VideoCapture(webcam,cv2.CAP_DSHOW)
elif inputss == "1":
    webcam = int(args["input1"])
    cam = cv2.VideoCapture(webcam,cv2.CAP_DSHOW)   
else:
    cam = cv2.VideoCapture('test_video.mp4')

#cam = cv2.VideoCapture("test_video.mp4")#0,cv2.CAP_DSHOW
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()