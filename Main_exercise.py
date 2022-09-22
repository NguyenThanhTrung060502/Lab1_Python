file = open("books.csv", encoding="windows-1251")
header = file.readline()
header = header.split(";")
name_array = []
line = file.readline()
amount = 0
while line != "":
    line = line.split(";") 
    name_array.append(line[1])
    amount += 1
    line = file.readline()
print("количество записей в файле ```books.csv``` : " + str(amount))
count = 0
for i in range(0, len(name_array)):
    if len(name_array[i]) > 30:
        count += 1
print("количество записей, у которых в поле ```Название``` строка длиннее 30 символов: " + str(count))
file.close()

# ======= equest - 3 ========

file = open("books.csv", "r", encoding="windows-1251")
header = file.readline()
book_title = []
production_date = []
array = []
line = file.readline()
while line != "":
    line = line.split(";")
    array.append(line)
    book_title.append(line[1])
    new_line = line[6].split()
    date = new_line[0].split(".")
    production_date.append(date)
    line = file.readline()
name = input("Пожалуйста, введите имя автора: ")
print("Список книг автора 2014, 2016, 2017 годов:")
while name != "" :
    for i in range(len(array)):
        if "2014" in production_date[i] or "2016" in production_date[i] or "2017" in production_date[i]:
            if name in array[i] : 
                print(book_title[i])
    name = input("Пожалуйста, введите имя автора: ")
    print("Список книг автора 2014, 2016, 2017 годов:")
file.close()

# ========== Request - 4 ==========

file = open("books.csv", encoding="windows-1251")
header = file.readline()
new_file = open("books_new.txt", "wt", encoding="utf8")
line = file.readline()
amount = 1
while line != "" and amount < 21:
    line_list =  line.split(';')
    line_list[6] = line_list[6].strip('""')
    new_list = line_list[6].split("-")
    new_file.write(str(amount) + "." + line_list[3].strip('""') + "." + line_list[1].strip('""') + "-" + new_list[0] + "\n")
    amount += 1
    line = file.readline()
file.close()







