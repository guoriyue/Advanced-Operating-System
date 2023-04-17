#### State what the point of section 5.1 is. Then state in what way Figure 3 undercuts the entire point of Section 5.1.
Section 5.1 shows all kinds of synchonization approaches, including mutex, spinlock, and update synchronization (e.g. volatile, cmpxchg), are more expensive than the non-synchronized version.

However, Figure 3 shows that the update version is faster than the non-synchronized version, which undercuts the point of Section 5.1.
I think this is just a specific case on a specific hardware.
Generally, synchronized version is more expensive than the non-synchronized version.

#### As suggested in class, you define the semantics of a volatile variable v as giving two guarantees: (i) no additional loads or stores can be done to v other than what appear in the program text, and (ii) an access to v cannot be reordered with any other volatile access or lock call. Which problems (if any) in Section 4 would this fix?
I think it would fix the concurrent modification problem and the rewriting of adjacent data problem. 
Because the volatile variable can cannot be reordered, so it ensures that all modifications to v are serialized and atomic, and there is no concurrent modification.
Also, the load and stores of v are load and stores that appear in the program text, the compiler cannot compile into some other adjacent fields, so it ensures that there is no concurrency problem of adjacent data.

#### You see the following code below, Eraser said this “double-check lock” idiom is tricky because of memory consistency. Assume the hardware is sequentially consistent and Boehm fixed the compiler to not be stupid about locks (describe your interpretation of what this means). Does this code break? Why or why not?

```c
if (!p) {
    lock();
    if (!p) {
        struct foo *t = foo_new();
        t->bar = bar_new();
        p = t;
    }
    unlock();
}
```

When multiple threads attempt to access p, a thread may observe that p is uninitialized and proceed to acquire the lock, while another thread may observe that p is initialized and skip the lock acquisition.
This can result in one thread initializing p while another thread proceeds to use an uninitialized version of p.

Here, being stupid about locks means that the compiler does not set appropriate memory barriers, and may reorder memory operations across the lock boundary.
Because lock is implemented as a library, which is not visible to the compiler, so the compiler cannot know that the lock is a synchronization point, and it cannot insert the appropriate memory barriers.

If Boehm fixed the compiler to not be stupid about locks, the compiler will insert appropriate memory barriers before the lock.
So if p is uninitialized, all threads will wait before the lock, then one thread successfully acquires the lock and initializes p.
Then, this thread will wait before the unlock.
All other threads will acquire the lock and see that p is initialized, and skip the lock.
Finally, all threads come to the memory barrier before the unlock, and finish the critical section.
Therefore, the code will not break.