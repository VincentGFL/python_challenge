def route_planner(peak):
    peak_list = peak.split(" ")
    route = []
    for peak in peak_list:
        if len(route) == 0:
            route.append(peak)
        elif int(peak) > int(route[len(route) - 1]):
            #print(peak)
            route.append(peak)
    return route

print(route_planner("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"))