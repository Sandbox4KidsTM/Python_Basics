import matplotlib.pyplot as plt

x = [1,3, 8]
y = [8, 3, 16]

x1 = [10,30, 80]
y1 = [80, 30, 160]

plt.plot(x,y, label='FirstLine')
plt.bar(x1,y1, label='Line TWO')

plt.xlabel('age')
plt.ylabel('income')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()