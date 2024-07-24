'''
    script hecho para guardar funciones útiles
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_important_terms_for_movie(movie_title: str, df, vectorizer, tfidf_matrix, top_n: int = 10) -> None:
    """
    Grafica los términos más importantes para una película dada.

    Parámetros:
        movie_title (str): El título de la película.
        df (pd.DataFrame): El dataframe que contiene la información de las películas.
        vectorizer (TfidfVectorizer): El vectorizador utilizado para la transformación TF-IDF.
        tfidf_matrix (scipy.sparse.csr_matrix): La matriz TF-IDF.
        top_n (int, opcional): El número de términos principales a graficar. Por defecto es 10.
    """
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
    plt.xlabel('Puntuación TF-IDF')
    plt.title(f'Términos más importantes para "{movie_title}"')
    plt.gca().invert_yaxis()  # Para que el término más importante esté en la parte superior
    plt.show()


def limpiar_ids(x):
    """
    Limpia los IDs convirtiéndolos a enteros.

    Parámetros:
        x (Any): El valor de entrada.

    Retorna:
        Union[int, np.nan]: El ID limpio como entero o NaN si la conversión falla.
    """
    try:
        return int(x)
    except:
        return np.nan


def obtener_director(x):
    """
    Obtiene el nombre del director de una lista de miembros del equipo.

    Parámetros:
        x (List[Dict[str, Any]]): La lista de miembros del equipo.

    Retorna:
        Union[str, np.nan]: El nombre del director o NaN si no se encuentra.
    """
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan


def generar_lista(x, cantidad_elementos: int):
    """
    Genera una lista de nombres a partir de una lista de diccionarios.

    Parámetros:
        x (Any): El valor de entrada.
        cantidad_elementos (int): El número de elementos a incluir en la lista.

    Retorna:
        List[str]: La lista de nombres.
    """
    if isinstance(x, list):
        names = [i['name'] for i in x]

        # Chequeo si hay más de 'cantidad_elementos' en la lista, si hay más retorno solo los indicados
        # de no ser así devuelvo la lista completa
        if len(names) > cantidad_elementos:
            return names[:cantidad_elementos]
        else:
            return names

    # si no es una lista retorno una lista vacía
    return []


def procesar_nombre(x):
    """
    Procesa el nombre eliminando espacios y convirtiéndolo a minúsculas.

    Parámetros:
        x (Union[str, List[str]]): El nombre de entrada o lista de nombres.

    Retorna:
        Union[str, List[str]]: El nombre procesado o lista de nombres.
    """
    if isinstance(x, list):
        # Quito espacios y lo llevo a minúsculas
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        # Chequeo si hay director, de no ser así devuelvo un string vacío
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


def juntar_features(x) -> str:
    """
    Une las palabras clave, el reparto, el director y los géneros en una sola cadena.

    Parámetros:
        x (Dict[str, Any]): El diccionario que contiene las características de la película.

    Retorna:
        str: La cadena concatenada de características.
    """
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
