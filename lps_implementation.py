from typing import *

def KMP_part_one(p : str) -> list:
    lps = [0 for _ in range(len(p))]
    j = 0
    i = 1

    while i < len(p):
        if p[i] == p[j]:
            lps[i] = j + 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
                continue
        i += 1
    return lps

    


assert KMP_part_one('aaacaaaa') == [0, 1, 2, 0, 1, 2, 3, 3], f'got {KMP_part_one('aaacaaaa')}'
assert KMP_part_one('dsgwadsgz') == [0, 0, 0, 0, 0, 1, 2, 3, 0], f'got {KMP_part_one('dsgwadsgz')}'