import datetime
import numpy as np

MINUTES = 5
MONTHS = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

time = datetime.datetime.now() - datetime.timedelta(minutes=5)
old_time = str(time.time()).split(".")[0][:-2]
s = old_time.split(":")
times = []
for i in range(MINUTES + 1):
    new_s = s.copy()
    new_s[1] = str(int(s[1]) + i)
    times.append(":".join(new_s))

ssh_string = "sshd["
password_accepted_line = "accepted password"


with open("/var/log/auth.log", "r") as f:
    lines = f.readlines()

for line in lines:
    if ssh_string in line.lower() and password_accepted_line in line.lower():
        if np.any([time in line.lower() for time in times]):
            print("user entered: {}".format(line))