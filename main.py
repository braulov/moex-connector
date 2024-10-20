import socket
import struct
import time

import sbe

# Параметры подключения
HOST = 'spectra-t1.moex.com'
PORT = 3001
with open('./simba.xml','r') as f:
    schema = sbe.Schema.parse(f)
message_id = 1000
obj = {}
message = schema.encode(schema.messages[message_id],obj)
print(schema.decode(message))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    # Отправляем сообщение
    s.sendall(message)
    print(f"Message sent: {message}")

    # Получаем ответ
    time.sleep(30)
    response = s.recv(1024)
    print(response)