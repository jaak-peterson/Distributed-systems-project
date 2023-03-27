# Distributed-systems-project

## Quick startup 
Run three or five python progams:

    python node.py --node_id=1 --nr_nodes=3
    python node.py --node_id=2 --nr_nodes=3
    python node.py --node_id=3 --nr_nodes=3

    python node.py --node_id=1 --nr_nodes=5
    python node.py --node_id=2 --nr_nodes=5
    python node.py --node_id=3 --nr_nodes=5
    python node.py --node_id=4 --nr_nodes=5
    python node.py --node_id=5 --nr_nodes=5



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
| Join-game |                   port                  |   Requests to join the game and sends it's port to master   |     players      |


