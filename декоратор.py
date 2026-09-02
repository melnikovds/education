def demo_decorator(func):
    def wrapper():
        print(f"starting '{func.__name__}'")
        func()
        print(f"finished '{func.__name__}'")
    return wrapper

@demo_decorator
def process_data():
    print("processing data")

@demo_decorator
def download_file():
    print("downloading file")

process_data()
download_file()

