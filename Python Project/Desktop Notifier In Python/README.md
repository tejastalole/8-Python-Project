# 💧 Python Desktop Water Reminder Notifier

A simple Python script that reminds you to **drink water every 30 minutes** by showing a desktop notification. It's a healthy habit tracker that runs quietly in the background to help you stay hydrated throughout the day.

---

## 🚀 Project Overview

This project uses the `plyer` library to show system notifications with a custom icon and message. The script runs in an infinite loop and reminds the user every 30 minutes to drink 250ML of water.

---

## 🛠️ Technologies Used

- **Python**
- **Plyer** – to send cross-platform desktop notifications
- **Time** – for managing the reminder intervals

---

## 🔧 Features

- ⏰ Automatic desktop notification every 30 minutes
- 💧 Encourages healthy water intake
- 🎨 Custom icon for the notification
- 🖥️ Runs silently in the background
- 🔁 Infinite loop for continuous reminders

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/water-reminder-notifier.git
   cd water-reminder-notifier
   ```

2. **Install Dependencies**
   ```bash
   pip install plyer
   ```

3. **Add your icon**
   Make sure you have an icon file named `icon1.ico` in the same folder as the script.

---

## ▶️ How to Run

To run the script normally:
```bash
python desktopnotifier.py
```

To run it in the background without opening a terminal window (on Windows):
```bash
pythonw desktopnotifier.py
```

> ✅ `pythonw` is used to run Python scripts silently (no terminal pop-up).

---

## 📌 Configuration

- The reminder interval is currently set to `30 minutes`. You can change this by modifying the line:
  ```python
  time.sleep(30 * 60)  # 30 minutes
  ```

- You can change the title, message, and icon of the notification:
  ```python
  notification.notify(
      title = "*** Drink Water ***",
      message="Drink a 250ML Water",
      app_icon = "icon1.ico",
      timeout = 5)
  ```

---

## 🧑‍💻 Author

**Tejas Talole**  
Full Stack Developer | Python Enthusiast  
📧 your-email@example.com

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✅ Tip

- Add this script to **Windows Startup folder** to start automatically on boot.
- Or convert it into an `.exe` using `pyinstaller` for easier distribution.

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile desktopnotifier.py
```

---

**Stay hydrated! Your body will thank you 💧**
