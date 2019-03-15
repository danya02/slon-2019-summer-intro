#TL;DR: `$\frac{1}{x+1} - 1$`

AKA "Rate limiting"

I'm guessing this was done because last time I spammed the server with too many requests -- sorry for that, BTW.
The fact that the blackbox is a simple equation means that that approach is actually unneccessary.

First, I tried looking at some integers near 0, and I noticed that at -1, the blackbox returns an error.
That's promising, so I then tried some real values very close to -1, and when they were closer to 0, the output is very positive, and when the input is just slightly farther from 0, the output is very negative.
This implies that this is a [hyperbolic curve](https://en.wikipedia.org/wiki/Hyperbola) of some sort, a hypothesis that is confirmed by the fact that at high input values, the output approaches -1 from above, and at very negative inputs the output approaches -1 from below.

So the center of mass for the curve as a whole is at (-1; -1).
And by varying the constants in the base hyperbola equation, `$y=\frac{1}{x}$`, in a [graphing calculator](https://www.geogebra.org/graphing), I got a curve that fits all the data from the blackbox: `$\frac{1}{x+1} - 1$`.
