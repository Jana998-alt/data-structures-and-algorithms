
  # InsertionSort(int[] arr)

  #   FOR i = 1 to arr.length

  #     int j <-- i - 1
  #     int temp <-- arr[i]

  #     WHILE j >= 0 AND temp < arr[j]
  #       arr[j + 1] <-- arr[j]
  #       j <-- j - 1

  #     arr[j + 1] <-- temp


def insertion_sort(arr):

  for i in  range(1,len(arr)):

    j = i-1
    temp = arr[i]

    while j>= 0 and temp < arr[j]:
      arr[j+1] = arr[j]
      j = j-1

      arr[j+1] = temp

  return arr

if __name__ == "__main__":
  arra = [8,4,23,42,16,15]
  print(insertion_sort(arra))

