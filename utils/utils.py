# utils.py
import time

def measure_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.
    
    Parameters:
    func (callable): The function to measure.
    *args: Positional arguments to pass to the function.
    **kwargs: Keyword arguments to pass to the function.
    
    Returns:
    float: The time taken to execute the function in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time