import concurrent.futures
import time
import random
import math
"""
Creates millions of random integers, exponents them to power of 3,
square roots them, converts them to cosine, and finally sums all.
Configurable processes and number of integers, performance gain
caps at physical core count.
"""
LENGTH_MIL = 100
MULTI_PROCESS = 12


def populate_list(numbers):
    full_list = []
    for a in range(numbers):
        full_list.append(random.randrange(100, 1000, 5))
    return full_list


def power_conv_to_cos(full_list):
    for a in full_list:
        a = math.cos(math.sqrt(math.pow(a, 3)))
    full_list = math.fsum(full_list)
    return full_list


def main():

    print("Testing with 1 thread.")
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:

        single_thr = executor.submit(populate_list, 1000000*LENGTH_MIL)
        full_list = single_thr.result()

        single_thr = executor.submit(power_conv_to_cos, full_list)
        full_list = single_thr.result()
        full_list = math.sqrt(full_list)
        print(full_list)
        print("--- %s seconds for 1 thr ---" % (time.time() - start_time))

    print(f"Testing with {MULTI_PROCESS} threads.")
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=MULTI_PROCESS) as executor:
        list_threads = []
        list_res = []

        for a in range(MULTI_PROCESS):
            thr = executor.submit(populate_list, 1000000 * LENGTH_MIL // MULTI_PROCESS)
            list_threads.append(thr)

        for a in list_threads:
            res = a.result()
            thr = executor.submit(power_conv_to_cos, res)
            list_res.append(thr)

        list_threads = []
        for a in list_res:
            res = a.result()
            list_threads.append(res)
        final_value = math.fsum(list_threads)
        final_value = math.sqrt(final_value)
        print(final_value)
        print(f"--- {time.time() - start_time} seconds for {MULTI_PROCESS} thr ---")


if __name__ == "__main__":
    main()
