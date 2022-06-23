alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caeser(text, shift, direction):
  finalText = ''
  if direction == 'decode':
    shift *= -1
  for i in text:
    position = alphabet.index(i)
    position += shift
    finalText += alphabet[position]
  print(f"The {direction}d text is {finalText}")
  
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(text , shift , direction)