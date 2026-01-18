📲 WhatsApp Automation using Twilio (Python)

This project is a WhatsApp Message Automation system built using Python and Twilio API.
It allows users to schedule WhatsApp messages using the datetime module and send them automatically at a specified future time.

🔗 Repository:
https://github.com/Abir-Shaikh/Whatsapp_Automation

🚀 Features

📅 Schedule WhatsApp messages for a future date & time

⏰ Time difference calculation using datetime

📤 Send WhatsApp messages via Twilio WhatsApp API

🧠 Simple Python logic (Beginner-friendly)

❌ Prevents sending messages for past times

🛡️ Basic error handling

🛠️ Technologies Used

Python 3

Twilio REST API

datetime module

time module

📂 Project Structure

Whatsapp_Automation/
│
├── main.py          # Main automation script
├── README.md        # Project documentation
├── .venv/           # Virtual environment (optional)
└── requirements.txt # Dependencies (optional)

🔑 Prerequisites

Make sure you have the following:

Python 3.x

A Twilio Account

Twilio WhatsApp Sandbox enabled

Internet connection

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/Abir-Shaikh/Whatsapp_Automation.git
cd Whatsapp_Automation

2️⃣ Install Required Library
pip install twilio

3️⃣ Configure Twilio Credentials

Open main.py and add your Twilio credentials:

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"


Also update the Twilio sandbox number:

from_='whatsapp:+14155238886'

4️⃣ Join Twilio WhatsApp Sandbox

Go to Twilio Console

Navigate to Messaging → Try it out → WhatsApp

Send the given join <code> message to:

+14155238886

▶️ How to Run the Project
python3 main.py

🧾 Inputs Required

Recipient name

Recipient WhatsApp number (with country code)

Message content

Date (YYYY-MM-DD)

Time (HH:MM – 24 hour format)

📌 Example
Enter the recipient name: Abir
Enter recipient WhatsApp number with country code: +911234567890
Enter the message you want to send: Hello from Python!
Enter the date (YYYY-MM-DD): 2026-01-20
Enter the time (HH:MM): 21:30

Message scheduled to be sent successfully!

⚠️ Limitations

Uses Twilio Sandbox (not production-ready)

Script must remain running until the scheduled time

Not suitable for bulk messaging without Twilio approval

🔮 Future Enhancements

⏳ Replace time.sleep() with proper schedulers

🖥️ GUI or Web interface

📊 Message status tracking

🔐 Environment variables for credentials

📜 Disclaimer

This project is for educational purposes only.
Please comply with Twilio’s WhatsApp messaging policies before production use.

👨‍💻 Author

Abir Shaikh
Learning Python | Automation | APIs 🚀
