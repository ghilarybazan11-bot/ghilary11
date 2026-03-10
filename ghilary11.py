import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
def hacer_circulo(radio, color):
   print("vas a hacer un circulo")
   fig, ax = plt.subplots()
   # Crear el círculo: (centro_x, centro_y), radio
   circulo = Circle((0.5, 0.5), radio, color=color, fill=True)
   # Añadir el círculo a los ejes
   ax.add_patch(circulo)
   # Asegurar que el círculo no se deforme (aspecto 1:1)
   ax.set_aspect('equal')
   # Ajustar límites de los ejes para ver el círculo
   ax.set_xlim(-radio, radio)
   ax.set_ylim(-radio, radio)
   plt.show()
def hacer_cuadrado():
   print("vas a hacer un cuadrado")
   x = [1, 3, 3, 1, 1]
   y = [1, 1, 3, 3, 1]
   # Crear la figura
   plt.figure()
   plt.plot(x, y, marker='o') # 'o' añade puntos en los vértices
   # Asegurar que los ejes tengan la misma escala
   plt.axis('equal')
   # Añadir etiquetas y mostrar
   plt.title("Cuadrado en Matplotlib")
   plt.grid(True)
   plt.show()
def hacer_pentagono():
   print("vas a hacer un pentagono")
   # Definir los ángulos para los 5 vértices (0, 72, 144, 216, 288 grados)
   theta = np.linspace(0, 2*np.pi, 6)
   r = 1 # Radio del pentágono
   # Calcular coordenadas x e y
   x = r * np.cos(theta)
   y = r * np.sin(theta)
   # Crear la figura
   fig, ax = plt.subplots()
   # Opción 1: Dibujar usando plot
   ax.plot(x, y, marker='o', linestyle='-')
   # Opción 2: Rellenar usando Polygon (más formal)
   # pentagon = Polygon(np.column_stack((x, y)), closed=True, alpha=0.3)
   # ax.add_patch(pentagon)
   # Ajustes de visualización
   ax.set_aspect('equal') # Asegura que el pentágono no sea elíptico
   plt.grid(True)
   plt.show()
def hacer_rectangulo3d():
   print("vas a hacer un rectangulo")
   # Crear figura
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   # Definir dimensiones del rectángulo
   x = [0, 5, 5, 0, 0]
   y = [0, 0, 3, 3, 0]
   z = [0, 0, 0, 0, 0] # Cara inferior
   # Graficar la cara base (plana, se puede extruir)
   ax.plot_trisurf(x, y, z, color='blue', alpha=0.5)
   # Añadir etiquetas
   ax.set_xlabel('Eje X')
   ax.set_ylabel('Eje Y')
   ax.set_zlabel('Eje Z')
   plt.show()
def hacer_triangulo3d():
   print("vas a hacer un triangulo")
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   # Definir los tres vértices del triángulo (x, y, z)
   v1 = [0, 0, 0]
   v2 = [1, 0, 0]
   v3 = [0, 1, 1]
   # Agrupar los vértices
   verts = [v1, v2, v3]
   # Crear el polígono
   triangulo = Poly3DCollection([verts])
   triangulo.set_color('cyan')
   triangulo.set_edgecolor('black')
   triangulo.set_alpha(0.5)
   # Añadir el triángulo al eje
   ax.add_collection3d(triangulo)
   # Configurar límites y mostrar
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.set_zlim(0, 1)
   plt.show()
def hacer_estrella3d():
   print("vas a hacer una estrella")
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   # Definir los vértices de una estrella 2D (radio interno y externo)
   r_in = 0.5
   r_out = 1.0
   n_puntas = 5
   angulos = np.linspace(0, 2*np.pi, 2*n_puntas + 1)
   puntos = []
   for i, angulo in enumerate(angulos):
    radio = r_out if i % 2 == 0 else r_in
    puntos.append([radio * np.cos(angulo), radio * np.sin(angulo)])
   puntos = np.array(puntos)
   x = puntos[:, 0]
   y = puntos[:, 1]
   z = np.zeros_like(x) # Estrella inicialmente plana
   # Elevar el centro (o puntas) para dar efecto 3D
   # Hacemos el centro (0,0) más alto
   z = np.sqrt(x*2 + y*2) # Ejemplo: más alto en el centro
   z = 1 - z # Invertir para que las puntas sean altas y el centro bajo
   # Graficar la superficie
   ax.plot_trisurf(x, y, z, color='gold', edgecolor='orange')
   # Ajustar vista
   ax.set_zlim(0, 1)
   plt.show()
def menu():
   print("Menu figuras geometricas")
   print("1. Circulo")
   print("2. Cuadrado")
   print("3. Pentagono")
   print("4. Rectangulo")
   print("5. Triangulo")
   print("6. Estrella")
   print("7. Finalizar programa")
while True:
  menu()
  try:
    opcion= int(input("Elige una opcion\n"))
    if opcion== "salir":
     break
    match opcion:
      case 1:
         radio=float(input("Ingrese el radio del circulo: "))
         color=(input("Ingrese el color del circulo"))
         hacer_circulo(radio,color)
      case 2:
         hacer_cuadrado()
      case 3:
          hacer_pentagono
      case 4:
         hacer_rectangulo3d()
      case 5:
         hacer_triangulo3d()
      case 6:
          hacer_estrella3d()
      case 7:
         print("Finalizar programa")
         break
      case _:
        print("opcion no valida")
  except ValueError:
   print("Por favor, ingrese un número válido")
  break # O continuar, según desees