def minimum(*args):
  for i in args:
    is_min = True
    for j in args:
      if i > j:
        is_min = False
        continue
    if is_min:
      return i


def maximum(*args):
  for i in args:
    is_max = True
    for j in args:
      if i < j:
        is_max = False
        continue
    if is_max:
      return i


print(minimum(5, 4, 2, 3, 2, 11, 6, 7, 9, 14, 3))
print(maximum(5, 4, 2, 3, 2, 21, 6, 7, 9, 14, 3, 21))
