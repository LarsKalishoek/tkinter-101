import tkinter
window = tkinter.Tk()

colors = ["yellow", "orange", "red", "purple", "black"]
length = 50
width  = 50
x = 0

def updateWindow():
    global x, length, width
    length += 50
    width += 50
    print(5-x)
    window.config(bg = colors[x])
    window.geometry(str(width)+"x"+str(length))
    x += 1

window.title("My First Window")
window.config(bg = "white")
window.geometry("50x50")
print("6")
for y in range(1, 6):
    window.after(2000*y, updateWindow)
def boom():
    print("BOOM!")
    window.destroy()
window.after(12000, boom)

window.mainloop()