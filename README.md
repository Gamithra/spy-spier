# gamithra's spy spier

### what is this?
The spy spier is a tool to assist using email tracker pixels and monitor requests sent to the server. It (currently) makes new tracker files, maps them to a recipient and uploads them to the server, downloads logs from the server and checks if the trackers have been requested, outputting the tracker requests along with the IP address and its location.


----
#### usage
Generating trackers: fill out login credentials for ssh in config.py; run

    python3 gen.py

Parsing logs: fill out login credentials for ssh in config.py; run

    python3 main.py

----

## // to-do
* change IP location provider (current one has a request limit)
* make a cronjob out of this and add function to send a mail notification on email pixel trigger
* gmail seems to use some kind of a proxy server to store images now, trackers might not work for gmail; have yet to find a workaround
* save known IPs (oh hey, I've seen you here before)
