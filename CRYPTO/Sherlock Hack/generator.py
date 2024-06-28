from scapy.all import *
import pickle
import base64
import zlib

# Crear una trama Ether con Scapy
ether_frame = Ether(dst='08:00:27:ff:ff:ff', src='00:11:22:33:44:55')

# Agregar una capa IP
ip_layer = IP(src='192.168.1.1', dst='8.8.8.8')  # Definir las direcciones IP de origen y destino

# Agregar una capa TCP con datos de FTP
tcp_layer = TCP(sport=1234, dport=21)  # Establecer los puertos fuente y destino (puerto 21 para FTP)
ftp_data = "USER hacker\nPASS UEIA{C1b3rS3gUr1d4d_3s_1mp0rt4nt3!@}\nLIST\n"  # Datos de ejemplo para comandos FTP

# Combinar las capas Ethernet, IP y TCP con los datos de FTP
ether_ip_tcp = ether_frame / ip_layer / tcp_layer / Raw(load=ftp_data)

# Serializar la trama Ethernet con las capas IP, TCP y datos FTP, comprimir los datos
serialized_frame = pickle.dumps(ether_ip_tcp)
compressed_frame = zlib.compress(serialized_frame)

# Codificar los datos comprimidos en base64
encoded_data = base64.b64encode(compressed_frame).decode('utf-8')

print(encoded_data)
