class LFUCache {
private:
    struct Node {
        int key;
        int value;
        int freq;
        uint32_t prev;
        uint32_t next;
    };

    struct FreqList {
        uint32_t head;
        uint32_t tail;
    };

    struct DenseMap {
        static constexpr uint32_t EMPTY = 0xFFFFFFFF;
        struct Bucket { int key; uint32_t node_idx; };
        std::vector<Bucket> table;
        uint32_t mask;

        void init(size_t cap) {
            size_t size = 1;
            while (size < cap * 2) size <<= 1;
            mask = size - 1;
            table.resize(size, {0, EMPTY});
        }

        inline uint32_t hash(int key) const {
            return (static_cast<uint32_t>(key) * 2654435761U) & mask;
        }

        void insert(int key, uint32_t node_idx) {
            uint32_t idx = hash(key);
            while (table[idx].node_idx != EMPTY) {
                idx = (idx + 1) & mask;
            }
            table[idx] = {key, node_idx};
        }

        uint32_t find(int key) const {
            uint32_t idx = hash(key);
            while (table[idx].node_idx != EMPTY) {
                if (table[idx].key == key) return table[idx].node_idx;
                idx = (idx + 1) & mask;
            }
            return EMPTY;
        }

        void erase(int key) {
            uint32_t idx = hash(key);
            while (table[idx].node_idx != EMPTY) {
                if (table[idx].key == key) {
                    table[idx].node_idx = EMPTY;
                    uint32_t i = (idx + 1) & mask;
                    while (table[i].node_idx != EMPTY) {
                        int rk = table[i].key;
                        uint32_t rn = table[i].node_idx;
                        table[i].node_idx = EMPTY;
                        insert(rk, rn);
                        i = (i + 1) & mask;
                    }
                    return;
                }
                idx = (idx + 1) & mask;
            }
        }
    };

    uint32_t capacity;
    uint32_t size;
    uint32_t min_freq;
    
    std::vector<Node> nodes;
    std::vector<uint32_t> free_slots;
    DenseMap key_to_idx;
    std::vector<FreqList> freq_map;   
    static constexpr uint32_t NULL_IDX = 0xFFFFFFFF;

    void detach(uint32_t node_idx) {
        Node& node = nodes[node_idx];
        FreqList& list = freq_map[node.freq];

        if (node.prev != NULL_IDX) nodes[node.prev].next = node.next;
        else list.head = node.next;

        if (node.next != NULL_IDX) nodes[node.next].prev = node.prev;
        else list.tail = node.prev;
    }

    void attach_to_front(uint32_t node_idx, int freq) {
        Node& node = nodes[node_idx];
        node.freq = freq;
        
        if (freq >= freq_map.size()) {
            freq_map.resize(freq * 2, {NULL_IDX, NULL_IDX});
        }

        FreqList& list = freq_map[freq];
        node.prev = NULL_IDX;
        node.next = list.head;

        if (list.head != NULL_IDX) {
            nodes[list.head].prev = node_idx;
        } else {
            list.tail = node_idx;
        }
        list.head = node_idx;
    }

    void promote(uint32_t node_idx) {
        int old_freq = nodes[node_idx].freq;
        detach(node_idx);
        attach_to_front(node_idx, old_freq + 1);

        if (old_freq == min_freq && freq_map[old_freq].head == NULL_IDX) {
            min_freq++;
        }
    }

public:
    LFUCache(int capacity) : capacity(capacity), size(0), min_freq(0) {
        if (capacity == 0) return;
        nodes.resize(capacity);
        free_slots.resize(capacity);
        for (int i = 0; i < capacity; ++i) {
            free_slots[i] = capacity - 1 - i;
        }
        key_to_idx.init(capacity);
        freq_map.resize(1024, {NULL_IDX, NULL_IDX});
    }
    
    int get(int key) {
        if (capacity == 0) return -1;
        uint32_t node_idx = key_to_idx.find(key);
        if (node_idx == DenseMap::EMPTY) return -1;

        promote(node_idx);
        return nodes[node_idx].value;
    }
    
    void put(int key, int value) {
        if (capacity == 0) return;

        uint32_t node_idx = key_to_idx.find(key);
        if (node_idx != DenseMap::EMPTY) {
            nodes[node_idx].value = value;
            promote(node_idx);
            return;
        }

        if (size >= capacity) {
            uint32_t evict_idx = freq_map[min_freq].tail;
            key_to_idx.erase(nodes[evict_idx].key);
            detach(evict_idx);
            free_slots.push_back(evict_idx);
            size--;
        }

        uint32_t new_idx = free_slots.back();
        free_slots.pop_back();

        nodes[new_idx] = {key, value, 1, NULL_IDX, NULL_IDX};
        key_to_idx.insert(key, new_idx);
        attach_to_front(new_idx, 1);
        
        min_freq = 1;
        size++;
    }
};