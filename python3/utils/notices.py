import os
import sys
sys.path.append(os.getcwd())

import requests
import smtplib

from email.mime.text import MIMEText
from email.header import Header


def send_ding(token, msg):
    url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(token)
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "msgtype": "text",
        "text": {
            "content": "{}".format(msg),
        }
    }
    try:
        print("Send ding staring...")
        resp = requests.post(url=url, json=params, headers=headers)
        print("Send ding ok! Resp:[{}]".format(resp.content))
    except Exception as e:
        print("Send ding failed! Error:[{}]".format(e))

def send_email(msg):
    sender = 'dusen@hex-tech.net'
    receivers = [
        'dusen@hex-tech.net',
    ] 
    
    text = msg
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("dusen@hex-tech.net", 'utf-8')   
    message['To'] =  Header("supports@hex-tech.net", 'utf-8')        
    
    subject = 'Sync data to kylin'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        print("Send email staring...")
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(EMAIL['host'], 25)    
        smtpObj.login(EMAIL['user'], EMAIL['password'])  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Send email ok!")
    except Exception as e:
        print("Send email failed! Error:[{}]".format(e))

def save_data(sql, values=()):
    conf = POSTGRES
    Postgresql(conf=conf).insert(sql, values=values)

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path, 0o777)

def try_catch(func, func_name=None, *args):
    try:
        func(*args)
    except Exception as e:
        msg = "Sync data to KYLIN [{}] error: [{}] func:[{}]".format(
            WHO, e, func_name,
        )
        send_ding(msg)
        send_email(msg)
        print(msg)
