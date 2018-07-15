import random as rand
def Question(e,o,ans,i,co):
    rand.shuffle(o)
    print e
    t=' '
    for k in range(len(o)):
        if ans==o[k]:
            if k==0:
               t='a'
            elif k==1:
                t='b'
            elif k==2:
                t='c'
            else:
                t='d'
    print'(A) %s  (B) %s  (C) %s  (D) %s'%(o[0],o[1],o[2],o[3]),
    b=raw_input('-->')
    if((ord(b)>64) and(ord(b)<69) or (ord(b)>96) and(ord(b)<101)):
       if (b=='b')or(b=='B'):
          b=1
       elif(b=='a')or(b=='A'):
          b=0
       elif(b=='c')or(b=='C'):
          b=2
       else:
          b=3
       b=o[b]
       if b==ans:
          print'Great',
          co=co+1
       else:
          print'oops!',
          i=i+1
    else:
         print'please enetr the valid option'
         i,co,t=Question(e,o,ans,i,co)
    return i,co,t   
i=0
co=0 
f=[] 
e='What is the unit digit in 7^105 ?'
a='1'
b='5'
ans=c='7'
d='9'
o=[a,b,c,d]
i,co,t=Question(e,o,ans,i,co)
f.append(t)
print 
print'incorrect= %d correct= %d'%(i,co)
e="The unit digit in the product (784 x 618 x 917 x 463) is:"
ans=a='2'
b='3'
c='4'
d='5'
o=[a,b,c,d]
i,co,t=Question(e,o,ans,i,co)
f.append(t)
print
print'incorrect= %d correct= %d'%(i,co)
e='Which of the following numbers will completely divide (4^61 + 4^62 + 4^63 + 4^64)?'
a='3'
ans=b='10'
c='11'
d='13'
o=[a,b,c,d]
i,co,t=Question(e,o,ans,i,co)
f.append(t)
print
print'incorrect= %d correct= %d'%(i,co)
e='106 x 106 - 94 x 94 = ?'
ans=a='2400'
b='2000'
c='1904'
d='1906'
o=[a,b,c,d]
i,co,t=Question(e,o,ans,i,co)
f.append(t)
print
print'incorrect= %d correct= %d'%(i,co)
print
print'          --wait--'
print
print'if you want to generate answer key then press Y  if not then press any keya'
y=raw_input('-->')
if y=='y'or y=='Y':
    for j in range(1,len(f)+1):
        print str(j)+'.'+f[j-1]
else:
    print'thank you for giving the tset'