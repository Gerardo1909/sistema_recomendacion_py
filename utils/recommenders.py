'''
    script hecho para guardar las funciones de los sistemas de recomendación
'''

import pandas as pd

def recomendar_peli(title: str, cosine_sim, df: pd.DataFrame) -> pd.DataFrame:
    """
    Función que recomienda películas similares a una dada.

    Parámetros:
    - title (str): Título de la película de referencia.
    - cosine_sim : Matriz de similitud coseno entre películas.
    - df (pd.DataFrame): DataFrame con los datos de las películas.

    Retorna:
    - recommendations (pd.DataFrame): DataFrame con las películas recomendadas y sus puntuaciones de similitud.
    """

    # Obtener el índice de la película que coincide con el título
    idx = df[df['title'] == title].index[0]

    # Obtener las puntuaciones de similitud en pares para todas las películas con la película dada
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenar las películas en base a las puntuaciones de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtener los índices de las 10 películas más similares (puedes ajustar el número de recomendaciones)
    sim_scores = sim_scores[1:11]

    # Obtener los índices de las películas
    movie_indices = [i[0] for i in sim_scores]

    # Obtener los títulos de las películas más similares y sus puntuaciones de similitud
    similar_movies = df['title'].iloc[movie_indices]
    similarity_scores = [i[1] for i in sim_scores]

    # Crear un DataFrame con los resultados
    recommendations = pd.DataFrame({
        'Pelicula': similar_movies,
        'Similitud': similarity_scores
    })

    return recommendations