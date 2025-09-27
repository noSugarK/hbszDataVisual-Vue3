
环境准备：

Ubuntu 22.04
docker 20.10.17
docker-compose 1.29.2
MySQL 8.0

一键启动：
```shell
docker-compose up -d
```

更改数据库名称和密码

同步更改`docker-compose.yml`文件和`backend/settings.py`文件

密码传输加密(已经写在`backend/docker_start.sh`文件中)

需要先运行该文件生成公钥与私钥，也可以设置定时任务进行更换公私钥

```bash
python backend/apps/account/generate_keys.py
```

开发环境下需要修改'web/vite.config.js'文件

```javascript
        proxy: {
            // 将 /api 开头的请求代理到后端服务器
            '/api': {
                target: 'http://localhost:8000', // Django后端地址
                changeOrigin: true,
                // 重写路径，去掉 /api 前缀（如果需要的话）
                rewrite: (path) => path.replace(/^\/api/, '')
            }
        }
```
