import time
import multiprocessing

def factorize_number(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

def factorize_sync(*numbers):
    result = []
    for number in numbers:
        result.append(factorize_number(number))
    return result

def factorize_parallel(*numbers):
    pool = multiprocessing.Pool()
    result = pool.map(factorize_number, numbers)
    pool.close()
    pool.join()
    return result

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    result_sync = factorize_sync(*numbers)
    end_time = time.time()
    print(f"Synchronous version took {end_time - start_time:.4f} seconds")
    
    start_time = time.time()
    result_parallel = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Parallel version took {end_time - start_time:.4f} seconds")

    a, b, c, d = result_sync
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]