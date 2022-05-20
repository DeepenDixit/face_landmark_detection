#This script is developed using 'dlib'
#This script will need "shape_predictor_68_face_landmarks.dat" file within the same folder as script

import cv2
import dlib
import time

cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()

#need to get this dat file for 68 face andmarks
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

prev_time = 0

while True:
    success, frame = cap.read()

    # Flipping horizontaly and converting to Gray for model to process the frame
    gray = cv2.cvtColor(cv2.flip(frame,1), cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,1)

    faces = hog_face_detector(gray)
    model_loading_time = float(0)

    for face in faces:
        model_loading_start = time.time()
        face_landmarks = dlib_facelandmark(gray, face)

        #model run time calculation
        model_loading_end = time.time()
        model_loading_time = model_loading_end - model_loading_start

        for n in range(0, 68):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

    model_loading_time *= 1000

    #fps calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)} MLT: {model_loading_time:.2}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3)

    cv2.imshow("Face Landmarks", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()