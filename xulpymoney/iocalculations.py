def same_sign(number1, number2):
    if (is_positive(number1)==True and is_positive(number2)==True) or (is_positive(number1)==False and is_positive(number2)==False):
        return True
    return False

def is_positive(number):
    if number>=0:
        return True
    return False

def process(op):
    cur=[]
    hst=[]

    print("Processing {}".format(op))

    for position, io in enumerate(op):
        if same_sign(sum(cur), io)==True:
            cur.append(io)
        elif same_sign(sum(cur), io)==False:
            rest=io
            while(rest!=0 and len(cur)!=0):
                first=cur[0]
                if same_sign(first, rest)==False:
                    if abs(first)>abs(rest):
                        hst.append(-rest)
                        cur.pop(0)
                        if rest+first!=0:
                            cur.insert(0, rest+first)
                        rest=0
                    else: #Mayor el resto
                        hst.append(-first)
                        rest=rest+first
                        cur.pop(0)
    #                print("     REST", rest, "Current", cur, "Historical", hst)
                else:
                    cur.insert(0, rest)
                    break
            if rest!=0:
                cur.insert(0, rest)
        print("  + IO", io, "Current", cur, "Historical", hst)
    print("")

process([1,-1,-2,2,3,4,-7,-3,-4,7]) #Exacto
process([1,-2,2,-3,4]) #Cambio signo
process([1,1,-3, -1, 5]) #Cambio signo generando 2 hst
