'''
    script hecho para guardar funciones útiles
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_important_terms_for_movie(movie_title:str, df, vectorizer, tfidf_matrix, top_n=10):
    
    # Obtener los nombres de las características
    feature_names = vectorizer.get_feature_names_out()
    
    # Obtener el índice de la película relevante
    idx_movie = df[df['title'] == movie_title].index[0]
    
    # Obtener los términos más importantes para la película dada
    movie_tfidf = tfidf_matrix[idx_movie].toarray().flatten()
    important_terms = [(feature_names[i], movie_tfidf[i]) for i in movie_tfidf.argsort()[-top_n:]]
    
    # Ordenar términos por importancia
    important_terms = sorted(important_terms, key=lambda x: x[1], reverse=True)
    
    # Extraer los términos y sus puntuaciones
    terms, scores = zip(*important_terms)
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.barh(terms, scores, color='skyblue', edgecolor='black')
    plt.xlabel('TF-IDF Score')
    plt.title(f'Términos más importantes para "{movie_title}"')
    plt.gca().invert_yaxis()  # Para que el término más importante esté en la parte superior
    plt.show()
    
    
def limpiar_ids(x):
    try:
        return int(x)
    except:
        return np.nan
    
def obtener_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def generar_lista(x, cantidad_elementos:int):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        return names
    
        # Chequeo si hay más de 'cantidad_elementos' en la lista, si hay más retorno solo los indicados
        # de no ser así devuelvo la lista completa
        if len(names) > cantidad_elementos:
            return names[:cantidad_elementos]
        else:
            return names
        
    # si no es una lista retorno una lista vacía
    return []

def procesar_nombre(x):
    
    if isinstance(x, list):
        # Quito espacios y lo llevo a minusculas
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        # Chequeo si hay director, de no ser así devuelvo un string vacío
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''
        
def juntar_features(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
        
