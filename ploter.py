import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def main():
    # Ler dados do stdin (pipe)
    data = sys.stdin.readlines()
    
    # Processar os dados (agora Y é a primeira coluna e X a segunda)
    y = []  # Antiga primeira coluna (agora Y)
    x = []  # Antiga segunda coluna (agora X)
    for line in data:
        parts = line.strip().split()
        if len(parts) >= 2:
            y.append(int(parts[0]))
            x.append(int(parts[1]))
    
    if not x:
        print("Nenhum dado válido recebido via pipe.")
        return
    
    z = x.copy()  # Z igual a X (como antes, mas agora X é o passo)
    
    # Criar figura 3D
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar os pontos originais (agora com X e Y invertidos)
    ax.scatter(x, y, z, c='r', marker='o', s=50, depthshade=True)
    
    # Plotar linhas conectando os pontos em ordem
    ax.plot(x, y, z, c='b', alpha=0.8, linewidth=2)
    
    # Criar planos verticais que prolongam as linhas
    for i in range(len(x)-1):
        # Definir os vértices do polígono para cada segmento
        vertices = [
            [x[i], y[i], 0],
            [x[i+1], y[i+1], 0],
            [x[i+1], y[i+1], z[i+1]],
            [x[i], y[i], z[i]]
        ]
        
        # Criar o polígono
        poly = Poly3DCollection([vertices], alpha=0.2, linewidths=1, edgecolor='k')
        poly.set_facecolor(plt.cm.viridis(i/len(x)))  # Gradiente de cor
        ax.add_collection3d(poly)
    
    # Adicionar um plano base
    xx, yy = np.meshgrid(range(min(x)-1, max(x)+2), range(min(y)-1, max(y)+2))
    zz = np.zeros_like(xx)
    ax.plot_surface(xx, yy, zz, color='gray', alpha=0.1)
    
    # Configurar labels
    ax.set_xlabel('Passo (X)')
    ax.set_ylabel('Valor (Y)')
    ax.set_zlabel('Altura (Z)')
    ax.set_title('Sequência de Collatz 3D com Planos Projetados')
    
    # Ajustar a visualização
    ax.view_init(elev=30, azim=-45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
