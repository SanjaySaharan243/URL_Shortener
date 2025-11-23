# 🔗 URL Shortener (Flask + Python)

A simple **URL Shortener Web App** built using **Flask**, **HTML**, and **pyshorteners**.  
It supports shortening URLs using TinyURL (no API key required) and also supports Bitly via `.env`.

---

## ✨ Features

✅ Shortens long URLs using TinyURL  
✅ Supports Bitly API (optional)  
✅ Clean HTML interface  
✅ Secure environment variables using `.env`  
✅ Error handling + debugging support  
✅ Easy to deploy & run locally  

---

## 📁 Project Structure

URL-Shortener/
│
├── app.py
├── .env (not uploaded to GitHub)
├── templates/
│ └── form.html
└── README.md

yaml
Copy code

> ⚠️ Important: Your `form.html` must be inside a folder named `templates/`

---

## 📌 Clone the Project

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
🐍 Create & Activate Virtual Environment
On macOS / Linux:
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
On Windows:
bash
Copy code
python -m venv .venv
.venv\Scripts\activate
📦 Install Dependencies
bash
Copy code
pip install flask pyshorteners python-dotenv
🔐 Create .env File
Create a file called .env in the project root:

ini
Copy code
FLASK_SECRET_KEY=your_random_secret_key_here
BITLY_ACCESS_TOKEN=your_bitly_api_key_here   # optional
🔑 How to generate Secret Key:
Run this in Python to generate one:

bash
Copy code
python -c "import secrets; print(secrets.token_hex(32))"
🚀 How to Run the Project
✅ Method 1 (Recommended):
bash
Copy code
python app.py
Open browser and go to:
👉 http://127.0.0.1:5000/

✅ Method 2 (Using Flask CLI):
First tell Flask which file is your app:

macOS / Linux:

bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=5001
Windows:

bash
Copy code
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --port=5001
Open in browser:
👉 http://127.0.0.1:5001/

🖼 HTML Interface
Your form.html file should be located here:

bash
Copy code
/templates/form.html
Example UI:

Input field for long URL

Shortened URL is shown in output field

Clean and minimal UI

🔧 How URL Shortening Works
Currently using:

python
Copy code
pyshorteners.Shortener().tinyurl.short(url)
To use Bitly instead:
Uncomment this in app.py:

python
Copy code
shortener = pyshorteners.Shortener(api_key=BITLY_ACCESS_TOKEN)
short_url = shortener.bitly.short(old_url)
Then set your Bitly API key in .env.

🚫 Important Notes
✅ Do NOT upload .env to GitHub
Add this to .gitignore:

bash
Copy code
.env
✅ Always activate your virtual environment before running the app
✅ Restart Flask server after making changes

👨‍💻 Developed By
Sanjay Saharan
