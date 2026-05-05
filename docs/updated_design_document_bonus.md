# Updated Design Notes - Spell Chess P4

**Team 11:** Lee, Reznik, Trestka, Tuli  
**Date:** May 4, 2026  
**System:** LISCO - Spell Chess variant  
**Reason for update:** Phase 4 testing found several places where the earlier design did not define state changes precisely enough.

## Revision History
| Version | Date | Change |
|---------|------|--------|
| P3 Design | Apr 2026 | Original class and interaction design for Spell Chess |
| P4 Update | May 4, 2026 | Added design corrections based on unit test defects D-01 through D-16 |

## Summary
The Phase 4 implementation uses a simplified `SpellChessGame` class instead of the full P3 class structure. These notes update the design rules that were unclear in P3, especially spell state, cooldowns, reset behavior, and turn lifecycle.

## Design Updates

### 1. Spell State Must Be Charge-Based
Each player's spell state must track:
- remaining Freeze charges, starting at 5
- remaining Jump charges, starting at 3
- separate cooldown values for Freeze and Jump
- whether each spell type has already been cast during the current turn

After a successful cast, the matching charge count is reduced by 1 and its per-turn flag is set. A spell cannot be cast with 0 charges, an active cooldown, or a prior cast that turn.

Related defects: D-02, D-03, D-04, D-05, D-08

### 2. Freeze Effect Must Target the Opponent
The Freeze spell should store the opponent as the frozen color. Legal move generation filters out moves that start from frozen squares only when the side to move is that frozen color.

The frozen area is a 3x3 region centered on the selected square, including the center. Interior targets affect 9 squares; edge and corner targets affect fewer.

Related defects: D-01, D-06

### 3. Jump Validation Must Be Complete Before Moving the Piece
Jump validates all target rules before changing the board:
- the origin square must contain the current player's piece
- the selected piece cannot be a King
- the destination square must be empty
- the destination must be within Chebyshev distance 2

The range rule is `max(abs(file_delta), abs(rank_delta)) <= 2`. Jump cannot be used as a capture.

Related defects: D-07, D-09, D-10

### 4. Turn Lifecycle Must Have One Clear Owner
Post-move lifecycle should have one sequence:
1. validate the move against the chess engine's legal move list
2. push the move to the board
3. expire any freeze effect if the frozen player just completed a turn
4. start the next turn by clearing per-turn spell flags
5. decrement cooldowns for the player whose turn is beginning

Because `python-chess` changes `board.turn` inside `board.push()`, the design must not manually switch turns again.

Related defects: D-04, D-14, D-15

### 5. Reset Must Reinitialize the Full Match
Starting a new game must reset all persistent state:
- board position and move history
- active turn
- Freeze charges and cooldowns
- Jump charges and cooldowns
- active freeze effect
- per-turn cast flags

One reset method should serve both GUI and tests.

Related defects: D-11, D-12, D-13

### 6. Standard Chess Rules Should Be Delegated to the Chess Engine
The design should avoid custom move heuristics when `python-chess` already provides the legal move list. Special rules such as en passant, castling, check, checkmate, and promotion should come from engine-generated legal moves. Custom logic should only add Spell Chess restrictions, such as frozen origin squares.

Related defects: D-15, D-16

## Traceability
| Defect | Design Area | Correction |
|--------|-------------|------------|
| D-01 | Freeze target color | Store opponent as frozen color |
| D-02 | Freeze charges | Decrement charge count after successful cast |
| D-03 | Freeze cooldown | Set Freeze cooldown to 3 |
| D-04 | Turn start | Decrement Freeze and Jump cooldowns for active player |
| D-05 | Once per turn | Track and reset per-turn spell cast flags |
| D-06 | Freeze area | Include center square in 3x3 area |
| D-07 | Jump range | Use Chebyshev distance <= 2 |
| D-08 | Jump cooldown | Set Jump cooldown to 2 |
| D-09 | Jump restrictions | Reject King as jump origin |
| D-10 | Jump destination | Reject occupied destination squares |
| D-11 | New game reset | Reset board to starting position |
| D-12 | Move history reset | Clear move history as part of board reset |
| D-13 | Spell reset | Restore Jump charges to starting values |
| D-14 | Turn switching | Do not manually flip turn after `board.push()` |
| D-15 | Check detection | Preserve correct turn/board state across move sequences |
| D-16 | Standard chess rules | Let engine legal moves handle en passant |
