# python3
import sys



def compute_min_refills(distance, tank, stops):
    remaining_fuel = tank
    cur_location = 0
    step_count = 0

    if remaining_fuel >= distance :
        return step_count
    for next_stop in stops :
        if remaining_fuel + cur_location >= next_stop:
            remaining_fuel = remaining_fuel - (next_stop-cur_location)
        else:
            remaining_fuel = tank - (next_stop-cur_location)
            if remaining_fuel < 0:
                return -1
            step_count += 1
        cur_location = next_stop

    if remaining_fuel + cur_location < distance :
        if cur_location + tank >= distance:
            step_count += 1
        else:
            return -1

    return step_count




if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
