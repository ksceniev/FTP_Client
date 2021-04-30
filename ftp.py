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
ftp.cwd('/')

def get_file():
    filename = command_list[-1]
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR {}'.format(filename), localfile.write, 2048)
    localfile.close()

while True:
    try:
        command = str(input('ftp> '))
        command_list = command.split(' ')

        if command == 'ls' or command == 'dir':
            ftp.retrlines('LIST')
        
        elif command_list[0] == 'cd':
            ftp.cwd(command_list[-1])
        elif command_list[0] == 'get':
            get_file()

        elif command == 'exit' or command == 'bye':
            ftp.quit()
            break
        else:
            ftp.sendcmd(command)
    
    except:
        continue
