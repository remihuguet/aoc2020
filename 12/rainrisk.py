from typing import List, Tuple


def compute_manhattan(filename: str) -> int:
    with open(filename, 'r') as f:
        mvts = f.readlines()
        final_pos = compute_final_position(mvts)
        return abs(final_pos[0]) + abs(final_pos[1])


directions = {
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'N': (0, 1)
}


def compute_new_direction(direction: Tuple[int, int], mvt: str) -> Tuple[int, i82nt]:
    dir_list = list(directions.values())
    if mvt[0] == 'R':
        return dir_list[(dir_list.index(direction) + int(int(mvt[1:]) / 90)) % 4]
    elif mvt[0] == 'L':
        return dir_list[(dir_list.index(direction) - int(int(mvt[1:]) / 90)) % 4]


def compute_final_position(mvts: List[str]) -> Tuple[int, int]:
    direction = directions['E']
    position = (0, 0)
    for mvt in mvts:
        if mvt[0] in ('R', 'L'):
            direction = compute_new_direction(direction, mvt)
        else:
            if mvt[0] == 'F':
                mv_dir = direction
            else:
                mv_dir = directions[mvt[0]]
            position = (position[0] + int(mvt[1:]) * mv_dir[0], position[1] + int(mvt[1:]) * mv_dir[1])
    return position


def compute_final_manhattan(filename: str) -> int:
    with open(filename, 'r') as f:
        mvts = f.readlines()
        final_pos = compute_position_waypoint(mvts, waypoint=(10, 1))
        return abs(final_pos[0]) + abs(final_pos[1])


def compute_position_waypoint(mvts: List[str], waypoint: Tuple[int, int]) -> Tuple[int, int]:
    boat = (0, 0)
    speed = waypoint
    direction = (1, 0)
    for mvt in mvts:
        if mvt[0] == 'F':
            boat = (boat[0] + int(mvt[1:]) * speed[0], boat[1] + int(mvt[1:]) * speed[1])
        elif mvt[0] in ['N', 'S', 'W', 'E']:
            direction = directions[mvt[0]]
            speed = (speed[0] + int(mvt[1:]) * direction[0], speed[1] + int(mvt[1:]) * direction[1])
        elif mvt[0] in ('R', 'L'):
            speed = compute_speed_rotation(speed, mvt)
    return boat


def compute_speed_rotation(speed: Tuple[int, int], mvt: str) -> Tuple[int, int]:
    transformations = {
        0: (1, 0, 0, 1),
        1: (0, -1, 1, 0),
        2: (-1, 0, 0, -1),
        3: (0, 1, -1, 0)
    }
    if mvt[0] == 'R':
        transfo = transformations[int(360 - int(mvt[1:]) / 90) % 4]
    else:
        transfo = transformations[int(int(mvt[1:]) / 90) % 4]

    speed = (speed[0] * transfo[0] + speed[1] * transfo[1], speed[0] * transfo[2] + speed[1] * transfo[3])
    return speed
