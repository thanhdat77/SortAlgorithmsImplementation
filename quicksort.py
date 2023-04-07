data = [8, 7, 2, 1, 0, 9, 6]

def quick_sort_self(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    return (
        quick_sort_self([a for a in data if a < pivot])
        + [pivot]
        + quick_sort_self([a for a in data if a > pivot])
    )
print(quick_sort_self(data))


