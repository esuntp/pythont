from netmiko import ConnectHandler

ios_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.246',
    'username': 'ehsan',
    'password': 'cisco',
}

net_connect = ConnectHandler(**ios_l2)
output = net_connect.send_command('show ip interface brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (20,29):
    print('Creating VLAN' + str(n))
    config_commands = ['vlan' + str(n), 'name Python_SSH_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)

