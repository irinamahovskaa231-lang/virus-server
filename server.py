import os
import urllib.request
from flask import Flask, request

app = Flask(__name__)

# Обрати внимание: если ты тестируешь control.py локально, Render не сможет 
# напрямую постучаться на http://localhost:4000/. Для локального теста control.py 
# нужен публичный адрес (например, через ngrok), либо сервер должен быть запущен локально.
CONTROL_URL = "http://localhost:4000/"

@app.route('/', methods=['POST'])
def receive_signal():
    source_code = request.form.get('source')
    print(f"[Server.py] Получен исходник! Длина кода: {len(source_code) if source_code else 0} символов")
    
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
