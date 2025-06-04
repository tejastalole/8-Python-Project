from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"

    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("400x550")
sp.config(bg="Blue")

Label(sp, text="Internet Speed Test", borderwidth=3, relief="ridge", font=("Times New Roman", 20, "bold"), bg="Blue", fg="White").place(x=50, y=40, height=50, width=300)

Label(sp, text="Download Speed", borderwidth=3, relief="ridge", font=("Times New Roman", 20, "bold")).place(x=50, y=130, height=50, width=300)
lab_down = Label(sp, text="00", borderwidth=3, relief="ridge", font=("Times New Roman", 20, "bold"))
lab_down.place(x=50, y=200, height=50, width=300)

Label(sp, text="Upload Speed", borderwidth=3, relief="ridge", font=("Times New Roman", 20, "bold")).place(x=50, y=290, height=50, width=300)
lab_up = Label(sp, text="00", borderwidth=3, relief="ridge", font=("Times New Roman", 20, "bold"))
lab_up.place(x=50, y=360, height=50, width=300)

Button(sp, text="Check Speed", font=("Times New Roman", 20, "bold"), relief=RIDGE, bg="Red", command=speedcheck).place(x=50, y=460, height=50, width=300)

sp.mainloop()
