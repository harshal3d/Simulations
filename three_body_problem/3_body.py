import turtle 

class charge:
    def __init__(self,x,y,charge=1,mass = 1,color="white"):
        self.x = x
        self.y = y
        self.charge = charge
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.pensize(2)
        self.t.shape('circle')
        self.t.shapesize(0.1)
        self.t.goto(x,y)
        self.mass = mass
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

    def set_color(self,color):
        self.t.color(color)

    def set_vel(self,vel):
        self.vx = vel[0]
        self.vy = vel[1]

    def update_pos(self):
        self.x += self.vx
        self.y += self.vy
        self.t.goto(self.x,self.y)

    def update_vel(self):
        self.vx = self.vx + self.ax
        self.vy = self.vy + self.ay

    def update_acc(self,F):
        self.ax = F[0]/self.mass
        self.ay = F[1]/self.mass

    def calc_force(self,other):
        k = 10
        dx = - self.x  + other.x
        dy = - self.y  + other.y
        r2 = (dx)**2  + (dy)**2
        r3 = r2**(3/2)

        return [k*dx/r3,k*dy/r3]

    def update_xva(self,Force):
        self.update_acc(Force)
        self.update_vel()
        self.update_pos()


wn = turtle.Screen()
wn.bgcolor("black")

q=charge(30,3,mass=5,color='black')
q.set_vel([0,-0.1])

p=charge(-30,6,mass=2,color='black')
p.set_vel([0,0.1])

r = charge(200,200,mass=25,color='black')
r.set_vel([0,0])

i = 10000
p.set_color("white")
q.set_color("yellow")
r.set_color("red")
while i > 0:

    F1 = q.calc_force(p)
    F2 = q.calc_force(r)
    F3 = p.calc_force(r)
    Fq = [F1[0]+F2[0],F1[1]+F2[1]]
    Fp = [-F1[0]+F3[0],-F1[1]+F3[1]]
    Fr = [-F2[0]-F3[0],-F2[1]-F3[1]]
    q.update_xva(Fq)
    p.update_xva(Fp)
    r.update_xva(Fr)
    
    """print('p:',str((p.x,p.y)))
    print('q:',str((q.x,q.y)))
    print('r:',str((r.x,r.y)))"""
    i-=1

wn.exitonclick()
