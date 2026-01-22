import numpy as np

def hAn(l_ratio,n): #l_ratio=l/L
    return 2*np.sin(n*np.pi*l_ratio)/(n**2*np.pi*(l_ratio)*(1-l_ratio))

def main():
    results=[]
    for n in range(1,8):
        for l_ratio in [1/10,1/4,1/2]:
            results.append({'n':n,'l/L':l_ratio,'hAn':hAn(l_ratio,n)})
    print(f"{'n':>2} {'l/L':>6} {'hAn':>12}")
    print("-" * 22)
    for r in results:
        print(f"{r['n']:>2} {r['l/L']:>6.2f} {r['hAn']:>12.6f}")


if __name__=='__main__':
    main()