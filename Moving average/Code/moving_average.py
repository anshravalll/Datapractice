import numpy as np

def moving_average(arr, window_size):
    if window_size <= 0:
        raise ValueError("Window size should be a positive integer.")
    
    if window_size > len(arr):
        raise ValueError("Window size cannot be larger than the array length.")
    
    averages = []
    
    for i in range(len(arr) - window_size + 1):
        # Calculate the sum of the current window and divide by the window size
        window_sum = sum(arr[i:i + window_size])
        averages.append(window_sum / window_size)
    
    return np.array(averages)


data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
window_size = 3
result = moving_average(data, window_size)
print("Moving Average:", result)
