import time
import fast_dynamic_random_graph as fdrg
import sparse
from pathlib import Path

if __name__ == "__main__":

    start_time = time.time()
    for _ in range(5):
        for n in [1000, 2000]:
            for t in [20000]:
                for up in [2 / n, 1 / n, 0.5 / n]:
                    for down in [0.3, 0.5, 0.7]:
                        start_it = time.time()
                        f_name = Path(
                            'data') / f'random_undirected_er_{n}_nodes_{t}_steps_{up}_up_{down}_down_{time.time()}.csv'
                        print(f'\n{f_name}')
                        fdrg.fast_dynamic_er_random_graph(n, t, up, down, f_name)
                        print(f"\nThis graph took: {time.time() - start_it} seconds")
    print("--- %s seconds ---" % (time.time() - start_time))
