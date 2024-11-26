<template>
  <div class="app-container dark">
    <!-- Include Watermark and Footer -->
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
  margin-top: 100px; /* Adjust this value to ensure no overlap */
  color: #fff; /* White text for dark mode */
}


</style>
