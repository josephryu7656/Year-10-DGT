string = "string"
integer = 7
float = 7.25
bool = True
# or 
bool = False

import socket
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error: {e}"
ip = get_ip_address()

print(f"Your IP adress is {ip}")