import OpenSSL
import ssl
import datetime
import csv
import pandas

fileobj=open("domains.txt") 
f = open("output.txt", "w", newline='')
lines=[]
for line in fileobj:
    lines.append(line.strip()) 
    for i in lines:
        cert=ssl.get_server_certificate((i, 443))
        decod = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)   
        expiry_date = datetime.datetime.strptime(decod.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')
    print(i, "|", expiry_date,file=f)

import pandas
f = open("output.txt")
df=pandas.read_table("output.txt", delimiter = "|")
df.columns = ['Domain', 'Expiry']
df.to_excel("book4.xlsx", index=False, header=True)