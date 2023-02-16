import cv2
import numpy as np


def yellow_detector(frame: np.ndarray[np.uint8], show_frame: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    
    '''
        Detects yellow objects in a frame and draws rectangles around them. 
        
        Increments a global count if objects is within a center x-coordinate range.
    '''
    
    lower_yellow = np.array((15, 150, 20))
    upper_yellow = np.array((35, 255, 255))
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame, lower_yellow, upper_yellow)
    
    (contours, hierachy) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                
                (x, y, w, h) = cv2.boundingRect(cnt)
                
                if x in range(145, 200):
                    global yellow_count
                    yellow_count += 1
                    
                cv2.rectangle(show_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    return cv2.cvtColor(show_frame, cv2.COLOR_BGR2RGB)


def red_detector(frame: np.ndarray[np.uint8], show_frame: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    
    '''
        Detects red objects in a frame and draws rectangles around them. 
        
        Increments a global count if objects is within a center x-coordinate range.
    '''
    
    lower_red = np.array((0, 87, 100))
    upper_red = np.array((10, 255, 255))
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame, lower_red, upper_red)
    
    (contours, hierachy) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                
                (x, y, w, h) = cv2.boundingRect(cnt)
                
                if x in range(145, 200):
                    global red_count
                    red_count += 1
                    
                cv2.rectangle(show_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    return cv2.cvtColor(show_frame, cv2.COLOR_BGR2RGB)
