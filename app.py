from flask import Flask, request, jsonify

# Create Flask app instance
app = Flask(__name__)

# ----------------------------
# ROUTES
# ----------------------------

# 1️⃣ Home route
@app.route('/')
def home():
    return "<h1>Welcome to the Collaborative Flask App!</h1>", 200


# 2️⃣ Health check route
@app.route('/health')
def health():
    return jsonify(status="OK"), 200


# 3️⃣ POST route to handle data
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    if not data:
        return jsonify(error="No JSON data provided"), 400

    # New logic — extract fields and respond
    name = data.get("name", "Anonymous")
    age = data.get("age", "unknown")

    return jsonify(
        message=f"Hello {name}, age {age}. Data processed successfully!",
        received=data
    ), 200
# ----------------------------
# MAIN ENTRY POINT
# ----------------------------
if __name__ == '__main__':
    # Run app on host 0.0.0.0 for Docker compatibility
    app.run(host='0.0.0.0', port=5000, debug=True)
