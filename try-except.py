from tqdm.utils import DisableOnWriteError

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Zero")
except Exception:
    print("Exception")
finally:
    print("Done")

# Zero
# Done
