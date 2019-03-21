# TL;DR: 10 actions; computed by [this](./main.py)

AKA "Bruteforce FTW!"

This is the sort of task that would be more efficient had I used dynamic programming, but since this is submitted from school, from a slightly-broken computer, via a flaky SSH connection, while I'm being told to "just f***ing do your job already!", I decided that it's too much trouble, so here we have a bruteforce solution using bitmasks.

Also, there is ambiguity as to whether the SLON(tm) is considered to have "reached" a value if it is exactly at that value (like I assumed here), or if it is OK for it to have passed the target mark during an action (e.g. if the SLON(tm) is at 38 and it goes forward 7 units, it ends up at 45, but realistically it would have spent some time at 40). In effect, the question is whether the SLON(tm) has a teleportation engine, or does it just walk.
