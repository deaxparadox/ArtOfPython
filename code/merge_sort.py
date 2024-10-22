import random

def merge_sort(num: list[int]) -> list[int]:
    if len(num) > 1:
        m = len(num) // 2
        left = num[:m]
        right = num[m:]
        merge_sort(left)
        merge_sort(right)

            
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                num[k] = left[i]
                i+=1
            else:
                num[k] = right[j]
                j+=1
            k+=1
            
        while i < len(left):
            num[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            num[k] = right[j]
            j+=1
            k+=1
    
def main():
    arr = [
        random.randint(1, 100) for x in range(11)
    ]
    print(arr)
    merge_sort(arr)
    print(arr)
    

if __name__ == "__main__":
    main()