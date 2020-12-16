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


def compute_fields_order(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        fields, ticket, nearby = f.read().split('\n\n')
        authorized = _authorized_values(fields)
        nearby = _keep_valids(nearby, authorized)
        d_fields = _parse_fields(fields)
        tickets_fields = {k: set() for k in range(len(d_fields.keys()))}
        for n in nearby:
            print(n)
            # n.replace('\n', '')
            values = [int(i) for i in n.split(',')]
            for i, t in enumerate(n.split(',')):
                tickets_fields[i].add(t)
        print(tickets_fields)
