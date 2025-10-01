from classes.movie_list import MovieList

def main ():
    filename = "movies.txt"
    movie_list = MovieList(filename)

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
            movie_list.add_movie(movie_name, director, year)
            print("Your movie was successfully added!")

        elif choice == 2:
            query = input("Enter the title or number of the movie to remove: ")
            movie_list.remove_movie(query)

        elif choice == 3:
            query = input("Enter search term here: ")
            found_movies = movie_list.search_movies(query)
            for movie in found_movies:
                print(f"{movie}")

        elif choice == 4:
            print("\nAll movies:")
            for idx, movie in enumerate(movie_list.get_movies(), start=1):
                print(f"  {idx}. {movie}")

        elif choice == 5:
            print("Goodbye! Run the script again to restart the programme.")
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
