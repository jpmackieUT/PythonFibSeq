import math
import matplotlib.pyplot as plt
x=[1]
ratios =[1]
fib1 = 1.0;
fib2 = 1.0;

#change end to extend graph
end = 15

for i in range(2,end):
    x.append(i)
    ratios.append(fib2/fib1)
    temp = fib2
    fib2 = fib1+fib2
    fib1 = temp
goldR = (1+math.sqrt(5))/2
plt.plot([1,end],[goldR, goldR], label='Golden Ratio')
plt.plot(x, ratios)

plt.xlabel('# x in fibonacci sequence')
plt.ylabel('# x in fibonacci number/ #x-1 in fibonacci sequence')

plt.title('dividing consequtive fibonacci numbers')

plt.show()
