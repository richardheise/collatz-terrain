import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def main():
    # Processar dados incrementalmente para economizar memória
    x, y = [], []
    
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 2:
            # Primeira coluna é valor (Y), segunda é passo (X)
            y_val, x_val = np.uint64(parts[0]), np.uint64(parts[1])
            y.append(y_val)
            x.append(x_val)
    
    if not x:
        print("Nenhum dado válido recebido via pipe.")
        return
    
    # Converter para arrays numpy com tipos específicos
    x_arr = np.array(x, dtype=np.uint64)
    y_arr = np.array(y, dtype=np.uint64)
    z_fixed = 1.0  # Valor fixo para Z
    
    # Para coordenadas 3D, usamos float64 (double)
    x_plot = x_arr.astype(np.float64)
    y_plot = y_arr.astype(np.float64)
    z_plot = np.full_like(x_plot, z_fixed, dtype=np.float64)  # Array preenchido com 50.0
    
    # Criar figura
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar pontos e linhas
    ax.scatter(x_plot, y_plot, z_plot, c='r', marker='o', s=20, depthshade=True)
    ax.plot(x_plot, y_plot, z_plot, c='b', alpha=0.6, linewidth=1)
    
    # Criar planos verticais - reduzindo quantidade para melhor performance
    step = max(1, len(x_arr) // 500)  # Mostrar no máximo 500 planos
    for i in range(0, len(x_arr)-1, step):
        vertices = [
            [x_plot[i], y_plot[i], 0.0],
            [x_plot[i+1], y_plot[i+1], 0.0],
            [x_plot[i+1], y_plot[i+1], z_fixed],
            [x_plot[i], y_plot[i], z_fixed]
        ]
        poly = Poly3DCollection([vertices], alpha=0.15, linewidths=0.5, edgecolor='k')
        poly.set_facecolor(plt.cm.viridis(i/len(x_arr)))
        ax.add_collection3d(poly)
    
    # Adicionar plano base (simplificado)
    x_min, x_max = np.min(x_plot), np.max(x_plot)
    y_min, y_max = np.min(y_plot), np.max(y_plot)
    
    xx, yy = np.meshgrid(
        np.linspace(x_min-1, x_max+1, 10, dtype=np.float64),
        np.linspace(y_min-1, y_max+1, 10, dtype=np.float64)
    )
    zz = np.zeros_like(xx, dtype=np.float64)
    ax.plot_surface(xx, yy, zz, color='gray', alpha=0.1)
    
    # Configurar labels
    ax.set_xlabel('Passo (X)')
    ax.set_ylabel('Valor (Y)')
    ax.set_zlabel('Altura (Z = 50)')  # Indicando que Z está fixo em 50
    ax.set_title('Sequência de Collatz 3D com Planos Projetados (Z fixo)')
    
    # Ajustar visualização
    ax.view_init(elev=30, azim=-45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
