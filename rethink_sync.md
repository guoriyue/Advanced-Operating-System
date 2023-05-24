####Suppose we disable the drive’s write cache. How does Figure 3 change? Be sure to explain your reasoning.

| File system configuration      | Data durable on write | Data durable on fsync  |
| ----------- | ----------- | ----------- |
| Asynchronous      | No       |      Not on power failure       |
| Synchronous   | Yes        |        Yes     |
| Synchronous with write barriers   | Yes        |        Yes     |
| External synchrony   | Yes        |        Yes     |

For Asynchronous, it still doesn't provide data durability guarantee on write because the data is not durably stored on the disk
when a power failure happens, and the application may have already generates some outputs.
With the use of fsync, it still doesn't provide data durability guarantee even if the fsync now syncs
to the disk instead of the cache when power failure, because the application may have already generates some outputs
and the power failure may happen before the fsync operation completes.

For Synchronous, it provides data durability guarantee on both write and fsync because the application will not produce any
output before the data is stored. Since there is no write cache, the data is durably stored on the disk directly.
As soon as the call finishes, the data is already stored on the disk, and then the application can use the stored data.
When there is a power failure, the data is not stored on the disk, the application will not produce any output, and the
durability guarantee is satisfied.

For Synchronous with write barriers and External synchrony, they already guarantee data durability on both write and fsync
in any cases, so without write cache (which actually increases the potential synchronization difficulty for write and fsync), 
they should still guarantee data durability.
Moreover, since they use barriers or journaling, which indeed help to take care of the issue that data doesn't stay in the disk buffer cache.
So without cache, in the worst case, they should still be better than the Synchronous case, which guarantees data durability.