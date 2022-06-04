def depth_first_search_graph(node, visited, goal) :
    if node is None :
        return False

    if node.val == goal :
        return True

    for neighbor in node.neighbors :
        if visited.contains(neighbor):
            continue
        visited.add(neighbor)

        is_found = depth_first_search_graph(neighbor, visited, goal)

        if is_found :
            return True

    return False

