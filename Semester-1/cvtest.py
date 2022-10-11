import cv2

cam_stream = cv2.VideoCapture(0)

while True:
	(check, frame) = cam_stream.read()
	
	if not check:
		break

	cv2.imshow('a', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cam_stream.release()
cv2.destroyAllWindows()
