import time
import logging
import copy

logging.basicConfig(level=logging.INFO)
def find_trading_cycle(preferences: list[list[int]]) -> list[int]:
    """
    preferences[i] is the i'th agent. The list in preferences[i] is the agent's list of wanted items. (sorted)
    usage examples:
    >>> find_trading_cycle([[0, 2, 1], [0, 2, 1], [1, 0, 2]])
    [0, 0]
    >>> find_trading_cycle([[1, 3, 2, 3], [0, 2, 3, 1], [1, 0, 3, 2], [3, 2, 1, 0]])
    [0, 1, 0]
    >>> # Notice for the next two examples how the circle enlarges due to agent 2 wanting 0's item
    >>> find_trading_cycle([[1, 3, 2, 3], [3, 2, 0, 1], [1, 0, 3, 2], [2, 3, 0, 1]])
    [1, 3, 2, 1]
    >>> find_trading_cycle([[1, 3, 2, 3], [3, 2, 0, 1], [0, 1, 3, 2], [2, 3, 0, 1]])
    [0, 1, 3, 2, 0]
    """
    logging.info("finding cycle in %s", str(preferences))
    active_agents = sum(map(lambda lst : len(lst) != 0, preferences)) # get how many "active" agents are involved
    if active_agents == 0: 
        return []
    longest_circle = active_agents+1 # Kn,n bipartite clique graph longest circle is 2*nodes+1 (for us each agent is 2 nodes)
    for i in range(len(preferences)): 
        if len(preferences[i]) == 0: # if the agent is not involved, continue
            continue
        cycle = []
        cycle.append(i)

        agent = preferences[i][0]
        while True: # while the circle is not closed (or len(cycle) > longest_circle)
            logging.info("source: %d agent: %d | cycle: %s", i, agent, str(cycle))
            if logging.root.level == logging.INFO:
                time.sleep(0.5)
                
            cycle.append(agent) # add current agent to cycle
            agent = preferences[agent][0] # agent is now the agent's most wanted item

            if len(cycle) > longest_circle or agent == i: # emulates do while
                break
        if len(cycle) > longest_circle:
            logging.info("continue to next agent start from %d", i)
            continue

        logging.info("source: %d agent: %d | cycle: %s", i, agent, str(cycle))
        if cycle[-1] != agent:
            cycle.append(agent)
            logging.info("source: %d agent: %d | cycle: %s", i, agent, str(cycle))
        return cycle
    logging.error("can't find trading cycle")

def find_trading(preferences: list[list[int]]):
    """
    Gets preferencces and prints to the screen the trade
    input: a list of lists, each inner list presents an agent with preferences
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
    """
    flag = True
    print("| ", end="")
    while flag:
        flag = any([len(lst) != 0 for lst in preferences]) # if atleast one of the agents still exists, continue (flag = True)
        current_trade = find_trading_cycle(preferences) # Gets current cycle from list of agents
        for i in range(len(current_trade)-1): # for each pair of agents in the cycle
            print(current_trade[i], "gets", current_trade[i+1], end=" | ") 
            preferences[current_trade[i]] = [] # delete each agent involved in the trade
        for agent in preferences: # for each agent remove items there were involved in the trade
            currentAgent = copy.deepcopy(agent)
            for index in currentAgent: 
                if index in current_trade: 
                    agent.remove(index)
    print()

if __name__ == "__main__":
    import doctest
    doctest.testmod()