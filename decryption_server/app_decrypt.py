from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# def get_key_using_keyid(KEY_ID):
#     # Define the URL
#     url = "https://192.36.164.182/api/v1/keys/alice_client1/dec_keys?key_ID="+KEY_ID

#     # Define the paths to the certificates and key
#     ca_cert = "rootCA_auth.crt"
#     client_cert = "bob_client1.crt"
#     client_key = "bob_client1.key"

#     # Set the headers
#     headers = {
#         "Content-Type": "application/json"
#     }

#     # Make the request with the certificates and key
#     response = requests.get(
#         url,
#         headers=headers,
#         cert=(client_cert, client_key),
#         verify=ca_cert
#     )

#     result = response.json()
#     return result['keys'][0]

def get_key_using_keyid(key_id):
    return {
        'key': base64.b64encode(b'16_byte_test_key').decode('utf-8')
    }

def decrypt_data(encrypted_data):
    try:
        encrypted_message = base64.b64decode(encrypted_data['encrypted_message'])
        iv = base64.b64decode(encrypted_data['iv'])
        key_id = encrypted_data['key_id']

        # Fetch decryption key
        key_data = get_key_using_keyid(key_id)
        key = base64.b64decode(key_data['key'])

        # Decrypt the message
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)
        
        return {"message": decrypted_message.decode('utf-8')}
    except Exception as e:
        return {"error": str(e)}

@socketio.on('decrypt_message')
def handle_decrypt_message(encrypted_data):
    result = decrypt_data(encrypted_data)
    socketio.emit('decrypted_message', result)

if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True)