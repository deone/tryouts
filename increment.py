f = open('ip_addresses.txt', 'r+')

for i in range(254):
    f.write('172.22.126.' + str(i+1) + '\n')

f.close()
