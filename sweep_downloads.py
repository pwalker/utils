import os
import subprocess
import datetime

directory = "/home/peterw/Downloads"
files = [ (directory + "/" + f) for f in os.listdir(directory)]

def is_old(f):
    # delta = 7 days
    delta = datetime.timedelta(7)

    # the last thing to happen to this file was 1 week ago
    last_time = datetime.datetime.fromtimestamp(max(os.stat(f).st_atime, os.stat(f).st_mtime)) 
    
    return (last_time + delta) < datetime.datetime.now()

def remove(f):
    subprocess.call(["trash-put",f])
    print(f + " id old!")

# process each file
for f in files:
    if is_old(f):
        remove(f)
