import time
import fast_dynamic_random_graph as fdrg
import sparse
from pathlib import Path

if __name__ == "__main__":
    start_time = time.time()
    for _ in range(3):
        for n in [1000, 5000]:
            for t in [1000, 5000, 10000]:
                for up in [1 / n, 10 / n]:
                    for down in [0.3, 0.5, 0.7]:
                        start_it = time.time()
                        f_name = f'random_er_{n}_nodes_{t}_steps_{up}_up_{down}_down_{time.time()}.npz'
                        print(f_name)
                        G = fdrg.fast_dynamic_er_random_graph(n, t, up, down)
                        sparse.save_npz(
                            Path('data') / f_name, G)
                        print(f"\nThis graph took: {time.time() - start_it} seconds")
    print("--- %s seconds ---" % (time.time() - start_time))
