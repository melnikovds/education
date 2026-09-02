s = set("Banana")
print(len(s))


for ch in "Python":
    if ch == "h":
        continue
    print(ch, end="")


nums = [1, 2, 3, 4]
for n in nums:
    if n < 3:
        nums.remove(n)
print(nums)



