import os
import urllib.request
from flask import Flask, request

app = Flask(__name__)

# URL твоего control.py (если тестируешь локально, нужен ngrok-адрес для control.py)
CONTROL_URL = "http://localhost:4000/"

@app.route('/', methods=['POST'])
def receive_signal():
    source_code = request.form.get('source')
    print(f"[Server.py] Получен исходник от клиента! Длина кода: {len(source_code) if source_code else 0} символов")
    
    # Передаем сигнал дальше на control.py
    try:
        urllib.request.urlopen(CONTROL_URL, timeout=3)
        print("[Server.py] Сигнал успешно передан на control.py")
    except Exception as e:
        print(f"[Server.py] Не удалось передать сигнал на control.py: {e}")
        
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)