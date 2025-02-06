def calculate(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("write gramms: "))
res = calculate(grams)
print(f"conversion to ounces {res}")