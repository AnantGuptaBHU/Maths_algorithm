import math
class Number():
    def __init__(self,num):
        self.num=num
    def sphenicNumber(self):
        n=self.num
        sph=0
        s=0
        while n % 2 == 0:
            s+=1
            n = n / 2
        if s==1:
            sph+=1
        for i in range(3,int(math.sqrt(n))+1,2):
            s=0
            while n%i==0:
                n=n/i
                s+=1
            if s>1:
                return False
            if s==1:
                sph+=1
        if n > 2 :
            sph+=1
        if sph == 3 :
            return True
        else:
            return False
n=Number(30)
print(n.sphenicNumber())