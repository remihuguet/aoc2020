from typing import List
from itertools import product


def _compute_mask(val: int, mask: str) -> str:
    a_val = [0] * 36
    b_val = bin(val)[2:]
    j = 0
    for i in range(36 - len(b_val), 36):
        a_val[i] += int(b_val[j])
        j += 1

    return [
        m if m in ('1', '0') else str(a_val[k]) for k, m in enumerate(mask)
    ]


def apply_mask(val: int, mask: str) -> int:
    return int(''.join(_compute_mask(val, mask)), 2)


def compute_init(filename: str) -> int:
    with open(filename, 'r') as f:
        lines = f.readlines()

        memory = {}

        mask = lines[0].split(' = ')[1].rstrip('\n')
        for line in lines[1:]:
            inst, val = line.split(' = ')
            if 'mask' in inst:
                mask = val.rstrip('\n')
                continue
            else:
                memory[inst] = apply_mask(int(val), mask)
        return sum(memory.values())


def compute_addresses(mem: int, mask: str) -> List[int]:
    masked = _compute_mask_mem(mem, mask)
    floatings = [((i, 1), (i, 0)) for i, v in enumerate(masked) if v == 'X']
    permutations = product(*[f for f in floatings])
    vals = []
    for p in permutations:
        val = masked.copy()
        for v in p:
            val[v[0]] = str(v[1])
        r = int(''.join(val), 2)
        vals.append(r)
    return vals


def _compute_mask_mem(val: int, mask: str) -> str:
    a_val = [0] * 36
    b_val = bin(val)[2:]
    j = 0
    for i in range(36 - len(b_val), 36):
        a_val[i] += int(b_val[j])
        j += 1
    return [
        m if m in ('1', 'X') else str(a_val[k]) for k, m in enumerate(mask)
    ]


def compute_init_2(filename: str) -> int:
    with open(filename, 'r') as f:
        lines = f.readlines()

        memory = {}

        mask = lines[0].split(' = ')[1].rstrip('\n')
        for line in lines[1:]:
            inst, val = line.split(' = ')
            if 'mask' in inst:
                mask = val.rstrip('\n')
                continue
            else:
                addr = compute_addresses(int(inst.split('[')[1].split(']')[0]), mask)
                for a in addr:
                    memory[a] = int(val)
        return sum(memory.values())
