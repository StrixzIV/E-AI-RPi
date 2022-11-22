import cv2

cam_stream = cv2.VideoCapture(0)

while True:
    
    (has_frame, frame) = cam_stream.read()
    
    if not has_frame:
        break
        
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imshow('Press x to capture the image / Press q to quit', frame)


cam_stream.release()
cv2.destroyAllWindows()