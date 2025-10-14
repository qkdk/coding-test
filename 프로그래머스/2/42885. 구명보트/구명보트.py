from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    count = 0
    stack = []

    first_index = 0
    last_index = len(people) - 1
    while last_index > first_index:
        tmp_sum = people[first_index] + people[-1]

        if tmp_sum <= limit:
            people.pop()
            first_index += 1
            count += 1

        else:
            stack.append(people.pop())

        last_index -= 1

    count += len(stack) + len(people) - first_index
    print(count)
    return count