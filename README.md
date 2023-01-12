# trading-algorithm
    >>> find_trading([[1, 2, 3], [2, 0, 1], [0, 1, 2]])
    | 0 gets 1 | 1 gets 2 | 2 gets 0 | 
    >>> find_trading([[0, 2, 1], [0, 2, 1], [1, 0, 2]])
    | 0 gets 0 | 1 gets 2 | 2 gets 1 | 
    >>> find_trading([[1, 3, 2, 0], [2, 0, 3, 1], [1, 3, 2, 0], [0, 2, 1, 3]])
    | 1 gets 2 | 2 gets 1 | 0 gets 3 | 3 gets 0 | 
    >>> find_trading([[1, 4, 3, 2, 5, 0], [4, 1, 3, 2, 5, 0],[1, 4, 5, 2, 3, 0],[1, 4, 3, 2, 5, 0],[0, 4, 3, 2, 5, 1],[1, 4, 3, 2, 5, 0]])
    | 0 gets 1 | 1 gets 4 | 4 gets 0 | 3 gets 3 | 2 gets 5 | 5 gets 2 | 
    >>> find_trading([[1, 0], [0, 1]])
    | 0 gets 1 | 1 gets 0 | 