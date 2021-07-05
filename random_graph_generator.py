import time
import fast_dynamic_random_graph as fdrg
import sparse
from pathlib import Path
from joblib import Parallel, delayed
import multiprocessing
import itertools

if __name__ == "__main__":

    mp = False

    if mp:
        start_time = time.time()

        num_cores = multiprocessing.cpu_count()
        n = 1000
        nodes = [1000]
        t = [10000]
        up = [4 / n, 3 / n, 2 / n, 1 / n, 0.5 / n, 0.333 / n, 0.25 / n]
        down = [0.1, 0.3, 0.5, 0.7, 0.9]
        inputs = itertools.product(nodes, t, up, down)
        results = Parallel(n_jobs=num_cores)(delayed(fdrg.fast_dynamic_er_random_graph)(*i) for i in inputs)
        print("--- %s seconds ---" % (time.time() - start_time))

    else:

        start_time = time.time()
        for i in range(1, 2):
            for n in [int(1000 / i)]:
                for _ in range(8):
                    for t in [10000]:
                        for up in [1 / n]:
                            for down in [0.5]:
                                start_it = time.time()
                                f_name = Path(
                                    'data') / f'random_undirected_er_{n}_nodes_{t}_steps_{up}_up_{down}_down_{time.time()}.csv'
                                print(f'\n{f_name}')
                                fdrg.fast_dynamic_er_random_graph(n, t, up, down, f_name)
                                print(f"\nThis graph took: {time.time() - start_it} seconds")
        print("--- %s seconds ---" % (time.time() - start_time))
