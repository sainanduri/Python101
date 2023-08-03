
word1 = "racer"
word2 = "carer"

word1_dict = {}
word2_dict = {}
#  O(n) + O(n) + O(n) + O(1) = O(3n+1) = O(n)
for c1 in word1:
    if c1 not in word1_dict:
        word1_dict[c1] = 1
    else:
        word1_dict[c1] += 1
print(word1_dict)

for c2 in word2:
    if c2 not in word2_dict:
        word2_dict[c2] = 1
    else:
        word2_dict[c2] += 1
print(word2_dict)

anagram_found = True
for key1 in word1_dict:
    if key1 not in word2_dict:
        anagram_found = False
        break
    else:
        if word1_dict[key1] != word2_dict[key1]:
            anagram_found = False
            break

if anagram_found:
    print("Anagram found")
else:
    print("Anagram not found")
