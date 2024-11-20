<template>
  <div class="app-container">
    <h1>Message Encryption/Decryption</h1>

    <!-- Encryption Section -->
    <section>
      <h2>Encrypt a Message</h2>
      <form @submit.prevent="encryptMessage">
        <label for="message">Enter Message:</label>
        <textarea
          id="message"
          v-model="message"
          placeholder="Write your message here"
        ></textarea>
        <button type="submit">Encrypt</button>
      </form>
      <div v-if="encryptedData">
        <h3>Encrypted Data:</h3>
        <p><strong>Encrypted Message:</strong> {{ encryptedData.encrypted_message }}</p>
        <p><strong>IV:</strong> {{ encryptedData.iv }}</p>
        <p><strong>Key ID:</strong> {{ encryptedData.key_id }}</p>
        <button @click="autoDecrypt">Decrypt Immediately</button>
      </div>
    </section>

    <!-- Decryption Section -->
    <section v-if="decryptedMessage || encryptedData">
      <h2>Decrypted Message:</h2>
      <p v-if="decryptedMessage">{{ decryptedMessage }}</p>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "", // Plaintext message to encrypt
      encryptedData: null, // Stores encrypted message, IV, and key ID
      decryptedMessage: "", // Decrypted message output
    };
  },
  methods: {
    // Encrypt the plaintext message
    async encryptMessage() {
      try {
        const response = await axios.post("http://localhost:5000/encrypt", {
          message: this.message,
        });
        this.encryptedData = response.data; // Store encrypted data
        this.decryptedMessage = ""; // Reset decrypted message
      } catch (error) {
        console.error("Error encrypting message:", error);
        alert("Failed to encrypt the message.");
      }
    },

    // Automatically decrypt the encrypted data
    async autoDecrypt() {
      if (!this.encryptedData) {
        alert("No encrypted data to decrypt.");
        return;
      }

      try {
        const response = await axios.post("http://localhost:5001/decrypt", {
          encrypted_message: this.encryptedData.encrypted_message,
          iv: this.encryptedData.iv,
          key_id: this.encryptedData.key_id,
        });
        this.decryptedMessage = response.data.message; // Display decrypted message
      } catch (error) {
        console.error("Error decrypting message:", error);
        alert("Failed to decrypt the message.");
      }
    },
  },
};
</script>

<style scoped>
.app-container {
  margin: 20px;
  font-family: Arial, sans-serif;
}

form {
  margin-bottom: 20px;
}

textarea,
input {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

section {
  margin-bottom: 40px;
}

h1,
h2 {
  color: #333;
}
</style>
