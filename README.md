# 💬 CipherTalk - Secure Chat App with End-to-End Encryption

CipherTalk is a real-time messaging platform inspired by WhatsApp that features:
- 🔒 End-to-End Encryption (RSA + AES)
- 👤 User Authentication (Login/Register)
- 🎨 Light/Dark Theme Toggle
- 😊 Emoji Picker Support
- 📎 File Sharing (Images/Docs)
- ✅ Message Status Ticks (Sent, Delivered, Seen)
- ✍️ Typing Indicator
- 🔑 Forgot Password Support

---

## 📁 Folder Structure

ciphertalk/
├── server.py # Backend server using Flask + Socket.IO
├── encryption.py # AES + RSA encryption logic
├── index.html # Frontend UI (WhatsApp style)
├── database.db # SQLite DB for users and chat (auto-created)
└── README.md # This file


---

## 🚀 How to Run

### ⚙️ Prerequisites
- Python 3.8+
- Flask
- Flask-SocketIO
- cryptography
- eventlet (for production-like Socket.IO)

### 🔧 Installation
```bash
# Install dependencies
pip install flask flask-socketio cryptography eventlet
▶️ Start the App
cd ciphertalk
python server.py
Then open your browser at:
http://192.168.xx.xx:5050/ (your IP address)

Features
Feature	Description
🔐 End-to-End Encryption	AES (symmetric) + RSA (key exchange)
👥 Login/Register	Auth with password validation
🎨 Theme Toggle	Switch between light and dark mode
📎 File Sharing	Send image and document files
✅ Ticks	Message status: ✔ Sent, ✔✔ Delivered, ✔✔ Seen
✍️ Typing Indicator	Shows when the other user is typing
🔑 Forgot Password	Reset password using username check

[Screenshot 2025-07-09 092639]![Screenshot 2025-07-09 091108](https://github.com/user-attachments/assets/08cb29ec-f561-465e-b0b9-c1fcbeab4343)
https://github.com/user-attachments/assets/923662cb-32b3-4845-9a98-003a453418d5

🔒 Security
RSA used for public/private key exchange

AES used to encrypt message content

Messages stored encrypted in DB

🛠️ Future Improvements
✅ Group chat support

🧑‍🤝‍🧑 Online user list

🔔 Notification support

📱 Mobile responsive UI

🤝 Contributing
Fork the repo


Commit your changes (git commit -m 'add feature')

Push to the branch (git push origin feature-name)

Create a Pull Request

📄 License
This project is under the MIT License.

👨‍💻 Developed by
Shanmukha Aditya
Saveetha School of Engineering
Reg No: 192365055
