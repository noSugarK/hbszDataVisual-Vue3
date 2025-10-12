
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

对于nginx服务启动时，会自动生成默认的配置文件，但是默认的配置文件会与my.conf文件冲突。

```bash
root@iZ7xvgzxufp7ob02qclqdsZ:/usr/local/webserver/hbszDataVisual-Vue3# docker-compose logs web-hbsz
Attaching to web-hbsz
web-hbsz       | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
web-hbsz       | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
web-hbsz       | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
web-hbsz       | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
web-hbsz       | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
web-hbsz       | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
web-hbsz       | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
web-hbsz       | /docker-entrypoint.sh: Configuration complete; ready for start up
web-hbsz       | 2025/10/12 18:49:31 [warn] 1#1: conflicting server name "localhost" on 0.0.0.0:80, ignored
web-hbsz       | nginx: [warn] conflicting server name "localhost" on 0.0.0.0:80, ignored
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: using the "epoll" event method
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: nginx/1.21.5
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: built by gcc 10.3.1 20211027 (Alpine 10.3.1_git20211027)
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: OS: Linux 5.15.0-152-generic
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: start worker processes
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: start worker process 32
web-hbsz       | 2025/10/12 18:49:31 [notice] 1#1: start worker process 33
web-hbsz       | 223.75.68.8 - - [12/Oct/2025:18:49:34 +0800] "GET /login HTTP/1.1" 404 555 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0" "-"
web-hbsz       | 2025/10/12 18:49:34 [error] 33#33: *2 open() "/usr/share/nginx/html/login" failed (2: No such file or directory), client: 223.75.68.8, server: localhost, request: "GET /login HTTP/1.1", host: "8.148.253.79"
web-hbsz       | 223.75.68.8 - - [12/Oct/2025:18:49:38 +0800] "GET /api/v1/account/public-key/ HTTP/1.1" 404 555 "http://8.148.253.79/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0" "-"
web-hbsz       | 2025/10/12 18:49:38 [error] 33#33: *2 "/usr/share/nginx/html/api/v1/account/public-key/index.html" is not found (2: No such file or directory), client: 223.75.68.8, server: localhost, request: "GET /api/v1/account/public-key/ HTTP/1.1", host: "8.148.253.79", referrer: "http://8.148.253.79/login"
```

解决方法：

清理冲突配置，确保 Nginx 只加载你的 my.conf
步骤 1：进入 Nginx 容器，查看所有配置文件
先确认 /etc/nginx/conf.d/ 目录下有哪些配置文件，找出冲突源：
```bash
# 进入 web-hbsz 容器
docker exec -it web-hbsz /bin/sh

# 查看 /etc/nginx/conf.d/ 目录下的所有文件
ls -l /etc/nginx/conf.d/
你会看到类似这样的结果（冲突文件通常是 default.conf）：
plaintext
-rw-r--r-- 1 root root  612 Oct 12 10:00 default.conf  # 默认配置（冲突源）
-rw-r--r-- 1 root root 1024 Oct 12 18:00 my.conf       # 你的配置
```
步骤 2：删除或重命名冲突的 default.conf
在容器内部，删除默认的 default.conf（或重命名，避免 Nginx 加载）：
```bash
# 在容器内执行：删除默认配置文件
rm /etc/nginx/conf.d/default.conf

# 或者重命名（更安全，后续可恢复）
mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak
```
步骤 3：重启 Nginx 服务，让配置生效
退出容器后，重启 web-hbsz 服务（确保 Nginx 重新加载配置）：
```bash
# 退出容器（输入 exit 并回车）
exit

# 重启 Nginx 服务
docker-compose restart web-hbsz
```
步骤 4：验证配置是否生效
查看 Nginx 启动日志：重启后查看日志，确认 冲突警告消失：
```bash
docker-compose logs web-hbsz | grep "conflicting server name"
```
如果没有输出，说明冲突已解决。
测试 API 请求：用 curl 测试，或直接访问页面，此时 Nginx 会触发 location /api/ 规则，将请求转发给 Django：
```bash
# 测试 API 请求（注意路径末尾的斜杠可加可不加，Django 通常兼容）
curl -v http://8.148.253.79/api/v1/account/public-key
```
成功标志：curl 输出中会显示 HTTP/1.1 200 OK（或 Django 返回的公钥内容），且 web-hbsz 日志中不再出现 open() "/usr/share/nginx/html/api/..." 错误。
