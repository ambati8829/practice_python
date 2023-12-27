def add_movie(movies):
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    actor = input("Enter the lead actor: ")
    year = input("Enter the release year: ")
        
    movies.append({
                'title': title,
                'director': director,
                'actor': actor,
                'year': year
            })
def show_movies(movies):
    for movie in movies:
        print_movie(movie)
        
def print_movie(movie):
    print(f"\nTitle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Actor: {movie['actor']}")
    print(f"Year: {movie['year']}")
    
def find_movie(movies):
    title=input("Enter a movie title: ")
    for movie in movies:
        if movie["title"].lower()==title.lower():
            print_movie(movie)
        
user_options={
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}
            
def menu():    
    movies=[]
    Prompt= "\nEnter 'a' to add the movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit:"
    
    selection=input(Prompt)
    while selection!="q":
        if selection in user_options:
            selected_function= user_options[selection]
            selected_function(movies)    
        else:
            print("Unknown command,please try again")
            
        selection = input(Prompt)
menu()