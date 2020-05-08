#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trips = dict()
    route = list()

    for something in tickets:
        trips[something.source] = something.destination

    index = 0

    current_dest = "NONE"

    while index < length:
        current_dest = trips.get(current_dest)
        route.append(current_dest)
        index += 1



    return route