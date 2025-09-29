# name, director, length in minutes, year
def validate_int(question, validation):
    value = input(question)
    while True:
        try:
            int(value)
            return value
        except ValueError:
            value = input(validation)

def validate_string(question, validation):
    value = input(question)
    while True:
        if value.rstrip() == '':
            value = input(validation)
        else:
            return value

def validate_quit():
    value = input("Would you like to enter another movie? (Enter Y or N) " )
    while True:
        if value.lower() == 'y':
            return True
        elif value.lower() == 'n':
            return False
        else:
            input("Enter Y or N")


movie_list = [  {
        "name": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "length": 142,
        "year": 1994
    },
    {
        "name": "Inception",
        "director": "Christopher Nolan",
        "length": 148,
        "year": 2010
    },
    {
        "name": "Parasite",
        "director": "Bong Joon-ho",
        "length": 132,
        "year": 2019
    },
    {
        "name": "The Godfather",
        "director": "Francis Ford Coppola",
        "length": 175,
        "year": 1972
    },
    {
        "name": "Spirited Away",
        "director": "Hayao Miyazaki",
        "length": 125,
        "year": 2001
    }]
repeat = True
while repeat:
    name = validate_string("Enter movie name: ", "Movie name cannot be empty: " )
    director = validate_string("Enter director: ", "Director name cannot be empty: ")
    length = validate_int(   "Enter length in minutes: ", "Please enter a valid length in minutes: " )
    year = validate_int("What year was the movie release? ", "Please enter a valid year: ")
    repeat = validate_quit()
    movie_list.append({"name": name.title(), "director": director.title(), "length": length, "year": year})

print('\nYour Movie List: ')
for movie in movie_list:
    print(f"\nName: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Length in minutes: {movie['length']}")
    print(f"Year: {movie['year']}\n")
