from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'temp_screen.jpg'

@app.route('/upload_screen', methods=['POST'])
def upload_screen():
    if 'file' in request.files:
        file = request.files['file']
        file.save(UPLOAD_FOLDER)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

@app.route('/get_screen', methods=['GET'])
def get_screen():
    if os.path.exists(UPLOAD_FOLDER):
        return send_file(UPLOAD_FOLDER, mimetype='image/jpeg')
    return "No image yet", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
