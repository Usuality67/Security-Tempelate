import string
Lowercases = string.ascii_lowercase
Uppercases = string.ascii_uppercase
Characters = string.punctuation
def Decryption(Password):
    stringer = ""
    for x in Password:
        if x in Lowercases:
            for y in range(len(Lowercases)):
                if x == Lowercases[y]:
                    if y >= 13:
                        stringer = stringer + Lowercases[y-13]
                    else:
                        stringer = stringer + Lowercases[y+13]
        elif x in Uppercases:
            for y in range(len(Uppercases)):
                if x == Uppercases[y]:
                    if y >= 13:
                        stringer = stringer + Uppercases[y-13]
                    else:
                        stringer = stringer + Uppercases[y+13]
        elif x in Characters:
            for y in range(len(Characters)):
                if x == Characters[y]:
                    if y >= 13:
                        stringer = stringer + Characters[y-13]
                    else:
                        stringer = stringer + Characters[y+13]
        else:
            if int(float(x)) > 2:
                x = str(int(float("1" + x)) - 13 )
            else:
                x = str(int(float("2"+x))-13)
            stringer = stringer + x
    return stringer




