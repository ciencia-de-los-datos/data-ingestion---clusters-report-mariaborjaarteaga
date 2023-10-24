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
    archivo = open("clusters_report.txt", mode='r')
    nombres = ["cluster", "cantidad de palabras clave", "porcentaje de palabras clave", "principales palabras clave"]
    archivo.readline()
    archivo.readline()
    archivo.readline()
    archivo.readline()
    data= archivo.read()
    archivo.close()
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
    
    data.pop()
    
    for i in data:
      txt.append(i.split('%')[0].replace(',','.').split()+[i.split('%')[1].strip()])
        
    df = pd.DataFrame(txt, columns=['Columna1', 'Columna2', 'Columna3', 'Columna4'])
    df.columns = nombres
    df.columns = df.columns.str.replace(' ', '_')
    
    df['cluster'] = pd.to_numeric(df['cluster'])
    df['cantidad_de_palabras_clave'] = pd.to_numeric(df['cantidad_de_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = pd.to_numeric(df['porcentaje_de_palabras_clave'])
    
    return df
