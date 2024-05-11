import socket

def get_info():
    while True:
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
        # En cas d'exception Erreur lors de l'envoi du message: [Errno 104] Connection reset by peer
        except Exception as e:
            print("Erreur lors de la reception du message:", e)
            return None, None

def get_my_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    return IPAddr

if __name__ == "__main__":
  # Exemple d'utilisation
  # Attend la reception d'un message
  ip, received_message = get_info()
  print("Votre adresse IP :", get_my_ip())
  print("Adresse IP de l'expediteur:", ip)
  print("Message reçu:", received_message)