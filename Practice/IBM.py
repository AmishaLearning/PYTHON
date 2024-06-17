
def getTotalExecutionTime(n, logs):
    exclusive_times = [0] * n
    stack = []
    prev_timestamp = 0

    for log in logs:
        log_parts = log.split(':')
        function_id, event, timestamp = int(log_parts[0]), log_parts[1], int(log_parts[2])
    
        if event == "start":
            if stack:
                exclusive_times[stack[-1]] += timestamp - prev_timestamp
            stack.append(function_id)
            prev_timestamp = timestamp
            
        else:
            if stack:
                popped_function = stack.pop()
                exclusive_times[popped_function] += timestamp - prev_timestamp + 1
            prev_timestamp = timestamp + 1
    return exclusive_times
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = getTotalExecutionTime(n, logs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()