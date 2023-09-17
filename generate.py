from random import randint


def gen_one_stat(n):
    a = []
    flag = True
    while flag:
        a = [randint(1, 6) for _ in range(n)]
        if a.count(min(a)) == 1:
            flag = False
    # print(a)
    a.remove(min(a))
    # print(a)
    return a


def gen_stats(n):
    mod = {
        '1': '-5',
        '2': '-4',
        '3': '-4',
        '4': '-3',
        '5': '-3',
        '6': '-2',
        '7': '-2',
        '8': '-1',
        '9': '-1',
        '10': '0',
        '11': '+1',
        '12': '+1',
        '13': '+2',
        '14': '+2',
        '15': '+3',
        '16': '+3',
        '17': '+4',
        '18': '+4',
        '19': '+5',
        '20': '+5',
        '21': '+6',
        '22': '+6',
        '23': '+7',
        '24': '+7',
        '25': '+8',
        '26': '+8',
        '27': '+9',
        '28': '+9',
        '29': '+10',
        '30': '+10'
    }

    stats = [sum(gen_one_stat(n)) for _ in range(6)]
    # print(stats)
    stats_mod = [mod[str(stats[i])] for i in range(6)]
    # print(stats)

    return stats, stats_mod
