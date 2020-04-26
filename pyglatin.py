pyg = 'ay'
print('yoyo')
original = raw_input("Enter a word:" )
word = original[1:]
first = original[0]
new_word = word + first + pyg
if len(original) > 0 and original.isalpha():
  print new_word
else:
  print "empty"

  