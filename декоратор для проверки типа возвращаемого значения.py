import faker

def ensure_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError(f"{func.__name__} returned non-string value: {result}")
        return result
    return wrapper

class DriverData:
    @staticmethod
    @ensure_string
    def driver_surname():
        return faker.last_name()

    @staticmethod
    @ensure_string
    def driver_name():
        return faker.first_name()

    @staticmethod
    @ensure_string
    def driver_patronymic():
        full_name = RussianNames(count=1, patronymic=True).get_batch()[0]
        parts = full_name.split()
        if len(parts) < 3:
            raise ValueError("Generated name does not contain a patronymic.")
        return parts[2]