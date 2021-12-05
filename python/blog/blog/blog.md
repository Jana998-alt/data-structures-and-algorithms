
Today we will be working out a code to sort an array assendengly.

Checkout our base Pseudocode that we will be following through out this totriul, it does not clear how it works at the first glimpse, do not worry. we will explain it step by step.

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

The best way to explain a solution is by example, so, let's take this array as our example to sort:
[8,4,23,42,16,15]

Let's dive into the code now!

as you can see in the picture below, in the first **FOR** loop, where i = 1 & j = 0. the element for the i index is smaller than the element for the j array, therefore, they should swap. notice in the pseudocode, there is a temperorry variable that holds the element for the i index (which is 4 in this case) throgh out the whole **FOR** loop. now entering the while loop, the two elements swap in there, this will be clearer in the next steps, bare with me.


![First and second loops in FOR]('../assets/nu-1-and-2.jpeg')

in the second **FOR** loop, where i = 2 & j = 1, there is no swapping because 23 is larger than 8. there is no swapping in the 3rd loop too.

![Third loop in FOR]('../assets/nu-3.jpeg')

Now to the 4th **FOR** loop, where i = 4 & j = 3.
Notice the steps in the hand written explenation below.
Also note that the *temp* variable stays the same throughout the while loop. it keeps changing its place untill it finds the right spot and sits there happily. things should be clear by now.

![Forth loop in FOR]('../assets/nu-4.jpeg')


finally, the 5th loop behaves the same way as the Forth one, check it out.

![Fifth loop in FOR]('../assets/nu-5.jpeg')


Now our array is beatifully sorted to become [4,8,15,16,23,42], and it isready to go!
