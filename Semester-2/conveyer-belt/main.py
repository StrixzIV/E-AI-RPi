import cv2
import tkinter as tk
import RPi.GPIO as gpio

from PIL import Image, ImageTk

gpio.setmode(gpio.BCM)

is_running = False

in1 = 13
in2 = 19
control = 25

wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

status = tk.StringVar()

def show_frame():

    global imgtk
    global frame

    check, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    # convert image for GUI
    img = Image.fromarray(cv2image)
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


window = tk.Tk() 

window.wm_title("Conveyer belt controller")
window.geometry('800x1000')
window.option_add("*font", "PSL-omyim 30")
window.config(background="#242526")

imageFrame = tk.Frame(window)
imageFrame.configure(width = 600, height = 500)
imageFrame.grid_propagate(False)
imageFrame.pack()




gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)

gpio.setup(control, gpio.OUT)
controller = gpio.PWM(control, 50)

gpio.output(in1, gpio.LOW)
gpio.output(in2, gpio.LOW)

controller.start(55)
    
# display image
lmain = tk.Label(imageFrame)
lmain.pack(pady = 3)

label20 = tk.Label(textvariable=status, bg="gold", fg="white", font="PSL-omyim 50")
label20.pack()

btn10 = tk.Button(text="Start Belt", fg='black', command=belt_start)
btn10.pack()

btn11 = tk.Button(text="Stop Belt", fg='black', command=belt_stop)
btn11.pack()

btn40 = tk.Button(text="หยุดการทำงาน", fg="red", command=stop)
btn40.pack()

show_frame()
window.mainloop()