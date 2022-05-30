secret = "abcdefghijklmnopqrstuvwxyz"
num = "1234567891011121314151617181920212223242526"

print("The number you are about to enter would form a word or a sentence...")
secret_ques = input("Enter a number: ")
secret_ques = secret_ques.lower()

for i in secret_ques:
    if i.isnumeric():
        print(secret[num.index(i)], end="")
    else:
        print(i, end=" ")   
print("\n")


print("The letter you are about to enter would produce sequence of numbers")
letter = input("Enter a word: ")
letter = letter.lower()

for i in letter:
    if i.isalpha():
        print(num[secret.index(i)], end="")
    else:
        print(i)
     

