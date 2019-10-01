import re
from json import load
from urllib.request import urlopen
from dateutil.parser import parse

LOG_DIRECTORY = "logfiles/"
LOG_FILE = "access_log"
TIME_ERROR = 60

last_IP = ''
last_visit = {}

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
    log = open(LOG_DIRECTORY+LOG_FILE, "r")
    if log.mode == "r":

        contents = log.readlines()
        for line in contents:
            line = line.split(" ")

            IP = line[0]
            timestamp = line[3][1:] + " " + line[4][:-1]
            new_time = fetch_time(timestamp)

            if check_duplicate(IP, new_time):
                data = fetch_location(IP)
                print("Requesting " + line[6] + " from " + IP + " at " + timestamp)
                print(data, "\n")

read_log()
