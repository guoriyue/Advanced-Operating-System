### Explain from the Mesa paper: “… while any procedure suitable for forking can also be called sequentially, the converse is not generally true.”

The converse is that any sequentially called procedure is also suitable for forking.
Actually, not every sequentially called procedure is suitable for forking, because when forking, one parent process creates a child process which runs the same program.
Sequentially called procedures may run different programs so they are not generally suitable for forking.

### Consider the memory allocation code in the Mesa paper.

### The paper states this code has a bug. What is it and what is the fix?

It is possible that a process is waiting even though there is now enough free memory available to satisfy its request.
If there are multiple processes waiting on this condition, only one of them will be woken up and allocate the newly available block of memory.
The fix is replace NOTIFY with BROADCAST.
This will wake up all processes waiting on the moreAvailable condition, giving all of them the chance to acquire the monitor lock and allocate memory from the newly available block.

### Intuitively, how would you change this code to work with Hoare wakeup semantics?

The while loop checks help processes to continue wait if they fail to acquire the monitor lock when BROADCAST.
If we want to change this code to work with Hoare wakeup semantics, we still need a loop to make sure that the process continues to wait if it fails to acquire the monitor lock.
So that we can add a while loop outside of the wakeup statement to make sure that the process continues to wait if it fails to acquire the monitor lock.

### What happens if we make EXPAND an ENTRY routine?

Now EXPAND is a PUBLIC procedure, it doesn't require do not require a lock on the monitor to execute and doesn't modify shared variables.
If we make it a ENTRY routine, it will require a lock on the monitor to execute.
Thus, it can potentially cause a deadlock.
Because we already acquired the monitor lock in EXPAND, and in ALLOCATE, we also need to acquire the monitor lock, since the lock is already acquired, we will get a deadlock.

### What happens if we make the WAIT call just put the current thread at the end of the run queue?

This doesn't make sense because the thread in the run queue should be the one that is ready to run, not the one that is waiting for a condition to be true.
Thus, the thread will not wait for the condition to be true and the WAIT call will not work.

### Give the main monitor invariant for this code.

Mutual Exclusion. At most one process can execute Allocation or Free at any time.