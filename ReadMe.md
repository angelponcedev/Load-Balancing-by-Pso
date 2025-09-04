# Load Balancing by Particle Swarm Optimization

##### This project aims to optimize the shared workload between processors in a machine, the objective is to minimize the total time needed to process any given workload by using all cores to the maximum capacity available at any moment.

### Code Flow
    - Taking number of tasks to process and number of available cores from the user
    - Defining a Sliding window to iterate through all of the tasks
    - Using PSO to find the combination of distributed tasks through cores that minimizes total time spent to finish
