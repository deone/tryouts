def selection_sort(alist):
  for n in range(len(alist)-1):
    min_index = n
    for o in range(n+1, len(alist)):
      print o
      if alist[o] < alist[n]:
        min_index = o
        swap(alist, n, min_index)
  return alist

def swap(alist, index1, index2):
  tmp = alist[index1]
  alist[index1] = alist[index2]
  alist[index2] = tmp

def bubble_sort(alist):
  for n in range(len(alist)-1):
    # print n, len(alist)-n-1
    is_sorted = True
    for o in range(len(alist)-n-1):
      # print alist[o+1], alist[o]
      if alist[o+1] < alist[o]:
        swap(alist, o, o+1)
        is_sorted = False
      # print alist
    if is_sorted:
      break
  return alist
