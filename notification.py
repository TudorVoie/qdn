import os
import sys
import requests

torrent_name = str(sys.argv[1])
category = str(sys.argv[2])
tags = str(sys.argv[3])
content_path = str(sys.argv[4])
root_path = str(sys.argv[5])
save_path = str(sys.argv[6])
number_of_files = str(sys.argv[7])
torrent_size = str(sys.argv[8])
current_tracker = str(sys.argv[9])
info_hash_v1 = str(sys.argv[10])
info_has_v2 = str(sys.argv[11])
torrent_id = str(sys.argv[12])

#here enter your message, string in between "" and then use + to add the variables from above
#to get pinged, put your user id in between <@ >, like this <@userid21316728312678>
message = ""
#here enter your webhook url
webhook_url = ""

data = {"content":message}
result = requests.post(webhook_url, json = data)