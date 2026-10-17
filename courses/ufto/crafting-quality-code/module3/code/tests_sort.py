import bubble_sort
import selection_sort
import insertion_sort

L = [4, 2, 5, 6, 7, 3, 1]

print("Buble sort - after each pass of sorting")
bubble_sort.bubble_sort(L)

L = [4, 2, 5, 6, 7, 3, 1]

print("Selection sort - after each pass of sorting")
selection_sort.selection_sort(L)

L = [4, 2, 5, 6, 7, 3, 1]

print("Insertion sort - after each pass of sorting")
insertion_sort.insertion_sort(L)

print("Selection sort - after each pass of sorting")
L = [1, 5, 8, 7, 6, 1, 7]
selection_sort.selection_sort(L)

print("Insertion sort - after each pass of sorting")
L = [6, 8, 2, 1, 1, 9, 4]
insertion_sort.insertion_sort(L)

print("Insertion sort - after each pass of sorting")
L = [2, 3, 4, 5, 6, 7, 1]
insertion_sort.insertion_sort(L)

print("Insertion sort - after each pass of sorting")
L = [2, 3, 4, 5, 6, 7, 8, 9, 1]
insertion_sort.insertion_sort(L)