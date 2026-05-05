## Non-Functional Requirements (Added in Phase 4)

The following non-functional requirements were identified during testing and defect analysis in Phase 4. These address performance, usability, reliability, and consistency concerns that were not explicitly defined in earlier phases.

Since our original requirements document did not discuss *any* non-functional requirements, we consider this part of the updates/revisions made as part of the bonus section for the assignment. 

### Performance
[1.1] The system shall process and validate a move (including spell logic) within 1000 milliseconds under normal gameplay conditions.

[1.2] The system shall update all display elements (board, status text, spell labels) immediately after each move or spell action.

[1.3] The system shall support continuous gameplay without noticeable lag for at least 100 consecutive moves.

[1.4] The system shall initialize a new game state within 500 milliseconds.

### Reliability
[2.1] The system shall maintain a consistent and valid board state after every move, spell cast, and game reset.

[2.2] The system shall ensure that all state transitions (turn switching, cooldown updates, spell effects) occur exactly once per action.

[2.3] The system shall not enter an invalid or undefined state due to repeated actions, invalid inputs, or partial updates.

[2.4] The system shall preserve game state integrity across all turns without data loss.

[2.5] The system shall produce the same game outcome given the same sequence of moves and actions.

### Usability
[3.1] The system shall display clear and consistent status messages, including current turn, check state, and game outcome.

[3.2] The system shall display accurate spell information (remaining charges and cooldowns) for the current player at all times.

[3.3] The system shall provide immediate feedback when an invalid move or spell action is attempted.

[3.4] The system shall ensure that all display text (status messages, errors, labels) is concise and unambiguous.

[3.5] The system shall present the game board and related information in a readable and organized format at all times.

### Consistency
[4.1] The system shall ensure that all state-reset operations fully restore the game to the starting board configuration.

[4.2] The system shall ensure that all spell mechanics are consistent with their defined rules.

### Robustness
[5.1] The system shall handle invalid inputs (e.g. illegal moves, invalid spell targets) without crashing the game state.

### Maintainability
[6.1] The system shall be modular, allowing individual components like game and spell logic to be implemented in separate functions.

[6.2] The system shall support unit testing of core functionality, including move validation and spell mechanics.