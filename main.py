from Login import *
from Books import * 
from random import choice
print("  ")
print(" \t ミ📚 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘛𝘖 𝘉𝘖𝘖𝘒𝘞𝘖𝘙𝘔 📚彡 ")
print("  ")
logedIn=login() 

def recomend():
     mood = str(input(" What is your mood 🎭 ? "))
     if mood == "happy" :
            print(choice(book_classic)) 
     elif mood == " Sad" :
        print(choice(book_Novel))
     elif mood == " Bored" :
        print(choice(book_thriller))
        exit()
     else :
        print("try")
    

def viewTBR() :
    for book in TbrList : 
        print(book) 


def booksCAT():
    for book in AllCat  :
        print(" 📗 "+book)
    namesOFbook()


def namesOFbook():
    br = str(input("what is your selection 💬 ? "))
    if br == "classic" :
        for i in  book_classic : 
            print(" 📕 " +i) 
    elif br == "Novel" :
        for i in  book_Novel : 
            print(" 📕 " +i) 
    elif br == "thriller " :
        for i in book_thriller : 
            print(" 📕 "+i)
def bookDescr():
    bookName = str(input(" What is the name of the book 🏷"))
    for key , value in describ_books.items():
             if key == bookName :
                 print(value)
                 
print(" ")
while logedIn :
        print("""  ----------M͓̽E͓̽N͓̽U͓̽-------------
    1- recomend you a book 📕
    2-  view a list of books by the catgory 📃
    3-  view book description 📖
    4-  add a book to your TBR 📍 
    5-  view TBR 🔖
    6-  exit /quit 👊 
    ----------------------------- """)
        try : 
          select = int (input(" What is your selection 💬 ?"))
          if select == 1 :
            recomend() 
          elif select == 2  :
            booksCAT()
          elif select ==  3 :
           bookDescr()
          elif select ==  4  :
           addTOtbr()
           viewTBR() 
          elif select ==  5  :
           viewTBR()
          elif select == 6 :
            break 
          else :
            print("try")
        except ValueError :
          print("invalid input ❌ ")
