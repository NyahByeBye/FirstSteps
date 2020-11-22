import random
import matplotlib

#Закипит ли вода

temp = 20
heat = 0
time = 0
while temp<100:
    heat=random.paretovariate(100000000)
    print(heat)
    temp+=heat
    time+=1
    heat=0
print("Температура: " + str(temp) + ", время: " + str(time//60) + " минут, " + str(time%60) + " секунд")