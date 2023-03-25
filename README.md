# Distributed-systems-project

## Quick startup 
Run three python progams:

    python node.py --node_id=1
    python node.py --node_id=2
    python node.py --node_id=3


Available commands

| command |              parameters               |                description                | availability |
| :---:   |:-------------------------------------:|:-----------------------------------------:|:------------:|
| Check-connections |                   -                   |   Check connection with all other nodes   |     all      |
| Start-game |                   -                   |              Starts the game              |    leader    |
| Elect-leader |                   -                   |   Performs time sync and elects leader    |     all      |
| List-board |                   -                   |         Shows current game state          |   players    |
| Set-symbol  |           loc(1-9) sym(X/O)           |   Places symbol on the tictactoe board    |   players    
| Set-node-time |     target(id) &  time(hh:mm:ss)      | Sets target node local time to given time |     all*     |
| Set-time-out | target(game-master/player) & duration |    Sets local timeout for target class    |     all      
| Enforce-time-out |                   -                   |   Enforces time-out of nodes/gamemaster   |     all      |


