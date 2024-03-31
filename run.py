import paramiko
from scp import SCPClient


openwrt_ip = input('請輸入 OpenWrt IP：')
openwrt_ip = openwrt_ip if openwrt_ip else '192.168.1.18'

username = 'root'
password = 'Zhaorui'
local_file_path = 'vhusbdmips'
remote_file_path = '/tmp/vhusbdmips'

# 創建 SSH 客戶端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(openwrt_ip, username=username, password=password)

    with SCPClient(client.get_transport()) as scp:
        scp.put(local_file_path, remote_file_path)

    command = f'chmod +x {remote_file_path} && {remote_file_path} -b'
    stdin, stdout, stderr = client.exec_command(command , timeout=10)
    output = stdout.read().decode()
    error = stderr.read().decode()

    # print(f'程式執行結果：\n{output}')
    # print(f'錯誤訊息：\n{error}')

    stdin, stdout, stderr = client.exec_command('ps')
    print(stdout.read().decode())
except Exception as e:
    print(f'Error: {e}')

finally:
    client.close()

print('press enter to exit....')
input()

