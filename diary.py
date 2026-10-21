
def authenticate():
    password = "griffindore"
    attempt = 3

    while attempt > 0:
        passwordx = input("Enter password: ")

        if passwordx == password:
            print("Welcome to your personal diary!")
            return True

        attempt -= 1
        print("Wrong password. Attempts remaining:", attempt)

    print("Your access has been denied.")
    return False


def encrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        else:
            result += char

    return result



def decrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        else:
            result += char

    return result



def read_entries():
    entries = []

    try:
        with open("diary.txt", "r") as file:
            lines = file.readlines()

        i = 0

        while i < len(lines):
            if lines[i].strip() == "ENTRY":
                details = {}

                i += 1
                details["date"] = lines[i].rstrip("\n").split(":", 1)[1]

                i += 1
                details["title"] = lines[i].rstrip("\n").split(":", 1)[1]

                i += 1
                details["mood"] = lines[i].rstrip("\n").split(":", 1)[1]

                i += 1  # Skip TEXT_START
                text_lines = []

                while i < len(lines) and lines[i].rstrip("\n") != "TEXT_END":
                    text_lines.append(lines[i].rstrip("\n"))
                    i += 1

                encoded_text = "\n".join(text_lines)
                details["text"] = decrypt(encoded_text.replace("~", "\n"))

                entries.append(details)

            i += 1

    except FileNotFoundError:
        pass

    return entries

def write_entry():
    current = input("Enter date (DD-MM-YYYY): ")
    title = input("Enter diary title: ")
    mood = input("Enter your mood: ")

    print("Enter your diary text (type END to finish):")
    text_lines = []

    while True:
        s = input()

        if s == "END":
            break

        text_lines.append(s)

    text = "\n".join(text_lines)

    details = {
        "date": current,
        "title": title,
        "mood": mood,
        "text": text
    }

    with open("diary.txt", "a") as file:
        file.write("ENTRY\n")
        file.write("DATE:" + current + "\n")
        file.write("TITLE:" + title + "\n")
        file.write("MOOD:" + mood + "\n")
        file.write("TEXT_START\n")
        file.write(encrypt(text).replace("\n", "~") + "\n")
        file.write("TEXT_END\n")

    print("Diary entry saved successfully!")


def view_entries():
    entries = read_entries()

    if not entries:
        print("No diary entries found.")
        return

    print("\n===== YOUR DIARY ENTRIES =====")

    for details in entries:
        print("\n------------------------")
        print("Date:", details["date"])
        print("Title:", details["title"])
        print("Mood:", details["mood"])
        print("Text:", details["text"])


def search_entries():
    keyword = input("Enter a keyword to search: ").strip().lower()

    if not keyword:
        print("Please enter a keyword.")
        return

    entries = read_entries()
    found = False

    for details in entries:
        if (keyword in details["title"].lower()
                or keyword in details["text"].lower()):

            found = True
            print("\n------------------------")
            print("Date:", details["date"])
            print("Title:", details["title"])
            print("Mood:", details["mood"])
            print("Text:", details["text"])

    if not found:
        print("No matching entries found.")



def date_key(date_text):
    parts = date_text.split("-")

    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])

    return year * 10000 + month * 100 + day


def filter_by_date():
    start = input("Enter start date (DD-MM-YYYY): ")
    end = input("Enter end date (DD-MM-YYYY): ")

    try:
        start_key = date_key(start)
        end_key = date_key(end)

        # Validate the basic date format
        for value in [start, end]:
            parts = value.split("-")

            if (len(parts) != 3 or len(parts[0]) != 2
                    or len(parts[1]) != 2 or len(parts[2]) != 4):
                print("Use DD-MM-YYYY format.")
                return

            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])

            if month < 1 or month > 12 or day < 1 or day > 31:
                print("Invalid date.")
                return

    except (ValueError, IndexError):
        print("Invalid date format.")
        return

    if start_key > end_key:
        print("Start date must be before end date.")
        return

    entries = read_entries()
    found = False

    for details in entries:
        entry_key = date_key(details["date"])

        if start_key <= entry_key <= end_key:
            found = True
            print("\n------------------------")
            print("Date:", details["date"])
            print("Title:", details["title"])
            print("Mood:", details["mood"])
            print("Text:", details["text"])

    if not found:
        print("No entries found in this date range.")



def edit_entry():
    entries = read_entries()

    if not entries:
        print("No diary entries to edit.")
        return

    print("\n===== EDIT DIARY ENTRY =====")

    for i, details in enumerate(entries, start=1):
        print(i, ".", details["title"], "|", details["date"])

    try:
        number = int(input("Enter entry number to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(entries):
        print("Invalid entry number.")
        return

    details = entries[number - 1]

    print("1. Edit title")
    print("2. Edit mood")
    print("3. Edit text")
    print("4. Cancel")

    choice = input("Enter choice: ")

    if choice == "1":
        details["title"] = input("Enter new title: ").strip()

    elif choice == "2":
        details["mood"] = input("Enter new mood: ").strip()

    elif choice == "3":
        print("Enter new text (type END to finish):")
        text_lines = []

        while True:
            line = input()

            if line == "END":
                break

            text_lines.append(line)

        details["text"] = "\n".join(text_lines)

    elif choice == "4":
        print("Edit cancelled.")
        return

    else:
        print("Invalid choice.")
        return

    # Rewrite the file with the updated entries
    with open("diary.txt", "w") as file:
        for entry in entries:
            file.write("ENTRY\n")
            file.write("DATE:" + entry["date"] + "\n")
            file.write("TITLE:" + entry["title"] + "\n")
            file.write("MOOD:" + entry["mood"] + "\n")
            file.write("TEXT_START\n")
            file.write(entry["text"] + "\n")
            file.write("TEXT_END\n")

    print("Entry updated successfully!")



def delete_entry():
    entries = read_entries()

    if not entries:
        print("No diary entries to delete.")
        return

    print("\n===== DELETE DIARY ENTRY =====")

    for i, details in enumerate(entries, start=1):
        print(i, ".", details["title"], "|", details["date"])

    try:
        number = int(input("Enter entry number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(entries):
        print("Invalid entry number.")
        return

    details = entries[number - 1]

    print("\nSelected entry:", details["title"])
    confirm = input("Are you sure you want to delete it? (yes/no): ")

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    entries.pop(number - 1)

    with open("diary.txt", "w") as file:
        for entry in entries:
            file.write("ENTRY\n")
            file.write("DATE:" + entry["date"] + "\n")
            file.write("TITLE:" + entry["title"] + "\n")
            file.write("MOOD:" + entry["mood"] + "\n")
            file.write("TEXT_START\n")
            file.write(entry["text"] + "\n")
            file.write("TEXT_END\n")

    print("Entry deleted successfully!")


def mood_statistics():
    entries = read_entries()

    moods = ["Happy", "Okay", "Sad", "Stressed", "Excited"]

    if not entries:
        print("No diary entries found.")
        return

    print("\nMood Statistics")

    for mood in moods:
        count = 0

        for entry in entries:
            if entry["mood"].lower() == mood.lower():
                count += 1

        print(mood + ": " + str(count))



if authenticate():
    while True:
        print("\n===== PERSONAL DIARY =====")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Search by keyword")
        print("4. Filter bt dates")
        print("5. Edit entry")
        print("6. delete entry")
        print("7. Mood Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            edit_entry()
        elif choice == "6":
            delete_entry()
        elif choice == "7":
            mood_statistics()
        elif choice =="8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
