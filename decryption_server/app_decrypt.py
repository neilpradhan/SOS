from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os

app = Flask(__name__)
CORS(app)

# Dummy function to simulate key fetching by key ID
def get_key_using_keyid(key_id):
    # Simulating fetching a key
    key = base64.b64encode(os.urandom(16)).decode('utf-8')  # Match encryption key structure
    return {"key": key}

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    input_data = request.get_json()
    encrypted_message = base64.b64decode(input_data['encrypted_message'])
    iv = base64.b64decode(input_data['iv'])
    key_id = input_data['key_id']

    # Fetch decryption key using key_id
    key_data = get_key_using_keyid(key_id)
    key = base64.b64decode(key_data['key'])

    # Decrypt the message
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

    return jsonify({"message": decrypted_message.decode('utf-8')}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
