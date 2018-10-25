from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox

root = Tk()
root.title("Alarm clock")
def SubmitButton():
  AlarmTime= entry1.get()
  Message1()
  CurrentTime = time.strftime("%H:%M")
  print("The Alarm Time is : {}".format(AlarmTime))
  while AlarmTime != CurrentTime:
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
     print("Alarm Music is now Playing")
     os.system("start alarm-music.mp3")
     label2.config(text = "Alarm music playing.....")
     messagebox.showinfo(title= 'Alarm Message', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="The Alarm time is Counting...")
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))     
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 200, width = 200)

label1= ttk.Label(frame1,text = "Enter the Alarm time :")
label1.pack()

entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()
entry1.insert(3,"Example - 13:15")

labelAlarmMessage= ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(frame1, width=30)
entry2.pack()

button1= ttk.Button(frame1, text= "submit", command=SubmitButton)
button1.pack()
label2= ttk.Label(frame1)
label2.pack()

  
root.mainloop()
