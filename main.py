# string = "string"
# integer = 7
# float = 7.25
# bool = True
# # or 
# bool = False

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance


def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


# Grab IP Adress of the user running the program
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
    # Print Errors
        return f"Error: {e}"
ip = get_ip_address()

print(f"Your IP adress is {ip}")

printDetails(ip)
