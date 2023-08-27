const { createProxyMiddleware } = require('http-proxy-middleware')
module.exports = function (app) {
    app.use(
        createProxyMiddleware('/api',
            {
                //target: "http://120.25.254.124",
                target: "http://127.0.0.1:5000",
                changeOrigin: true,
                pathRewrite: { '^/api': '/' }
            }
        ),
    )
}