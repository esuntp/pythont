from netmiko import ConnectHandler

ios_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'ehsan',
    'password': 'cisco',
}

with open('cisco_conf_file') as configFile:
    lines = configFile.read()
print(lines)

net_connect = ConnectHandler(**ios_l2)
output = net_connect.send_config_set(lines)
print(output)
