You re-run the experiment from Figure 8 in the LFS paper on two NFS file systems – one that runs on top of LFS and the other running on top of FFS (sunos). Roughly speaking, what do you expect to happen to the relative difference between the two?

The task is about 10000 1K file create and access.

We should expect that the relative difference between the two will be smaller than the original one.

LFS is good at writing large files sequentially, which will not work in this task because the file size is small.
Also, the NFS system will break large writes into smaller ones to write to disk before replying.
For these writes, LFS might collapse and only operation one file at a time (and the file is 1 KB).

However, LFS might still perform better, because FFS may require more synchorization and disk seek.