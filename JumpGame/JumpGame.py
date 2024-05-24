class Solution(object):
    def canJump(self, nums):
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
        return True

def main():
    solution = Solution()

    in_array = [2, 3, 1, 1, 4]
    result = solution.canJump(in_array)
    print(f"Can jump to the last index: {result}")
    
    in_array = [3, 2, 1, 0, 4]
    result = solution.canJump(in_array)
    print(f"Can jump to the last index: {result}")


if __name__ == "__main__":
    main()
