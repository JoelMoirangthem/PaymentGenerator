import qrcode

# Step 1: Take the UPI ID as input from the user
upi_id = input("Enter your UPI ID: ")

# Step 2: Define the payment URL based on the UPI ID and payment app
# Format: upi://pay?pa={upi_id}&pn={name}&mc={merchant_code}
# pa = Payee Address (UPI ID)
# pn = Payee Name (Recipient Name)
# mc = Merchant Code (Optional, used 1234 as example)

# Constructing URLs for different apps (The core UPI link format is the same)
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Step 3: Generate QR Codes using the make() function
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Step 4: Save the QR Codes as image files (Optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Step 5: Display the QR Codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()