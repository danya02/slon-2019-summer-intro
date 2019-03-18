# TL;DR: [this program](./main.py), also [this](./outp.svg)

AKA "Offset Trouble"

The most challenging thing here was determining the width of the entire tree -- this is needed to fit the tree into the canvas, because without the top-layer border the root node gets truncated in the top-left corner.
I ended up doing a hack-around with multiplying whatever value I got from the recursive tree building algorithm by some constant, picked so the trees I tested had a not-too-large gap to the right edge of the canvas.
That's probably going to fail for different trees, but when it does, the human using the program may fix it themselves -- that is facilitated by the width parameter being in front of the output file.
