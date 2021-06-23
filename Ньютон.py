import math
import numpy as np
import sympy as sym



x = sym.Symbol('x')
y = sym.Symbol('y')

f1 = sym.sin(x)+2*y-2
f2 = x+sym.cos(y-1)-0.7


j11=f1.diff(x)
j12=f1.diff(y)
j21=f2.diff(x)
j22=f2.diff(y)
x0=-1
y0=-2
g0=np.array([-1,-2])
j11=sym.lambdify([x,y],j11)
j12=sym.lambdify([x,y],j12)
j21=sym.lambdify([x,y],j21)
j22=sym.lambdify([x,y],j22)
f1=sym.lambdify([x,y],f1)
f2=sym.lambdify([x,y],f2)
for i in range(10): #задается количество итераций
    j=np.array([[j11(x0,y0),j12(x0,y0)],[j21(x0,y0),j22(x0,y0)]])
    #print(j)
    f0=np.array([f1(x0,y0),f2(x0,y0)])
    d0=np.linalg.solve(j, -f0)
    #print(d0)
    g1=d0+g0
    g0=g1
    x0=g0[0]
    y0=g0[1]
    #print(x0,y0)
print(round(g0[0],4),round(g0[1],4))
#f=sym.lambdify([x,y],f1)
#print(f(1,2))
