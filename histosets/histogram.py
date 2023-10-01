import threading
import numpy as np

class Histogram:
    def __init__(self, intervals):
        # Initialize histogram data structures, thread locks, etc.
        self.intervals = intervals
        self.interval_counts = {interval: 0 for interval in intervals}
        self.sample_count = 0
        self.sample_sum = 0
        self.sample_sum_squared = 0
        self.lock = threading.Lock()

    def insert_samples(self, samples):
        for sample in samples:
            interval = self.find_interval(sample)
            if interval:
                with self.lock:  
                    self.interval_counts[interval] += 1
                    self.update_statistics(sample)

    def find_interval(self, sample):
        for interval in self.intervals:
            if interval[0] <= sample < interval[1]:
                return interval
        return None  # Sample does not belong to any interval

    def update_statistics(self, sample):
        with self.lock:  # Lock to ensure thread safety
            self.sample_count += 1
            self.sample_sum += sample
            self.sample_sum_squared += sample ** 2

    def get_metrics(self):
        with self.lock:  # Lock to ensure thread safety while calculating metrics
            if self.sample_count == 0:
                sample_mean = 0.0
                sample_variance = 0.0
            else:
                sample_mean = self.sample_sum / self.sample_count
                sample_variance = (
                    self.sample_sum_squared / self.sample_count
                ) - (sample_mean ** 2)

            metrics = {
                "sample_mean": sample_mean,
                "sample_variance": sample_variance,
                "interval_counts": self.interval_counts,
            }
            return metrics
if __name__ == '__main__':
    intervals = [(3, 4.1), (8.5, 8.7), (4, 4.5), (0, 1.1), (31.5, 41.27)]
    histogram = Histogram(intervals)
    