# Documentation
# Input = list of starting times (Start[]) and ending times (end[]) for the tasks
# example input:    start[] = (12, 10, 20)
#                   end[] = {25, 20, 30}

# Output: Number of non-conflicted tasks:  n
#         List of non-conflicting tasks:  []
# example of output: Number non-conflicting tasks:  2
#                    List of non-conflicting tasks:  [(10, 20), (20, 30)]

# Functions: task_selection ---> prints only the tasks that do not collide w
# ith each other’s start and end time and max number of such tasks
# scripted by: Sajib Ryhan Sunny




def task_selection(start, end):
    # build a tuple of tasks containing their start time and end time
    # (eg: [(x, y), (x, y) ..] where for each task (x, y) -> x = start, y = end)
    tasks = []
    for i in range(len(start)):
        tasks.append((start[i], end[i]))
    print("The Tasks: ", tasks)

    # Sort the tasks in ascending order by their end time
    tasks.sort(key=lambda x: x[1])
    print("Tasks sorted: ", tasks)

    selected_task = []
    counter = 0

    # Keep a track of the current time as we pass each task
    current_time = 0  # starting from 0

    for current_task in tasks:
        # Pick the activity whose start time is on or after current time
        if current_task[0] >= current_time:  # for each task (x, y), index 0 = start, index 1 = end,
            # start time of current task >= end time of previous task
            selected_task.append(current_task)
            counter += 1

            # Update the current time to the end time of the current task
            current_time = current_task[1]
    print("\nNumber non-conflicting tasks: ", counter)
    print("List of non-conflicting tasks: ", selected_task)


# TESTING FUNCTION INPUTS
start = (4, 3, 0, 1, 8, 5)
end = (7, 4, 6, 2, 9, 9)
task_selection(start, end)

# END
