from datetime import date

password = "griffindore"
attempt = 3

while(attempt > 0):
    attempt -= 1
    passwordx = input("Enter password: ")
    if(password==passwordx):
        print("Welcome to your personal diary.")
        break
    else:
        print("You have entered worng password. Try again.")
else:
    print("Your access has been denied.")


entries = []

current = date.today().strftime("%d-%m-%Y")

title = input("Enter diary title: ")
mood = input("Enter your mood: ")

text = ""
print("Enter your diary text(Type END to finish)")
s=""
while(s != "END"):
    s = input().strip()

    if s != "END":
        text +="/n" + s

details ={}

details["date"]=current
details["title"]=title
details["mood"]=mood
details["text"]=text

entries.append(details)

print(details)

    
    