class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current_path, visited):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])      # Choose
                    current_path.append(nums[i])
                    
                    backtrack(current_path, visited) # Explore
                    
                    current_path.pop()        # Backtrack
                    visited.remove(nums[i])

        visited = set()
        backtrack([], visited)
        return result