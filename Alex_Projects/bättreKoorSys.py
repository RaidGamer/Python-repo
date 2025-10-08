def main():
    print('funktion calc, slang för kalkylator'.upper())
    func = input('f(x) = ').lower()
    x = input('För f(x) hur många x vill du lösa ut?: ')
    y_värd, x_värd = func_retrieve(x, func)
    print(f'   x= '+', '.join(map(str, x_värd)))
    print(f'f(x)= '+', '.join(map(str, y_värd)))
    print(' ')
    print(f'Koordinatsystem: Graf för f(x)={func} :\n')
    koorsystem(x_värd, y_värd)



def func_retrieve(x, function): #ger tillbaka lista för antal f(x) resp. x-värden
    x_värde = []
    y_värde = []
    for i in range(0, int(x)):
        y = int((eval(function.replace('x', str(i)))))
        y_värde.append(y)
        x_värde.append(i)
    return y_värde, x_värde


def koorsystem(xlist, ylist): #bygger upp och visar ett koordinatsystem med önskade funktion 
    max_y = max(ylist) + 1 
    max_x = len(xlist)

    for y in range(max_y, -1, -1):  
        print(f'{y:2}', end="")     
        for x in range(max_x):
            if ylist[x] == y:
                print('▇▇', end='')  
            else:
                print(' .', end='')  
        print()

    print('   ', end='')
    for i in range(max_x):
        print(f'{i:2}', end='')

    print()

#■
main()

#gör def() functions for gods sake
#gör detta mer "pythonic" som de där elitist yt python tutorial gubbarna säger