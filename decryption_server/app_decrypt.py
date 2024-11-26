# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# import base64
# import os

# app = Flask(__name__)
# CORS(app)

# # Dummy function to simulate key fetching by key ID
# # def get_key_using_keyid(key_id):
# #     # Simulating fetching a key
# #     key = base64.b64encode(os.urandom(16)).decode('utf-8')  # Match encryption key structure
# #     return {"key": key}

# def get_key_using_keyid(key_id):
#     # Return a mock response for testing
#     return {
#         'key': base64.b64encode(b'16_byte_test_key').decode('utf-8')
#     }

# @app.route('/decrypt', methods=['POST'])
# def decrypt_message():
#     input_data = request.get_json()
#     encrypted_message = base64.b64decode(input_data['encrypted_message'])
#     iv = base64.b64decode(input_data['iv'])
#     key_id = input_data['key_id']

#     # Fetch decryption key using key_id
#     key_data = get_key_using_keyid(key_id)
#     key = base64.b64decode(key_data['key'])

#     # Decrypt the message
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

#     return jsonify({"message": decrypted_message.decode('utf-8')}), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os

app = Flask(__name__)
CORS(app)

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
    # Replace with actual key fetching logic
    return {
        'key': base64.b64encode(b'16_byte_test_key').decode('utf-8')
    }

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    try:
        # Parse JSON input
        input_data = request.get_json()
        encrypted_message = base64.b64decode(input_data['encrypted_message'])
        iv = base64.b64decode(input_data['iv'])
        key_id = input_data['key_id']

        # Fetch decryption key
        key_data = get_key_using_keyid(key_id)
        key = base64.b64decode(key_data['key'])

        # Decrypt the message
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)

        return jsonify({"message": decrypted_message.decode('utf-8')}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": "Invalid input format"}), 400
    except Exception as e:
        return jsonify({"error": "Decryption failed", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
