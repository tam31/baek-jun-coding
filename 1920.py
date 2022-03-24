n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = int(input())
m_data = (list(map(int, input().split())))


def array(start, end, target):
    while start <=end:
        mid = (start+end)//2
        if n_data[mid] == target:
            return True
        else:
            if n_data[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    return False

for i in m_data:
    if array(0, n-1, i):
        print(1)
    else:
        print(0)

                
