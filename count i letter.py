def count_words_starting_with_i(input_string):
    words = input_string.split()
    count_i_words =0
    for word in words:
        if word.startswith('I'):
            count_i_words += 1

    return count_i_words

input_string = "I love ice cream and India. The igloo is an interesting place."
result = count_words_starting_with_i(input_string)
print(f"Number of words starting with 'I': {result}")
