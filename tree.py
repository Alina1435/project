from graph import*
def triangle(x,y,a,b):
    polygon([(x,y),(x+a,y+b),(x-a,y+b)])
brushColor('green')
penColor('green')
triangle(150,120,80,120)
triangle(150,60,60,60)
triangle(150,30,60,30)
triangle(150,240,120,240)
run()
