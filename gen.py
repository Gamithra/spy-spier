import subprocess
import paramiko
import random
import string
from scp import SCPClient
import os

from config import *


def createSSHClient(server, port, user, key_filename):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    key = paramiko.RSAKey.from_private_key_file(key_filename)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, pkey=key)
    return client


def transfer_tracker(name):
    ssh = createSSHClient(ssh_server, ssh_port, ssh_user, ssh_key_location)
    scp = SCPClient(ssh.get_transport())
    print("SSH and SCP established!")

    scp.put(tracker_folder + name + ".png", server_web_root + server_tracker_folder)
    print(name + ".png copied to destination folder of remote server")


def register_tracker(name, recipient):
    with open(register_file, 'a') as file:
        file.write(str(recipient) + ";" + name +'\n')
    print("Saved tracker " + name + " for recipient " + recipient + " in " + register_file)


def generate():
    name = input("Specify tracker name (leave open to generate random string): ")
    recipient = input("Recipient of the tracker (to look them up later): ")
    if name == "":
        name = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(12))

    if not os.path.isdir('./trackers'):
        subprocess.Popen(("mkdir " + tracker_folder).split())

    subprocess.Popen(("cp " + tracker_file + " " + tracker_folder + name + ".png").split())
    print("Generated " + name + ".png in the local folder " + tracker_folder)

    transfer_tracker(name)
    register_tracker(name, recipient)
    print("Your tracker is at:")
    print(server_name + server_tracker_folder + name + ".png")


if __name__ == "__main__":
    generate()
