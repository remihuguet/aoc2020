import re
from typing import List


def read_batch(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        content = f.read()
        return [
            p.replace('\n', ' ') for p in content.split('\n\n')
        ]


def is_valid(passport: str) -> bool:
    patterns = [
        re.compile('byr:'),
        re.compile('iyr:'),
        re.compile('eyr:'),
        re.compile('hgt:'),
        re.compile('hcl:'),
        re.compile('ecl:'),
        re.compile('pid:'),
        # re.compile('cid:'),
    ]
    for p in patterns:
        if not p.search(passport):
            return False
    return True


def count_valids(filename: str) -> int:
    passports = read_batch(filename)
    return _count_valids(passports)


def _count_valids(passports: List[str]) -> int:
    return len(
        list(
            filter(
                lambda c: c is True,
                [
                    is_valid(i) for i in passports
                ]
            )
        )
    )


def count_valid_passports(passports: List[str]) -> int:
    return len(
        list(
            filter(
                lambda c: c is True,
                [
                    are_fields_valid(i) for i in passports
                ]
            )
        )
    )


def are_fields_valid(passport):
    funcs = [
        is_byr_valid,
        is_hgt_valid,
        is_iyr_valid,
        is_eyr_valid,
        is_hcl_valid,
        is_ecl_valid,
        is_pid_valid
    ]
    for f in funcs:
        if not f(passport):
            return False
    return True


def is_byr_valid(passport: str) -> bool:
    p = re.compile(r'byr:(19[2-9][0-9]($|\s)|(200[0-2]($|\s)))')
    return p.search(passport) is not None


def is_hgt_valid(passport: str) -> bool:
    p = re.compile(r'hgt:(1(([5-8][0-9])|(9[0-3]))cm($|\s))|(59|(6[0-9])|(7[0-6]))in($|\s)')
    return p.search(passport) is not None


def is_iyr_valid(passport: str) -> bool:
    p = re.compile(r'iyr:20((1[0-9])|20)($|\s)')
    return p.search(passport) is not None


def is_eyr_valid(passport: str) -> bool:
    p = re.compile(r'eyr:20((2[0-9])|30)($|\s)')
    return p.search(passport) is not None


def is_hcl_valid(passport: str) -> bool:
    p = re.compile(r'hcl:#([0-9a-z]{6})($|\s)')
    return p.search(passport) is not None


def is_ecl_valid(passport: str) -> bool:
    p = re.compile(r'ecl:((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))($|\s)')
    return p.search(passport) is not None


def is_pid_valid(passport: str) -> bool:
    p = re.compile(r'pid:[0-9]{9}($|\s)')
    return p.search(passport) is not None
