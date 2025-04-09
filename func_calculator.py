def calculator(a,b,op):
    if op =='+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b 
    elif op == '/':
        if b == 0:
            return "에러 : 0으로 나눌 수 없습니다."
        else:
            return a/b
    else:
        return "에러 : 잘못된 연산입니다."