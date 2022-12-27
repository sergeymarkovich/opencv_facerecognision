import cv2
import os

cam = cv2.VideoCapture(0)


face_detector = cv2.CascadeClassifier('faces.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user name end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", img[y:y+h,x:x+w])
        cv2.imshow('image', img)

    key = cv2.waitKey(100) & 0xFF
    if key == ord('q'):
        break
    elif count >= 10: # Take 10 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()