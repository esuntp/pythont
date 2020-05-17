import getpass
import telnetlib


HOST = "0.0.0.0"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open('mySwitches')

for IP in f:
    IP = IP.strip()
    HOST = str(IP)
    print("gGet running config from switch " + HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readOutput = tn.read_all()
    saveOutput = open("switch" + HOST + ".cfg", "w")
    saveOutput.write(readOutput.decode('ascii'))
    saveOutput.write("\n")
    saveOutput.close()



    for n in range (2,11):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")



