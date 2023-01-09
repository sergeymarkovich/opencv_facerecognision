import cv2
import os

cam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('faces.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user name end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while True:

    ret, img = cam.read()
    fps = cam.get(cv2.CAP_PROP_FPS)
    multiplier = fps * 3
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    if ret:
        frame_id = int(round(cam.get(0)))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            cv2.imshow('image', img)

        if frame_id % multiplier == 0:
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", img[y:y + h, x:x + w])
            print(f"Take a screenshot number {count}")

        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", img[y:y + h, x:x + w])
            print(f"Take a screenshot number {count}")
        elif key == ord('q'):
            print("\n [INFO] Program exited with hot key")
            break
        elif count >= 20: # Take 20 face sample and stop video
            print("\n [INFO] 20 Screens taken. Exiting Program...")
            break

# Do a bit of cleanup
cam.release()
cv2.destroyAllWindows()