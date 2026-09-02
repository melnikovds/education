def load_data(path: str) -> list[str]:
    """load lines from file and return as list"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def filter_valid(lines: list[str]) -> list[str]:
    """keep only non-empty lines"""
    return [line for line in lines if line.strip()]

def count_unique(lines: list[str]) -> int:
    """return number of unique lines"""
    return len(set(lines))


