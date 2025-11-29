#3-misol
sentence = input("Jumla kiriting: ")

words = sentence.split()  
secret_code = ""          

for w in words:
    secret_code += w[0]   

print(secret_code)
