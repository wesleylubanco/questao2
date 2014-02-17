import socket
HOST = '192.168.1.37'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
HOST2 = '127.0.0.2'
PORT2 = 5001

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
udp.bind(dest)
orig = (HOST2,PORT2)

print 'Para sair use CTRL+X\n'
manda = ()

while manda <> '\x18':
   manda = raw_input("sua mensagem")
   udp.sendto (manda, dest)
   resposta, cliente = udp.recvfrom(1048)
   print cliente, resposta
         
udp.close()
