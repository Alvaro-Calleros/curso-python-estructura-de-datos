import sys

def gotoxy(x, y):
    # x = columna (1..), y = fila (1..)
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def cls():
    sys.stdout.write("\033[2J\033[H")  # limpia y va a (1,1)
    sys.stdout.flush()
def imprimir_matt(m,ren,f,x):
    for i in range(0,f,1):
        gotoxy(x,ren+i)
        print(*m[i])