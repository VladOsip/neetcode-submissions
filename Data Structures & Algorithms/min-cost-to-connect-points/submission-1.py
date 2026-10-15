class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        INF = float('inf')
        edges = []

        for k in range(4):
            # transforms: (x,y), (y,x), (-y,x), (x,-y)
            if k == 0:
                pts = [(x, y, i) for i, (x, y) in enumerate(points)]
            elif k == 1:
                pts = [(y, x, i) for i, (x, y) in enumerate(points)]
            elif k == 2:
                pts = [(-y, x, i) for i, (x, y) in enumerate(points)]
            else:
                pts = [(x, -y, i) for i, (x, y) in enumerate(points)]

            # sweep by descending x, ties by descending y
            pts.sort(key=lambda p: (-p[0], -p[1]))

            keys = sorted(set(y - x for x, y, _ in pts))
            m = len(keys)
            # reversed rank so that "key >= current" becomes a prefix query
            rank = {v: m - j for j, v in enumerate(keys)}  # 1..m

            tree_val = [INF] * (m + 1)
            tree_id = [-1] * (m + 1)

            for x, y, i in pts:
                r = rank[y - x]

                # query prefix [1..r]: points already seen with key >= y-x
                best, best_id = INF, -1
                j = r
                while j > 0:
                    if tree_val[j] < best:
                        best, best_id = tree_val[j], tree_id[j]
                    j -= j & -j
                if best_id != -1:
                    d = (abs(points[i][0] - points[best_id][0]) +
                         abs(points[i][1] - points[best_id][1]))
                    edges.append((d, i, best_id))

                # insert current point, minimizing x+y
                s = x + y
                j = r
                while j <= m:
                    if s < tree_val[j]:
                        tree_val[j] = s
                        tree_id[j] = i
                    j += j & -j

        # Kruskal
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        edges.sort()
        total, used = 0, 0
        for d, u, v in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                total += d
                used += 1
                if used == n - 1:
                    break
        return total