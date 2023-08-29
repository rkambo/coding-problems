class TimeMap:

    def __init__(self):
        self.map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.map.get(key) == None:
            self.map[key] = []
        self.map.get(key).append([timestamp,value])
    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key)
        if values == None or len(values) == 0:
            return ""
        left, right = 0, len(values) - 1
        while left <= right:
            # print("LEFT: " + str(values[left]))
            mid = (left + right) // 2
            if(values[mid][0] == timestamp):
                return values[mid][1]
            elif timestamp < values[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        if values[left-1][0] <= timestamp:
            return values[left-1][1]
        else:
            return ""