# Pseudocode

tbc.py

Import random

Define class Character with attributes for name, hit points, hit chance, maximum damage, and armour

Initializing Character:<br/>
    Set the character’s name, hit points, hit chance, max damage, and armor, with default values<br/>
    Ensure hit chance stays within a 0-100 range.<br/>
    Ensure max damage is at least 1.<br/>
    Ensure armor is at least 0.<br/>

Define properties for each attribute

Define hitValues to check if values are within a specified range

Define printStats to display character name and stats

Define hit to determine if a hit lands based on hit chance<br/>
If the hit lands:<br/>
        Calculate random damage up to the character’s max<br/>
        Reduce damage by opponent’s armor, with a minimum of 0<br/>
        Subtract damage from the opponent’s hit points<br/>
        Print damage dealt and armor absorption<br/>
If the hit misses print a miss message<br/>

Define fight as a combat loop between two characters<br/>
    Loop while both characters have hit points above 0<br/>
    Character 1 attacks Character 2<br/>
    Print current HP for both<br/>
    If Character 2’s hit points are 0 or below set Character 1 as the winner and exit<br/>
    Prompt user to start Character 2’s turn<br/>
    Character 2 attacks Character 1<br/>
    Print current HP for both<br/>
    If Character 1’s hit points are 0 or below set Character 2 as the winner and exit<br/>
    Prompt user to start Character 1’s turn again<br/>


    
combat.py

Import tbc

Define main function to set up combat:<br/>
    Create a character with name Hero with hit points 10, hit chance 50, max damage 5, and armor 2<br/>
    Create a character with name Monster with hit points 20, hit chance 30, max damage 5, and armor 0<br/>

Display stats for both characters by calling printStats for hero and monster

Print a message for start of combat

Call fight function with hero and monster to initiate combat until one is defeated

Call main
