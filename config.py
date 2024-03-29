
server_name = "https://example.com/" # used to return the tracker's address
server_web_root = "/var/www/html/" # web root folder of your server
server_tracker_folder = "hi/" # where the trackers will be stored on the remote server
server_log_location = "/here/are/logs/logfile" # server access log, for example /etc/httpd/logs/access_log
server_home = "/home/user/" # used to store a temporary file


tracker_folder = "trackers/" # local folder where the tracker files will be copied
logs_folder = "logfiles/"


ssh_server = "server.com" # ssh server address
ssh_port = 22
ssh_user = "user" # must have the correct to permissions to write in the target directory of the server
ssh_key_location = "/secret/location/key.pem" # location of your ssh key


tracker_file = "image.png" # the file that will be uploaded to the server
register_file = "register.txt" # file where tracker-recipient files will be stored
