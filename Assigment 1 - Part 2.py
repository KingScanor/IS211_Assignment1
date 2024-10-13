#Part 2 Simple Class

class Book:
    def __init__(self, title , author):
        """
          Constructor of a Book Class

          :param author: The name of the author of the book
          :param title: The title of the book
          """
        self.author = author
        self.title = title


    def display(self):
        """ Display the title and author of the book"""
        print (f"The book {self.title} written by {self.author} ")

if __name__ == "__main__":
    book1 = Book ("Harry Potter and the Goblet of Fire","J. K. Rowling")
    book2 = Book ("Ivanhoe: A Romance","Walter Scott")

    book1.display()
    book2.display()