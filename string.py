
s = "hello"

print(s + " how are you")

print(s[0::2])
print(s[::-1])
print(s[-1])

text = 'jake\'s book'                 #jake's book
print(text)

path = "C:\\notepad"                  #C:\notepad
print(path)

path = r"C:\\notepad"                 #C:\\notepad
print(path)

words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)                         #Python is awesome

print(len(s))
print(s.upper())
print(s.lower())
print(s.capitalize())

text =  "    hello   "
print(text.strip())

fruits = "apple, banana, cherry, mango"
print(fruits.split(","))


text = ("hello, "
		"how are you?")
print(text)

text = '''hello,
    how are you
	    bye'''
print(text)