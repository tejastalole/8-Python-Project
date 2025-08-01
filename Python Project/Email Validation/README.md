# 📧 Python Email Validation Script

A simple Python script to validate email addresses based on a set of custom rules. This script checks whether the entered email follows a basic structure and rules commonly expected in valid email formats.

---

## ✅ Features

- Checks minimum length of email (at least 6 characters)
- Ensures the first character is an alphabet
- Validates presence and count of '@' symbol (only one allowed)
- Ensures '.' is present in the right position (before 3rd or 4th character from end)
- Disallows:
  - Whitespaces
  - Uppercase letters
  - Invalid special characters

---

## 🧠 Logic Used

1. Length of email must be **≥ 6**
2. The first character must be an **alphabet**
3. Email must contain exactly **one '@'**
4. Email must end with either **.com** or **.in**, etc. (3rd or 4th position from last should be '.')
5. The email should not contain:
   - Whitespaces
   - Uppercase letters
   - Special characters other than `@`, `_`, and `.`

---

## 💻 Code Example

```python
email = input("Enter Your Email : ")  # e.g., tejastalole7@gmail.com
k, j, d = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d == 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
```

---

## 📌 Notes

- This is a basic validation script. For production use, consider using Python's `re` module (regex) or libraries like `validate_email`.

---

## 👨‍💻 Author

**Tejas Talole**  
Full Stack Developer | Python Enthusiast  
📧 your-email@example.com

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
