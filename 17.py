nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)

num = (3, 6, 8, 2, 5)
print(num[2])
print(type(num))

sports = ["Cricket", "Football", "Badminton"]
choice = sports[0]
for s in sports:
    if "ball" in s.lower():
        choice = s
print(choice)

def update(x):
    x = x + [4]
a = [1, 2, 3]
update(a)
print(a)
print([4] + [1,2,3])

b = "10"
c = 3
print(int(b) ** c)
