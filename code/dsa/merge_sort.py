import asyncio
from random import randint


async def merge(left: list[int], right: list[int], arr: list[int]) -> None:
    left_len, right_len = len(left), len(right)
    left_index, right_index, array_index = 0, 0, 0
    
    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            arr[array_index] = left[left_index]
            left_index += 1
        else:
            arr[array_index] = right[right_index]
            right_index += 1
        array_index += 1
    
    while left_index < left_len:
        arr[array_index] = left[left_index]
        left_index += 1
        array_index += 1
        
    while right_index < right_len:
        arr[array_index] = right[right_index]
        right_index += 1
        array_index += 1

async def merge_sort(arr: list[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        await merge_sort(left)
        await merge_sort(right)
        await merge(left, right, arr)
        
        
async def main():
    arr: list[int] = [randint(1, 1000) for _ in range(100)]
    print("Unsorted array:", arr)
    await merge_sort(arr)
    print("Sorted array:", arr)
    
if __name__ == "__main__":
    asyncio.run(main())
    