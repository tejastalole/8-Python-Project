# 🖋️ Text to Handwriting Converter

This project demonstrates how to convert plain text into a handwritten-style image using the Python library ```pywhatkit.```

## 📌 Features
- Converts any text into a handwriting-styled image.

- Customizable ink color using RGB values.

- Saves output as a .jpg file.

## 🧰 Requirements
- Python 3.x

- ```pywhatkit```

- ```OpenCV``` (automatically installed with ```pywhatkit```)

- ```Pillow``` (optional but recommended)

## 📦 Installation
Install dependencies using pip:

``` pip install pywhatkit ```

## 🚀 How to Use

```
import pywhatkit as pw

txt = "quick brown fox jump over the lazy dog"

# Save handwritten image with custom color (RGB format)
pw.text_to_handwriting(txt, "demo1.jpg", [0, 0, 138])

# Optionally, just display in default black color
pw.text_to_handwriting(txt)

print("END")
```

## 📌 Notes
- The third argument [0, 0, 138] defines the ink color in RGB.
- Default location for saved image is the project folder unless full path is provided.

## 🙋‍♂️ Author
**Tejas Talole** <br>
Feel free to use, modify, and share.
