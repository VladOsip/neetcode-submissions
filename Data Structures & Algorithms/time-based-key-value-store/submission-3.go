type Entry struct {
	Timestamp int
	Value     string
}

type TimeMap struct {
	store map[string][]Entry
}

func Constructor() TimeMap {
	return TimeMap{
		store: make(map[string][]Entry),
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.store[key] = append(this.store[key], Entry{Timestamp: timestamp, Value: value})
}

func (this *TimeMap) Get(key string, timestamp int) string {
	history, exists := this.store[key]
	if !exists {
		return ""
	}

	// sort.Search finds the smallest index i where the condition is true.
	// We want the first element strictly greater than our target timestamp.
	idx := sort.Search(len(history), func(i int) bool {
		return history[i].Timestamp > timestamp
	})

	// If idx is 0, it means even the first element has a timestamp greater than requested.
	if idx == 0 {
		return ""
	}

	// Go back one index to get the largest timestamp <= requested timestamp
	return history[idx-1].Value
}