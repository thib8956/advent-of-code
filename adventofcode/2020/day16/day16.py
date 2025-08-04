# /usr/bin/env python3
import re
from collections import defaultdict

"""
identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field.
"""


def main(content):
    rules, my_ticket, other_tickets = content.split("\n\n")
    rules = parse_fields(rules)
    my_ticket = my_ticket.splitlines()[1]
    other_tickets = other_tickets.splitlines()[1:]
    print("Ticket scanning error rate ", part1(other_tickets, rules))
    part2(my_ticket, other_tickets, rules)


def parse_fields(fields):
    fields_dict = {}
    for field in fields.splitlines():
        k, v = field.split(": ")
        ranges = re.findall(r"(\d+)-(\d+)", v)
        fields_dict[k] = [range(int(r[0]), int(r[1]) + 1) for r in ranges]
    return fields_dict


def part1(tickets, rules):
    scanning_error_rate = 0
    for ticket in tickets:
        scanning_error_rate += sum(validate_ticket(ticket, rules))
    return scanning_error_rate


def validate_ticket(ticket, rules):
    invalid_fields = []
    for value in ticket.split(","):
        value = int(value)
        if not validate_field(value, *rules.values()):
            invalid_fields.append(value)
    return invalid_fields


def validate_field(field, *rules):
    validations = (any(field in r for r in rule) for rule in rules)
    return any(validations)


def part2(my_ticket, other_tickets, rules):
    # filter only valid tickets
    valid_tickets = [ticket for ticket in other_tickets if validate_ticket(ticket, rules) == []]
    valid_tickets.append(my_ticket)  # my ticket is valid

    # possible field for each index of a ticket
    candidates = defaultdict(set)
    for index in range(len(rules)):
        def inner():
            for rule_name, constraints in rules.items():
                for ticket in valid_tickets:
                    field_value = int(ticket.split(",")[index])
                    if not validate_field(field_value, constraints):
                        return
                candidates[index].add(rule_name)
        inner()
    
    sorted_candidates = sort_candidates(candidates)

    fields_indexes = {}
    try:
        while len(fields_indexes) != len(rules):
            index, found = sorted_candidates.popitem()
            found = next(iter(found))
            fields_indexes[index] = found
            sorted_candidates = remove_item(sorted_candidates, found)
    except:
        pass

    fields_indexes = {k: v for k,v in fields_indexes.items() if v.startswith('departure')}

    total = 1
    my_ticket = my_ticket.split(',')
    for index in fields_indexes:
        total *= int(my_ticket[index])
    a = 1


def sort_candidates(c):
    return {x: c[x] for x in sorted(c, key=lambda k: len(c[k]), reverse=True)}

def remove_item(candidates, item):
    ret = {}
    for key, value in candidates.items():
        try:
            value.remove(item)
        except ValueError:
            pass
        ret[key] = value

    #candidates = {k: set(v - item) for k,v in candidates.items()}
    return ret



if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        main(f.read())

