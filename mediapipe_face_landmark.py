#This script is developed using 'mediapipe'

import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
prev_time = 0

with mp_face_mesh.FaceMesh(max_num_faces=5, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
	while cap.isOpened():
		success, frame = cap.read()

		# Flipping horizontaly and converting to RGB for model to process the frame
		frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

		# For performance tunning, setting Writable to False
		frame.flags.writeable = False
		model_loading_start = time.time()
		results = face_mesh.process(frame)

		#model loading calculation
		model_loading_end = time.time()
		model_loading_time = (model_loading_end - model_loading_start) * (1000)

		# Draw the face mesh annotations on the frame.
		frame.flags.writeable = True
		frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
		
		if results.multi_face_landmarks:
			for face_landmarks in results.multi_face_landmarks:
				mp_drawing.draw_landmarks(
					image=frame,
					landmark_list=face_landmarks,
					connections=mp_face_mesh.FACEMESH_CONTOURS,
					landmark_drawing_spec=drawing_spec,
					connection_drawing_spec=drawing_spec)
		
		#fps calculation
		curr_time = time.time()
		fps = 1 / (curr_time - prev_time)
		prev_time = curr_time
		
		cv2.putText(frame, f'FPS: {int(fps)}, MLT: {model_loading_time:.2f}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3)
		cv2.imshow('Face Landmarks', frame)
		
		key = cv2.waitKey(1)
		if key == 27:
			break

cap.release()
cv2.destroyAllWindows()