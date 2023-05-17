#### As always, be sure to explain your answers:

#### Segment S contains a live inode 5 that points to data block 10. Is 10 live?
Since Sprite LFS uses segment summary information to distinguish live blocks and dead blocks,
we need to discuss this question in two cases:
    1. They are in the same segment. So we can use the knowledge of segment summary block. Since the inode is live and it is pointing to the data block 10, 10 is live.
    2. They are in different segments. We can't know if 10 is live or not. Without block allocation maps or block usage information, we can't know if 10 is live or not.

#### Segment S contains a dead inode 5 that points to data block 10. Is 10 dead?
For a dead inode, it is no longer associated with a valid file or directory entry in the file system.
we need to discuss this question in three cases:
    1. No other inode is pointing to data block 10. 10 is dead.
    2. Some other live inode is pointing to data block 10, and they are in the same segment. 10 is live.
    3. Some other live inode is pointing to data block 10, and they are in different segments. We can't know if 10 is live or not. 