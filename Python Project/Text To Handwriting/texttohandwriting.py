import pywhatkit as pw

txt = "quick brown fox jump over the lazy dog"

pw.text_to_handwriting(txt, "demo1.jpg", [0,0,138])
pw.text_to_handwriting(txt)
print("END")