def DFS(index: int):
    s = [index]
    while len(s) != 0:
        index = s.pop()
        if not visited[index]:
            stack.append(index + 1)  # Убрать "+ 1", если хочется, чтобы нумерация была с нуля
            visited[index] = True
        for i in range(n):
            if table[index][i] != 0 and not visited[i]:
                s.append(i)


with open("input.txt", "r") as f:
    n = int(f.readline())
    table = []

    for i in range(n):
        data = list(map(int, f.readline().split()))
        table.append(data)

visited = [False] * n
current_pos = 0
counter = 1

stack = list()
for i in range(n):
    if not visited[i]:
        DFS(i)

        stack.sort()
        print(f"{counter}: {str(stack)}\n")
        counter += 1
        stack = list()
print(f"Количество компонент связности: {counter - 1}")
