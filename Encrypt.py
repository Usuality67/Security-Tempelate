import string
Lowercases = string.ascii_lowercase
Uppercases = string.ascii_uppercase
Characters = string.punctuation



def Encrypt(Password):
    stringer = ""

    for x in Password:
        if x in Lowercases:
            for y in range(len(Lowercases)):
                if x == Lowercases[y]:
                    if y <= 12:
                        stringer = stringer+Lowercases[y+13]
                    else:
                        stringer = stringer+Lowercases[y-13]
        elif x in Uppercases:
            for y in range(len(Uppercases)):
                if x == Uppercases[y]:
                    if y <= 12:
                        stringer = stringer + Uppercases[y + 13]
                    else:
                        stringer = stringer + Uppercases[y - 13]
        elif x in Characters:
            for y in range(len(Characters)):
                if x == Characters[y]:
                    if y <= 18:
                        stringer = stringer + Characters[y + 13]
                    else:
                        stringer = stringer + Characters[y - 13]
        else:
            x = int(float(x)) + 13
            stringer = stringer + str(x)[1]

    return stringer



