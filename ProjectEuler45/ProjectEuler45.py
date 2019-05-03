import math
num = 144.0;
def quad(a,b, result):
    return (-b + math.sqrt(b* b -4*a*( result)))/(2*a);
while True:
    result = 2*(num * num ) -num;
    pentaNum = quad(1.5,-.5,result *-1);
    triagNum = quad(.5, .5, result * -1);
    isPenta = (triagNum %1) == 0;
    isTriag = (pentaNum %1) ==0;
    if isPenta and isTriag:
        break;
    else :
        num+=1;
print(result);
input();
exit;