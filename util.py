import paramiko
from scp import SCPClient
from config_local import *

def createSSHClient(server, port, user, key_filename):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    key = paramiko.RSAKey.from_private_key_file(key_filename)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, pkey=key)
    return client

def create_connection():
    ssh = createSSHClient(ssh_server, ssh_port, ssh_user, ssh_key_location)
    scp = SCPClient(ssh.get_transport())
    print("SSH and SCP established!")
    return ssh, scp
