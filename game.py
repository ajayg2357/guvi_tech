from random import choice
from string import ascii_lowercase
n=''.join(choice(ascii_lowercase)for i in range(6))
f=list(n)
bull=0
c=0
while c<15:
    bull=0
    cock=0
    i=str(input('Enter a word'))
    l=list(i)
    while len(l)!=6:
        print('you have to enter only 6 letters word')
        i=str(input())
        l=list(i)
    for h in range(6):
        for g in range(6):
            if(l[h]==f[g]):
                cock=cock+1
    for m in range(6):
        if(l[m]==f[m]):
            bull=bull+1
            cock=cock-1
    print('no. of characters that are correct, but in wrong place{}'.format(cock))
    print('no. of characters that are correct and in correct place{}'.format(bull))
    c+=1
    if(c<15):
        print('you have {}chances left'.format(15-c))
    elif(c==15):
        print('you have crossed all the chances, the answer is {}'.format(n))   
    if(bull==6):
        print('Congrats! you found the word. The answer is{}'.format(n))
        break
