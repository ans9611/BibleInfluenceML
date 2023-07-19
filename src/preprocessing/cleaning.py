import os 
output = "books"
if not os.path.exists(output):
    os.makedirs(output)

lines = open("../../data/bible.txt", "r").readlines()

books = [] 
books_idx = {}
tmp_book = None
# there are books which are First of, second of etc 
# we need to pick up their names 
multinames = ["Kings", "Paralipomenon", "Esdras", "Machabees",
              "Corinthians","Thessalonians", "Timothy", "Peter", "John"]
# then collect the name of the old testament books
old_books = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy","Josue", 
             "Judges", "Ruth", "1Kings", "2Kings", "3Kings", "4Kings", 
             "1Paralipomenon","2Paralipomenon", "1Esdras", "2Esdras", 
             "Tobias", "Judith", "Esther", "Job", "Psalms", "Proverbs", 
             "Ecclesiastes", "Canticle", "Wisdom", "Ecclesiasticus", "Isaias", 
             "Jeremias", "Lamentations", "Baruch", "Ezechiel", 
             "Daniel", "Osee", "Joel", "Amos", "Abdias", "Joans", "Micheas",
             "Nahum", "Habacuc", "Sophonias", "Aggeus", "Zacharias", "Malachias", 
             "1Machabees", "2Machabees"]


for i, val in enumerate(lines, 0):
    if "Chapter" in val:
        book_name = val.split()[0]
        possible_further_name = val.split()[1]
        if possible_further_name in multinames:
            current_book_name = book_name + possible_further_name
        else:
            current_book_name = book_name

        if not current_book_name in books:
            print(f"Adding {current_book_name} to books, starting idx {i}")
            tmp_book = current_book_name
            books.append(current_book_name)
            books_idx[current_book_name] = [i]
        else:
            books_idx[tmp_book].append(i)  # Update tmp_book when the book is already in books

# rest of the code