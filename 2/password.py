def validate_occurences(policy: str, pwd: str) -> bool:
    occurences, letter = policy.split(' ')
    min_occ, max_occ = occurences.split('-')

    return int(min_occ) <= pwd.count(letter) <= int(max_occ)


def validate_position(policy: str, pwd: str) -> bool:
    positions, letter = policy.split(' ')
    p1, p2 = (int(i) for i in positions.split('-'))
    return (
        pwd[p1 - 1] == letter and not pwd[p2 - 1] == letter
    ) or (
        not pwd[p1 - 1] == letter and pwd[p2 - 1] == letter
    )


def count_valids_positions(input_file: str) -> int:
    with open(input_file, 'r') as f:
        inputs = f.readlines()
        return len(
            list(
                filter(
                    lambda p: validate_position(
                        p.split(':')[0], p.split(': ')[1]
                    ), inputs
                )
            )
        )


def count_valids_occurences(input_file: str) -> int:
    with open(input_file, 'r') as f:
        inputs = f.readlines()
        return len(
            list(filter(
                lambda p: validate_occurences(p.split(': ')[0], p.split(':')[1]), inputs
            ))
        )
