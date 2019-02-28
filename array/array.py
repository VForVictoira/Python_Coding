# 顺序表
class List:

    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def put(self, item):
        self.list.append(item)

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []

list=List()
for i in range(0,10):
    list.put(i)
print(list.size())
print(list)