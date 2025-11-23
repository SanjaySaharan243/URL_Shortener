import os
import traceback
from flask import Flask, render_template, request
import pyshorteners
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Validate env variables early
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
BITLY_ACCESS_TOKEN = os.getenv("BITLY_ACCESS_TOKEN")

if not FLASK_SECRET_KEY:
    # For dev: fail fast so you notice missing key
    print("WARNING: FLASK_SECRET_KEY not set in .env")

app.secret_key = FLASK_SECRET_KEY or "dev-secret-key"

@app.route("/", methods=["GET", "POST"])
def home():
    error_msg = ""
    new_url = ""
    old_url = ""
    if request.method == "POST":
        try:
            old_url = request.form.get("url", "").strip()
            if not old_url:
                raise ValueError("No URL provided")

            # Use TinyURL (no API key required)
            short_url = pyshorteners.Shortener().tinyurl.short(old_url)

            # If you want Bitly (requires valid BITLY_ACCESS_TOKEN):
            # shortener = pyshorteners.Shortener(api_key=BITLY_ACCESS_TOKEN)
            # short_url = shortener.bitly.short(old_url)

            new_url = short_url

        except Exception as e:
            # Capture full traceback for debugging
            tb = traceback.format_exc()
            print("=== Exception occurred ===")
            print(tb)            # This prints to terminal
            # Show a friendly (but detailed) message in the page so you can debug
            error_msg = f"{str(e)}\n\nFull traceback:\n{tb}"

    return render_template("form.html", old_url=old_url, new_url=new_url, error=error_msg)

if __name__ == "__main__":
    app.run(debug=True)   # choose 5001 or any free port

