# -*- coding: utf-8 -*-
# @Author  : xiaoke


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # 控制将拿到的元素放到前面有序序列中正确位置的过程
        for i in range(j, 0, -1):
            # 如果比前面的元素小，则往前移动
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # 否则代表比前面的所有元素都小，不需要再移动
            else:
                break

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insert_sort(alist)
    print("新列表为：%s" % alist)