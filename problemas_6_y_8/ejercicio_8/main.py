n = int(input())
operations = []
heap = set()
output = []

for _ in range(n):
    record = input().split()
    operations.append(record)

for record in operations:
    if record[0] == "insert":
        x = int(record[1])
        output.append(record)
        heap.add(x)
    elif record[0] == "getMin":
        x = int(record[1])
        output.append(record)
        if len(heap) == 0 or min(heap) != x:
            output.append(["removeMin"])
            output.append(["insert", str(x)])
            heap.add(x)
    elif record[0] == "removeMin":
        output.append(record)
        if len(heap) == 0:
            output.append(["insert", "1"])
        heap.remove(min(heap))

print(len(output))
for record in output:
    print(" ".join(record))
