class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        grid = sorted( c for r in grid for c in r)

        def binary_search(arr):
            low = 0
            high = len(arr) - 1
            mid = 0
        
            while low <= high:
        
                mid = (high + low) // 2
        
                # If x is greater, ignore left half
                if arr[mid] < 0:
                    low = mid + 1
        
                # If x is smaller, ignore right half
                else:
                    high = mid - 1
        
            return 0 if low == 0 and arr[low] >= 0 else low
        
        
        # Function call
        result = binary_search(grid)
        
        return result