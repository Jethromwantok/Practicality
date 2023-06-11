import tkinter as tk

window = tk.Tk()
window.title("My Own GUI")
window.geometry("800x500")

frame=tk.Frame(master=window)
frame.pack()
label= tk.Label(master=frame, text="Hello World!")
label.pack(padx=20, pady=20)
#.pack is used to show what the label code topic on the GUI
#(padx and pad y ) is used to give padding to whatever its topic is on the x and y axes respectively

textbox=tk.Text(master=frame, height=3, width=20)
textbox.pack(pady=20)
#.Text is to introduce a text box and the window is the parent topic


entry=tk.Entry(master=frame, text="put in your phone number")
entry.pack(pady=20)

Button1=tk.Button(frame, text='Push Here')
Button1.pack()

window.mainloop()