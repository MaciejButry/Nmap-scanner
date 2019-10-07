import nmap

nScan = nmap.PortScanner()
nmap_version = nScan.nmap_version()
print('Welcome to my nmap version: ' + str(nmap_version) + ', scanner tool! ')
print('==================================================')

input_ip = input('Type IP address you want to scan: ')
print('\nPerforming your scan... It might take a few seconds... \n')

nScan.scan(input_ip, '1-1024', '-sV')

for protocol in nScan[input_ip].all_protocols():
    print('Protocol: %s' %(protocol))
    for port in nScan[input_ip][protocol].keys():
        print("Port: %s | State: %s" %(port, nScan[input_ip][protocol][port]['state']))
