# transformar decimal em haxadecimal ou hexadecimal para decimal
def he_deci(d):# funçao para coverter hexadecimal para decimal
    d = int(d, 16)
    return d

while True:
    nu = input()
    if nu != '-1':
        if 'x' in nu:
            converter = he_deci(d=nu)
            print(converter)

        elif nu != 'x':
            converter = hex(int(nu))
            print(converter)

    else:
        print('')
        break