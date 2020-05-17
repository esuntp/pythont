import getpass
import telnetlib


def getSwitchCredentials():
    user = input("Enter your remote account: ")
    password = getpass.getpass()
    return user, password

def telentSwitch(swHost, swUsername, swPassword):
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


f = open ('mySwitches')
swUsername: str
swPassword: str

swUsername, swPassword = getSwitchCredentials()

for IP in f:
    IP=IP.strip()
    HOST=str(IP)
    telentSwitch(HOST, str(swUsername), str(swPassword))


    tn.write(b"conf t\n")

    for n in range (2,11):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
