from tabulate import tabulate

# Define a process class to hold information about each process
class Process:
    def __init__(self, name, priority, burst_time):
        self.name = name
        self.priority = priority
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1

# Define a function to simulate the CPU scheduler
def priority_scheduling(process_list):
    # Sort the process list by priority
    process_list.sort(key=lambda x: x.priority)
    
    # Initialize the current time, total waiting time, total turnaround time, and total response time
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    
    # Create the Gantt chart
    gantt_chart = []
    
    # Loop through the process list and simulate the CPU scheduler
    for process in process_list:
        # Add the process name to the Gantt chart
        gantt_chart.append([process.name, current_time])
        
        # Calculate the response time
        if process.response_time == -1:
            process.response_time = current_time
        
        # Run the process
        current_time += process.burst_time
        waiting_time = current_time - process.burst_time
        process.waiting_time = waiting_time
        total_waiting_time += waiting_time
        
        # Add the process duration to the Gantt chart
        gantt_chart[-1].append(current_time)
        
        # Calculate the turnaround time
        turnaround_time = current_time
        process.turnaround_time = turnaround_time
        total_turnaround_time += turnaround_time
        
        # Calculate the response time
        total_response_time += process.response_time
    
    # Calculate the average waiting time, turnaround time, and response time
    avg_waiting_time = total_waiting_time / len(process_list)
    avg_turnaround_time = total_turnaround_time / len(process_list)
    avg_response_time = total_response_time / len(process_list)
    
    # Create a list of lists containing the process metrics
    process_metrics = []
    for process in process_list:
        process_metrics.append([process.name, process.priority, process.burst_time, process.waiting_time, process.turnaround_time - process.response_time, process.response_time])
    
    # Print the table and Gantt chart
    print("Process metrics:")
    print(tabulate(process_metrics, headers=["Process name", "Priority", "Burst time", "Waiting time", "Response time", "Turnaround time"]))
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)
    print("Average response time:", avg_response_time)
    print("Gantt chart:")
    print(tabulate(gantt_chart, headers=["Process name", "Start time", "End time"]))

# Example usage:
process_list = [
    Process("P1", 2, 5),
    Process("P2", 1, 3),
    Process("P3", 4, 8),
    Process("P4", 3, 4),
]

priority_scheduling(process_list)

