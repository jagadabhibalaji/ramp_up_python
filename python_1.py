# string = input("Enter the the string statement :")
string = "Balu is my Balu"
print("The main string statement :",string)

# number of characters
print("number of characters in a string :",(len(string)))

# number of duplicate Characters
num_dup = []
for s in string:
   if s not in num_dup and string.count(s)>1:
      num_dup.append(s)
print("number of duplicate Characters in string :",len(num_dup))

# number of words
words = 1
for w in string:
   if (w == ' '):
      words = words+1
print("number of words in a string :",(words))

# number of duplicate words
word_count = {}
num_word = string.split()
for word in num_word:
   if word in word_count:
      word_count[word] += 1
   else:
      word_count[word] = 1
for key, value in word_count.items():
   if value > 1:
      print("number of duplicate words :",(f"'{key}' appears {value} times"))

# Reverse the characters
print("Reversing the characters :",(string[::-1]))

# Reverse the words and forming ne statement
s = string.split()[::-1]
output = []
for i in s:
   output.append(i)
new_statement = ' '.join(output)
print("Reversing the string and forming new statement :",new_statement)

# Remove the duplicate characters
dup_char = ""
for o in new_statement:
   if o not in dup_char:
      dup_char = dup_char + o
print("Removing the duplicate characters :",dup_char)

# Print final latest String
print("Final latest String :",dup_char)


