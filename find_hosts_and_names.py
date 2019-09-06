list_of_hosts = open('list_of_hosts.txt', 'w')
list_of_hosts_array = []
address_book_string = ''
address_book = open('addresses.WBX', 'r')
for line in address_book:
    address_book_string = address_book_string + str(line)
list_of_hosts_string = address_book_string.split('host')
for host in list_of_hosts_string:
    list_of_hosts_array.append(host + str('\n_NEW_HOST_'))

for host in list_of_hosts_array:
    list_of_hosts.write(host)

list_of_hosts.close()
address_book.close()