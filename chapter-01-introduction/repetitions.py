input_sequence = input()
max_len = 0
curr_len = 0
for idx, char in enumerate(input_sequence):
    curr_len += 1
    max_len = max(max_len, curr_len)
    if not ((idx + 1) >= len(input_sequence)):
        next_char = input_sequence[idx + 1]
        if next_char != char:
            curr_len = 0
print(max_len)
