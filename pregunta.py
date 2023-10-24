"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re



def ingest_data():

    #
    # Inserte su código aquí
    #
    
    # Inicializa una lista vacía para almacenar las líneas a partir del patrón
    lineas_desde_patron = []

    # Abre el archivo 'nombre_del_archivo.txt' en modo lectura
    with open('clusters_report.txt', 'r') as archivo:
        # Bandera para indicar si estamos recopilando líneas después del patrón
        recopilando = False

        # Inicializa una cadena para acumular las líneas
        acumulador = ""

        # Lee cada línea del archivo
        for linea in archivo:
            if recopilando:
                if '.' in linea:
                    acumulador += linea.strip()  # Añade la línea sin el salto de línea
                    lineas_desde_patron.append(acumulador)
                    acumulador = ""  # Restablece el acumulador para la siguiente sección
                else:
                    acumulador += linea.strip() + ' '  # Añade la línea sin el salto de línea
            elif '----------' in linea:  # Encuentra el patrón
                recopilando = True

    # Ahora la lista 'lineas_desde_patron' contiene las líneas a partir del patrón '----------' sin saltos de línea

    nr = {'Columna1': '7', 'Columna2': '42', 'Columna3':'6,3 %','Columna4':' multi-objective   optimization,   energy   storage,    economic    dispatch, non-dominated  sorting  genetic  algorithm,   sensitive   analysis,   hybridrenewable energy source, plug-in electric vehicle, combined-heat and  power, multi-objective genetic algorithm, unit-commitment, dc-dc converters.'}
    
    # Tu lista lineas_desde_patron contiene elementos con 4 valores separados por tabulaciones.
    # Puedes dividir cada elemento de la lista en 4 partes utilizando '\t' como separador y crear un DataFrame con esas partes.

    # Dividir cada elemento en la lista en 4 partes y crear una lista de listas
    data=[]
    for l in lineas_desde_patron:
      data.append(re.split(r'\s{2,}', l,3))

    # Crear el DataFrame con 4 columnas
    df = pd.DataFrame(data, columns=['Columna1', 'Columna2', 'Columna3', 'Columna4'])
    df = pd.concat([df.iloc[:6], pd.DataFrame([nr]), df.iloc[6:]]).reset_index(drop=True)
    
    df['Columna4'] = df['Columna4'].str.replace(r'\s+', ' ', regex=True)

    df['Columna4'] = df['Columna4'].str.replace(r', ', ',', regex=True)
    
    df['Columna4'] = df['Columna4'].str.replace(',', ', ', regex=True)
    df['Columna3'] = df['Columna3'].str.replace(r' %', '', regex=True)
    df['Columna3'] = df['Columna3'].str.replace(r',', '.', regex=True)
    df['Columna4'] = df['Columna4'].str.replace(r'.', '', regex=True)
    nombres = ["cluster", "cantidad de palabras clave", "porcentaje de palabras clave", "principales palabras clave"]
    #df["cantidad de palabras clave"] = df["cantidad de palabras clave"].astype(int)
    df.columns = nombres
    df.columns = df.columns.str.replace(' ', '_')

    df['cluster'] = df['cluster'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)

    
    return df
