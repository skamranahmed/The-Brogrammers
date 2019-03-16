from tkinter import *
import speech_recognition as speech


a = Tk()
a.title('SAFEST ROUTE PREDICTOR')
a.geometry('1440x900+300+100')
a.configure(background='powder blue')

""" --- Using Google Speech to Text to take input from the user through microphone ---"""

def voice1():
    b = speech.Recognizer()
    with speech.Microphone() as source:
        audio = b.listen(source)
    try:
        text = b.recognize_google(audio)
        name1.set(text)
    except:
        print('error')
def voice2():
    b = speech.Recognizer()
    with speech.Microphone() as source:
        audio = b.listen(source)
    try:
        text = b.recognize_google(audio)
        name2.set(text)
    except:
        print('error')

background_image = PhotoImage(file='images/big_map.gif')
background_label = Label(a,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
label0 = Label(text='SAFEST ROUTE PREDICTOR',width=30,font=("bold",34),background='white')
label0.place(x=400,y=25)
label1 = Label(text='SOURCE',font=35)
label1.place(x=480,y=150)
name1 = StringVar()
text1 = Entry(textvariable=name1,width=25,font=20)
text1.place(x=650,y=150)
label2 = Label(text='DESTINATION',font=35)
label2.place(x=480,y=205)
name2 = StringVar()
text2 = Entry(textvariable=name2,width=25,font=20)
text2.place(x=650,y=205)


## Button for getting route (not configured as of now)
button1 = Button(a,text='GET ROUTE',fg='black',width=15,font=15,background='white')
button1.place(x=650,y=280)
img = PhotoImage(file='images/voice_btn.gif')

## Button for taking source input
button2 = Button(a,text='voice',fg='black',width=40,height=30,font=5,background='black',command=voice1,image=img)
button2.place(x=920,y=145)

## Button for taking destination input
button3 = Button(a,text='voice',fg='black',width=40,height=30,font=5,background='black',command=voice2,image=img)
button3.place(x=920,y=200)

a.mainloop()
