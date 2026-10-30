class FreqStack {
private:
    std::unordered_map<int, int> freqMap;
    std::unordered_map<int, std::stack<int>> groupMap;
    int maxFreq;

public:
    FreqStack() {
        maxFreq = 0;
    }
    
    void push(int val) {

        int freq = ++freqMap[val];
        maxFreq = std::max(maxFreq, freq);
        groupMap[freq].push(val);
    }
    
    int pop() {
        int val = groupMap[maxFreq].top();
        groupMap[maxFreq].pop();
        
        freqMap[val]--;
        
        if (groupMap[maxFreq].empty()) {
            maxFreq--;
        }
        
        return val;
    }
};