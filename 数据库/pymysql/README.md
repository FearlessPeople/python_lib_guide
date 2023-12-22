# 使用案例

```python

dbconfg = {
    'host': '127.0.0.1',
    'username': 'root',
    'password': '123456',
    'port': 3306,
    'db': 'test',
    'charset': 'utf8mb4'
}
server = SSHTunnelForwarder(
    ssh_address_or_host=('127.0.0.1', 45535),
    ssh_username='admin',
    ssh_password='2893823',
    local_bind_address=('127.0.0.1', 9704),
    remote_bind_address=(dbconfg['host'], dbconfg['port'])
)

# 使用堡垒机
db = MySQL(dbconfg, ssh_tunnel=server)
# 不使用堡垒机
db = MySQL(dbconfg)

```