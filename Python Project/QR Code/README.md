# QR Code Generator in Python

This project is a simple QR Code generator using Python. It creates a high-quality QR code image for any given URL or text. You can customize the size, colors, and error correction level.

## ✅ Features

- Generate QR code for a given URL or text.
- Customize:
  - Error correction level
  - Box size
  - Border
  - Fill and background color
- Save QR code as an image (e.g., PNG).

## 🛠️ Technologies Used

- `qrcode` – to generate QR codes  
- `Pillow (PIL)` – for image handling

## 💻 Requirements

Make sure you have Python installed, then install required libraries:

```bash
pip install qrcode[pil]
```

## 📄 How It Works

```
import qrcode
from PIL import Image
import qrcode.constants

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR Code
qr.add_data("https://www.google.com/")
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="red", back_color="blue")
img.save("google_qrcode.png")
```

## 📁 Output
The script saves a file named google_qrcode.png with a red QR code on a blue background that links to https://www.google.com/.


## ✍️ Author
Developed by Tejas Talole
