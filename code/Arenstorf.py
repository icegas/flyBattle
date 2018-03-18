from MathModel import MathModel

class Arenstorf(MathModel):
    
    def __init__(self, t0, t1, steps, y0):
        super().__init__(t0, t1, steps, y0)
               

    def model(self, y, t):
        y[0, 0] = y[1, 0] * y[1, 1]
        y[1, 0] = y[0, 1] + y[0, 2] * y[1, 1]
        res =  [ y[0, 0], y[0, 1], y[0, 2] , y[1, 0], y[1, 1] ] 
        return res
'''    a=0.012277471; b=1.0-a;    
        D1=((y[0]+a)**2+y[1]**2)**(3.0/2);
        D2=((y[0]-b)**2+y[1]**2)**(3.0/2);
        res = [y[2],\
               y[3],\
               y[0]+2.0*y[3]-b*(y[0]+a)/D1-a*(y[0]-b)/D2, \
               y[1]-2.0*y[2]-b*y[1]/D1-a*y[1]/D2
               ]
    
        return res'''