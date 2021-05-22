def countingSort(a):
    count = [0] * (max(a)+1)

    for i in range(len(a)):
        count[a[i]] += 1

    output = []
    for i in range(len(count)):
        for k in range(count[i]):
            output.insert(len(a)-1, i)
    return output
