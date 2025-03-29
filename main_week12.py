from mammal import Mammal
from Person_W12 import Person
from tick import Tick
from puma import Puma

m=Mammal(10)
m.speak()
#d=m.__str__()
print(m)

p=Person("John Doe",20,6)
p.speak()
p.heart.beat()

t = Tick()
t.suck_blood()
print(t)

pm = Puma(5,t)
pm.tick.suck_blood()

