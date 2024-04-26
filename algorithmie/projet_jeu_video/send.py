import socket

def send_info(ip, message):
   try:
       # Creation d'un socket TCP/IP
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           # Connecte le socket a l'adresse IP et au port 12345
           s.connect((ip, 12345))
           # Envoie le message
           s.sendall(message.encode())
       print("Message envoye avec succès.")
    # En cas d'exception
   except Exception as e:
       print("Erreur lors de l'envoi du message:", e)

if __name__ == "__main__":
    send_info("172.16.41.42", "miaou")