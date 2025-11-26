notes = []  # List to store all notes


def show_notes():
    if not notes:
        print("No notes yet!")
        return
    print("\nAll Notes:")
    for i, note in enumerate(notes, 1):
        fav = "⭐" if note.get("favorite") else ""
        print(f"{i}. {note['title']} {fav}")
        print(f"   {note['content'][:30]}...")  # show first 30 chars


def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({"title": title, "content": content, "favorite": False})
    print("Note added!\n")


# TODO: add edit_note(), delete_note(), search_notes(), favorite_note()


# Main menu loop
while True:
    print("\n--- Notes App ---")
    print("1. Show notes")
    print("2. Add note")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Search notes")
    print("6. Favorite/Unfavorite note")
    print("7. Exit")


    choice = input("Enter choice: ")
    if choice == "1":
        show_notes()
    elif choice == "2":
        add_note()
    elif choice == "7":
        print("Exiting Notes App...")
        break
    else:
        print("Option not implemented yet.")