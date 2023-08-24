# matching words in list
def find_word(words):
    for word in words:
        match word:
            case 'product':
                print('1')
            case 'text':
                print('2')
            case 'abs':
                print('3')
            case _:
                print('error')


words = ['for sale', 'sold', 'discount', 'product', 3, 3.14]
find_word(words)


# unpacking values from list


def unpack_data(book):
    match book:
        case [author, title, price, *_]:
            print(f"Book: {author}, {title}, {price}")
        case [index, author, title, price, year, *_]:
            print(f"Book: {index}, {author}, {title}, {price}, {year}")
        case _:
            print("incorrect data input")

book1 = ("John van Dijk", "Python", 1500)
book2 = [1, "Pirate", "Java", 3200.32, 2023]

unpack_data(book1)
unpack_data(book2)

