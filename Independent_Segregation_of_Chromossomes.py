def binomial_prob(n:int, k:int, p:float) -> float:
    from math import comb
    return comb(n, k) * p**k * (1-p)**(n-k)
    

if __name__ == "__main__":
    from math import log10, floor
    n = 2 * int(input("Insert Number: "))
    probs = []
    prob = 0
    for k in range(n, 0, -1):
        prob += binomial_prob(n, k, 0.5)
        probs.append(log10(prob))
    
    probs = probs[::-1]
    print(*map(lambda x: "{:.3f}".format(x), probs))