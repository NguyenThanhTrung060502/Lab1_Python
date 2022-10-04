file = open("books.csv", encoding="windows-1251")
header = file.readline()
array = []
new_array = []

count = 0

book_title = []
amount = []
line = file.readline()
while line != "":
	line = line.split(";")
	array.append(line)
	book_title.append(line[1])
	amount.append(line[10])
	line = file.readline()


for i in range(len(array)):
	if i not in new_array:
		count += 1
print("Количество неповторяющихся строк : " + str(count))


length = len(amount)
for i in range(length):
	if amount[i] == "":
		amount[i] = "0"
for i in range(0, length - 1):
	for j in range(i + 1, length):
		if int(amount[i]) > int(amount[j]):
			tmp = amount[i]
			amount[i] = amount[j]
			amount[j] = tmp
			name = book_title[i]
			book_title[i] = book_title[j]
			book_title[j] = name
print(" Самые популярные 20 книг ")
for i in range(20):
	print(book_title[i] + ": " + amount[i] + "\n")
file.close()






