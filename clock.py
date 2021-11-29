# import

from tkinter import Label, Tk 
import time

# making the window

window = Tk() 
window.config(bg = "green")
window.title("Digital Clock") 
window.geometry("150x100") 
window.resizable(1,1)

# editing the numbers
font= ("Helvetica", 12, "bold")
background = "magenta"
foreground= "white"

# making label

label = Label(window, font=font, bg=background, fg=foreground, pady = 10, padx = 40) 
label.grid(row=0, column=1)

# making the clock

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
window.mainloop()