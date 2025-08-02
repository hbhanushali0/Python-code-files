
import tkinter
from tkinter import messagebox
from tkinter import *
from gtts import gTTS
import os
from playsound import playsound




def f1():
    language = "en"
    
    myobj = gTTS(text = ent1.get(), lang=language, slow=False)
    myobj.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    
    
    messagebox.showinfo("message", "generated")
    playsound("audio.mp3")
    
    

    

root = Tk()
root.geometry("500x500+500+500")
root.configure(background = "grey")
root.title("Text to Speech")

lbl1 = Label(root, text = "Enter the Text below that you want to convert into Speech",
        font = ("arial", "18", "bold italic"))
        
        
ent1 = Entry(root, bd = 2.5, font = ("arial", 18, "bold italic"))

btn1 = Button(root, text = "Generate", font = ("arial", 18, "bold italic"), command = f1)


lbl1.pack(pady = 10)
ent1.pack(pady = 10)
btn1.pack(pady = 10)


root.mainloop()

