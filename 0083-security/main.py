def validate_one(start_schedule, end_schedule):
    if start_schedule[0] == 0 and end_schedule[0] == 10000:
        print('Accepted')
    else:
        print('Wrong Answer')


def validate_more_two(start_schedule, end_schedule):
    max_end = end_schedule[0]
    min_start = start_schedule[0]

    for time in range(1, len(start_schedule)):
        if end_schedule[time] <= max_end or start_schedule[time] > end_schedule[time-1] or start_schedule[time] <= min_start:
            print('Wrong Answer')
            break
        else:
            max_end = end_schedule[time]
            min_start = end_schedule[time-1]
    else:
        print('Accepted')


def main():
    count = int(input())
    for _ in range(count):
        numbers = [int(x) for x in input().split()]
        n = numbers[0]

        start_schedule = numbers[1: 2 * n + 1: 2]
        end_schedule = numbers[2: 2 * n + 1: 2]

        guards = sorted(zip(start_schedule, end_schedule))
        start_schedule = [g[0] for g in guards]
        end_schedule = [g[1] for g in guards]

        count_employees = len(start_schedule)
        if start_schedule[0] != 0 or end_schedule[-1] != 10000:
            print('Wrong Answer')
            continue

        if count_employees == 1:
            validate_one(start_schedule, end_schedule)
            continue

        if count_employees >= 2:
            validate_more_two(start_schedule, end_schedule)
            continue

if __name__ == '__main__':
    main()