# def longest_substring_with_k_distinct(str, k):
#     window_start = 0
#     max_length = 0
#     char_frequency = {}

#     # in the following loop we'll try to extend the range(window_start, window_end)
#     for window_end in range(len(str)):
#         right_char = str(window_end)
#         if right_char not in char_frequency:
#             char_frequency[right_char] = 0
#         char_frequency[right_char]+=1

#         # Shrink the sliding window, until we are left with 'k' distinct characters in the char-frequency
#         whiel
