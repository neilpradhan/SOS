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




// const { defineConfig } = require('@vue/cli-service')

// module.exports = {
//   devServer: {
//     headers: {
//       'Access-Control-Allow-Origin': '*',
//       'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
//       'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
//     }
//   }
// }
