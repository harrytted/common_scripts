"""
启动minio服务
1、docker直接启动
第一步：
mkdir -p /data/minio/config
mkdir -p /data/minio/data

宿主机与容器挂载映射
宿主机位置	容器位置
/data/minio/config	/data
/data/minio/data	/root/.minio

第二步
docker run -p 9000:9000 -p 9001:9001 --name minio \
-d --restart=always \
-e "MINIO_ACCESS_KEY=admin" \
-e "MINIO_SECRET_KEY=admin123456" \
-v /data/minio/data:/data \
-v /data/minio/config:/root/.minio \quay.io/minio/minio:RELEASE.2022-08-02T23-59-16Z \
server /data --console-address ":9001"

# 使用最新版镜像minio/minio
docker run -p 9000:9000 -p 9090:9090 --name minio \
-d --restart=always \
-e "MINIO_ACCESS_KEY=admin" \
-e "MINIO_SECRET_KEY=admin123456" \
-v /data/minio/data:/data \
-v /data/minio/config:/root/.minio \minio/minio \
server /data --console-address ":9090"
2、docker-compose
docker-compose up -d
"""