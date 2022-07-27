import tkinter as tk

window = tk.Tk()
window.title("Monster Hunter Rise Sunbreak Database")
window.resizable(width=True, height=True)

frame = tk.Frame(master=window, width=200, height=200)
frame.pack()

label1 = tk.Label(master=frame, text="Monster Class", bg="#FFFFFF")
label1.place(x=0, y=0)

button1 = tk.Button(master=frame, text="Flying Wyvern", bg="#87CEEB")
button1.place(x=0, y=0)

button2 = tk.Button(master=frame, text="Fanged Wyvern", bg="#BA55D3")
button2.place(x=0, y=0)

button3 = tk.Button(master=frame, text="Brute Wyvern", bg="#B22222")
button3.place(x=0, y=0)

button4 = tk.Button(master=frame, text="Bird Wyvern", bg="#FAEBD7")
button4.place(x=0, y=0)

button5 = tk.Button(master=frame, text="Piscine Wyvern", bg="#00FFFF")
button5.place(x=0, y=0)

button6 = tk.Button(master=frame, text="Levianth", bg="#7FFFD4")
button6.place(x=0, y=0)

button7 = tk.Button(master=frame, text="Fanged Beast", bg="#B8860B")
button7.place(x=0, y=0)

button8 = tk.Button(master=frame, text="Amphian", bg="#98FB98")
button8.place(x=0, y=0)

button9 = tk.Button(master=frame, text="Carapaceon", bg="#")
button9.place(x=0, y=0)

button10 = tk.Button(master=frame, text="Elder Dragon", bg="#778899")
button10.place(x=0, y=0)

button12 = tk.Button(master=frame, text="Other", bg="black")
button12.place(x=0, y=0)

window.mainloop()
