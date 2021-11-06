def positive_negative(numbers):
    positive_sum = sum(list(filter(lambda x: (int(x) > 0), numbers)))
    negative_sum = sum(list(filter(lambda x: (int(x) < 0), numbers)))
    print(negative_sum, positive_sum, sep='\n')
    if abs(positive_sum) > abs(negative_sum):
        result = 'The positives are stronger than the negatives'
    else:
        result = "The negatives are stronger than the positives"
    print(result)


nums = [int(x) for x in input().split()]
positive_negative(nums)
