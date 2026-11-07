guest_list=[]
i=0
number=int(input("How many people do you want to invite:"))
while i<number:
    guest=str(input("enter guest name:"))
    guest_list.append(guest)
    i=i+1

for guest in guest_list: #printing a message to each guest
    print(f"{guest},Welcome to dinner")

absent=str(input("Unavailable:"))
if absent in guest_list:
    print(f"{absent} is not available for the dinner")
    guest_list.remove(absent)  #removing absents from guests
for guest in guest_list:
        print(f"{guest},Welcome to dinner")

# adding guests after founding a bigger dinner table

print("I found a bigger dinner table")
add_guest=input("Are there some people you forgot to invite('Yes'/'No'):")
add_guest=add_guest.lower()
if add_guest =="yes":
    n=int(input("How many people do you want to add:"))
    for j in range (n):
        guest=str(input("enter guest name:"))
        guest_list.append(guest)

# reducing guests after seeing that I'm able to invite 2 people only

for i in range(len(guest_list)-1):
      if i >1 :
        guest_list.pop()
        i= i-1
print("Hi guys.Unfortunately,I found that I'm able to invite two people only.I really apologize")
print(guest_list)
for guest in guest_list:
    print(f"Hello {guest},you are still invited to dinner")

# deleting the left guests in my list
del (guest_list[0])
del (guest_list[1])
print(f"My guest list right now is {guest_list}")





