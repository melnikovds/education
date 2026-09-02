names = ["Nisha", "Rani", "Ashu"]
for n in names:
    print(n[0])


class Solution:
    List = [1,4,2,3]
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return nums[0] * nums[1] * nums[2]

    def function(self, test_list: list | None = None) -> None:
        if test_list is None:
            test_list = []
        test_list.append(1)
        print(test_list)






