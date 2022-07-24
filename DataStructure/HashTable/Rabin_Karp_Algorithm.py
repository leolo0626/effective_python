# python3
random_x = 263
prime = 1000000007


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash_function(substring, p=prime, x=random_x):
    '''
    it is the hash function used in java for hashing the string
    :param substring:
    :param p: prime number
    :param x: x is random number between 1 to prime number
    :return: hash value of substring
    '''
    hash_value = 0
    for i in range(len(substring) - 1, -1, -1):  # reverse the substring
        hash_value = (hash_value * x + ord(substring[i])) % p
    return hash_value


def pre_compute_hashes(text: str, pattern_length: int):
    text_length = len(text)
    list_of_hash_value_of_sub_array = [None] * (len(text) - pattern_length + 1)
    last_substring = text[text_length - pattern_length:]
    list_of_hash_value_of_sub_array[-1] = poly_hash_function(last_substring)
    y = 1
    for _ in range(1, pattern_length + 1):
        y = (y * random_x) % prime

    for i in range(text_length - pattern_length - 1, -1, -1):
        list_of_hash_value_of_sub_array[i] = (random_x * list_of_hash_value_of_sub_array[i + 1] + ord(text[i])
                                              - y * ord(text[i + pattern_length])) % prime

    return list_of_hash_value_of_sub_array


def rabin_karp(text, pattern):
    positions = []
    p_hash = poly_hash_function(pattern)
    hash_table = pre_compute_hashes(text, len(pattern))
    for i in range(0, len(text) - len(pattern) + 1):
        if p_hash != hash_table[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)

    return positions


def get_occurrences(pattern, text):
    position = []
    if len(pattern) > len(text):
        return position

    return rabin_karp(text, pattern)


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

'''
aba
abacaba
'''

'''
Test
testTesttesT
'''

'''
aaaaa
baaaaaaa
'''