import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import matplotlib.patches as patches
import math

# Configuración global para mayor nitidez en las fuentes
plt.rcParams['figure.dpi'] = 120 
plt.rcParams['font.size'] = 10

# --- FUNCIONES DE CÁLCULO ---
def calcular_estrella():
    radio_ext, radio_int, puntas = 1, 0.5, 5
    area = puntas * radio_ext * radio_int * math.sin(math.pi / puntas)
    lado = math.sqrt(radio_ext**2 + radio_int**2 - 2*radio_ext*radio_int*math.cos(math.pi/puntas))
    perimetro = lado * puntas * 2
    return area, perimetro

def calcular_circulo():
    radio = 0.2
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

def calcular_triangulo():
    base, altura = 4, 3
    lado_a, lado_b, lado_c = 4, 3, 5
    area = (base * altura) / 2
    perimetro = lado_a + lado_b + lado_c
    return area, perimetro

def calcular_cuadrado3d():
    lado = 1
    area = 6 * (lado**2)
    perimetro = 12 * lado
    return area, perimetro

def calcular_circulo3d():
    radio = 0.5
    area = math.pi * (radio**2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

def calcular_triangulo3d():
    lado = 1.414
    area = 0.866
    perimetro = 3 * lado
    return area, perimetro

# --- FUNCIONES DE DIBUJO ---
def hacer_estrella():
    a, p = calcular_estrella()
    puntas, r_ext, r_int = 5, 1, 0.5
    vertices = []
    for i in range(puntas * 2):
        r = r_ext if i % 2 == 0 else r_int
        angle = i * math.pi / puntas - math.pi/2 # Rotada para que la punta mire arriba
        vertices.append([r * math.cos(angle), r * math.sin(angle)])
    vertices.append(vertices[0])
    v_np = np.array(vertices)

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(v_np[:,0], v_np[:,1], color='#FFD700', linewidth=2, antialiased=True)
    ax.fill(v_np[:,0], v_np[:,1], color='#FFF700', alpha=0.4)
    
    plt.text(0, 0, f"A:{a:.3f}\nP:{p:.3f}", ha='center', va='center', weight='bold')
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_aspect('equal')
    ax.axis('off') # Más limpio sin ejes
    plt.title("Estrella 2D Nitidez Alta")
    plt.show()

def hacer_circulo():
    a, p = calcular_circulo()
    fig, ax = plt.subplots(figsize=(5,5))
    circle = patches.Circle((0.5, 0.5), 0.2, edgecolor='deeppink', facecolor='none', linewidth=2, antialiased=True)
    ax.add_patch(circle)
    plt.text(0.5, 0.5, f"A:{a:.3f}\nP:{p:.3f}", ha='center', va='center')
    ax.set_xlim(0.2, 0.8); ax.set_ylim(0.2, 0.8); ax.set_aspect('equal')
    plt.title("Círculo Nitidez Alta")
    plt.show()

def hacer_triangulo():
    a, p = calcular_triangulo()
    x, y = [1, 5, 3, 1], [1, 1, 4, 1]
    plt.figure(figsize=(5,5))
    plt.plot(x, y, color='royalblue', linewidth=2, marker='o', markersize=4, antialiased=True)
    plt.text(3, 2, f"A:{a:.3f}\nP:{p:.3f}", ha='center', va='center')
    plt.title("Triángulo Nitidez Alta")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def hacer_cuadrado3d():
    a, p = calcular_cuadrado3d()
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    # Dibujo simplificado del cubo para nitidez
    r = [0, 1]
    for s, e in [(0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1)]:
        for s1, e1 in [(0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1)]:
            if np.sum(np.abs(np.array(s)-np.array(s1))) == 1:
                ax.plot3D(*zip(s, s1), color="black", linewidth=1)
    plt.title(f"Cubo: A={a:.3f}, P={p:.3f}")
    plt.show()

def hacer_circulo3d():
    a, p = calcular_circulo3d()
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2 * np.pi, 200) # Más puntos para curvas suaves
    ax.plot(0.5 * np.cos(theta), 0.5 * np.sin(theta), 0, linewidth=2, antialiased=True)
    plt.title(f"Círculo 3D Nitidez Alta\nA={a:.3f}, P={p:.3f}")
    plt.show()

def hacer_triangulo3d():
    a, p = calcular_triangulo3d()
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([1,0,0,1], [0,1,0,0], [0,0,1,0], marker='o', linewidth=2, antialiased=True)
    plt.title(f"Triángulo 3D: A={a:.3f}, P={p:.3f}")
    plt.show()

def menu():
    print("\n--- Menú (Nitidez Mejorada) ---")
    print("1. Estrella 2D  | 2. Círculo 2D | 3. Triángulo 2D")
    print("4. Cuadrado 3D  | 5. Círculo 3D | 6. Triángulo 3D")
    print("7. Salir")

while True:
    menu()
    try:
        sel = int(input("Elige una opción: "))
    except ValueError: continue
    if sel == 1: hacer_estrella()
    elif sel == 2: hacer_circulo()
    elif sel == 3: hacer_triangulo()
    elif sel == 4: hacer_cuadrado3d()
    elif sel == 5: hacer_circulo3d()
    elif sel == 6: hacer_triangulo3d()
    elif sel == 7: break