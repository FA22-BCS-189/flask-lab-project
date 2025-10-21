from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list to store book entries (temporary, not database)
library = []

@app.route('/')
def home():
    return render_template('home.html', books=library)

@app.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title', '').strip()
    rating = int(data.get('rating', 0))
    review = data.get('review', '').strip()

    if not title or not review:
        return jsonify(error="Please enter both a book title and review."), 400

    entry = {"title": title, "rating": rating, "review": review}
    library.append(entry)
    return jsonify(success=True, message="Book added successfully!", books=library), 200

# ✅ Health check route for CI/CD
@app.route('/health')
def health():
    return jsonify(status="OK"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
