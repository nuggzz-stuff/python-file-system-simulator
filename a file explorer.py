def login():
    password = "1234"
    attempts = 3

    while attempts > 0:
        userinput = input("enter password: ")

        if userinput == password:
            print("access granted")
            print()
            return True

        else:
            attempts -= 1
            print("wrong password, attempts left: " , attempts,)

    print("access denied")
    return False

files = []

if login():
    
    while True:
        print("total files:", len(files))
        print("1. add new file")
        print("2. view all files")
        print("3. search for a file")
        print("4. delete file")
        print("5. exit")

        try:
            choice = int(input("choose 1-5: "))
            print()
        except ValueError:
            print("invalid input, please enter a number 1-5")
            continue

        if choice == 1:
            name = input("file name: ")
            content = input("file content: ")
            author = input("file author: ")

            file = {
                "name": name,
                "content": content,
                "author": author
            }

            files.append(file)
            print("file added!")
            print()

        elif choice == 2:
            if len(files) == 0:
                print("no files yet. :(")
                print()
            else:
                for f in files:
                    print("file name:", f["name"])
                    print("file author:", f["author"])
                    print()

        elif choice == 3:
            filename = input("enter file name to search: ")

            found = False

            for f in files:
                if f["name"] == filename:
                    print("\n--- file opened ---")
                    print("name:", f["name"])
                    print("content:", f["content"])
                    print("author:", f["author"])
                    print()
                    found = True
                    break

            if not found:
                print("file not found. :(")
                print()

        elif choice == 4:
            filename = input("enter file name to delete: ")

            found = False

            for f in files:
                if f["name"] == filename:

                    confirm = input("are you sure? y/n: ")

                    if confirm.lower() != "y":
                        print("deletion cancelled")
                        print()
                        found = True
                        break

                    files.remove(f)
                    print("file deleted successfully.")
                    print()
                    found = True
                    break

            if not found:
                print("file not found. :(")
                print()

        elif choice == 5:
            print("goodbye")
            break

        else:
            print("invalid choice, please select 1-5")
            print()
