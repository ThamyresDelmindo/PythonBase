#!/usr/bin/env python

"""Imprime a mensagem de um e-mail

NÃO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, templatename) #email_tmpl.txt

with smtplib.SMTP(host="localhost", port=8025) as server:
    #server.login(username=, password) #Para enviar os emails de verdade
    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read()
            % {
                "nome": name,   
                "produto": "caneta", 
                "texto": "Problemas de má escrita e dores no pulso", 
                "link": "https://canetaslegais.com", 
                "quantidade": 1, 
                "preço": 50.5, 
            }
        )

        from_ = "thamy@del.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
        
