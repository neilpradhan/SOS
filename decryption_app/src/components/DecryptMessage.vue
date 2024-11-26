<template>
  <div class="app-container dark">
    <!-- Include Watermark and Footer -->
    <WatermarkAndFooter />

    <div class="main-content">
      <h1>Message Decryption</h1>
      <section>
        <h2>Decrypt a Message</h2>
        <button @click="decryptMessage">Decrypt Message</button>
        <div v-if="decryptedMessage" class="result-section">
          <h3>Decrypted Message:</h3>
          <p>{{ decryptedMessage }}</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import WatermarkAndFooter from "./WatermarkAndFooter.vue";
import axios from "axios";

export default {
  components: { WatermarkAndFooter },
  data() {
    return {
      decryptedMessage: "", // Final decrypted message
    };
  },
  methods: {
    async decryptMessage() {
      try {
        // Step 1: Fetch encrypted data from PC 1
        const encryptedDataResponse = await axios.get("http://localhost:5000/get-encrypted-data");

        // Step 2: Extract encrypted message, IV, and Key ID
        const { encrypted_message, iv, key_id } = encryptedDataResponse.data;

        // Step 3: Decrypt the message on PC 2
        const decryptionResponse = await axios.post("http://localhost:5001/decrypt", {
          encrypted_message,
          iv,
          key_id,
        });

        // Step 4: Display the decrypted message
        this.decryptedMessage = decryptionResponse.data.message;
      } catch (error) {
        console.error("Error during decryption:", error);
        alert("An error occurred during the decryption process.");
      }
    },
  },
};
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 20px;
  margin-top: 100px; /* Adds space between watermark and content */
  color: #fff; /* White text for dark mode */
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
}

button:hover {
  background-color: #0056b3;
}

.result-section {
  margin-top: 20px;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}
</style>
