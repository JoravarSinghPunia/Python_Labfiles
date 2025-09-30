def search_by_title(title, movies):
    for movie in movies:
        if title.lower() in movie["title"].lower():
            idx = movies.index(movie)
            return movie, idx
    return None

def search_movies(query, movies):
    results = []
    for idx, movie in enumerate(movies):
        if query.lower() in movie["title"].lower() or query.lower() in movie["director"].lower():
            results.append(movie)
    return results