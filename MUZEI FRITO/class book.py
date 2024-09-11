class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# Create a book object
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")

# Call the method
book1.display_book_info()