import matplotlib.pyplot as plt
import numpy as np
import imageProcessor as ip

y1 = [10, 10, 10, 12, 230, 400]
y2 = [10, 10, 10, 12, 12, 120]
x = [5, 10, 15, 20, 25, 30]

plt.plot(x,y1)
plt.plot(x,y2)
plt.title('Rozmiar błędu w pikslach w zależności od poziomu zaszumienia')
plt.xlabel('Wielkość szumu w obrazie [% całego obrazu]')
plt.ylabel('Błąd [px]')
plt.legend(['Metoda ostra', 'Metoda rozmyta'], loc='upper left')
plt.savefig('test.png')
plt.show()
