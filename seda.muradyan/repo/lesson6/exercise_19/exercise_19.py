text = input("Please enter your plaintext: ")
shift = input("Please enter your key: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""

while isinstance(int(shift), int) == False:

 shift = input("Please enter your key (integers only!): ")

shift = int(shift)
  
for i in text:
  if i.lower() in alphabet:
    new_ind = alphabet.index(i) + shift
    ciphertext += alphabet[new_ind % 26]
  else:
    ciphertext += i    
print("The ciphertext is: " + ciphertext)