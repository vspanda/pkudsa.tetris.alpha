# Team ALPHA for pkudsa.tetris 2022

Start Date: 2022.5.22

## References

Alpha Heuristics:
https://blog.csdn.net/qq_41882147/article/details/80005763
https://imake.ninja/el-tetris-an-improvement-on-pierre-dellacheries-algorithm/

Delta and Omega Heuristics:
https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/

Board/Game Data
https://github.com/pkulab409/pkudsa.tetris


## Heuristics Used

- Lines Deleted
- Holes Created
- Aggregate Height
- Bumpiness
- Whether Enemy can get a line next turn (should this be in the next node?)

Scoring Thoughts:
Stopping Enemy from Scoring > Points Won > Holes Created > Bumpiness > Aggregate Height

## DFS: MinMax Algorithm or Alpha Beta algorithm

Using A Tree to go through and score options, then going to the next layer and so on.

Each Node has to calculate:
- Possible Lines
- Possible New Holes
- New Aggregate Height
- New Bumpiness
- Whether doing this move leads directly to enemy getting a line
