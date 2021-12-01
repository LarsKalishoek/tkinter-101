import tkinter
window = tkinter.Tk()

window.title("Hello")
window.config(bg= "black")
window.geometry("100x100")

widget = tkinter.Label(
    window,
    text = "Hello\n tkinter!\n", 
    bg = "red",
    fg = "white",
    font= ('Helvetica 12 bold')).place(relx=.2, rely=.2
    
    )
        
window.mainloop()