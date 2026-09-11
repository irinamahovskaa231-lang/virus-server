import os
import urllib.request
from flask import Flask, request

app = Flask(__name__)

# СЮДА вставь публичную ссылку, которую тебе выдаст ngrok (например: "https://xxxx.ngrok-free.app/")
CONTROL_URL = "https://ТВОЙ-NGROK-АДРЕС.ngrok-free.app/"

@app.route('/', methods=['POST'])
def receive_signal():
    source_code = request.form.get('source')
    print(f"[Server.py] Получен исходник! Длина: {len(source_code) if source_code else 0} символов")
    
    # Сервер передает сигнал на твой компьютер через ngrok
    try:
        urllib.request.urlopen(CONTROL_URL, timeout=5)
        print("[Server.py] Сигнал успешно передан на control.py!")
    except Exception as e:
        print(f"[Server.py] Не удалось передать сигнал на control.py: {e}")
        
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
