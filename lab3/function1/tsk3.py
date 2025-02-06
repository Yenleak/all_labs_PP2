def solve(numheads, numlegs):
    rabbit=(numlegs - 2 * numheads) // 2
    chicken=numheads-rabbit
    return f"chikens {chicken}, rabbits {rabbit}"

heads=int(input("Num of heads: "))
legs=int(input("Num of legss: "))
print(solve(heads, legs))

