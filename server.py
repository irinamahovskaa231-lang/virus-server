from flask import Flask, jsonify, request

app = Flask(__name__)

# Временное хранилище состояния
server_data = {
    "triggered": False,
    "source_code": "Сигнал еще не поступал."
}

@app.route('/signal', methods=['POST'])
def receive_signal():
    global server_data
    data = request.json
    if data and data.get("status") == "triggered":
        server_data["triggered"] = True
        server_data["source_code"] = data.get("source_code", "")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "ignored"}), 400

@app.route('/status', methods=['GET'])
def check_status():
    return jsonify(server_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
