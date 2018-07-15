#why this is not working in the program###--doubt
#a={}
#b=raw_input('-->')
#if(b.count(' ')==0):
#    print b
#print b
#a[b]='none'
#print a
print'enter the no. of entries you wnat to enter' 
t=input('-->') 
b=[]
d={}
for i in range(t):
    a=raw_input('entry '+str(i+1)+' :')
    if len(a)>0:
       if (a.count(' ')==0):
          d[a]='None'
          c=0
       else:
          b.append(a.split())
          d1=dict(b)
          d.update(d1)
if len(d)>0:
   print
   print'press 1:for update'
   print'press 2:for insert'
   print'press 3:for delete'
   print'press 4:for view result'
   print'press 5:for exit'
   print
   def Update(d):
       print'enter the key to which you want to perforn updation and also new value to that key',
       k1=raw_input('1st enter key :'),
       k1=list(k1)
       if k1[0] in d:
          k2=raw_input('2nd enter new value :'),
          k2=list(k2)
          d[k1[0]]=k2[0]
       else:
         print'----please enter the valid key-----'
       return d
   def Insert(d):
        print'enter the key to which you want to perform insertion and also value to that key',
        k1=raw_input('1st enter key :'),
        k1=list(k1)
        k2=raw_input('2nd enter new value :'),
        k2=list(k2)
        d[k1[0]]=k2[0]
        return d
   def Delete(d):
        print'enter the key to which you want to perfrom deletion',
        k1=raw_input('1st enter key :'),
        k1=list(k1)
        if k1[0] in d:
          del d[k1[0]]
        else:
            print'---key does not exists----'
        return d
   while 1:
       print'enter your choice',
       a=input('-->')
       if((a>0)and(a<6)):
           if(a==1):
              d=Update(d)
           elif(a==2):
              d=Insert(d)
           elif(a==3):
             d=Delete(d)
           elif(a==4):
              print d
           else:
               print
               print'thank you!'
               break
       else:
          print'----please choose the correct option----'
else:
    print'---please enter data(entry) first----'