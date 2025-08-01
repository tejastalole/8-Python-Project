# 👁️🖱️ Eye Controlled Mouse using Python

This Python project lets you **control your mouse pointer using eye movements** and **click with a blink** using a webcam! It uses **MediaPipe's Face Mesh** to detect eye landmarks and **PyAutoGUI** to move the cursor and perform clicks.


## 📸 How It Works
- Tracks your eye movement using a webcam.

- Moves the mouse pointer based on the position of your right eye.

- Detects a blink of the left eye to trigger a mouse click.

## 🛠️ Technologies Used
- OpenCV – For webcam access and image processing

- MediaPipe – For real-time face and eye landmark detection

- PyAutoGUI – To control mouse cursor and simulate clicks

## 📦 Installation
Install the required libraries with pip:

``` pip install opencv-python mediapipe pyautogui```


## ▶️ How to Run
```
python eye_controlled_mouse.py 
```
- Make sure your webcam is active.

- Look at different parts of the screen to move the cursor.

- Blink your **left eye** to simulate a mouse click.

## 📄 Code Overview

```
cv2.VideoCapture(0)                   # Start webcam
mp.solutions.face_mesh.FaceMesh()    # Initialize face mesh detector
pyautogui.moveTo()                    # Move mouse to calculated coordinates
pyautogui.click()                     # Click on blink detection
```

## 🧠 How Blink is Detected

Using two left eye landmarks:
- If the vertical distance between them is very small (i.e., eye is closed), it triggers a ```click()```.

## 📌 Notes

- Make sure you have good lighting for better facial landmark detection.

- Adjust the blink sensitivity by changing the condition:

```
if (left[0].y - left[1].y) < 0.004:
```

## 👤 Author

**Tejas Talole**

This project is part of real-time computer vision experiments using Python.
