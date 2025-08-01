# 🔒 Shutdown App using Python (Tkinter)

This is a simple GUI-based Shutdown Utility app built using Python and Tkinter. The app allows users to perform system-level operations like Shutdown, Restart (immediate and delayed), Logout, and Lock the workstation.

## 🚀 Features

- 🔁 Restart your system instantly.
- ⏱️ Restart after a 20-second delay.
- 🔒 Lock the screen.
- 🔌 Shutdown the system.
- 👤 Logout from the current user session.
- Easy-to-use graphical interface.

## 🛠️ Tech Stack

- Python 🐍
- Tkinter (Python GUI Library)
- OS Module (for executing system commands)

## 📦 Requirements

Make sure Python is installed on your system. No external libraries are needed.

```bash
python --version
```

## ▶️ How to Run

1. Copy the code to a Python file, e.g., shutdown_app.py
2. Run the file:
   ```bash
   python shutdown_app.py
   ```
   - ⚠️ Important: Some operations (shutdown, restart, etc.) may require administrator privileges on Windows.
  
## 🧠 How It Works
Each button is bound to a specific function:
- shutdown() → Shuts down the computer.
- restart() → Restarts immediately.
- restart_time() → Restarts with a 20-second delay.
- logout() → Logs out the current user.
- lock() → Locks the computer screen.

All commands use os.system() with appropriate Windows shutdown options.

## 👤 Author
Developed by Tejas Talole
