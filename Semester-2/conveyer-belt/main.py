import os
import cv2
import csv
import tkinter as tk
import datetime as dt
import RPi.GPIO as gpio

from PIL import Image, ImageTk
from belt_utils import belt_start, belt_stop, belt_reverse
from color_detector import red_detector, yellow_detector

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

def show_frame() -> None:
    
    '''
        Update and display a video stream to the UI.
    '''

    global imgtk
    global frame
    global status1

    check, frame = cap.read()
    
    if is_counting:
        label00.configure(bg = '#32CD32')
        filtered = yellow_detector(frame, frame)
        filtered = red_detector(frame, frame)
        
    elif not is_counting:
        label00.configure(bg = '#EE4B2B')
        filtered = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    status1.set(f'Yellow: {yellow_count}')
    status2.set(f'Red: {red_count}')
    status3.set(f'Total: {yellow_count + red_count}')
    status4.set(f'Counting: {is_counting}')
    
    # convert image for GUI
    img = Image.fromarray(filtered)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    

def stop() -> None:
    
    '''
        Stop the program and release all of the resources allocated.
    '''
    
    gpio.cleanup()
    cap.release()
    window.destroy()
    

def reset_count() -> None:
    
    '''
        Reset the color counter.
    '''
    
    global yellow_count, red_count
    
    yellow_count = 0
    red_count = 0
    
    
def toggle_count() -> None:
    
    '''
        Toggle the color counter.
    '''
    
    global is_counting
    
    is_counting = not is_counting
    
    
def save_count() -> None:
    
    '''
        Append counter data to the CSV file.
    '''
    
    data = [
        dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        red_count,
        yellow_count,
        red_count + yellow_count
    ]
    
    if not os.path.isfile('./data.csv'):
        with open('data.csv', 'a+') as file:
            
            write = csv.writer(file)
            write.writerow(['last saved', 'red', 'yellow', 'total'])
            write.writerow(data)
            
            return
    
    with open('data.csv', 'a+') as file:
        write = csv.writer(file)
        write.writerow(data)


window = tk.Tk() 

status1 = tk.StringVar()
status2 = tk.StringVar()
status3 = tk.StringVar()
status4 = tk.StringVar()

is_counting = False

window.wm_title('Conveyer belt controller')
window.geometry('1130x600')
window.option_add('*font', 'PSL-omyim 30')
window.config(background='#242526')

left_frame = tk.Frame(window,  width = 200,  height = 400, background='#242526')
left_frame.grid(row=1,  column=0,  padx=10,  pady=5)

mid_frame = tk.Frame(window,  width=650,  height=400, background='#242526')
mid_frame.grid(row=1,  column=1,  padx=10,  pady=5)

right_frame = tk.Frame(window,  width = 200,  height = 400, background='#242526')
right_frame.grid(row=1,  column=3,  padx=10,  pady=5)

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

label00 = tk.Label(window, textvariable=status4, bg='#EE4B2B', fg='white', font='PSL-omyim 50')
label00.grid(row=0,  column=1,  padx=10,  pady=5)

label20 = tk.Label(left_frame, textvariable=status1, bg='gold', fg='white', font='PSL-omyim 50')
label20.pack()

label21 = tk.Label(left_frame, textvariable=status2, bg='red', fg='white', font='PSL-omyim 50')
label21.pack()

label22 = tk.Label(left_frame, textvariable=status3, bg='#000080', fg='white', font='PSL-omyim 50')
label22.pack()

btn10 = tk.Button(right_frame, text='Start Belt', fg='black', command= lambda: belt_start(in1, in2))
btn10.pack(pady = 5)

btn11 = tk.Button(right_frame, text='Stop Belt', fg='black', command= lambda: belt_stop(in1, in2))
btn11.pack(pady = 5)

btn12 = tk.Button(right_frame, text='Reverse Belt', fg='black', command= lambda: belt_reverse(in1, in2))
btn12.pack(pady = 5)

btn13 = tk.Button(right_frame, text='Toggle count', fg='black', command=toggle_count)
btn13.pack(pady = 5)

btn14 = tk.Button(right_frame, text='Reset count', fg='black', command=reset_count)
btn14.pack(pady = 5)

btn15 = tk.Button(right_frame, text='Save count', fg='black', command=save_count)
btn15.pack(pady = 5)

btn40 = tk.Button(right_frame, text='Exit', fg='red', command=stop)
btn40.pack(pady = 5)

show_frame()
window.mainloop()