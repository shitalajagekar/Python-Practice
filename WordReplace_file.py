# Replacing word from file by another word eg. "excellent" by "very good"
"""
with open ("sample.txt") as f:
    content= f.read()

content= content.replace("excellent","Very good")
with open ("sample.txt","w") as f:
    f.write(content)

"""

# replace the words of list by "love" present in fie

words=["donky","Haramkhor","veda"]

with open("sample.txt") as f:
    conent=f.read()

for word in words:
    conent= conent.replace(word, " loves ")
    with open("sample.txt","w") as f:
        f.write(conent)