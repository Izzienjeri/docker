def getInaccurateProcesses(processOrder: list[int], executionOrder: list[int]) -> int:
    """
    Counts the number of elements in `executionOrder` that do not maintain their relative order as present in `processOrder`.
    Args:
        processOrder: A list of integers representing the intended process order.
        executionOrder: A list of integers representing the actual execution order.
    Returns:
        An integer representing the number of elements executed out of order.
    """
    # Create a mapping of process ID to its position in processOrder
    process_positions = {pid: i for i, pid in enumerate(processOrder)}
    out_of_order = set()
    n = len(executionOrder)
    # Compare each pair of processes in executionOrder
    for i in range(n):
        for j in range(i + 1, n):
            # Get the positions of these processes in the original order
            pos_i = process_positions[executionOrder[i]]
            pos_j = process_positions[executionOrder[j]]
            # If their relative order is different, both processes are out of order
            if pos_i > pos_j:
                out_of_order.add(executionOrder[i])
                out_of_order.add(executionOrder[j])
    return len(out_of_order)