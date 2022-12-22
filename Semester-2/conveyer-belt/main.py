import cv2
import csv
import numpy as np
import tkinter as tk
import datetime as dt
import RPi.GPIO as gpio

from PIL import Image, ImageTk

gpio.setmode(gpio.BCM)

is_running = False

in1 = 13
in2 = 19
control = 25

yellow_count = 0
red_count = 0

wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

def yellow_detector(frame: np.ndarray[np.uint8], show_frame: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    
    global yellow_count
    
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
                    yellow_count += 1
                    
                cv2.rectangle(show_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    return cv2.cvtColor(show_frame, cv2.COLOR_BGR2RGB)


def red_detector(frame: np.ndarray[np.uint8], show_frame: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    
    global red_count
    
    lower_red = np.array((0, 87, 100))
    upper_red = np.array((10, 255, 255))
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame, lower_red, upper_red)
    
    (contours, hierachy) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                
                (x, y, w, h) = cv2.boundingRect(cnt)
                print(x)
                
                if x in range(145, 200):
                    red_count += 1
                    
                cv2.rectangle(show_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    return cv2.cvtColor(show_frame, cv2.COLOR_BGR2RGB)


def show_frame():

    global imgtk
    global frame
    global status1

    check, frame = cap.read()

    filtered = yellow_detector(frame, frame)
    filtered = red_detector(frame, frame)
    
    status1.set(f'Yellow: {yellow_count}')
    status2.set(f'Red: {red_count}')
    status3.set(f'Total: {yellow_count + red_count}')
    
    # convert image for GUI
    img = Image.fromarray(filtered)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    

def stop():
    cap.release()
    window.destroy()
    
    
def belt_start():
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.HIGH)


def belt_stop():
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.LOW)
    
    
def reset_count():
    
    global yellow_count, red_count
    
    yellow_count = 0
    red_count = 0
    
    
def save_count():
    
    data = [
        dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        red_count,
        yellow_count,
        red_count + yellow_count
    ]
    
    with open('data.csv', 'a+') as file:
        write = csv.writer(file)
        write.writerow(data)


window = tk.Tk() 

status1 = tk.StringVar()
status2 = tk.StringVar()
status3 = tk.StringVar()

window.wm_title("Conveyer belt controller")
window.geometry('1300x500')
window.option_add("*font", "PSL-omyim 30")
window.config(background="#242526")

left_frame = tk.Frame(window,  width = 200,  height = 400, background="#242526")
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

mid_frame = tk.Frame(window,  width=650,  height=400, background="#242526")
mid_frame.grid(row=0,  column=1,  padx=10,  pady=5)

right_frame = tk.Frame(window,  width = 200,  height = 400, background="#242526")
right_frame.grid(row=0,  column=3,  padx=10,  pady=5)

gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)

gpio.setup(control, gpio.OUT)
controller = gpio.PWM(control, 50)

gpio.output(in1, gpio.LOW)
gpio.output(in2, gpio.LOW)

controller.start(55)
    
# display image
lmain = tk.Label(mid_frame)
lmain.pack(pady = 3)

label20 = tk.Label(left_frame, textvariable=status1, bg="gold", fg="white", font="PSL-omyim 50")
label20.pack()

label21 = tk.Label(left_frame, textvariable=status2, bg="red", fg="white", font="PSL-omyim 50")
label21.pack()

label22 = tk.Label(left_frame, textvariable=status3, bg="#000080", fg="white", font="PSL-omyim 50")
label22.pack()

btn10 = tk.Button(right_frame, text="Start Belt", fg='black', command=belt_start)
btn10.pack(pady = 5)

btn11 = tk.Button(right_frame, text="Stop Belt", fg='black', command=belt_stop)
btn11.pack(pady = 5)

btn12 = tk.Button(right_frame, text="Reset count", fg='black', command=reset_count)
btn12.pack(pady = 5)

btn13 = tk.Button(right_frame, text="Save count", fg='black', command=save_count)
btn13.pack(pady = 5)

btn40 = tk.Button(right_frame, text="หยุดการทำงาน", fg="red", command=stop)
btn40.pack(pady = 5)

show_frame()
window.mainloop()