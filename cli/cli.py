import sys
import os

# This must be the absolute first thing that happens.
# bcoz python is a bitch at imports handling. doesnt allow me to use relative paths.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from core import formatter
from core import requester as mailboy
from core import dbm

# Initialization
parser = argparse.ArgumentParser(prog="mailboy", description="API client")

# Args adding.
# "help=" adds the help menu.
# "type=" specifies the type it accepts.
# ("-x", "--xxxxxx") can be used to specify long and short args. 
parser.add_argument("method",nargs="?", help="HTTP method: GET POST PUT DELETE")
parser.add_argument("url",nargs="?", help="Request URL")
parser.add_argument("-H", "--header", action="append", help="Header in Key:Value format. Repeatable.")
parser.add_argument("-b", "--body", help="Request body as JSON string")
parser.add_argument("-l", "--list", action="store_true", help="Lists all the requests made.")
parser.add_argument("-d", "--delete", action="store_true", help="Deletes all the requests made.")

# Compiling the args
args = parser.parse_args()

# Execution based on flags placed.
if args.list:
    rows = dbm.get_history()
    for row in rows:print(*row, end='\n')

elif args.delete:
    if input("Delete all history?(y/n) : ").lower() == 'y':
        dbm.delete()
        print("All Records Deleted.")

elif args.method and args.url:
    print("Method : ",args.method)
    print("URL : ",args.url)
    print("Headers : ",args.header)
    print("Body : ",args.body)

    request_info = (args.method, args.url, args.header, args.body)
    output = mailboy.send(*request_info)
    formatted = formatter.response_formatter(output)
    print(formatted)
    dbm.input_record(request_info, output)