OOP,  Unit Testing Practice

# dragonball game

## to run
1. python main.py

## game progression
1. start game; 2 players, infinite rounds, 1 winner
1. both players start with 3 lives and 0 charges
1. every round, players decide to either: BLOCK, CHARGE, FIRE, or KAMEHAMEHA
1. player 1 chooses an action, then player 2 chooses; player 1's action is hidden during player 2's turn
1. round result of both player's lives and charges are revealed
1. rounds repeat until one player reaches 0 lives; other player wins game

## game action rules and descriptions
* using BLOCK does not affect charges or lives
* using CHARGE adds 1 charge for player; players can save infinite charges
* using FIRE negates 1 charge for player; FIRE requires 1 charge
* using KAMEHAMEHA negates 3 charges for player; KAMEHAMEHA requires 3 charges
* receiving FIRE when using CHARGE negates 1 life
* receiving FIRE when using BLOCK does not affect lives
* receiving FIRE when using FIRE does not affect lives
* receiving KAMEHAMEHA when CHARGE negates 3 lives
* receiving KAMEHAMEHA when FIRE negates 2 lives
* receiving KAMEHAMEHA when BLOCK negates 1 life
* receiving KAMEHAMEHA when KAMEHAMEHA does not affect lives
* none of the receiving actions affect saved charges