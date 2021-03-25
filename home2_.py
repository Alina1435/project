from graph import*
def frame(x,y):
    penColor('black')
    brushColor('green')
    rectangle(x,y,x+100,y+100)
def roof(x,y):
    brushColor('brown')
    polygon([(x-10,y),(x+50,y-50),(x+110,y),(x-10,y)])
def window(x,y):
    penColor('white')
    penSize(3)
    brushColor('black')
    rectangle(x+20,y+20,x+50,y+70)
    line(x+20,y+40,x+50,y+40)
    line(x+35,y+40,x+35,y+70)
def home(x,y):
    frame(x,y)
    roof(x,y)
    window(x,y)
print('Введите координаты домика')
x=int(input())
y=int(input())
home(x,y)
run()
