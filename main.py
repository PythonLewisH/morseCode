text = input("What text would you like converted into morse code?")

f = open("morse.txt", 'r')
morse_dictionary = {}
for line in f:
    k, v = line.strip().split(':')
    morse_dictionary[k.strip()] = v.strip()
f.close()

result = []

for i in text:
    i = i.upper()
    if i in morse_dictionary:
        result.append(morse_dictionary[i])
    elif i == ' ':
        result.append('/')
    else:
        result.append('#')

answer = " ".join(result)

print(answer)