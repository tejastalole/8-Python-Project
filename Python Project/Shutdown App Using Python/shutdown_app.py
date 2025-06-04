from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")  # Restart immediately

def restart_time():
    os.system("shutdown /r /t 20")  # Restart after 20 seconds

def logout():
    os.system("shutdown -l")  # Logout user

def shutdown():
    os.system("shutdown /s /t 1")  # Shutdown immediately

def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock screen

st = Tk()
st.title("Shutdown App")
st.geometry("400x520")  # Increased height to fit Lock button
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart)
r_button.place(x=100, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Timer", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=100, y=150, height=50, width=200)

lg_button = Button(st, text="Log Out", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=100, y=240, height=50, width=200)

st_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=100, y=330, height=50, width=200)

lock_button = Button(st, text="Lock", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=lock)
lock_button.place(x=100, y=420, height=50, width=200)  # Added lock button

st.mainloop()
