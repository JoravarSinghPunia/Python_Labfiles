from movie_lib.movie_funcs import search_movies, search_by_title
from movie_lib.file_funcs import load_movies, save_movies

def main ():
    filename = "movies.txt"
    movies = load_movies(filename)

    print("---Movie Dictionary---")
    print("Select an option: ")
    print("1 - Add movie")
    print("2 - Remove movie")
    print("3 - Search movie")
    print("4 - List all movies")
    print("5 - Exit")

    choice = 0
    while choice != 5:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            movie_name = input("Enter movie title: ").capitalize()
            director = input("Enter movie director: ").capitalize()
            year = input("Enter movie year: ")
            movies.append({"title": movie_name, "director": director, "year": year})
            save_movies(filename, movies)
            print("Your movie was successfully added!")

        elif choice == 2:
            query = input("Enter the title or number of the movie to remove: ")
            if query.isdigit():
                idx_to_remove = int(query) - 1
                if 0 <= idx_to_remove < len(movies):
                    removed_movie = movies.pop(idx_to_remove)
                    print(f"Successfully removed '{removed_movie['title']}'.")
                else:
                    print(f"Error: Index {idx_to_remove} is invalid.")
            else:
                result = search_by_title(query, movies)
                if result is not None:
                    movie_to_remove, idx = result
                    movies.remove(movie_to_remove)
                    print(f"Successfully removed '{movie_to_remove['title']}'.")
                else:
                    print(f"Error: Movie with title '{query}' not found.")

        elif choice == 3:
            query = input("Enter search term here: ")
            found_movies = search_movies(query, movies)
            for movie in found_movies:
                print(f"{movie['title']} ({movie['year']}) - Director: {movie['director']}")

        elif choice == 4:
            if movies:
                print("\nAll movies:")
                for idx, movie in enumerate(movies, start=1):
                    print(f"  {idx}. {movie['title']} ({movie['year']}) - Director: {movie['director']}")
            else:
                print("No movies in the list.")
        elif choice == 5:
            print("Goodbye! Run the script again to restart the programme.")
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
