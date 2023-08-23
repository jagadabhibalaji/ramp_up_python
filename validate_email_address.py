import re

while True:
    user_input = input("Do you want to enter an email address? (Yes/No) :").lower()

    if user_input == 'no':
        file_read = open("email_txt.txt","r")
        print(file_read.read())
        break

    elif user_input == 'yes':
        email = input("Enter the email address :").lower()
        pattern = r"\w+(|.)\w+@[a-z]+\.[A-Za-z]{2,3}"
        out = re.search(pattern,email)
        if out:
            file_write = open(r"email_txt.txt","a")
            file_write.write(out.group()+"\n")
            file_write.close()
