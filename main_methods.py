# __str__() ; __len__() ; __del__() function methods
print("Main function methods:")
class Book():
    # Book class default method
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # Book class string method
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Book class lenght method
    def __len__(self):
        return self.pages

    # Book class deleted method
    def __del__(self):
        print("A book object has benn deleted.")

b = Book('Python rocks','Jose',200)
print()
print(b)
print(str(b))
print(len(b))

# Delete variable value form the memory 
del b

# It goes fail cause delete from memory
print(b)