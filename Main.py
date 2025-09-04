'''
Sliding window for processing the tasks
pso
totalTime compute
'''
import random

class Task:
    def __init__(self, id: int, timeToFinish: float):
        self.id = id
        self.timeToFinish = timeToFinish

if __name__ == '__main__':
    # Initializing Task List
    taskList = []

    # Asking for amount of tasks to use
    numberOfTasks = int(input("Enter the number of tasks: "))
    # Asking for amount of cores available to use
    numberOfCores = int(input("Enter the number of cores: "))

    # Adding tasks to taskList
    for i in range(numberOfTasks):
        # random.random() generates a number within [0,1] interval, we multiply by 10 to make the difference greater
        task = Task(id=i + 1, timeToFinish=random.random() * 10)
        taskList.append(task)

    # Sliding window implementation