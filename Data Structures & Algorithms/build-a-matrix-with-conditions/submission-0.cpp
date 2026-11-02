class Solution {
public:
    auto buildGraph(vector<vector<int>>& edges, int k) {
        vector<vector<int>> graph(k + 1);
        vector<int> indegree(k + 1);

        for (auto& e: edges) {
            graph[e[0]].push_back(e[1]);
            ++indegree[e[1]];
        }

        return make_pair(graph, indegree);
    }

    vector<int> topoSort(vector<vector<int>>& conditions, int k) {
        auto [graph, indegree] = buildGraph(conditions, k);

        vector<int> res;
        queue<int> q;

        for (int i = 1; i <= k; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            res.push_back(curr);

            for (auto& next: graph[curr]) {
                if (--indegree[next] == 0) {
                    q.push(next);
                }
            }
        }

        return res;
    }

    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<int> row = topoSort(rowConditions, k);
        if (row.size() < k) return {};

        vector<int> col = topoSort(colConditions, k);
        if (col.size() < k) return {};

        vector<int> indexes(k + 1);
        for (int j = 0; j < k; j++) {
            indexes[col[j]] = j;
        }

        vector<vector<int>> res(k, vector<int>(k, 0));
        for (int i = 0; i < k; i++){
            res[i][indexes[row[i]]] = row[i];
        }

        return res;
    }
};