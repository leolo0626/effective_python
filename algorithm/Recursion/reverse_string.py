def reverse_string(input) :
    if input == "" :
        return ""
    return reverse_string(input[1:]) + input[0]

if __name__ == "__main__":
    print(reverse_string("Leo"))