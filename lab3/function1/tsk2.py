def conVerTocel(F):
    C = (5 / 9) * (F - 32)
    return C

temperature = float(input("write frongate: "))
res = conVerTocel(temperature)
print(f"conversion to celcie: {res}")