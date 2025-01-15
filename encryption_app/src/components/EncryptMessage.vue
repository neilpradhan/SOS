<template>
  <div class="app-container dark">
    <WatermarkAndFooter />
    <div class="main-content">
      <h1>Message Encryption</h1>
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
        <div v-if="encryptedData" class="result-section">
          <h3>Encrypted Data:</h3>
          <p><strong>Encrypted Message:</strong> {{ encryptedData.encrypted_message }}</p>
          <p><strong>IV:</strong> {{ encryptedData.iv }}</p>
          <p><strong>Key ID:</strong> {{ encryptedData.key_id }}</p>
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
      message: "",
      encryptedData: null,
    };
  },
  methods: {
    async encryptMessage() {
      try {
        const response = await axios.post("http://localhost:5000/encrypt", {
          message: this.message,
        });
        this.encryptedData = response.data;
      } catch (error) {
        console.error("Error encrypting message:", error);
        alert("Failed to encrypt the message.");
      }
    },
  },
};
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 20px;
  margin-top: 100px;
  color: #fff;
}

textarea {
  width: 100%;
  min-height: 100px;
  margin: 10px 0;
  padding: 8px;
  background-color: #2d2d2d;
  color: #fff;
  border: 1px solid #444;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.result-section {
  margin-top: 20px;
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}
</style>