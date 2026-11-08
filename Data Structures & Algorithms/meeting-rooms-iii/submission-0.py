from typing import List
from operator import setitem

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        return [r:=[0]*n, c:=[0]*n] and \
            [next(([setitem(r,i,e), setitem(c,i,c[i]+1)] for i,f in enumerate(r) if f<=s), 0) or setitem(r, q:=r.index(min(r)), r[q]+e-s) or setitem(c, q, c[q]+1) for s,e in sorted(m)] and \
            c.index(max(c))