# 💸 PaymentGenerator (UPI QR Code Generator)

A simple and efficient **Python** project that generates custom UPI QR codes for major payment applications like **Google Pay**, **PhonePe**, and **Paytm**.

This tool takes a user's UPI ID as input and automatically creates scannable QR codes that can be used to accept payments directly.

---

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Output](#output)

---

## 📖 About the Project
In the digital payment era, having a quick way to share payment details is essential. **PaymentGenerator** automates the creation of standard UPI QR codes.

It uses the `qrcode` library in Python to encode the standard UPI link format (`upi://pay?pa=...`) into an image. When scanned by any UPI app, these codes automatically fill in the recipient's details.

---

## ✨ Features
* **Multi-App Support:** Generates separate QR codes for Google Pay, PhonePe, and Paytm.
* **User Input:** Accepts any valid UPI ID (e.g., `username@oksbi`, `mobile@ybl`).
* **Instant Generation:** Creates and saves `.png` images in milliseconds.
* **Preview:** Automatically displays the generated QR code upon creation.

---

## ⚙️ Prerequisites
To run this project, you need the following installed on your system:
* **Python 3.x**
* **Pip** (Python Package Installer)

---

## 🚀 Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/JoelMoirangthem/PaymentGenerator.git](https://github.com/JoelMoirangthem/PaymentGenerator.git)
    cd PaymentGenerator
    ```

2.  **Install Required Libraries**
    This project uses the `qrcode` library (with `pillow` for image handling).
    ```bash
    pip install qrcode[pil]
    ```

---

## 💻 Usage

1.  **Run the Script**
    Execute the main Python file:
    ```bash
    python code.py
    ```

2.  **Enter Details**
    * The terminal will prompt you to enter your **UPI ID**.
    * *Example:* `joel@oksbi`

3.  **Get Results**
    * The script will generate three image files in the current folder.
    * It will also open the images for you to view.

---

## 📂 Project Structure

```text
PaymentGenerator/
├── code.py              # Main Python script for generating QRs
├── google_pay_qr.png    # Generated QR for Google Pay
├── paytm_qr.png         # Generated QR for Paytm
├── phonepe_qr.png       # Generated QR for PhonePe
└── README.md            # Project documentation
