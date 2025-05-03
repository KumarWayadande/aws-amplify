# Function to perform job scheduling
def job_scheduling(jobs, n):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Array to keep track of free time slots
    # Initially, all slots are empty (False)
    slots = [False] * n

    # Result array to store the jobs that are selected
    result = [None] * n

    # Variable to store total profit
    total_profit = 0

    # Iterate through all jobs
    for job in jobs:
        # Find a free slot for this job (starting from its deadline)
        for j in range(min(n, job[1]) - 1, -1, -1):
            if not slots[j]:
                # Slot is free, schedule this job
                slots[j] = True
                result[j] = job[0]  # Job ID
                total_profit += job[2]  # Add profit
                break

    return result, total_profit

# Example usage:
# Job format: (Job ID, Deadline, Profit)
jobs = [
    ('J1', 4, 20),
    ('J2', 1, 10),
    ('J3', 1, 40),
    ('J4', 1, 30),
    ('J5', 3, 50),
]

n = len(jobs)

# Call the job scheduling function
scheduled_jobs, total_profit = job_scheduling(jobs, n)

# Print the results
print("Jobs scheduled:", scheduled_jobs)
print("Total profit:", total_profit)
