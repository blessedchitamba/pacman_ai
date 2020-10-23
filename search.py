# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack() #stack to keep all the states in the tree
    visitedStates = []  #list to keep all visited states
    actionsList = []
    startState = problem.getStartState()
    # stack.push(startState)
    current = [startState, "", ""]
    stack.push((startState, actionsList))

    while not stack.isEmpty():
        current, actions = stack.pop()
        unvisitedSucc = False
        if not problem.isGoalState(current):    #if the state is not the goal state
            if current not in visitedStates:     #if the node is not visited
                successors = problem.getSuccessors(current)    #get the successors
                visitedStates.append(current)
                for succ in successors:
                    nextAction = actions+[succ[1]]
                    #actions.append(succ[1])
                    stack.push((succ[0], nextAction))
        else:
            return actions
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue() #stack to keep all the states in the tree
    visitedStates = []  #list to keep all visited states
    actionsList = []
    startState = problem.getStartState()
    # stack.push(startState)
    current = [startState, "", ""]
    queue.push((startState, actionsList))

    while not queue.isEmpty():
        current, actions = queue.pop()
        unvisitedSucc = False
        if not problem.isGoalState(current):    #if the state is not the goal state
            if current not in visitedStates:     #if the node is not visited
                successors = problem.getSuccessors(current)    #get the successors
                visitedStates.append(current)
                for succ in successors:
                    nextAction = actions+[succ[1]]
                    #actions.append(succ[1])
                    queue.push((succ[0], nextAction))
        else:
            return actions
    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue() #stack to keep all the states in the tree
    visitedStates = []  #list to keep all visited states
    actionsList = []
    startState = problem.getStartState()
    # stack.push(startState)
    current = [startState, "", ""]
    pqueue.update((startState, actionsList, 0), 0)  #start state has a cost of 0
    cost_thus_far = 0

    while not pqueue.isEmpty():
        current, actions, cost_thus_far = pqueue.pop()
        unvisitedSucc = False
        if not problem.isGoalState(current):    #if the state is not the goal state
            if current not in visitedStates:     #if the node is not visited
                successors = problem.getSuccessors(current)    #get the successors
                visitedStates.append(current)
                for succ in successors:
                    nextAction = actions+[succ[1]]
                    #actions.append(succ[1])
                    pqueue.update((succ[0], nextAction, cost_thus_far+succ[2]), cost_thus_far+succ[2])
        else:
            return actions
    return []
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from searchAgents import manhattanHeuristic

    pqueue = util.PriorityQueue() #stack to keep all the states in the tree
    visitedStates = []  #list to keep all visited states
    actionsList = []
    startState = problem.getStartState()
    current = [startState, "", ""]
    heuristic_cost = 0+heuristic(startState, problem)
    pqueue.update((startState, actionsList, heuristic_cost), heuristic_cost)  #start state has a cost of 0
    cost_thus_far = 0

    while not pqueue.isEmpty():
        current, actions, cost_thus_far = pqueue.pop()
        unvisitedSucc = False
        if not problem.isGoalState(current):    #if the state is not the goal state
            if current not in visitedStates:     #if the node is not visited
                successors = problem.getSuccessors(current)    #get the successors
                visitedStates.append(current)
                for succ in successors:
                    nextAction = actions+[succ[1]]
                    #actions.append(succ[1])
                    heuristic_cost = problem.getCostOfActions(nextAction)+heuristic(succ[0], problem)
                    pqueue.update((succ[0], nextAction, heuristic_cost), heuristic_cost)
        else:
            return actions
    return []
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
