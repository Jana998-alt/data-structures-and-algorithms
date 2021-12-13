from blog.insertion_sort import insertion_sort


def test_for_case_1():
  arr = [8,4,23,42,16,15]
  excepted = [4, 8, 15, 16, 23, 42]
  actual = insertion_sort(arr)
  assert excepted == actual


def test_for_case_2():
  arr = [20,18,12,8,5,-2]
  excepted = [-2,5,8,12,18,20]
  actual = insertion_sort(arr)
  assert excepted == actual


def test_for_case_3():
  arr = [5,12,7,5,5,7]
  excepted = [5,5,5,7,7,12]
  actual = insertion_sort(arr)
  assert excepted == actual


def test_for_case_4():
  arr = [2,3,5,7,13,11]
  excepted = [2,3,5,7,11,13]
  actual = insertion_sort(arr)
  assert excepted == actual
  