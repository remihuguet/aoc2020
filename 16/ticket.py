from typing import Dict, Set, List


def parse_authorize_values(filename: str) -> Set[int]:
    with open(filename, 'r') as f:
        data = f.read()
        fields, ticket, nearby = data.split('\n\n')
        return _authorized_values(fields)


def _parse_fields(fields: str) -> Dict:
    res = {}
    for f in fields.split('\n'):
        f.replace('\n', '')
        key, values_raw = f.split(':')
        if key not in res:
            res[key] = []
        values = values_raw.split('or')
        for v in values:
            res[key].extend(list(range(int(v.split('-')[0]), int(v.split('-')[1]) + 1)))
        res[key] = set(res[key])
    return res


def _authorized_values(fields: str) -> Set[int]:
    d_fields = _parse_fields(fields) 
    res = set()
    for f in d_fields.values():
        res.update(f)
    return res


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


def _keep_valids(nearby: str, authorized: List[int]) -> List[List[int]]:
    nearby = nearby.split('\n')[1:-1]
    valids = []
    for t in nearby:
        t.replace('\n', '')
        values = [int(i) for i in t.split(',')]
        if len(list(filter(lambda p: p not in authorized, values))) > 0:
            continue
        valids.append(values)
    return valids


def keep_valid_tickets(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        return _keep_valids(nearby, authorized)


def _fields_order(d_fields: Dict, nearby: List[List[int]]) -> List[str]:
    tickets_fields = {k: set() for k in range(len(d_fields.keys()))}
    for n in nearby:
        for i, t in enumerate(n):
            tickets_fields[i].add(t)

    res = {}
    for f, v in tickets_fields.items():
        for k, a in d_fields.items():
            if v.issubset(a):
                if f not in res:
                    res[f] = [k]
                else:
                    res[f].append(k)

    fields = [0] * len(tickets_fields.keys())

    c = {k: len(v) for k, v in res.items()}
    candidates = [k for k in sorted(c.keys(), key=lambda e: c[e])]
    for candidate in candidates:
        f_cand = [i for i in res[candidate] if i not in fields]
        fields[candidate] = f_cand[0]
    return fields


def compute_fields_order(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        nearby = _keep_valids(nearby, authorized)
        d_fields = _parse_fields(fields)
        return _fields_order(d_fields, nearby)


def decode(filename: str) -> Dict:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        nearby = _keep_valids(nearby, authorized)
        d_fields = _parse_fields(fields)
        order = _fields_order(d_fields, nearby)
        ticket = [int(i) for i in ticket.split('\n')[1].split(',')]
        return {order[i]: v for i, v in enumerate(ticket)}


def compute_part_2(filename: str) -> Dict:
    ticket = decode(filename)
    res = 1
    for k, v in ticket.items():
        if 'departure' in k:
            res *= v
    return res
