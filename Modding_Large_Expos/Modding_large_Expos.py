# Just randomly decided to implement an algorithm I saw on computerphile :--)

a = int(input("Please input the coefficient\n>"))
b = int(input("Please input the power\n>"))
x = int(input("Please input the MOD\n>"))
b = list(map(int, list(bin(b).lstrip("0b"))))
ans = 1
for y in b:
    ans **= 2
    if y == 1:
        ans *= a
    ans %= x
print(ans)
