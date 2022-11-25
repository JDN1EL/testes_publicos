from datetime import *

n = 1

if n > 0:
    n = timedelta(hours = n)
    print(f'são \n{n}\n horas acordado')

elif n <= 0:
    print(f'são \n{timedelta(n)}\n horas sem dormir')
