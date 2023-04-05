# Eraser (reading question)
# Please submit your response on Gradescope by Wednesday, April 5, 2023, 3pm PST.
# Eraser only ensures that data is protected by a consistent set of locks. Give:
# 1. An intuitive sketch of a class of race conditions it will miss,
# 2. An example of a race condition in that class, and
# 3. An explanation of how Eraser could be extended to catch such race conditions.

# ### 1. An intuitive sketch

# Eraser may miss write-read or read-write races because it focuses on checking shared memory access with its Lockset algorithm, so it is insensitive in thread scheduling.

# ### 2. An example

# There are no locks in this case. So we will always get an empty set after each read or write.
# We assume that a is already allocated by some other thread.

# | Thread 1 | Thread 2 | 
# |    ...   | a = ...  | 
# |  ... = a |   ...    | 

# Suppose Thread 2 access a first, Eraser will be in shared-modified state after Thread 2 accesses a and before Thread 1 accesses a.
# In which C(v) is updated and data race is reported.

# | Thread 1 | Thread 2 | 
# |  ... = a |   ...    | 
# |    ...   | a = ...  | 

# In this case, Thread 1 accesses a before Thread 2.
# Eraser will be in shared state after Thread 1 accesses a and before Thread 2 accesses a.
# Thus, C(v) will be updated to an empty set, but data race is not reported.
# Then Thread 2 writes a, and changes the state to shared-modified state.
# Since variable a enters shared-modified state with an empty C(v), which means that the error should be reported in the previous state. 
# Thus, Eraser misses this race.

# ### 3. An explanation of how Eraser could be extended

# If variable a enters shared-modified state with an empty C(v), this is a potential race, we should check .

# report 


Eraser (reading question)
Please submit your response on Gradescope by Wednesday, April 5, 2023, 3pm PST.
Eraser only ensures that data is protected by a consistent set of locks. Give:
1. An intuitive sketch of a class of race conditions it will miss,
2. An example of a race condition in that class, and
3. An explanation of how Eraser could be extended to catch such race conditions.

### 1. An intuitive sketch

Eraser may miss write-read or read-write races because it focuses on checking shared memory access with its Lockset algorithm, so it is insensitive in thread scheduling.

### 2. An example

There are no locks in this case. So we will always get an empty set after each read or write.

| Thread 1 | Thread 2 | 
|    ...   | a = ...  | 
|  ... = a |   ...    | 

Suppose Thread 2 access a first, Eraser will be in exclusive state after Thread 2 accesses a and before Thread 1 accesses a.
Then will be in shared state after Thread 1 reads a, so no data race is reported.

| Thread 1 | Thread 2 | 
|  ... = a |   ...    | 
|    ...   | a = ...  | 

In this case, Thread 1 accesses a before Thread 2.
Eraser will be in virgin state after Thread 1 accesses a and before Thread 2 accesses a.
Then Thread 2 writes a and changes the state to exclusive state.
Because we only report in shared-modified state, no data race is reported here either.

Thus, Eraser misses this race.

### 3. An explanation of how Eraser could be extended
We should add an initializing state. Then we could know that the race condition happens when initializing.

We should follow this Figure on page 5 (https://dl.acm.org/doi/pdf/10.1145/781498.781529).

In condition 1, it goes to shared state with an empty C(v), then a race warning is issued.
But in condition 2, it goes to initializing state and C(v) is empty, so a race warning is reported.

Because multi-read single-write is handled with these status transition rules, a race warning is reported whenever C(v) is empty, so it is also reported in shared state.
