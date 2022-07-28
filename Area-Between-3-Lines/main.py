import math
def point(foo, bar):
    a1, a2, c1, c2 = int(foo[0]), int(bar[0]), int(foo[1]), int(bar[1])
    x = (c2-c1) / (a1-a2)
    y = a1*x + c1
    return (x, y)
equ = [input("Give a and b in the form 'a b' where ax + b is equation 1: ").split(), input("Give a and b in the form 'a b' where ax + b is equation 2: ").split(), input("Give a and b in the form 'a b' where ax + b is equation 3: ").split()]
        
inter = []
inter.append(point(equ[0],equ[1]))
inter.append(point(equ[1],equ[2]))
inter.append(point(equ[0],equ[2]))
print(inter)
a = math.hypot(abs(inter[1][1] - inter[0][1]), abs(inter[1][0] - inter[0][0]))
b = math.hypot(abs(inter[2][1] - inter[1][1]), abs(inter[2][0] - inter[1][0]))
c = math.hypot(abs(inter[2][1] - inter[0][1]), abs(inter[2][0] - inter[0][0]))
print(a, b, c)
ans = 0.5 * b * c * math.sin(math.acos( (a**2 + (-1)*b**2 + (-1)*c**2 ) / (-2*b*c)) )
print(ans)
