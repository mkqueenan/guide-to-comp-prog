n = int(input())
generated_nums = {i for i in range(1, n + 1)}
input_nums = {int(x) for x in input().split(' ')}
print((generated_nums - input_nums).pop())
