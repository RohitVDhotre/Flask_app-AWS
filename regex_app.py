from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

matches = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        regex_pattern = request.form.get("regex_pattern")

        if text and regex_pattern:
            try:
                matches.extend(re.findall(regex_pattern, text))
            except re.error as e:
                return render_template("combined_app.html", error=str(e), matches=matches)

    return render_template("combined_app.html", matches=matches)

@app.route('/validate_email', methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form.get("email")

        if email:
            email_pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            is_valid = bool(re.match(email_pattern, email))
            return jsonify({"is_valid": is_valid, "email": email})

    return render_template("combined_app.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)
