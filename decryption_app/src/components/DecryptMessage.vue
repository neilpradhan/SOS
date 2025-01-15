<template>
  <div class="app-container dark">
    <WatermarkAndFooter />
    <div class="main-content">
      <h1>Message Decryption</h1>
      <section>
        <h2>Decrypted Messages</h2>
        <div class="messages-container">
          <div v-for="(message, index) in messages" :key="index" class="message-item">
            <p class="timestamp">{{ message.timestamp }}</p>
            <p class="content">{{ message.content }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import WatermarkAndFooter from "./WatermarkAndFooter.vue";
import { io } from "socket.io-client";

export default {
  components: { WatermarkAndFooter },
  data() {
    return {
      messages: [],
      encryptSocket: null,
      decryptSocket: null,
    };
  },
  created() {
    // Connect to both WebSocket servers
    this.encryptSocket = io("http://localhost:5000");
    this.decryptSocket = io("http://localhost:5001");

    // Listen for new encrypted messages
    this.encryptSocket.on("new_encrypted_message", (encryptedData) => {
      // Forward to decryption server
      this.decryptSocket.emit("decrypt_message", encryptedData);
    });

    // Listen for decrypted messages
    this.decryptSocket.on("decrypted_message", (data) => {
      if (data.message) {
        this.messages.unshift({
          content: data.message,
          timestamp: new Date().toLocaleTimeString(),
        });
      }
    });
  },
  beforeUnmount() {
    // Clean up socket connections
    if (this.encryptSocket) this.encryptSocket.disconnect();
    if (this.decryptSocket) this.decryptSocket.disconnect();
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

.messages-container {
  margin-top: 20px;
}

.message-item {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  padding: 15px;
  margin-bottom: 10px;
}

.timestamp {
  font-size: 0.8em;
  color: #888;
  margin-bottom: 5px;
}

.content {
  margin: 0;
  word-break: break-word;
}
</style>