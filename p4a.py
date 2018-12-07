import re
from collections import Counter

test_input = \
    '''[1518-11-01 00:00] Guard #10 begins shift
    [1518-11-01 00:05] falls asleep
    [1518-11-01 00:25] wakes up
    [1518-11-01 00:30] falls asleep
    [1518-11-01 00:55] wakes up
    [1518-11-01 23:58] Guard #99 begins shift
    [1518-11-02 00:40] falls asleep
    [1518-11-02 00:50] wakes up
    [1518-11-03 00:05] Guard #10 begins shift
    [1518-11-03 00:24] falls asleep
    [1518-11-03 00:29] wakes up
    [1518-11-04 00:02] Guard #99 begins shift
    [1518-11-04 00:36] falls asleep
    [1518-11-04 00:46] wakes up
    [1518-11-05 00:03] Guard #99 begins shift
    [1518-11-05 00:45] falls asleep
    [1518-11-05 00:55] wakes up'''


def take_first(elem):
    return elem[0]


def sort_by_time(inlist: list):
    outlist = []
    for entry in inlist:
        date, action = entry.split(']')
        timestamp = int(''.join(re.findall('\d+', date)))
        guard, state = re.findall('\d+', action), re.findall('\w+', action)
        outlist.append([timestamp, guard, state])
    outlist.sort(key=take_first)
    for i, entry in enumerate(outlist):
        if entry[1] == []:
            outlist[i][1] = outlist[i - 1][1]
    return outlist


def count_asleep(guard_info):
    guard_dict = Counter()

    for i, (timestamp, guard, activity) in enumerate(guard_info):
        if 'wakes' in activity:
            guard_dict[guard[0]] += timestamp - guard_info[i - 1][0]

    return guard_dict


def extract_most_asleep_minute(guard_info, guard_in):
    minute_dict = Counter()
    for i, (timestamp, guard, activity) in enumerate(guard_info):
        if 'wakes' in activity and guard[0] == guard_in:
            for j in range(timestamp - guard_info[i - 1][0]):
                this_minute = abs(guard_info[i - 1][0]) % 100 + j
                minute_dict[this_minute] += 1
    return minute_dict


if __name__ == '__main__':
    with open('4.txt') as f:
        test_input = f.read()
        guard_info = sort_by_time(test_input.split('\n'))
        guard_sleep = count_asleep(guard_info)
        sleepiest_guard = ''
        sleep_max = max(guard_sleep.values())
        for guard in guard_sleep.keys():
            if guard_sleep[guard] == sleep_max:
                sleepiest_guard = guard
        guard_minute = extract_most_asleep_minute(guard_info, sleepiest_guard)
        minute_max = max(guard_minute.values())
        sleepiest_minute = 0
        for minute in guard_minute.keys():
            if guard_minute[minute] == minute_max:
                sleepiest_minute = minute
        print(int(sleepiest_guard) * sleepiest_minute)
