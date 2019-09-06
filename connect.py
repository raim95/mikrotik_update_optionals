import librouteros
import getpass

#host = input("Write host: ")
#username = input("Write username: ")
#passwd = getpass.getpass()

try:
    session = librouteros.connect(username='raim', password=getpass.getpass(), host='alpl.ml')
    input("Connection success")
except:
    input("Could not connect to alpl.ml")