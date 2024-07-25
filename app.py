from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    
    # Process the user text and generate a list of results
    # For demonstration, we'll simply split the text into words
    result = user_text.split()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
