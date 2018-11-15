import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect("192.168.70.10", username="gryffindor_user_3", password="gryffindor", port=1337)
    print("Connected!")
except Exception as e:
    print("Couldn't connect: {}".format(e))
