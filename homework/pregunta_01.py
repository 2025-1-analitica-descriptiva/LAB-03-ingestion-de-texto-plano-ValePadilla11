"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re
    
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    clusters = []
    cantidades = []
    porcentajes = []
    palabras_clave = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        

        if re.match(r'^\s*\d+\s+', line):
            parts = re.split(r'\s+', line.strip())
            cluster_num = int(parts[0])
            cantidad = int(parts[1])
            porcentaje_str = parts[2]
            
            porcentaje = float(porcentaje_str.replace(',', '.'))

            palabras_texto = ' '.join(parts[4:])
            j = i + 1
            while j < len(lines) and not re.match(r'^\s*\d+\s+', lines[j].strip()) and lines[j].strip() and not lines[j].strip().startswith('-'):
                palabras_texto += ' ' + lines[j].strip()
                j += 1

            palabras_texto = re.sub(r'\s+', ' ', palabras_texto).strip()

            if palabras_texto.endswith('.'):
                palabras_texto = palabras_texto[:-1]
            palabras_lista = [palabra.strip() for palabra in palabras_texto.split(',')]
            palabras_final = ', '.join(palabras_lista)
            clusters.append(cluster_num)
            cantidades.append(cantidad)
            porcentajes.append(porcentaje)
            palabras_clave.append(palabras_final)
            
            i = j
        else:
            i += 1
    

    df = pd.DataFrame({
        'cluster': clusters,
        'cantidad_de_palabras_clave': cantidades,
        'porcentaje_de_palabras_clave': porcentajes,
        'principales_palabras_clave': palabras_clave
    })
    
    return df
