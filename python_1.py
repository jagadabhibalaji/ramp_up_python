string = input("Enter the the string statement :")
print("1. The main string statement :",string)

# ---> number of characters
print("2. Number of characters in a string :",(len(string)))

# ---> number of duplicate Characters
num_dup = []
try:
   for s in string:
      if s not in num_dup and string.count(s)>1:
         num_dup.append(s)
except:
   print("There is no duplicate characters in the string")
print("3. Number of duplicate Characters in string :",f"{num_dup} are {len(num_dup)}")

# ---> number of words
words = 1
try:
   for w in string:
      if (w == ' '):
         words = words+1
except:
   print("No words in the string")
print("4. Number of words in a string :",(words))

# ---> number of duplicate words
word_count = {}
num_word = string.split()
for word in num_word:
   if word in word_count:
      word_count[word] += 1
   else:
      word_count[word] = 1
for key, value in word_count.items():
   if value > 1:
      print("5. Number of duplicate words :",(f"'{key}' appears {value} times"))
else:
   print("5. There is no duplicate words in a string")

# ---> Reverse the characters
print("6. Reversing the characters :",(string[::-1]))

# ---> Reverse the words and forming ne statement
s = string.split()[::-1]
output = []
for i in s:
   output.append(i)
new_statement = ' '.join(output)
print("7. Reversing the string and forming new statement :",new_statement)

# ---> Remove the duplicate characters
dup_char = ""
for char in new_statement:
   if char not in dup_char:
      dup_char = dup_char + char
print("8. Removing the duplicate characters :",dup_char)

# ---> Print final latest String
print("9. Final latest String :",dup_char)



