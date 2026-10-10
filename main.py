#8-misol
word = "Python"

for i in word:
    print(word, len(word),  sep="")

#9-misol
a = int(input("Son kirit: "))

while a:
    if a == 0:
        break
    elif a > 10:
        print(a)

#10-misol
n = 7

for n in range(n):
    print("*" * 7 )

#11-misol
text = "Pyhon dasturlash"

a = text.index('a')
print(a)

#12-misol
text = "programming"

a = text[::-1]
print(a)

#13-misol
text = "Men Python dasturlash tilini o‘rganaman"

a = len(text)
print(f" So'zlar Soni: {a}")
