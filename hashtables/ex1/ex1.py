def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    
    weights_dict = dict()

    for something in range(length):
        x = weights_dict.get(limit - weights[something])
        if x != None:
            return(something,x)
        else:
            weights_dict[weights[something]] = something
    
    print(weights_dict)

    return None