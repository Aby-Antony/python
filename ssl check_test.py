import OpenSSL
import ssl
import datetime

lines=[]
fileobj=open("domains.txt") 
for line in fileobj:
    lines.append(line.strip()) 
    for i in lines:
        cert=ssl.get_server_certificate((i, 443))
        decod = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)   
        expiry_date = datetime.datetime.strptime(decod.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')
    print(i, expiry_date)
