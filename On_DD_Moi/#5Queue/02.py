from collections import deque
def pageFaults(pages, capacity):
    memory = set()
    queue = deque()
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.add(page)
                queue.append(page)
            else:
                oldest = queue.popleft()
                memory.remove(oldest)
                memory.add(page)
                queue.append(page)
            page_faults += 1
    return page_faults

pages1 = [1, 3, 0, 3, 5, 6]
capacity1 = 3
print("Tổng lỗi trang ví dụ 1:", pageFaults(pages1, capacity1))

pages2 = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
capacity2 = 4
print("Tổng lỗi trang ví dụ 2:", pageFaults(pages2, capacity2))
