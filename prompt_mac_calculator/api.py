import logging

from tdma_calc.algorithms.bernoulli import communication_success_bernoulli
from tdma_calc.algorithms.tslots import communication_success_probability


def tslots_success_probability(transmitters: int, slots: int, selects: int) -> float:
    """
    Calculates the all-agents communication success probability for tSlots strategy.
    tSlots strategy assumes that each agent selects t-size transmission set of available slots.

    :param transmitters: number of the transmitting agents
    :param slots: number of the available slots
    :param selects: predefined size of each agent's transmission slot
    :return: all-agents communication success probability
    """
    try:
        return communication_success_probability(transmitters, slots, selects)
    except ValueError as ex:
        logging.warning(f'Calculation threw exception: {ex}')
        return 0.0


def tslots_optimal_selects_choice(transmitters: int, slots: int) -> (int, float):
    """
    Finds the optimal size of agents' transmission set and the corresponding success probability.
    tSlots strategy assumes that each agent selects t-size transmission set of available slots.

    :param transmitters: number of the transmitting agents
    :param slots: number of the available slots
    :return: tuple of (optimal size of the transmission set, communication success probability)
    """
    best_selects = initial_selects = max(slots//transmitters, 1)
    probability = 0.0
    for selects in range(initial_selects, 0, -1):
        new_probability = tslots_success_probability(transmitters, slots, selects)
        if new_probability >= probability:
            probability = new_probability
            best_selects = selects
        else:
            break
    return best_selects, probability


def bernoulli_success_probability(transmitters: int, slots: int, broadcast_probability: float) -> float:
    """
    Calculates the all-agents communication success probability for BT strategy.
    Bernoulli trials (BT) strategy assumes that each agent tosses whether to transmit in each slot separately.

    :param transmitters: number of the transmitting agents
    :param slots: number of the available slots
    :param broadcast_probability: probability of the transmission in each slot
    :return: all-agents communication success probability
    """
    return communication_success_bernoulli(transmitters, slots, broadcast_probability)


def bernoulli_optimal_probability_choice(transmitters: int, slots: int) -> (float, float):
    """
    Finds agents' best broadcast probability setup and the corresponding communication success probability.
    Bernoulli trials (BT) strategy assumes that each agent tosses whether to transmit in each slot separately.

    :param transmitters: number of transmitting agents
    :param slots: number of available slots
    :return: tuple of (optimal slot transmission probability, communication success probability)
    """
    best_probability = 1 / transmitters
    return best_probability, bernoulli_success_probability(transmitters, slots, best_probability)

