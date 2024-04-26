import socket

def get_info():
   try:
       # Creation d'un socket TCP/IP
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           # Lier le socket au port 12345
           host = socket.gethostname()
           port = 12345
           print("host :", host+",", "port :", port)
           s.bind((host, port))
           # Etre en ecoute des connexions entrantes
           s.listen()
           print("En attente de connexion...")
           conn, addr = s.accept()
           with conn:
               print("Connexion etablie avec", addr)
               # Obtenir les donnees du client
               data = conn.recv(1024)
               message = data.decode()
               return addr[0], message
    # En cas d'exception 
   except Exception as e:
       print("Erreur lors de la reception du message:", e)
       return None, None

if __name__ == "__main__":
  # Exemple d'utilisation
  # Attend la reception d'un message
  ip, received_message = get_info()
  print("Adresse IP de l'expediteur:", ip)
  print("Message reçu:", received_message)