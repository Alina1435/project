from graph import*
brushColor('yellow')
polygon([(30,35),(35,40),(40,35),(35,30),(30,35)])
def vertical(x,y):
    polygon([(x,y),(x-5,y+10),(x,y+20),(x+5,y+10),(x,y)])
brushColor('green')
vertical(35,10)
brushColor('blue')
vertical(35,40)
def horizontal(a,b):
    polygon([(a,b),(a+10,b-5),(a+20,b),(a+10,b+5),(a,b)])
brushColor('red')
horizontal(10,35)
horizontal(40,35)
run()
