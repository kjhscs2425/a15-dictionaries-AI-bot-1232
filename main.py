text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
 

character_counts = {} #initialization
for char in text: #iterate through a string
    if char in character_counts:
        character_counts[char] += 1 
    else:
        character_counts[char] = 1 
print(character_counts)




