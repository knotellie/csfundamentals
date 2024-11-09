def word_reverser(word):
  return word[::-1]

# Three calls:
# First call: Value

print(word_reverser("This sentence will be reversed"))

# Second call: Variable

text_to_reverse = input("I can reverse your text! Write anything! ")
reversed_text = word_reverser(text_to_reverse)
print(reversed_text)

# Third call: Expression

print(word_reverser(text_to_reverse + " this will be reversed too"))