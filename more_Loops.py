for i in range(11):
    pass
#we need to understand the purpose of using the pass intruction. - loops always needs to include at least on intruction.

for a in range (1,6):
    for b in range(1,6):
        print(a,'x',b,'=',a*b)

i = 5
while i < 5:
    print(i)
    i+= 1
else:
    print('else', i)