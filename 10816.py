from bisect import bisect_left, bisect_right

n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()

m = int(input())
m_data = list(map(int, input().split()))

def array(nums, left_value, right_value):
    right_data = bisect_right(nums, right_value)
    left_data = bisect_left(nums, left_value)
    return right_data-left_data

for i in m_data:
    count = array(n_data, i, i)
    print(count, end=' ')
