import heapq


PRIORITY = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}


class EmergencyQueue:

    def __init__(self):
        self.queue = []

    def add_request(self, request):
        priority = PRIORITY[request["priority"]]

        heapq.heappush(
            self.queue,
            (priority, request)
        )

    def get_next(self):
        if not self.queue:
            return None

        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0