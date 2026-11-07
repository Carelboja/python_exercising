name="Ada lovelace"
greeting='Hello'
print(name.title())
print(name.upper())
print(name.lower())
user_last_name=str(input("enter your last name:"))
user_first_name=str(input("enter your first name:"))
print(greeting + " "+user_first_name.title() + " "+user_last_name.upper())
print(f"{user_first_name.title()},we gonna play a game,you enter every name you want and I'm gonna write it correctly")
print("If for every question you respond (yes),we will continue but if (no),we stop")
user_agreement=str(input("Let's start:"))
while user_agreement == "yes":
      last_name=str(input("enter the last name:"))
      first_name=str(input("enter the first name:"))
      print(f"Hello {first_name.title()} {last_name.upper()}")
      user_agreement=str(input("Let's continue:"))


print (f"{user_first_name.title()} ,game ended automatically,see you ")

