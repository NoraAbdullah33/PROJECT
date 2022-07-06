def login():
   User = input(" 🔑 Enter userName : ")
   Password = input(" 🔑 Enter Password : ")
    
   fa = open("USER.txt","r")
   for l in fa.readlines():
      use , pw = l.strip().split("|")
   if (User in use ) and (Password in pw) :
      print("\t login is successful ✅ ")
      return True 
   print("\t wrong userName or Password ❌ ")
   return False