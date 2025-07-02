from flask import Flask, render_template, request, jsonify
from main import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
