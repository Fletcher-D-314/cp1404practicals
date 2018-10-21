import wikipedia

search = input("Enter title or search phrase: ")
while search != "":
    try:
        page = wikipedia.page(search)
        print(page.title)
        print(page.url)
        print(page.summary)
        # print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print("\t\t***Search is too general***")
        print("Here is a disambiguation of more refined results:")
        print(e.options)
    search = input("Enter title or search phrase: ")
print("Thanks for searching")