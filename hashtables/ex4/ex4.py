def has_negatives(a):

    """
    YOUR CODE HERE
    """

    num = dict()
    results = list()

    for something in a:
        if num.get(abs(something)):
            if(num.get(abs(something)) + something) == 0:
                results.append(abs(something))
        else:
            num[abs(something)] = something

    return results


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
