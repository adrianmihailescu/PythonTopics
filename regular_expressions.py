import re

pattern = r"\b[A-Za-z]{3,}\b"  # Match words with 3 or more letters
text = "Python is fun!"

matches = re.findall(pattern, text)
print(matches)

text = "The color is green."
new_text = re.sub(r"green", "blue", text)
print(new_text)