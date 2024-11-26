const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})



module.exports = {
  devServer: {
    proxy: {
      '/encrypt': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
      '/decrypt': {
        target: 'http://localhost:5001',
        changeOrigin: true,
      },
    },
  },
};
