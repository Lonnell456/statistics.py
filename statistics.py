class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        from collections import Counter
        data_count = Counter(self.data)
        max_count = max(data_count.values())
        modes = [key for key, value in data_count.items() if value == max_count]
        return modes

# Example usage
data = [1, 2, 2, 3, 4, 5, 5, 5]
stats = StatisticsCalculator(data)
print(f"Mean: {stats.mean()}")
print(f"Median: {stats.median()}")
print(f"Mode: {stats.mode()}")
