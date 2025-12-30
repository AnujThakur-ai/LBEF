data = [10, 20, 30, 40, 50]
mean_  = sum(data) / len(data)
data_sorted = sorted(data)
if len(data_sorted) % 2 == 0:
    mid_index1 = len(data_sorted) // 2
    mid_index2 = mid_index1 - 1
    meadian_ = (data_sorted[mid_index1] + data_sorted[mid_index2]) / 2
else:
    mid_index = len(data_sorted) // 2
    meadian_ = data_sorted[mid_index]
print("Mean:", mean_)
print("Median:", meadian_)