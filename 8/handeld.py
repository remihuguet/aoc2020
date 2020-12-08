from typing import List, Tuple


def _execute_code(code: List[str]) -> Tuple[int, int]:
    accu, register, current_index = 0, list(), 0

    while current_index < len(code):
        instr, val = code[current_index].split(' ')
        val = int(val)

        if current_index in register:
            return accu, False
        register.append(current_index)

        current_index += val if instr == 'jmp' else 1
        accu += val if instr == 'acc' else 0

    return accu, True


def compute_accumulator_value(filename: str) -> int:
    with open(filename, 'r') as f:
        instructions = f.readlines()
        return _execute_code(instructions)[0]


def compute_final_value_debugged_code(filename: str) -> int:
    with open(filename, 'r') as f:
        instructions = f.readlines()

        candidates = [(i, v) for i, v in enumerate(instructions) if 'nop' in v or 'jmp' in v]
        accu, ok = _execute_code(instructions)

        for c, v in candidates:
            inst, _ = v.split(' ')
            cinst = instructions.copy()
            if inst == 'jmp':
                cinst[c] = v.replace('jmp', 'nop')
            else:
                cinst[c] = v.replace('nop', 'jmp')
            accu, ok = _execute_code(cinst)
            if ok:
                break
        return accu
