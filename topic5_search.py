"""Тема 5. Хеш-таблиця з delete + двійковий пошук з "верхньою межею"."""


# Завдання 1
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False


# Завдання 2
def binary_search_upper_bound(arr: list[float], target: float) -> tuple[int, float | None]:
    """Повертає (кількість ітерацій, найменший елемент >= target або None)."""
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            if arr[mid] == target:
                break
            high = mid - 1

    return iterations, upper_bound


if __name__ == "__main__":
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    print(H.get("orange"))   # 20
    H.delete("orange")
    print(H.get("orange"))   # None
    print(H.get("apple"))    # 10

    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
    print(binary_search_upper_bound(arr, 3.5))  # (3, 3.8)
    print(binary_search_upper_bound(arr, 2.5))  # знайдено точно
    print(binary_search_upper_bound(arr, 6.0))  # (.., None)
    print(binary_search_upper_bound(arr, 0.5))  # (.., 1.1)
