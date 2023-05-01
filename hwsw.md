####Consider the isPrime code in Section 3.2.

####After translation, does isPrime run as unprivileged code or as privileged code?
Before translation, isPrime runs as unprivileged code. After translation, isPrime runs as unprivileged code.
Since the binary translator translates faithfully, it shouldn't change the privilege state of the code.

####Give concrete inputs to eliminate the jumps to takenAddr and fallthrAddr3.
As long as input is greater than 2, jge will not be taken and the code will not jump to takenAddr.
If at the end of the loop, the code fail to jump nexti, it will jump to fallthrAddr3, which indicates that the number is a prime.
So if we want to eliminate the jumps to fallthrAddr3, we need to find a number that is not a prime.
The inputs should be any number greater than 2 and is not a prime, e.g. 4, 6, 8, etc.