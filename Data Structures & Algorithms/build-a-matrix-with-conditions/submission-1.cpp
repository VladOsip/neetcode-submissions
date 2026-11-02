class Solution {
public:
    bool toposort(unordered_map<int, vector<int>> &adj, int start, vector<int> &visited, vector<int> &toposortlist) {
        if(visited[start] == 1) return false;
        if(visited[start] == 2) return true;
        visited[start] = 1;
        for(int n: adj[start]) {
            if(!toposort(adj, n, visited, toposortlist)) return false;
        }
        visited[start] = 2;
        toposortlist.push_back(start);
        return true;
    }
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<vector<int>> res(k, vector<int> (k, 0));
        unordered_map<int, vector<int>> rowadj, coladj;
        for(auto &rowcond: rowConditions) {
            rowadj[rowcond[0]].push_back(rowcond[1]);
        }
        for(auto &colcond: colConditions) {
            coladj[colcond[0]].push_back(colcond[1]);
        }
        vector<int> toposortrow, toposortcol;
        vector<int> rowvisited(k+1, 0), colvisited(k+1, 0);
        for(int i=1; i<=k; i++) {
            if(rowvisited[i] == 0) {
                if(!toposort(rowadj, i, rowvisited, toposortrow)) return {};
            }
        }
        for(int i=1; i<=k; i++) {
            if(colvisited[i] == 0) {
                if(!toposort(coladj, i, colvisited, toposortcol)) return {};
            }
        }
        reverse(toposortrow.begin(), toposortrow.end());
        reverse(toposortcol.begin(), toposortcol.end());
        unordered_map<int,int> rowindmp, colindmp;
        for(int i=0; i<toposortrow.size();  i++) {
            rowindmp[toposortrow[i]] = i;
        }
        for(int i=0; i<toposortcol.size();  i++) {
            colindmp[toposortcol[i]] = i;
        }
        int nextrow = toposortrow.size(), nextcol = toposortcol.size();
        for(auto [rowele, rowind]: rowindmp) {
            if(colindmp.count(rowele)) {
                int colind = colindmp[rowele];
                res[rowind][colind] = rowele;
            } else {
                res[rowind][nextcol++] = rowele;
            }
        }
        for(auto [colele, colind]: colindmp) {
            if(rowindmp.count(colele)) {
                int rowind = rowindmp[colele];
                res[rowind][colind] = colele;
            } else {
                res[nextrow++][colind] = colele;
            }
        }
        return res;
    }
};