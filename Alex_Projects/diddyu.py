#fibonachi talföljd

def main():
    
    x = 0
    
    y = 1

    print(f"{x}\n{y}")
    
    while True:
        z = x + y
        if z > 1000000000:
            break
        print(z)
        x = y
        y = z
         
        
        
        

if __name__ == "__main__":
    main()
