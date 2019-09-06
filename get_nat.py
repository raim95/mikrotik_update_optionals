import connect
nat = connect.session(cmd = '/ip/firewall/nat/print')

f = open ('stdout.txt', 'w')
for elem in nat:
    f.write(str(elem))
f.close()