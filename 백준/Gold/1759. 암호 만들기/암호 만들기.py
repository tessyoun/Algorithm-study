L, C = map(int, input().split())
alphabet = input().split()
alphabet.sort()

def dfs(idx, word):
    global result
    
    if len(word) == L:
        vowels = 0
        consonants = 0
        for w in word:
            if w in "aeiou":
                vowels += 1
            else:
                consonants += 1
        
        if vowels >= 1 and consonants >= 2:
            result.append(word[:])
        return
    
    if idx == C:
        return
    
    dfs(idx + 1, word)
    
    word.append(alphabet[idx])
    dfs(idx + 1, word)
    word.pop() 


result = []
dfs(0, [])

for i in range(len(result)):
    print("".join(result[len(result) - i - 1]))