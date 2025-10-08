import math 

def main():
    inte_der = input("Skriv in det du vill derivera av formen n*x^n-1: ")
    exp = inte_der[2:]
    # bas = inte_der[:1]
    ny_der = der(exp)
    print(ny_der)

def der(exponent):
    derexp = int(exponent)
    derexp -= 1
    if derexp == 0:
        return "0"
    elif derexp == 1:
        return f"{exponent}*X"
    else:
        str(derexp)
        return f"{exponent}*X^{derexp}"
        
if __name__ == "__main__":
    main()