import matplotlib
import matplotlib.pyplot as plt

# Exemplo simples de teste para matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title('Exemplo de teste com matplotlib')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.show()
