def add_book():
    # purpose: add a book
   # print()
    print("Adding a New Book..")
    print()
    inventory = [] 
    ch1 = int( input ("enter the number of book that you want to add "))
    for i in ch1:  
      title = input("Title> ")
      author = input("Author> ")    
      inventory.append = (title, author)
    print(inventory)
    find  = input("enter the book title  that you want to find ") 
    for j in inventory :
       if j[0] == find :
          print (j)
          


