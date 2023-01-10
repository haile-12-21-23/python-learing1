def find_maxNumber(numbers):
    maxNumber = numbers[0]
    for number in numbers:
        if maxNumber < number:
            maxNumber = number
    return maxNumber
