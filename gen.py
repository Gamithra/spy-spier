import subprocess
import paramiko
import random
import string
from scp import SCPClient
import os

from config import *
from util import *


def transfer_tracker(name):
    ssh, scp = create_connection()
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
