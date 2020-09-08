from datetime import datetime

def time_this(NUM_RUNS=10):
    def decorator(func_to_run):
        def func(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            fn = func_to_run.__name__
            print(f"Среднее время выполнения {fn} за {NUM_RUNS} запусков: {datetime.now() - start} секунд")
            return result
        return func
    return decorator


#класс-секундомер
import time
class Timing:
    def __init__(self, function_to_run):
        self.num_runs = 100
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(f"Среднее время выполнения {fn} за {self.num_runs}: {avg} секунд.")
        return self.func_to_run(*args, **kwargs)