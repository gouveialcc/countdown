import datetime
from fileinput import close
import time

def countdown(h, m, s):
    # Calcula o total de segundos
    total_seconds = h * 3600 + m * 60 + s
 
    # Verifica se o total de segundos alcanca zero
    # se nao estiver em zero, decrementa o valor do tempo total em um segundo.
    while total_seconds > 0:
 
        # Timer representa o tempo restante do countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Printa o tempo restante do Timer
        print(timer, end="\r")
 
        # Atrasa o inicio do countdown
        time.sleep(1)
 
        # Reduz o tempo total em um segundo
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
 
# Entrada para hora, minuto e segundos no Timer
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))

quit()