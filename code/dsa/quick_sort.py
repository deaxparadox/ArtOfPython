from random import randint




class QuickSortPivotHigh:
    # swap function
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # partition function
    def partition(self, arr, low, high):
        pivot = arr[high]
        
        # index of smaller element and indicates
        # the right position of pivot found so far
        i = low - 1
        
        # traverse arr[low..high] and move all smaller
        # elements to the left side. Elements from low to
        # i are smaller after every iteration.
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                self.swap(arr, i, j)
        
        # move pivot after smaler elements and 
        # return its position
        self.swap(arr, i+1, high)
        return i+1

    # the QuickSort function implementation
    def quick_sort(self, arr, low, high):
        if low < high:
            
            # pi is the partition function index of pivot
            pi = self.partition(arr, low, high)
            
            # recursion calls for smaller elements
            # and greater or equals elements
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
    
    def main(self):
        arr = [10, 7, 8, 4, 2, 5, 1]
        n = len(arr)
        self.quick_sort(arr, 0, n-1)
        print(arr)
        
        
class QuickSortPivotLow:
    def partition(self, arr: list[int], low: int, high: int):
        pivot = arr[low]
        start = low+1
        end = high
        
        while True:
            while start <= end and arr[end] >= pivot:
                end -= 1
                
            while start <= end and arr[start] <= pivot:
                start += 1

            if start <= end:
                arr[start], arr[end] = arr[end], arr[start]
            else:
                break
        
        arr[low], arr[end] = arr[end], arr[low]
        return end

    
    def quicksort(self, arr: list[int], low: int, high: int):
        
        if low < high:
                
            idx = self.partition(arr, low, high)
            self.quicksort(arr, low, idx-1)
            self.quicksort(arr, idx+1, high)
            
        
    def main(self):
        # Example usage
        nums = [7, 2, 1, 6, 8, 5, 3, 4]
        print("Original array:", nums)
        low = 0
        high = len(nums) - 1
        self.quicksort(nums, low, high)
        print("Sorted  :", nums)

if __name__ == '__main__':
    QuickSortPivotLow().main()