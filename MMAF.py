# En este archivo estará la librería de funciones que se utilizarán en el programa principal

#LIBRERIAS: 
import math
from sympy import symbols, Eq, solve
from ipywidgets import interact, FloatSlider

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

#Funciones Actividad 3 (Pepito Perez)
# -------------------------------------------------------------------------------------
# Función para el costo cuadrático de Pepito_Perez
def calcular_costos(t_seleccionado):
    # Definir las funciones de costo
    valor_interprase = 950000 + 5500 * t_seleccionado + 30000 + 25 * t_seleccionado
    valor_soluciones = 1100000 + 150 * t_seleccionado + 50000 - 10 * t_seleccionado
    valor_pepito     = -2000 * t_seleccionado**2 + 20000 * t_seleccionado + 1130000
    
    # Imprimimos los valores en la consola
    print(f"Para t = {t_seleccionado}:")
    print(f"  - Interprase         : ${valor_interprase:,.2f}")
    print(f"  - Soluciones Express : ${valor_soluciones:,.2f}")
    print(f"  - Pepito             : ${valor_pepito:,.2f}")

    return interact(
            calcular_costos, 
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
  discriminante = Calcular_Discriminante(a,b,c)
  #discriminante = b*2 - 4 a* c
  x1 = (-b + math.sqrt(discriminante)) / (2*a)
  x2 = (-b - math.sqrt(discriminante)) / (2*a)

  print("las soluciones son: ", x1, "y", x2)
  return x1, x2
#--------------------------------------------------------------------------------------
