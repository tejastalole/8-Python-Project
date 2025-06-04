import qrcode as qr
img = qr.make("https://www.youtube.com/@FitwithPranav-Fit_pranav")
img.save("FitWithPranav.png")