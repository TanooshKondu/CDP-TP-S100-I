#https://pastebin.com/RZgWrKYy

def Way1(word, index, n, result):
    if index == n:
        print("Vowels count is: ", result)
        return
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1
    Way1(word, index +1, n, result)

word = "abcdeefuigh"
Way1(word, 0, len(word), 0)

def Way2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = Way2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
word = "abcdeefuigh"
result = Way2(word, 0, len(word))
print("Vowels count is:", result)