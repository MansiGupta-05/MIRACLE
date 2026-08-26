from priority_queue import EmergencyQueue


queue = EmergencyQueue()


queue.add_request({
    "id": "P01",
    "priority": "Low"
})

queue.add_request({
    "id": "P02",
    "priority": "Critical"
})

queue.add_request({
    "id": "P03",
    "priority": "High"
})

queue.add_request({
    "id": "P04",
    "priority": "Medium"
})


print("Processing order:")

while not queue.is_empty():
    request = queue.get_next()
    print(
        request["id"],
        "-",
        request["priority"]
    )