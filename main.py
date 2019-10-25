import re
from json import load
from urllib.request import urlopen
from dateutil.parser import parse
import subprocess
from datetime import datetime

from config import *
from util import *

TIME_ERROR = 60

last_log = -1
last_IP = ''
last_visit = {}


def fetch_log():
    global last_log
    timestamp = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
    ssh, scp = create_connection()

    ssh.exec_command("sudo cp " + server_log_location + " " + server_home + "tracker-tmp")
    scp.get(server_home + "tracker-tmp", logs_folder + log_name + "-" + timestamp)
    ssh.exec_command("sudo rm " + server_home + "tracker-tmp")
    last_log = log_name + "-" + timestamp
    print("Fetched latest log file!")


def fetch_time(timestamp):
    result = parse(timestamp[:11] + " " + timestamp[12:])
    return result


def fetch_location(ip):
    url = 'http://ipinfo.io/' + ip + '/json'
    try:
        response = urlopen(url)
        data = load(response)

        org = data['org']
        city = data['city']
        country = data['country']
        region = data['region']

        result = 'Country: {2}, City: {3}, Region: {1}, Org: {0}'.format(org, region, country, city, ip)

    except:
        result = "could not fetch"

    return result


def check_duplicate(IP, new_time):
    global last_visit, TIME_ERROR

    if IP in last_visit:
        diff = new_time - last_visit[IP]
        time_difference = diff.total_seconds()
    else:
        time_difference = TIME_ERROR*2;

    last_visit[IP] = new_time
    last_IP = IP

    if time_difference > TIME_ERROR:
        return True
    return False



def read_log():
    log = open(logs_folder+last_log, "r")
    if log.mode == "r":

        contents = log.readlines()
        for line in contents:
            format_entry(line)


def get_tracker_name(recipient):
    registry = open(register_file, "r")
    if registry.mode == "r":
        contents = registry.readlines()
        for line in contents:
            if recipient in line:
                line = line.strip().split(";")
                return line[1]


def format_entry(line):
    line = line.split(" ")
    IP = line[0]
    timestamp = line[3][1:] + " " + line[4][:-1]
    new_time = fetch_time(timestamp)

    if check_duplicate(IP, new_time):
        data = fetch_location(IP)
        print("Requesting " + line[6] + " from " + IP + " at " + timestamp)
        print(data, "\n")



def search_log():
    recipient = input("Recipient of tracker: ")
    name = get_tracker_name(recipient)
    print("Looking for tracker called " + name)

    log = open(logs_folder+last_log, "r")
    if log.mode == "r":

        contents = log.readlines()
        for line in contents:
            if name in line:
                format_entry(line)


if __name__ == "__main__":
    fetch_log()
    search_log()
