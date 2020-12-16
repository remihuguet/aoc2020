from typing import Set, List


def parse_authorize_values(filename: str) -> Set[int]:
    with open(filename, 'r') as f:
        data = f.read()
        fields, ticket, nearby = data.split('\n\n')
        return _authorized_values(fields)


def _authorized_values(fields: str) -> Set[int]:
    res = []
    for f in fields.split('\n'):
        values = f.split(':')[1].split('or')
        for v in values:
            v.replace('\n', '')
            res.extend(list(range(int(v.split('-')[0]), int(v.split('-')[1]) + 1)))
    return set(res)


def compute_error_rate(filename: str) -> int:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        invalid = 0
        for t in nearby.split('\n')[1:-1]:
            t.replace('\n', '')
            for i in t.split(','):
                if int(i) not in authorized:
                    invalid += int(i)
        return invalid


def keep_valid_tickets(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        nearby = nearby.split('\n')[1:-1]
        valids = []
        for t in nearby:
            t.replace('\n', '')
            values = [int(i) for i in t.split(',')]
            if len(list(filter(lambda p: p not in authorized, values))) > 0:
                continue
            valids.append(values)
        return valids
