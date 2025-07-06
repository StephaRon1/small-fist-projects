# Traker of books read and ratings

# Greetings + method
# Explanations for the user:
# - Able to enter book title
# - Enter rating(0-10): Interstellar - 10/10       --- USE ''' tripple quotes
# - "done" when finished     --- CHECK THE SPELLING WITH .lower()

# store titles and ratings as a list
# After "done":
# - print all books with ratings
# - print average rating

user = input("Name: ")
print("\nGreetings, " + user)
print('''Welcome to your book tracker.\nHere we'll collect all the books that you input and its ratings(0-10),
      with a final average result at the end.\n"done" when completed''')
print('''(input "d" on Title if you'd like to remove the previous)''')

book_rating_list = []
ratings = []

while True:    
    title = str(input('''\nTitle: '''))
    if title == "d":
        book_rating_list.pop()
        title = str(input('''\nTitle: '''))
    
    elif title.lower() == "done":
        avg_rating = sum(ratings) / len(ratings)
        if len(ratings) == 0:
            print("No books were added.")
            exit()

        for books in book_rating_list:
            print("-", books)
        print(f"Average rating: {avg_rating}")
        exit()

    rating = int(input("Rating(your own/10): "))
    book_rating_list.append(f'''{title} - {rating}/10''')
    ratings.append(rating)
    print(f'''{title} - {rating}/10''')
