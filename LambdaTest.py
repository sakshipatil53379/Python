resultList = [[1, 80.0], [2, 73.33333333333333], [3, 80.0], [4, 88.33333333333333]]

resultList.sort(key=lambda result: result[1], reverse=True)

print(resultList)



def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(50)
print(f(10))

f1 = make_incrementor(100)
print(f1(-10))






