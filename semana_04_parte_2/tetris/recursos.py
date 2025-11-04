import time
import keyboard
import lib_mat_alvaro
import semana_05.tetris.SU as SU
p=[["[] "],
   ["[] "],
   ["[][]"]]
r=1
print("\033[2J\033[H", end="")
while True:
    SU.imprimir_matt(p,r)
    time.sleep(2)
    SU.cls()
    r=r+1



import sys

def gotoxy(x, y):
    # x = columna (1..), y = fila (1..)
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def cls():
    sys.stdout.write("\033[2J\033[H")  # limpia y va a (1,1)
    sys.stdout.flush()
def imprimir_matt(x,ren):
    for i in range(0,3,1):
        gotoxy(15,ren+i)
        print(*x[i])