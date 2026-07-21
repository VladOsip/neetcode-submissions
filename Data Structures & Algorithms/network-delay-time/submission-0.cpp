class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // 1. Build the adjacency list
        vector<vector<pair<int, int>>> adj(n + 1);
        for (const auto& edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            adj[u].push_back({v, w});
        }

        // 2. Initialize distances array with infinity
        vector<int> dist(n + 1, 1e9);
        dist[k] = 0;

        // 3. Min-Heap tracking {travel_time, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k});

        while (!pq.empty()) {
            auto [time, u] = pq.top();
            pq.pop();

            // Skip outdated or suboptimal paths
            if (time > dist[u]) continue;

            // 4. Relax neighbors
            for (const auto& neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }

        // 5. Find the maximum time required
        int max_time = 0;
        for (int i = 1; i <= n; ++i) {
            if (dist[i] == 1e9) return -1; // Node is unreachable
            max_time = max(max_time, dist[i]);
        }

        return max_time;
    }
};