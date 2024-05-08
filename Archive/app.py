from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():

    if request.is_json:
        data = request.get_json()
        print(data)
        text = data.get('text', '')
        
        response = {"message": f"Received text: {text}"}
        return jsonify(response), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)


