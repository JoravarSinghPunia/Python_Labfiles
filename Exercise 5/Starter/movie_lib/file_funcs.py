def load_movies(filename):
    movies = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    title, director, year = line.split(',')
                    movies.append({"title": title.strip(), "director": director.strip(), "year": year.strip()})
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty movie list.")
    return movies

def save_movies(filename, movies):
    with open(filename, "w") as f:
        for movie in movies:
            f.write(f"{movie['title']},{movie['director']},{movie['year']}\n")