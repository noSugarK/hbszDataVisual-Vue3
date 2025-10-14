## 运行环境：

- Ubuntu 22.04
- docker 20.10.17
- docker-compose 1.29.2
- MySQL 8.0

## 一键启动：

```shell
docker-compose up -d
```

更改数据库名称和密码

同步更改`docker-compose.yml`文件和`backend/settings.py`文件

密码传输加密(已经写在`backend/docker_start.sh`文件中)

需要先运行该文件生成公钥与私钥，也可以设置定时任务进行更换公私钥

```bash
python backend/generate_keys.py
```
