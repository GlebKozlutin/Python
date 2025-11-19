text="hello world"
length=len(text)
print(length)

lengthh=0
for i in text:
    lengthh +=1
print(lengthh)

lengthhh=sum(1 for char in text)
print(lengthhh)