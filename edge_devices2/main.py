import cv2
import numpy as np
import argparse
import threading
import time
# Get the number of active threads
num_threads = threading.active_count()

# Print the result
print(f"Number of active threads: {num_threads}")

ap = argparse.ArgumentParser()

ap.add_argument("-i1", "--input1", type=str, default="test_video.mp4",
    help="path to input video file")
args = vars(ap.parse_args())

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileDetect=cv2.CascadeClassifier('haarcascade_smile.xml')
#cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

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
#0,cv2.CAP_DSHOW
if not cam.isOpened():
    print("Cannot open camera")
    exit()

#facerec=cv2.face.LBPHFaceRecognizer_create()
facerec=cv2.face.LBPHFaceRecognizer_create()
#eigenfacerec = cv2.face.EigenFaceRecognizer_create()

facerec.read("facemodel/trainer_3cls.yml")
#eigenfacerec.read("eigenfacemodel/trainingData.yml")

shift = 0
while(True):
    start_time = time.time()
    s=0
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)

    for (fx,fy,fw,fh) in faces:
        cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,0,255),2)
        roi_gray = gray[fy:fy + fh, fx:fx + fw]
        roi_color = img[fy:fy + fh, fx:fx + fw]

        smile = smileDetect.detectMultiScale(roi_gray,scaleFactor=1.7,minNeighbors=22,minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 1)
            s = 1


        id,conf=facerec.predict(gray[fy:fy + fh, fx:fx + fw])
        if conf<66:
            print("id : ",id)
            if(id==1):
                display="Husein"
            elif(id==2):
                display="Uknown"
            elif(id==3):
                display="George_W_Bush"
                print(display)
            elif(id==4):
                display="Username_4"
            elif(id==5):
                display="Username_5"
            elif(id==6):
                display="Username_6"
        else:
            display="UNKNOWN"
        if s != 1:
            cv2.putText(img,"FACE", (fx, fy), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 50), 2)

        cv2.putText(img, str(display), (fx, fy+fh+30), cv2.FONT_HERSHEY_COMPLEX, 1, (60, 180, 180), 2)
            
    end_time = time.time()
    frame_time = end_time - start_time
    print(f"Inference time for frame: {frame_time:.4f} seconds")
    #if(cv2.waitKey(1)==ord('q')):
    #    break
cam.release()
#cv2.destroyAllWindows()
