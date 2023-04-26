# Patryk Stopyra
# Department of Fundamentals of Computer Science
# Wroclaw University of Technology
# 2022
#
# Slots/TDMA dynamic-programming calculator (v0.1)
import time
from prompt_mac_calculator.api import *

logging.basicConfig(level=logging.DEBUG)


def find_best_selects(k_transmitters: int, n_slots: int) -> None:
    tslots = tslots_optimal_selects_choice(k_transmitters, n_slots)
    bernoulli = bernoulli_optimal_probability_choice(k_transmitters, n_slots)
    print(f'Optimal config tSlots (size, probability):\t\t{tslots}')
    print(f'Optimal config Bernoulli (size, probability):\t{bernoulli}')
    print(f'Ratio: {tslots[1] / bernoulli[1]}')


if __name__ == '__main__':
    transmitters: int = 10
    slots: int = 64
    start_t = time.time()
    find_best_selects(transmitters, slots)
    print(f'time: {time.time() - start_t}')
