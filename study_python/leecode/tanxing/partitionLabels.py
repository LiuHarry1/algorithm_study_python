
def partitionLabels(s):

    # record the last occurance for each letter
    last_occurance = {char: idx for idx , char in enumerate(s)}

    start = end = 0
    result = []
    for i , char in enumerate(s):

        end = max(end, last_occurance[char])

        if i == end:

            result.append(end - start +1)
            start = i +1

    return result