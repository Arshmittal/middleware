from flask import Flask, request, jsonify

app = Flask(__name__)

# Fixed login credentials
VALID_EMAIL = "arshmittal740@gmail.com"
VALID_PASSWORD = "Arsh123#Mittal"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"success": False, "message": "Email and password are required"}), 400

    # Check only against fixed values
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        return jsonify({"success": True, "message": "Login successful!"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid email or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)