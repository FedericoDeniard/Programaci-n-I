def decode(message: str, flag = False) -> str:
    for i in range(len(message)):
        if message[i] == "(":
            return message[:i] + decode(message[i+1:][::-1], True) 
        elif message[i] == "(" and flag == True:
            return message[:i] + decode(message[i+1:]) 
        elif message[i] == ")":
            return message[:i] + decode(message[i+1:])
    return message
        

print(decode('hola (odnum)'))
print(decode('(olleh) (dlrow)!'))
print(decode('sa(u(cla)atn)s'))



