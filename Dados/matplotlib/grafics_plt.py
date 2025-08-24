import matplotlib.pyplot as plt

x =[1,2,3,4]
y =[1,4,2,3]
plt.plot(x, y)
plt.show()

plt.ylabel('Eixo y')
plt.xlabel('Eixo x')
plt.title('Gráfico')
plt.xticks([0,2,4,6,8])
plt.yticks([0,3,5,7,9])
plt.plot(x, y,label='dados', linestyle='--', color='m', lw=3.0)
plt.scatter(x,y, label='Dados', color='k')
plt.bar(x,y, label='dados')
plt.scatter(x,y, label='Dados', color='k', marker='d')
plt.legend() 

plt.plot(x,y)
plt.axis(xmin=-1, xmax=10, ymin=0, ymax=12)
plt.axis('auto')
plt.axis('square')

fig = plt.figure(figsize=(20,5))
fig.suptitle('Gráficos')
fig.add_subplot(131)
plt.plot(x,y, label='valores')
plt.legend()
plt.title('Gráfico 1')

fig.add_subplot(132)
plt.scatter(x, y)
plt.title('Gráfico 2')

fig.add_subplot(133)
plt.bar(x,y)
plt.title('Gráfico 3')

plt.savefig('./figs/graficos.png')
plt.show()