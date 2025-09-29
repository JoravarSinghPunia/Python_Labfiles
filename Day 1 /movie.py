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
        if not value:
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


movie_list = []
repeat = True
while repeat:
    name = validate_string("Enter movie name: ", "Movie name cannot be empty: " )
    director = validate_string("Enter director: ", "Director name cannot be empty: ")
    length_in_minutes = validate_int(   "Enter length in minutes: ", "Please enter a valid length in minutes: " )
    year = validate_int("What year was the movie release? ", "Please enter a valid year: ")
    repeat = validate_quit()
    movie_list.append({"name": name.title(), "director": director.title(), "length_in_minutes": length_in_minutes, "year": year})

for movie in movie_list:
    print(movie["name"])



