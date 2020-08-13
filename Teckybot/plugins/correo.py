#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random
import smtplib 
from email.mime.text import MIMEText

def execute(*args):
    var=args[0]
    print(var)
    print()
    mensaje = MIMEText(str(var) ) 
    emisor = "ciro482@gmail.com" 
    receptor = args[1]
    mensaje['From']=emisor 
    mensaje['To']=receptor 
    mensaje['Subject']="Ingreso" 
    serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
    serverSMTP.ehlo() 
    serverSMTP.starttls() 
    serverSMTP.ehlo() 
    serverSMTP.login(emisor,"Pollos23$$") 
    serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
    serverSMTP.close()
    return 'set_slot listo'

