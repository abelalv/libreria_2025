# En este archivo estará la librería de funciones que se utilizarán en el programa principal

#LIBRERIAS: 
import math
import numpy as np
from sympy import symbols, Eq, solve
from ipywidgets import interact, FloatSlider, interactive_output, VBox, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import fsolve
from IPython.display import display

# Función Actividad 1 (Población de Ardillas)
# -------------------------------------------------------------------------------------
def calcular_poblacion(juveniles_iniciales, adultas_iniciales, tasa_reproduccion, tasa_conversion, tasa_supervivencia, epocas):
    """
    Calcula la población de ardillas a lo largo de varios años.
    
    Parámetros:
        juveniles_iniciales (int): Número inicial de ardillas juveniles.
        adultas_iniciales (int): Número inicial de ardillas adultas.
        tasa_reproduccion (float): Número promedio de juveniles generados por cada adulta.
        tasa_conversion (float): Proporción de juveniles que pasan a ser adultas.
        tasa_supervivencia (float): Proporción de adultas que sobreviven.
        anos (int): Número de años a calcular.
        
    Retorna:
        lista_poblaciones (list): Lista con las poblaciones totales de cada año.
    """
    # Valores iniciales
    juveniles = juveniles_iniciales
    adultas = adultas_iniciales

    lista_poblaciones = []

    for epocas in range(1, epocas + 1):
        # Cálculos
        juveniles_nuevas = adultas * tasa_reproduccion
        juveniles_que_pasan = juveniles * tasa_conversion
        adultas_sobrevivientes = adultas * tasa_supervivencia

        # Nuevos valores de juveniles y adultas
        juveniles = juveniles_nuevas
        adultas = juveniles_que_pasan + adultas_sobrevivientes

        # Población total
        poblacion_total = juveniles + adultas
        lista_poblaciones.append((epocas, juveniles, adultas, poblacion_total))
        # --- RESULTADOS ---
    print(f"{'Año':<5}{'Juveniles':<15}{'Adultas':<15}{'Población Total':<15}")
    for epocas, juveniles, adultas, total in lista_poblaciones:
        print(f"{epocas:<5}{int(juveniles):<15}{int(adultas):<15}{int(total):<15}")
    
    return 
# -------------------------------------------------------------------------------------

# Función Actividad 2 (Diferencia de cuadrados)
# -------------------------------------------------------------------------------------
def analizar_diferencia_cuadrados(radio_exterior, radio_interior, altura): 
    """
    Analiza el impacto de errores comunes al calcular el volumen de una capa cilíndrica.
    Comparación entre:
    - Cálculo correcto: π(R^2 - r^2)h
    - Cálculo erróneo: π(R - r)^2h
    """
    # Cálculo correcto
    volumen_correcto = math.pi * (radio_exterior**2 - radio_interior**2) * altura

    # Error común: cuadrado de la diferencia
    volumen_erroneo = math.pi * (radio_exterior - radio_interior)**2 * altura

    # Diferencia entre ambos cálculos
    diferencia = volumen_correcto - volumen_erroneo

    # Resultados
    print("=== Resultados ===")
    print(f"Radio exterior (R): {radio_exterior} m")
    print(f"Radio interior (r): {radio_interior} m")
    print(f"Altura (h): {altura} m")
    print("\n--- Cálculo correcto ---")
    print(f"Volumen correcto (π(R² - r²)h): {volumen_correcto:.2f} m³")
    print("\n--- Cálculo erróneo ---")
    print(f"Volumen erróneo (π(R - r)²h): {volumen_erroneo:.2f} m³")
    print("\n--- Diferencia entre ambos ---")
    print(f"Diferencia: {diferencia:.2f} m³")
    return 
# -------------------------------------------------------------------------------------

# Funciones Actividad 3 (Pepito Perez)
# -------------------------------------------------------------------------------------
# Función para obtener los costos asociados a las tres propuestas
def obtener_costos(t_seleccionado):
    # Definir las funciones de costo
    valor_interprase = 950000 + 5500 * t_seleccionado + 30000 + 25 * t_seleccionado
    valor_soluciones = 1100000 + 150 * t_seleccionado + 50000 - 10 * t_seleccionado
    valor_pepito     = -2000 * t_seleccionado**2 + 20000 * t_seleccionado + 1130000
    
    return valor_interprase, valor_soluciones, valor_pepito

# Función para mostrar los costos asociados a las tres propuestas
def mostrar_costos(t_seleccionado):
    # Obtener los costos
    valor_interprase, valor_soluciones, valor_pepito = obtener_costos(t_seleccionado)
    
    # Imprimir los valores en la consola
    print(f"Para t = {t_seleccionado}:")
    print(f"  - Interprase         : ${valor_interprase:,.2f}")
    print(f"  - Soluciones Express : ${valor_soluciones:,.2f}")
    print(f"  - Pepito             : ${valor_pepito:,.2f}")

    return None


# Función para el slider
def interactuar_con_slider():
    return interact(
        mostrar_costos, 
        t_seleccionado=FloatSlider(
            value=0,      # Valor inicial del slider
            min=0,        # Valor mínimo
            max=20,       # Valor máximo
            step=0.5,     # Incremento
            description='Tiempo (t)'  # Etiqueta del slider
        )
    )
# -------------------------------------------------------------------------------------

# Funciones auxiliares para Taller 3 y Python 3
# -------------------------------------------------------------------------------------
# Función para calcular el discriminante
def calcular_discriminante(a, b, c):
  discriminante = b**2 - 4*a*c
  print("discriminante: ", discriminante)
  return discriminante

# Función para resolver ecuaciones cuadráticas
def resolver_ecuacion_cuadratica(a, b, c):
  discriminante = calcular_discriminante(a,b,c)
  #discriminante = b*2 - 4 a* c
  x1 = (-b + math.sqrt(discriminante)) / (2*a)
  x2 = (-b - math.sqrt(discriminante)) / (2*a)

  print("las soluciones son: ", x1, "y", x2)
  return x1, x2
#--------------------------------------------------------------------------------------

# Funciones Actividad 4 (Brecha de acceso a internet Buenaventura)
# -------------------------------------------------------------------------------------
# Función para calcular la temperatura en función del flujo de datos D
def calcular_temperatura(B):
    D = np.linspace(0, 10, 400)
    T = 8 * D + B
    return D, T

# Función para mostrar la gráfica de la temperatura y el flujo crítico
def mostrar_temperatura(B):
    D, T = calcular_temperatura(B)
    
    plt.figure(figsize=(8, 4))
    plt.plot(D, T, 'm-', lw=2, label='T(D) = 8D + B')
    plt.axhline(50, color='k', linestyle='--', label='T_c = 50°C')
    plt.xlabel('Flujo de datos D')
    plt.ylabel('Temperatura T (°C)')
    plt.title('Función de Temperatura del Cable')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))
    plt.show()

    # Cálculo del flujo crítico D_c
    D_c = (50 - B) / 8
    print(f'Para B = {B:.2f}, el flujo crítico es D_c = {D_c:.2f}')

# Función para calcular el desgaste del cable en función del tiempo t
def calcular_desgaste():
    t_vals = np.linspace(0, 10, 400)
    d = -9/10 * t_vals + 10
    return t_vals, d

# Función para mostrar la gráfica del desgaste del cable
def mostrar_desgaste(D_c):
    t_vals, d = calcular_desgaste()
    
    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, d, 'b-', lw=2, label='d(t) = -9/10t + 10')
    plt.axhline(D_c, color='r', linestyle='--', label=f'D_c = {D_c:.2f}')
    plt.xlabel('Tiempo t (años)')
    plt.ylabel('Capacidad D(t)')
    plt.title('Función de Capacidad máxima de transmisión del Cable')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 11, 1))
    plt.show()

# Función para la interacción con el slider de temperatura
def interactuar_con_temperatura():
    return interact(
        mostrar_temperatura, 
        B=FloatSlider(value=10, min=0, max=20, step=0.5, description='Parámetro B')
    )

# Función para la interacción con el slider de desgaste
def interactuar_con_desgaste():
    return interact(
        mostrar_desgaste, 
        D_c=FloatSlider(value=5, min=0, max=10, step=0.1, description='Capacidad Crítica D_c')
    )

# Funciones Actividad 5 (Deflexión de una viga en voladizo)
# -------------------------------------------------------------------------------------
def deflexion_viga(x, t):
    """
    Calcula la deflexión de la viga para un nivel de carga proporcional t,
    usando la función:
        d(x) = -t * (1/16000) * (60*x**2 - x**3)
    """
    return -t * (1/16000) * (60*x**2 - x**3)

# Función para mostrar la animación de la deflexión de la viga
def animar_deflexion_viga():
    x = np.linspace(0, 20, 400)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 20)
    y_min = deflexion_viga(20, 1)
    ax.set_ylim(y_min * 1.2, 0)

    line, = ax.plot([], [], lw=3, color='blue')

    def init():
        line.set_data([], [])
        ax.set_xlabel("Posición a lo largo de la viga (m)")
        ax.set_ylabel("Deflexión (cm)")
        ax.set_title("Animación de deflexión en viga en voladizo")
        return line,

    def update(frame):
        t = frame  # t varía de 0 a 1 (0% a 100% de carga)
        y = deflexion_viga(x, t)
        line.set_data(x, y)
        ax.set_title(f"Deflexión de la viga (Carga aplicada: {t*100:.1f}%)")
        return line,

    frames = np.linspace(0, 1, 100)
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

    anim.save("viga_animation.gif", writer="pillow", fps=30)

# Funciones para encontrar el intervalo seguro 

# Función de deflexión: d(x, C_g) en cm, x en m
def d(x, C_g):
    return -C_g * (60 * x**2 - x**3) / 16000

# Función para encontrar intersecciones: se busca x tal que d(x, C_g) = d_objetivo
def encontrar_intersecciones(d_objetivo, C_g):
    x_dom = np.linspace(0, 20, 400)
    dif = d(x_dom, C_g) - d_objetivo
    indices = np.where(np.diff(np.sign(dif)))[0]
    soluciones = []
    for i in indices:
        sol = fsolve(lambda x: d(x, C_g) - d_objetivo, x_dom[i])
        soluciones.append(sol[0])
    return sorted(soluciones)

# Función que grafica la curva, la línea horizontal en d_objetivo y la vertical en el punto de intersección
def interactuar(d_objetivo, C_g):
    intersecciones = encontrar_intersecciones(d_objetivo, C_g)
    
    x = np.linspace(0, 20, 400)
    y = d(x, C_g)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=r'$d(x,C_g)=-C_g\frac{60x^2-x^3}{16000}$')
    plt.axhline(d_objetivo, color='red', linestyle='--', label=f'd_objetivo = {d_objetivo:.3f} cm')
    
    if intersecciones:
        for x_int in intersecciones:
            y_int = d(x_int, C_g)
            plt.axvline(x_int, color='green', linestyle='--', label=f'x = {x_int:.3f} m')
            plt.scatter(x_int, y_int, color='blue', s=100, zorder=5)
    else:
        print("No se encontraron intersecciones en el dominio analizado.")

    plt.xlabel('x (m)')
    plt.ylabel('d(x, C_g) (cm)')
    plt.title('Flexión de la viga en voladizo')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 20)
    plt.ylim(min(y) - 0.1, max(y) + 0.1)
    plt.show()

    print(f'Para d_objetivo = {d_objetivo:.3f} cm y C_g = {C_g:.2f}.')
    if intersecciones:
        print('Intersección en x = ' + ", ".join(f"{xi:.3f}" for xi in intersecciones) + " m.")

def visualizar_limites():
    C_g_slider = FloatSlider(min=0.1, max=2, step=0.05, value=1.0, description='C_g')
    d_objetivo_slider = FloatSlider(min=-C_g_slider.value, max=0, step=0.025, value=-0.125, description='d_objetivo')

    def actualizar_d_objetivo_range(change):
        C_g_val = change['new']
        d_objetivo_slider.min = -C_g_val
        d_objetivo_slider.max = 0
        if d_objetivo_slider.value < -C_g_val or d_objetivo_slider.value > 0:
            d_objetivo_slider.value = -min(0.125, C_g_val)

    C_g_slider.observe(actualizar_d_objetivo_range, names='value')

    out = interactive_output(interactuar, {'d_objetivo': d_objetivo_slider, 'C_g': C_g_slider})
    ui = VBox([C_g_slider, d_objetivo_slider])
    display(ui, out)









