from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

app = Flask(__name__)
CORS(app)

# Dummy function to simulate key fetching
# def get_key():
#     # Simulating fetching a key
#     key = os.urandom(16)  # 128-bit AES key
#     key_id = "dummy-key-id"
#     return {"key": base64.b64encode(key).decode('utf-8'), "key_ID": key_id}

def get_key():
    return {
        'key_ID': 'dummy_key_id',
        'key': base64.b64encode(b'16_byte_test_key').decode('utf-8')
    }

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    input_data = request.get_json()
    plaintext = input_data['message']

    # Fetch encryption key
    key_data = get_key()
    key = base64.b64decode(key_data['key'])
    key_id = key_data['key_ID']

    # Encrypt the message
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

    return jsonify({
        "encrypted_message": base64.b64encode(ciphertext).decode('utf-8'),
        "iv": base64.b64encode(iv).decode('utf-8'),
        "key_id": key_id
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
