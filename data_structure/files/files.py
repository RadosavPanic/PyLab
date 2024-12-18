sentenceToAddToFile = """Python is a general-purpose, high-level, object-oriented programming language.
It's used for web development, machine learning, data science and more."""

fp = open("pythoninfo.txt", "w")
fp.write(sentenceToAddToFile)
fp.close()

fp = open("pythoninfo.txt", "r")
# print(fp.read())  # reads file from start to the end, returns single string
# print(fp.read(10))  # reads first 10 characters in the line
# print(fp.readline())  # reads the whole line
print(fp.readlines())  # reads file from start to the end, returns a list with strings where each represent one line
fp.close()

fp = open("pythoninfo.txt", "a+")
fp.write("\nPython has a simple syntax, but is very powerful.")
fp.close()

fp = open("pythoninfo.txt", "r")
# getting the last line that was just appended
print(fp.readlines()[-1])  # Python has a simple syntax, but is very powerful.
print(fp.tell())  # 200, returns a current position of pointer within a file
fp.seek(10)  # change pointer position to 10
print(fp.tell())  # 10
print(fp.readline())  # a general-purpose, high-level, object-oriented programming language.