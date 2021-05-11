import argparse
from ftplib import FTP

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    return args.ip, args.port

ip, port = argument_parser()
user = str(input('[*] Please insert USER: '))
passwd = str(input('[*] Please insert PASS: '))

ftp = FTP(host=ip, user=user, passwd=passwd)
ftp.set_debuglevel(2)
print(ftp.getwelcome())
print('[*]?/help')
ftp.cwd('/')

def download_file():
    filename = command_list[-1]
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR {}'.format(filename), localfile.write, 2048)
    localfile.close()

def upload_file():
    filename = command_list[-1]
    localfile = open(filename, 'rb')
    ftp.storbinary('STOR {}'.format(filename), localfile.read, 2048)
    localfile.close()

while True:
    try:
        command = str(input('ftp> '))
        command_list = command.split(' ')

        if command == '?' or command == 'help':
            print('Commands:\n\n- ls, dir -> List the current directory\n- cd <DIRECTORY> -> Change to chosen directory\n- get <FILENAME> -> Download FILENAME from the server\n- exit -> Quit FTP connection\n')

        elif command == 'ls' or command == 'dir':
            ftp.retrlines('LIST')
        
        elif command_list[0] == 'cd':
            ftp.cwd(command_list[-1])
        
        elif command_list[0] == 'get':
            download_file()
        elif command_list[0] == 'put':
            upload_file()

        elif command == 'exit' or command == 'bye':
            ftp.quit()
            break
        else:
            ftp.sendcmd(command)
    
    except:
        continue
