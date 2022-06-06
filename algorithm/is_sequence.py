

def is_sequence(s, t) :
    if len(s) > len(t):
        return False

    if len(s) == 0:
        return True

    i = 0
    j = 0
    while i < len(t) and j < len(s):
        if t[i] == s[j] :
            j+=1
        i+=1

    if j == len(s) :
        return True

    return False

if __name__ == "__main__" :
    print(is_sequence("abc", "abbbbc"))
