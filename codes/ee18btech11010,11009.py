import numpy as np
import matplotlib.pyplot as plt

p = np.zeros(2)#Point A in matrix form
p[0] = 4
p[1] = 1

q = np.zeros(2)
q[0] =0
q[1] =1

r = np.zeros(2)
r[0]=1
r[1]=0

X = np.vstack((q,r)) #The reflection matrix which is equivalent ofreflection about the line y=x)
Y = np.matmul(X,p) #The transformed point of A to Y

l = np.zeros(2)#Transformation(not linear) Matrix for the translation of point Y to Z.  
l[0] = 2
l[1] = 0

Z = Y + l #The transformed point of Y


w = np.zeros(2)
w[0] = 1/(np.sqrt(2))
w[1] = 1/(np.sqrt(2))

o = np.zeros(2)
o[0] = -1/(np.sqrt(2))
o[1] = 1/(np.sqrt(2))
 
O = np.vstack((w,o)) #Rotation transformation matrix which is equivalent to the rotation of point Z to U by 45 degrees in anticlockwise sense.

U = np.matmul(O,Z)  #The final point.

print (U)

x=np.linspace(0,10,100)
y=x
plt.plot(x,y,label='$x - y = 0$')
A=np.array([4,1])
P1=np.array([1,4])
P2=np.array([3,4])
P3=np.array([4.94,0.707])
plt.plot(A[0],A[1],'o')
plt.plot(P1[0],P1[1],'o')
plt.plot(P2[0],P2[1],'o')
plt.plot(P3[0],P3[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A(4,1)')
plt.text(P1[0]*(1+0.1),P1[1]*(1-0.1),'P1(1,4)')
plt.text(P2[0]*(1+0.1),P2[1]*(1-0.1),'P2(3,4)')
plt.text(P3[0]*(1+0.1),P3[1]*(1-0.1),'P3(4.94,0.707)')
plt.grid()
plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.show()

