data = [8, 7, 2, 1, 0, 9, 6]
def merge_sort_self(data):
    def merge_1(left, right):
        merged = list()
        l_idx, r_idx = 0, 0
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                merged.append(left[l_idx])
                l_idx += 1
            else:
                merged.append(right[r_idx])
                r_idx += 1
        merged.extend(left[l_idx:])
        merged.extend(right[r_idx:])
        return merged

    if len(data) <= 1:
        return data
    half = len(data) // 2
    return merge_1(merge_sort_self(data[:half]), merge_sort_self(data[half:]))


print(merge_sort_self(data))