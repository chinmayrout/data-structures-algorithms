# Sorting Algorithms

**1. Bubble Sort**\
**2. Selection Sort**\
**3. Insertion Sort**\
**4. Merge Sort(Both Recur and Iterative)**\
**5. Quicksort(Both Recur and Iterative)**\

#### Pending

**6. Heapsort**\
**7. Counting Sort**\
**8. Radix Sort**\
**9. Bucket Sort**
<br/>

## **_Summary_**

|                | Worst    | Best     | Average  | Space   |
| -------------- | -------- | -------- | -------- | ------- |
| Selection Sort | O(n^2)   | O(n^2)   | O(n^2)   | O(1)    |
| Insertion Sort | O(n^2)   | O(n)     | O(n^2)   | O(1)    |
| Merge Sort     | O(n lgn) | O(n lgn) | O(n lgn) | O(n)    |
| Quicksort      | O(n^2)   | O(n lgn) | O(n lgn) | O(lg n) |
| Heapsort       | O(n lgn) | O(n)     | O(n lgn) | O(1)    |
| Counting Sort  | O(n)     | O(n)     | O(n)     | O(n)    |
| Radix Sort     | O(n)     | O(n)     | O(n)     | O(n)    |

## **_Which Sorting Algorithm Should I Use?_**

**_It depends. Each algorithm comes with its own set of pros and cons._**

- **Quicksort** is a good default choice. It tends to be fast in practice, and with some small tweaks its dreaded O(n^2) worst-case time complexity becomes very unlikely. A tried and true favorite.
- **Heapsort** is a good choice if you can't tolerate a worst-case time complexity of O(n^2) or need low space costs. The Linux kernel uses heapsort instead of quicksort for both of those reasons.
- **Merge sort** is a good choice if you want a stable sorting algorithm. Also, merge sort can easily be extended to handle data sets that can't fit in RAM, where the bottleneck cost is reading and writing the input on disk, not comparing and swapping individual items.
- **Radix sort** looks fast, with its O(n) worst-case time complexity. But, if you're using it to sort binary numbers, then there's a hidden constant factor that's usually 32 or 64 (depending on how many bits your numbers are). That's often way bigger than O(lg(n)), meaning radix sort tends to be slow in practice.
- **Counting sort** is a good choice in scenarios where there are small number of distinct values to be sorted. This is pretty rare in practice, and counting sort doesn't get much use.
