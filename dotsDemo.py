#Ray Tso
#3/1/18
#dotsDemo.py- how to use loops with graphics

from ggame import *

red=Color('0xFF0000',1)

dot=CircleAsset(25,LineStyle(1,red),red)

for i in range(10):
    Sprite(dot,(10+60*i,10))

App().run()


