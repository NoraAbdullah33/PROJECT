class Book : 

     def __init__(self, name : str , catgory : str ,descrip : str ) :
        self.name = name 
        self.catgory = catgory 
        self.descrip = descrip 

book1 = Book("Crime and Punishment","classic","Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, an old woman who stores money and valuable objects in her flat.")
book2 = Book("To the Lighthouse" ,"classic","The serene and maternal Mrs. Ramsay, the tragic yet absurd Mr. Ramsay, and their children and assorted guests are on holiday on the Isle of Skye. From the seemingly trivial postponement of a visit to a nearby lighthouse, Woolf constructs a remarkable, moving examination of the complex tensions and allegiances of family life")
book3 = Book("A Tale of Two Cities","classic","set against the violent upheaval of the French Revolution. The most famous and perhaps the most popular of his works, it compresses an event of immense complexity to the scale of a family history")
book4 = Book("You've reached sam ","Novel" ,"Seventeen-year-old Julie has her future all planned out—move out of her small town with her boyfriend Sam, attend college in the city, spend a summer in Japan. But then Sam dies. And everything changes.")
book5 = Book(" All the bright places " ,"Novel" ,"When Finch and Violet meet on the ledge of the bell tower at school, its unclear who saves whom. And when they pair up on a project to discover the “natural wonders” of their state, both Finch and Violet make more important discoveries." )
book6 = Book("Sad girls ","Novel" ,"School is almost out for Audrey,but the panic attacks are just beginning. Because Audrey told a lie and now her classmate, Ana, is dead. Just as her world begins to spin out of control, Audrey meets the enigmatic Rad—the boy who could turn it all around. But will their ill-timed romance drive her closer to the edge?")
book7 = Book("When no on is watching","thriller",
"Sydney and Theos deep dive into history quickly becomes a dizzying descent into paranoia and fear. and the push to revitalize the community may be more deadly than advertised.When does coincidence become conspiracy? Where do people go when gentrification pushes them out? Can Sydney and Theo trust each other―or themselves―long enough to find out before they too disappear?")
book8 = Book("The Silent Patient","thriller","One evening Alicia's husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, and then never speaks another word.Alicias refusal to talk, or give any kind of explanation")
book9 = Book("Gone Girl" ,"thriller","On a warm summer morning in North Carthage, Missouri, it is Nick and Amy Dunnes fifth wedding anniversary. Presents are being wrapped and reservations are being made when Nicks clever and beautiful wife disappears from their rented McMansion on the Mississippi River.")


book_classic =[book1.name , book2.name , book3.name]
book_Novel = [book4.name,book5.name,book6.name]
book_thriller = [book7.name,book8.name,book9.name] 

AllCat = ["classic" , " Novels " , "thriller"]

describ_books = { "Crime and Punishment" :"Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov,\n an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, \n an old woman who stores money and valuable objects in her flat." , "To the Lighthouse" : "The serene and maternal Mrs. Ramsay, \n the tragic yet absurd Mr. Ramsay, and their children and assorted guests are on holiday on the Isle of Skye.\n From the seemingly trivial postponement of a visit to a nearby lighthouse,\n Woolf constructs a remarkable, moving examination of the complex tensions and allegiances of family life",
"A Tale of Two Cities" : "set against the violent upheaval of the French Revolution.\n The most famous and perhaps the most popular of his works, \n it compresses an event of immense complexity to the scale of a family history" ,
 "You've reached sam " : "Seventeen-year-old Julie has her future all planned out—move out of her small town with her boyfriend Sam,\n attend college in the city, spend a summer in Japan.\n But then Sam dies. And everything changes." ,
  " All the bright places " : "When Finch and Violet meet on the ledge of the bell tower at school, \n its unclear who saves whom. And when they pair up on a project to discover the “natural wonders” of their state,\n both Finch and Violet make more important discoveries." ,
"Sad girls " : "School is almost out for Audrey,but the panic attacks are just beginning.\n Because Audrey told a lie and now her classmate, \n Ana, is dead. Just as her world begins to spin out of control, \n Audrey meets the enigmatic Rad—the boy who could turn it all around.\n But will their ill-timed romance drive her closer to the edge?" ,
"When no on is watching" : "Sydney and Theos deep dive into history quickly becomes a dizzying descent into paranoia and fear.\n and the push to revitalize the community may be more deadly than advertised. \n When does coincidence become conspiracy? Where do people go when gentrification pushes them out? Can Sydney and Theo trust each other―or themselves―long enough to find out before they too disappear?" , 
"The Silent Patient" : "One evening Alicia's husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, \n and then never speaks another word.Alicias refusal to talk,\n or give any kind of explanation",
 "Gone Girl" : "On a warm summer morning in North Carthage, Missouri, it is Nick and Amy Dunnes fifth wedding anniversary.\n Presents are being wrapped and reservations are being made when Nicks clever and beautiful wife disappears from their rented McMansion on the Mississippi River."}


TbrList = []

def addTOtbr() :
    newRead = str(input(" \t what is the name of the book 🏷 \t ")) 
    TbrList.append(newRead)
    print(" \t ✅ Added to your TBR A new book")