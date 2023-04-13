
processes = [("p1", 0, 4, 2), ("p2", 1, 3, 3), ("p3", 2, 1, 4), ("p4", 3, 5, 5), ("p5", 4, 2, 5)]
processes.sort(key=lambda x: x[1])

n = len(processes)
ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n
S_T = [-1] * n

remaining_bt = [processes[i][2] for i in range(n)]
priorities = [processes[i][3] for i in range(n)]
C_T = 0
C = []

while len(C) < n:
    H_P = -1
    LBT = float('inf')
    select = -1
    for i in range(n):
        if remaining_bt[i] > 0 and processes[i][1] <= C_T:
            if priorities[i] > H_P:
                H_P = priorities[i]
                select = i
            elif priorities[i] == H_P and remaining_bt[i] < LBT:
                LBT = remaining_bt[i]
                select = i

    if select == -1:
        C_T += 1
    else:
        if S_T[select] == -1:
            S_T[select] = C_T
        remaining_bt[select] -= 1
        C_T += 1
        if remaining_bt[select] == 0:
            ct[select] = C_T
            C.append(processes[select])
        else:
            # update priority of the selected process
            priorities[select] += 1

# calculate the turnaround times and waiting times
for i in range(n):
    tat[i] = ct[i] - processes[i][1]
    wt[i] = tat[i] - processes[i][2]
    rt[i] = S_T[i] - processes[i][1]

# print the results
print("Process\tAT\tBT\tPriority\tCT\tTAT\tWT\tRT")
T_tat = 0
T_WT = 0
T_RT = 0
for i in range(n):
    print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{processes[i][3]}\t\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}")
    T_tat += tat[i]
    T_WT += wt[i]
    T_RT += rt[i]

avg_tat = T_tat / n
avg_wt = T_WT / n
avg_rt = T_RT / n
print(f"\nAvg turnaround time: {avg_tat:.2f}")
print(f"Avg waiting time: {avg_wt:.2f}")
print(f"Avg response time: {avg_rt:.2f}")
