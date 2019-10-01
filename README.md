# gamithra's spy spier

### what is this?
The spy spier is a tool to assist using email tracker pixels and monitor requests sent to the server. It (currently) parses Apache logs, bulks similar entries together and outputs the location of the IP address.


----
#### usage
set LOG\_DIRECTORY and LOG\_FILE variables in _main.py_ to Apache log file location; run

    python3 main.py

----

## // to-do
* save config variables
* save known IPs
* change IP location provider
* generate email tracker pixels
* add function to send a mail notification on email pixel trigger
* filter out bots


