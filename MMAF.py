# En este archivo estará la librería de funciones que se utilizarán en el programa principal

#LIBRERIAS: 
import math
from sympy import symbols, Eq, solve

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
def costo_pepito_perez(t):
    return -2000 * t**2 + 20000 * t + 800000

# Función para el costo lineal de Interprase
def costo_interprase(t):
    return 850000 + 22000 * t

# Función para el costo lineal de Soluciones Express
def costo_soluciones(t):
    return 1150000 + 420 * t

# Resolver la ecuación cuadrática de Pepito_Perez para encontrar el tiempo
def calcular_tiempo_limite(limite):
    t = symbols('t', real=True)
    ecuacion = Eq(costo_pepito_perez(t), limite)
    soluciones = solve(ecuacion, t)
    # Filtrar soluciones válidas (tiempo positivo y real)
    soluciones_validas = [sol for sol in soluciones if sol.is_real and sol > 0]
    return soluciones_validas[0] if soluciones_validas else None

# Comparar los costos en el tiempo calculado
def comparar_costos(limite):
    t_max = calcular_tiempo_limite(limite)
    if t_max:
        ci = costo_interprase(t_max)
        cs = costo_soluciones(t_max)
        return t_max, ci, cs
    else:
        return None, None, None
# -------------------------------------------------------------------------------------
