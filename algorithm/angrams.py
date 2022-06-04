from collections import defaultdict
from collections import Counter
#problem anagrams
#Frequency of words must be the same and frequency of char in s1 and s2 must be the same

#first solution
def are_anagrams(s1,s2):
    if len(s1) != len(s2) :
        return False

    f1 = defaultdict(int)
    for c1 in s1 :
        f1[c1] += 1

    f2 = defaultdict(int)
    for c2 in s2 :
        f2[c2] += 1

    for key in f1 :
        if key not in f2 or f1[key] != f2[key] :
            return False

    return True

#Second solution
def are_anagrams_2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

if __name__ == "__main__" :
    print(are_anagrams("salesman", "salesman"))

    print(are_anagrams("salesman", "alessman"))

    print(are_anagrams_2("salesman", "salesman"))

    print(are_anagrams_2("salesman", "alessman"))