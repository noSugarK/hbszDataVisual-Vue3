module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                devhub: {
                    primary: '#1e80ff',    // 主色
                    secondary: '#0e639c',  // 次要色
                    light: '#e8f3ff',      // 浅色背景
                    dark: '#0a4c7c',       // 深色
                    gray: '#f5f7fa',       // 灰色背景
                    text: '#4e5969',       // 文本色
                    darkText: '#1d2129'    // 深色文本
                }
            },
        },
    },
    plugins: [],
}