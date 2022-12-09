import datetime
import time
import os


def mainej4():

    while True:
        os.system('cls')
        tiempo = datetime.datetime.now()
        print(tiempo.hour, ":", tiempo.minute, ":", tiempo.second)
        time.sleep(1)
