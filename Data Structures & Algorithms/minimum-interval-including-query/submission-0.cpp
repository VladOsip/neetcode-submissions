class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size();
        int q = queries.size();
        
        sort(intervals.begin(), intervals.end());
        
        vector<pair<int, int>> sortedQueries(q);
        for (int i = 0; i < q; ++i) {
            sortedQueries[i] = {queries[i], i};
        }
        sort(sortedQueries.begin(), sortedQueries.end());
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> res(q, -1);
        int i = 0;
        
        for (const auto& queryPair : sortedQueries) {
            int qVal = queryPair.first;
            int originalIdx = queryPair.second;
            
            while (i < n && intervals[i][0] <= qVal) {
                int l = intervals[i][0];
                int r = intervals[i][1];
                minHeap.push({r - l + 1, r});
                i++;
            }
            
            while (!minHeap.empty() && minHeap.top().second < qVal) {
                minHeap.pop();
            }
            
            if (!minHeap.empty()) {
                res[originalIdx] = minHeap.top().first;
            }
        }
        
        return res;
    }
};