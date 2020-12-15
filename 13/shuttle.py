from typing import List


def compute_earliest_bus(time: int, buses: List[int]) -> int:
    earliest, bus_id = time, 0

    for bus in buses:
        before = (time // bus) * bus
        if before == time:
            earliest, bus_id = 0, bus
        else:
            after = before + bus

            if after - time < earliest:
                earliest, bus_id = after - time, bus
    return bus_id, earliest


def compute_result_part_1(filename: str) -> int:
    with open(filename) as f:
        d = f.readlines()
        time = int(d[0].rstrip('\n'))
        buses = [int(i) for i in d[1].rstrip('\n').split(',') if i != 'x']
        bus_id, waiting_time = compute_earliest_bus(time, buses)
        return bus_id * waiting_time
