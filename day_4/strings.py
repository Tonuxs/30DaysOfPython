#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md
# 1

thirty = 'thirty'
days = 'days'
of = 'of'
python = 'python'
full = thirty + ' ' + days + ' ' + of + ' ' + python
print(full)

# 2
Coding = 'Coding'
fore = 'for'
all = 'all'
coding_for_all = Coding + ' ' + fore + ' ' + all
print(coding_for_all)

# 3
company = 'coding for all'

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[7:10])

# 10
print(company.index('coding'))

# 11
print(company.replace('coding', 'python'))

# 12
print(company.replace('all', 'everyone'))

# 13
print(company.split())

# 14
tech = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(tech.split(', '))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
phrase = "Python For Everyone"
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)

# 19
phrase = "Coding for all"
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)

# 20
position = company.index('C')
print(position)

# 21
position = company.index('f')
print(position)

# 22
text = "Coding For All People"

position = text.rfind("l")
print(position)

# 23
text = "You cannot end a sentence with because because because is a conjunction"
position = text.find("because")
print(position)

# 24
sentence = "You cannot end a sentence with because because because is a conjunction"

start = sentence.index("because")
end = start + len("because because because")

phrase = sentence[start:end]
print(phrase)

# 25
text = "You cannot end a sentence with because because because is a conjunction"
position = text.rfind("because")
print(position)

# 26
text = "You cannot end a sentence with because because because is a conjunction"
start = text.rfind("because")
end = start + len("because because because")
phrase = text[start:end]
print(phrase)

# 27
text = "You cannot end a sentence with because because because is a conjunction"
position = text.find("because")
print(position)

# 28
string = "Coding For All"
print(string.startswith("Coding"))

# 29
print(string.endswith("coding"))

# 30
text = "   Coding For All      "
print(text.strip())

# 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")