def evaluate1(s):
    nums=[]
    symbol=[]
    presedence={"+":1,"-":1,"*":11,"/":11}
    i=0
    while(i<len(s)):
        
        if s[i].isdigit():
            num=""
            while i<len(s)and s[i].isdigit():
                num+=s[i]
                i+=1
            nums.append(int(num))
        else:
            while(symbol and presedence[symbol[-1]]>=presedence[s[i]]):
                n1=nums.pop()
                n2=nums.pop()
                op=symbol.pop()
                if op=="+":
                    nums.append(n1+n2)
                elif op=="-":
                    nums.append(n2-n1)
                    
                elif op=="*":
                    nums.append(n1*n2)
                elif op=="/":
                    nums.append(n2//n1)
            symbol.append(s[i])        
            i+=1
    while symbol:
        n1=nums.pop()
        n2=nums.pop()
        op=symbol.pop()
        if op=="+":
            nums.append(n1+n2)
        elif op=="-":
            nums.append(n1-n1)
            
        elif op=="*":
            nums.append(n1*n2)
        elif op=="/":
            nums.append(n1//n2)
    return nums


s="8/2+4/3*7" 
x=evaluate1(s)
print(x)
