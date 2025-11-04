import time
import keyboard
import lib_mat_alvaro
import SU
#import SO
filas=3
cols=4
p=[["[]  "],
   ["[]  "],
   ["[][]"]]

pd=[["[]  "],
   ["[]  "],
   ["[][]"]]

p_2=[["[]    "],
     ["[][][]"]]

pr=[["[][][]"],
    ["[]    "]]

pl=[["    []"],
    ["[][][]"]]

r=1
x=15

print("\033[2J\033[H", end="")

while True:
   SU.imprimir_matt(p,r,filas,x)
   time.sleep(0.5)
   SU.cls()
   r=r+1
   if keyboard.is_pressed("q"):
        break
   elif keyboard.is_pressed("e"):
      p=p_2
      filas=2
   elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
      x-=1
   elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
      x+=1
   elif keyboard.is_pressed("w") or keyboard.is_pressed("up"):
      p=pr
      filas=2
   elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
      p=pl
      filas=2
   elif keyboard.is_pressed("c") or keyboard.is_pressed("down"):
      p=pd
      filas=3