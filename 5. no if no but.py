#made this without starting learning the if chapter XD

a=3
if (a==2):
    print("hello")
elif(a!=2):
    print("bye")

#mixing lists with if statements

names=['eenie','minnie','penguiny','mo']
for na in names:
    print(na)

    if(na=="eenie"):
        print(f'hi this is {na}, find me minnie')
    elif(na=="minnie"):
        print(f'hi this is {na}, find me penguiny')
    elif(na=="penguiny"):
        print(f'hi this is {na}, find me mo')
    else:
        print(f'this is {na}, give me any')

