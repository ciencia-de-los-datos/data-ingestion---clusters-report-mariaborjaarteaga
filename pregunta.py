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
    documento = open("clusters_report.txt", mode='r')
    nombres = ["cluster", "cantidad de palabras clave", "porcentaje de palabras clave", "principales palabras clave"]
    documento.readline()
    documento.readline()
    documento.readline()
    documento.readline()
    # Ahora la lista 'lineas_desde_patron' contiene las líneas a partir del patrón '----------' sin saltos de línea
    data= documento.read()
    documento.close()
    data = ' '.join(''.join(data).split())
    data = data.split('.')
    data.pop()
    aux1 = []
    aux2 = []
    
    aux1 = re.split('([o][l][ ])+',data[5])[0] + re.split('([o][l][ ])+',data[5])[1]
    aux2 = re.split('([o][l][ ])+',data[5])[2]
    
    data[5] = aux1
    data.insert(6, aux2)
    txt = []
    
    
    for i in data:
      txt.append(i.split('%')[0].replace(',','.').split()+[i.split('%')[1].strip()])
        
    df_ = pd.DataFrame(txt, columns=['Columna1', 'Columna2', 'Columna3', 'Columna4'])
    df_.columns = nombres
    df_.columns = df_.columns.str.replace(' ', '_')
    
    df_['cluster'] = pd.to_numeric(df_['cluster'])
    df_['cantidad_de_palabras_clave'] = pd.to_numeric(df_['cantidad_de_palabras_clave'])
    df_['porcentaje_de_palabras_clave'] = pd.to_numeric(df_['porcentaje_de_palabras_clave'])

    # Tu lista lineas_desde_patron contiene elementos con 4 valores separados por tabulaciones.
    # Puedes dividir cada elemento de la lista en 4 partes utilizando '\t' como separador y crear un DataFrame con esas partes.

    # Dividir cada elemento en la lista en 4 partes y crear una lista de listas
    dat=[]
    for l in lineas_desde_patron:
      dat.append(re.split(r'\s{2,}', l,3))

    # Crear el DataFrame con 4 columnas
    df = pd.DataFrame(dat, columns=['Columna1', 'Columna2', 'Columna3', 'Columna4'])

    df['Columna4'] = df['Columna4'].str.replace(r'\s+', ' ')

    df['Columna4'] = df['Columna4'].str.replace(r', ', ',')
    df['Columna4'] = df['Columna4'].str.replace(',', ', ')
    df['Columna3'] = df['Columna3'].str.replace(r' %', '', regex=True)
    df['Columna3'] = df['Columna3'].str.replace(r',', '.', regex=True)
    nombres = ["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"]
    df.columns = nombres
    df.columns = df.columns.str.replace(' ', '_')

    
    return df_
