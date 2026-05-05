# Test Cases

## Description

For convenience, test cases may be logically grouped together in what are called **Test Modules**, based on areas of testing. The use of Test Modules helps make the Traceability Matrices and archiving Test Cases more manageable.

---

## Test Case Template

### Test Case ID — Test Case Title

The Test Case ID may be any convenient identifier, as decided upon by the tester. Identifiers should follow a consistent pattern within Test Cases, and similar consistency should apply across Test Modules for the same project.

#### Description
The purpose of the Test Case, usually to verify a specific requirement. This is a high-level description of the test.

#### Test Inputs
Any required data input for the Test Case.

#### Expected Results
Describe the expected results and outputs from this Test Case. This may include any possible output, including exceptions or errors.

#### Dependencies
If correct execution of this Test Case depends on other Test Cases or external systems, those dependencies should be listed here.

#### Initialization
Any required setup of the system (software or hardware) before executing the test.

#### Test Steps
An ordered list of steps describing how to execute the Test Case.

#### Owner
The person(s) or team responsible for maintaining the Test Case.

---

Additional relevant data (e.g., tables, tools, configurations) may be included as needed to support execution.

---

# Test Modules

## Module 1: Freeze Spell

### TC-01 — Freeze Targets Opponent, Not Caster

#### Description
Verify that casting the Freeze spell records the opponent as the frozen color, not the caster.

#### Test Inputs
- Center square: `chess.E5`

#### Expected Results
- `game.freeze_effect_color == chess.BLACK`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White to move by default)

#### Test Steps
1. Call `game.cast_freeze(chess.E5)`
2. Assert `game.freeze_effect_color == chess.BLACK`

#### Owner
Team 11

---

### TC-02 — Freeze Decrements Charge on Cast

#### Description
Verify that casting the Freeze spell decrements the caster's charge count by 1.

#### Test Inputs
- Center square: `chess.E5`

#### Expected Results
- `game.freeze_remaining[chess.WHITE] == 4` (decremented from 5)

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White starts with 5 freeze charges)

#### Test Steps
1. Call `game.cast_freeze(chess.E5)`
2. Assert `game.freeze_remaining[chess.WHITE] == 4`

#### Owner
Team 11

---

### TC-03a — White Starts with 5 Freeze Charges

#### Description
Verify that White begins the game with 5 freeze charges as specified.

#### Test Inputs
- None

#### Expected Results
- `game.freeze_remaining[chess.WHITE] == 5`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Read `game.freeze_remaining[chess.WHITE]`
2. Assert the value equals `5`

#### Owner
Team 11

---

### TC-03b — Black Starts with 5 Freeze Charges

#### Description
Verify that Black begins the game with 5 freeze charges as specified.

#### Test Inputs
- None

#### Expected Results
- `game.freeze_remaining[chess.BLACK] == 5`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Read `game.freeze_remaining[chess.BLACK]`
2. Assert the value equals `5`

#### Owner
Team 11

---

### TC-03c — Freeze Blocked at Zero Charges

#### Description
Verify that a player cannot cast Freeze when they have 0 charges remaining.

#### Test Inputs
- `freeze_remaining[WHITE] = 0`
- Center square: `chess.E5`

#### Expected Results
- `cast_freeze(chess.E5)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.freeze_remaining[chess.WHITE] = 0`

#### Test Steps
1. Set `game.freeze_remaining[chess.WHITE] = 0`
2. Call `result = game.cast_freeze(chess.E5)`
3. Assert `result is False`

#### Owner
Team 11

---

### TC-03d — Freeze Returns True on Successful Cast

#### Description
Verify that `cast_freeze` returns `True` when all conditions for casting are satisfied.

#### Test Inputs
- Center square: `chess.E5`

#### Expected Results
- `cast_freeze(chess.E5)` returns `True`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White to move, 5 charges, cooldown = 0)

#### Test Steps
1. Call `result = game.cast_freeze(chess.E5)`
2. Assert `result is True`

#### Owner
Team 11

---

### TC-04 — Freeze Cooldown Set to 3 After Cast

#### Description
Verify that casting Freeze sets the caster's cooldown to 3 turns as specified.

#### Test Inputs
- Center square: `chess.E5`

#### Expected Results
- `game.freeze_cooldown[chess.WHITE] == 3`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White to move)

#### Test Steps
1. Call `game.cast_freeze(chess.E5)`
2. Assert `game.freeze_cooldown[chess.WHITE] == 3`

#### Owner
Team 11

---

### TC-05 — Freeze Blocked While on Cooldown

#### Description
Verify that a player cannot cast Freeze while their cooldown counter is greater than 0.

#### Test Inputs
- `freeze_cooldown[WHITE] = 2`
- Center square: `chess.E5`

#### Expected Results
- `cast_freeze(chess.E5)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set `game.freeze_cooldown[chess.WHITE] = 2`

#### Test Steps
1. Set `game.freeze_cooldown[chess.WHITE] = 2`
2. Call `result = game.cast_freeze(chess.E5)`
3. Assert `result is False`

#### Owner
Team 11

---

### TC-05b — Freeze Can Be Cast After Cooldown Reaches Zero

#### Description
Verify that a player may cast Freeze again once their cooldown has returned to 0 and they have remaining charges.

#### Test Inputs
- `freeze_cooldown[WHITE] = 0`
- `freeze_remaining[WHITE] = 3`
- Center square: `chess.D4`

#### Expected Results
- `cast_freeze(chess.D4)` returns `True`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.freeze_cooldown[chess.WHITE] = 0`
- Set `game.freeze_remaining[chess.WHITE] = 3`

#### Test Steps
1. Set `game.freeze_cooldown[chess.WHITE] = 0`
2. Set `game.freeze_remaining[chess.WHITE] = 3`
3. Call `result = game.cast_freeze(chess.D4)`
4. Assert `result is True`

#### Owner
Team 11

---

### TC-06 — Freeze Cooldown Decrements at Turn Start

#### Description
Verify that the freeze cooldown decrements by 1 when `on_turn_start()` is called at the start of the caster's turn.

#### Test Inputs
- `freeze_cooldown[WHITE] = 3`
- Board turn: White to move

#### Expected Results
- `game.freeze_cooldown[chess.WHITE] == 2` after `on_turn_start()`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.freeze_cooldown[chess.WHITE] = 3`
- Set `game.board.turn = chess.WHITE`

#### Test Steps
1. Set `game.freeze_cooldown[chess.WHITE] = 3`
2. Set `game.board.turn = chess.WHITE`
3. Call `game.on_turn_start()`
4. Assert `game.freeze_cooldown[chess.WHITE] == 2`

#### Owner
Team 11

---

### TC-07 — Freeze Blocked on Second Cast Same Turn

#### Description
Verify that a player may not cast Freeze more than once per turn; the second attempt must be rejected.

#### Test Inputs
- First cast center: `chess.E5`
- Second cast center: `chess.D4`

#### Expected Results
- First cast returns `True`
- Second cast returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White to move)

#### Test Steps
1. Call `game.cast_freeze(chess.E5)` (first cast)
2. Call `result = game.cast_freeze(chess.D4)` (second cast, same turn)
3. Assert `result is False`

#### Owner
Team 11

---

### TC-08 — Freeze Area Includes Center Square

#### Description
Verify that the 3×3 freeze area returned by `squares_in_3x3()` includes the center square that was passed as input.

#### Test Inputs
- Center square: `chess.E4`

#### Expected Results
- `chess.E4 in squares_in_3x3(chess.E4)`

#### Dependencies
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- None (pure function, no game state required)

#### Test Steps
1. Call `area = squares_in_3x3(chess.E4)`
2. Assert `chess.E4 in area`

#### Owner
Team 11

---

### TC-08b — Freeze Area Has 9 Squares for Interior Center

#### Description
Verify that `squares_in_3x3()` returns exactly 9 squares when the center is an interior square (not on an edge or corner).

#### Test Inputs
- Center square: `chess.E4` (interior)

#### Expected Results
- `len(squares_in_3x3(chess.E4)) == 9`

#### Dependencies
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- None

#### Test Steps
1. Call `area = squares_in_3x3(chess.E4)`
2. Assert `len(area) == 9`

#### Owner
Team 11

---

### TC-08c — Freeze Area Has Fewer Than 9 Squares at Corner

#### Description
Verify that `squares_in_3x3()` returns fewer than 9 squares when the center is a corner square, since part of the 3×3 area falls off the board.

#### Test Inputs
- Center square: `chess.A1` (corner)

#### Expected Results
- `len(squares_in_3x3(chess.A1)) < 9`

#### Dependencies
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- None

#### Test Steps
1. Call `area = squares_in_3x3(chess.A1)`
2. Assert `len(area) < 9`

#### Owner
Team 11

---

### TC-08d — Freeze Area Has Fewer Than 9 Squares at Edge

#### Description
Verify that `squares_in_3x3()` returns fewer than 9 squares when the center is on an edge of the board.

#### Test Inputs
- Center square: `chess.A4` (edge)

#### Expected Results
- `len(squares_in_3x3(chess.A4)) < 9`

#### Dependencies
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- None

#### Test Steps
1. Call `area = squares_in_3x3(chess.A4)`
2. Assert `len(area) < 9`

#### Owner
Team 11

---

### TC-08e — Freeze Area Includes All 8 Neighbours

#### Description
Verify that all 8 squares immediately surrounding the center square are included in the freeze area.

#### Test Inputs
- Center square: `chess.E4`

#### Expected Results
- All of D3, E3, F3, D4, F4, D5, E5, F5 are present in the returned area

#### Dependencies
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- None

#### Test Steps
1. Call `area = squares_in_3x3(chess.E4)`
2. Assert each of the 8 neighbour squares (D3, E3, F3, D4, F4, D5, E5, F5) is in `area`

#### Owner
Team 11

---

### TC-09 — Frozen Piece Excluded from Legal Moves

#### Description
Verify that a piece whose square falls inside the active freeze area cannot be selected as the origin of a move during the frozen side's turn.

#### Test Inputs
- `freeze_effect_color = chess.BLACK`
- `freeze_effect_squares = squares_in_3x3(chess.E7)` (covers the Black pawn on E7)
- `freeze_effect_plies_left = 1`
- Board turn: Black to move

#### Expected Results
- `chess.E7` is not present among the origin squares in `game.get_legal_moves()`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set `game.freeze_effect_color = chess.BLACK`
- Manually set `game.freeze_effect_squares = squares_in_3x3(chess.E7)`
- Manually set `game.freeze_effect_plies_left = 1`
- Set `game.board.turn = chess.BLACK`

#### Test Steps
1. Apply freeze effect state manually as described in Initialization
2. Call `legal_origins = {m.from_square for m in game.get_legal_moves()}`
3. Assert `chess.E7 not in legal_origins`

#### Owner
Team 11

---

### TC-10 — Freeze Effect Clears After Frozen Side Moves

#### Description
Verify that the active freeze effect is cleared after the frozen side completes their turn, so the freeze does not persist beyond 1 of the opponent's turns.

#### Test Inputs
- `freeze_effect_color = chess.BLACK`
- `freeze_effect_squares = {chess.E7}`
- `freeze_effect_plies_left = 1`
- Move: Black plays d5 (pushed directly via `board.push_san`)

#### Expected Results
- `game.freeze_effect_plies_left == 0`
- `game.freeze_effect_color is None`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set `freeze_effect_color = chess.BLACK`, `freeze_effect_squares = {chess.E7}`, `freeze_effect_plies_left = 1`
- Set `game.board.turn = chess.BLACK`

#### Test Steps
1. Apply freeze effect state manually as described in Initialization
2. Push Black's move directly via `game.board.push_san("d5")` (bypasses `make_move` to isolate this test)
3. Call `game.after_move_pushed()`
4. Assert `game.freeze_effect_plies_left == 0`
5. Assert `game.freeze_effect_color is None`

#### Owner
Team 11

---

### TC-11 — `is_frozen` Returns True for Frozen Square

#### Description
Verify that `is_frozen(sq, color)` returns `True` when the given color is actively frozen and the given square is within the frozen area.

#### Test Inputs
- `freeze_effect_color = chess.BLACK`
- `freeze_effect_squares = squares_in_3x3(chess.E5)` (includes E5)
- `freeze_effect_plies_left = 1`
- Query: `is_frozen(chess.E5, chess.BLACK)`

#### Expected Results
- `game.is_frozen(chess.E5, chess.BLACK) is True`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`
- `squares_in_3x3` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set `freeze_effect_color`, `freeze_effect_squares`, and `freeze_effect_plies_left`

#### Test Steps
1. Set `game.freeze_effect_color = chess.BLACK`
2. Set `game.freeze_effect_squares = squares_in_3x3(chess.E5)`
3. Set `game.freeze_effect_plies_left = 1`
4. Call `result = game.is_frozen(chess.E5, chess.BLACK)`
5. Assert `result is True`

#### Owner
Team 11

---

### TC-11b — `is_frozen` Returns False for Caster's Color

#### Description
Verify that `is_frozen(sq, color)` returns `False` for the caster's color, since the freeze only applies to the opponent.

#### Test Inputs
- `freeze_effect_color = chess.BLACK`
- `freeze_effect_squares = squares_in_3x3(chess.E5)`
- `freeze_effect_plies_left = 1`
- Query: `is_frozen(chess.E5, chess.WHITE)`

#### Expected Results
- `game.is_frozen(chess.E5, chess.WHITE) is False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set freeze effect targeting `chess.BLACK`

#### Test Steps
1. Set `game.freeze_effect_color = chess.BLACK`
2. Set `game.freeze_effect_squares = squares_in_3x3(chess.E5)`
3. Set `game.freeze_effect_plies_left = 1`
4. Call `result = game.is_frozen(chess.E5, chess.WHITE)`
5. Assert `result is False`

#### Owner
Team 11

---

## Module 2: Jump Spell

### TC-12 — Jump Range Valid
#### Description
Verify that a piece can jump to a square within a Chebyshev distance of 2, ignoring obstacles.

#### Test Inputs
- `piece_sq`: `chess.B1` (White Knight)
- `dest_sq`: `chess.B3` (Empty square, distance 2)

#### Expected Results
- `cast_jump(chess.B1, chess.B3)` returns `True`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.cast_jump(chess.B1, chess.B3)`
2. Assert `result is True`

#### Owner
Team 11

---

### TC-13 — Jump Range Invalid
#### Description
Verify that a piece cannot jump to a square beyond a Chebyshev distance of 2.

#### Test Inputs
- `piece_sq`: `chess.A1` (White Rook)
- `dest_sq`: `chess.A4` (Empty square, distance 3)

#### Expected Results
- `cast_jump(chess.A1, chess.A4)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.cast_jump(chess.A1, chess.A4)`
2. Assert `result is False`

#### Owner
Team 11

---

### TC-14 — White Starts with 3 Jump Charges
#### Description
Verify that White begins the game with 3 jump charges as specified.

#### Test Inputs
- None

#### Expected Results
- `game.jump_remaining[chess.WHITE] == 3`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Read `game.jump_remaining[chess.WHITE]`
2. Assert the value equals `3`

#### Owner
Team 11

---

### TC-15 — Jump Decrements Charge on Cast
#### Description
Verify that casting the Jump spell decrements the caster's charge count by 1.

#### Test Inputs
- `piece_sq`: `chess.B1`
- `dest_sq`: `chess.B3`

#### Expected Results
- `game.jump_remaining[chess.WHITE] == 2`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.cast_jump(chess.B1, chess.B3)`
2. Assert `game.jump_remaining[chess.WHITE] == 2`

#### Owner
Team 11

---

### TC-16 — Jump Blocked at Zero Charges
#### Description
Verify that a player cannot cast Jump when they have 0 charges remaining.

#### Test Inputs
- `jump_remaining[WHITE] = 0`
- `piece_sq`: `chess.B1`
- `dest_sq`: `chess.B3`

#### Expected Results
- `cast_jump(chess.B1, chess.B3)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.jump_remaining[chess.WHITE] = 0`

#### Test Steps
1. Call `result = game.cast_jump(chess.B1, chess.B3)`
2. Assert `result is False`

#### Owner
Team 11

---

### TC-17 — Jump Cooldown Set to 2 After Cast
#### Description
Verify that casting Jump sets the caster's cooldown to 2 turns as specified.

#### Test Inputs
- `piece_sq`: `chess.B1`
- `dest_sq`: `chess.B3`

#### Expected Results
- `game.jump_cooldown[chess.WHITE] == 2`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.cast_jump(chess.B1, chess.B3)`
2. Assert `game.jump_cooldown[chess.WHITE] == 2`

#### Owner
Team 11

---

### TC-18 — Jump Blocked While on Cooldown
#### Description
Verify that a player cannot cast Jump while their cooldown counter is greater than 0.

#### Test Inputs
- `jump_cooldown[WHITE] = 1`
- `piece_sq`: `chess.B1`
- `dest_sq`: `chess.B3`

#### Expected Results
- `cast_jump(chess.B1, chess.B3)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.jump_cooldown[chess.WHITE] = 1`

#### Test Steps
1. Call `result = game.cast_jump(chess.B1, chess.B3)`
2. Assert `result is False`

#### Owner
Team 11

---

### TC-19 — Jump Cooldown Decrements at Turn Start
#### Description
Verify that the jump cooldown decrements by 1 when `on_turn_start()` is called at the start of the caster's turn.

#### Test Inputs
- `jump_cooldown[WHITE] = 2`

#### Expected Results
- `game.jump_cooldown[chess.WHITE] == 1` after `on_turn_start()`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.jump_cooldown[chess.WHITE] = 2`
- Set `game.board.turn = chess.WHITE`

#### Test Steps
1. Call `game.on_turn_start()`
2. Assert `game.jump_cooldown[chess.WHITE] == 1`

#### Owner
Team 11

---

### TC-20 — Jump Blocked on Second Cast Same Turn
#### Description
Verify that a player may not cast Jump more than once per turn.

#### Test Inputs
- First cast: `chess.B1` to `chess.B3`
- Second cast: `chess.G1` to `chess.G3`

#### Expected Results
- First cast returns `True`
- Second cast returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.cast_jump(chess.B1, chess.B3)`
2. Call `result = game.cast_jump(chess.G1, chess.G3)`
3. Assert `result is False`

#### Owner
Team 11

---

### TC-21 — Jump Blocked for King
#### Description
Verify that the King cannot be jumped.

#### Test Inputs
- `piece_sq`: `chess.E1` (White King)
- `dest_sq`: `chess.E3`

#### Expected Results
- `cast_jump(chess.E1, chess.E3)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.cast_jump(chess.E1, chess.E3)`
2. Assert `result is False`

#### Owner
Team 11

---

### TC-22 — Jump Destination Must Be Empty
#### Description
Verify that the piece can only land on an empty square.

#### Test Inputs
- `piece_sq`: `chess.A1`
- `dest_sq`: `chess.A2` (Occupied by White Pawn)

#### Expected Results
- `cast_jump(chess.A1, chess.A2)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.cast_jump(chess.A1, chess.A2)`
2. Assert `result is False`

#### Owner
Team 11

---

### TC-23 — Jump Must Be Own Piece
#### Description
Verify that a player can only cast Jump on their own pieces.

#### Test Inputs
- `piece_sq`: `chess.A7` (Black Pawn)
- `dest_sq`: `chess.A5`

#### Expected Results
- `cast_jump(chess.A7, chess.A5)` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.cast_jump(chess.A7, chess.A5)`
2. Assert `result is False`

#### Owner
Team 11

---

## Module 3: Game State Display

### TC-24 — Status Text Shows White Turn at Start

#### Description
Verify that a new game displays "white" as the initial current player.

#### Test Inputs
- New `SpellChessGame` instance

#### Expected Results
- `game.status_text() == "Turn: White."`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.status_text()`
2. Assert the result equals `"Turn: White."`

#### Owner
Team 11

---

### TC-25 — Status Text Shows Black Turn

#### Description
Verify that the status display updates when it is black's turn.

#### Test Inputs
- `game.board.turn = chess.BLACK`

#### Expected Results
- `game.status_text() == "Turn: Black."`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set `game.board.turn = chess.BLACK`

#### Test Steps
1. Set `game.board.turn = chess.BLACK`
2. Call `game.status_text()`
3. Assert the result equals `"Turn: Black."`

#### Owner
Team 11

---

### TC-26 — Status Text Shows Check

#### Description
Verify that the status display indicates when the current player is in check.

#### Test Inputs
- Board FEN: `"4k3/8/8/8/8/8/8/4R3 b - - 0 1"`

#### Expected Results
- `game.status_text() == "Turn: Black (check)."`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set the board to a position where Black is in check

#### Test Steps
1. Call `game.board.set_fen("4k3/8/8/8/8/8/8/4R3 b - - 0 1")`
2. Call `game.status_text()`
3. Assert the result equals `"Turn: Black (check)."`

#### Owner
Team 11

---

### TC-27 — Status Text Shows Checkmate Game Over

#### Description
Verify that the status display shows the game-over message, termination type, and winner when the game ends by checkmate.

#### Test Inputs
- Board FEN: `"7k/6Q1/6K1/8/8/8/8/8 b - - 0 1"`

#### Expected Results
- `game.status_text() == "Game over: CHECKMATE — White wins"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set the board to a checkmate position with White winning

#### Test Steps
1. Call `game.board.set_fen("7k/6Q1/6K1/8/8/8/8/8 b - - 0 1")`
2. Call `game.status_text()`
3. Assert the result equals `"Game over: CHECKMATE — White wins"`

#### Owner
Team 11

---

### TC-28 — Freeze Info Text Shows Initial White Charges

#### Description
Verify that the Freeze display shows White's initial number of Freeze charges.

#### Test Inputs
- New `SpellChessGame` instance

#### Expected Results
- `game.freeze_info_text() == "Freeze: 5"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance with White to move

#### Test Steps
1. Call `game.freeze_info_text()`
2. Assert the result equals `"Freeze: 5"`

#### Owner
Team 11

---

### TC-29 — Freeze Info Text Shows Cooldown

#### Description
Verify that the Freeze display includes cooldown information when the current player has an active Freeze cooldown.

#### Test Inputs
- `game.freeze_cooldown[chess.WHITE] = 2`

#### Expected Results
- `game.freeze_info_text() == "Freeze: 5  (cooldown 2)"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set White's Freeze cooldown to 2

#### Test Steps
1. Set `game.freeze_cooldown[chess.WHITE] = 2`
2. Call `game.freeze_info_text()`
3. Assert the result equals `"Freeze: 5  (cooldown 2)"`

#### Owner
Team 11

---

### TC-30 — Freeze Info Text Shows Frozen Area Message

#### Description
Verify that the Freeze display indicates when the current player's pieces are frozen.

#### Test Inputs
- `game.board.turn = chess.BLACK`
- `game.freeze_effect_color = chess.BLACK`
- `game.freeze_effect_plies_left = 1`
- `game.freeze_effect_squares = {chess.E7}`

#### Expected Results
- `game.freeze_info_text() == "Freeze: 5  — pieces in area are frozen"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Manually set the board turn and active Freeze effect state

#### Test Steps
1. Set `game.board.turn = chess.BLACK`
2. Set `game.freeze_effect_color = chess.BLACK`
3. Set `game.freeze_effect_plies_left = 1`
4. Set `game.freeze_effect_squares = {chess.E7}`
5. Call `game.freeze_info_text()`
6. Assert the result equals `"Freeze: 5  — pieces in area are frozen"`

#### Owner
Team 11

---

### TC-31 — Jump Info Text Shows Initial White Charges

#### Description
Verify that the Jump display shows White's initial number of Jump charges.

#### Test Inputs
- New `SpellChessGame` instance

#### Expected Results
- `game.jump_info_text() == "Jump: 3"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance with White to move

#### Test Steps
1. Call `game.jump_info_text()`
2. Assert the result equals `"Jump: 3"`

#### Owner
Team 11

---

### TC-32 — Jump Info Text Shows Cooldown

#### Description
Verify that the Jump display includes cooldown information when the current player has an active Jump cooldown.

#### Test Inputs
- `game.jump_cooldown[chess.WHITE] = 1`

#### Expected Results
- `game.jump_info_text() == "Jump: 3  (cooldown 1)"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set White's Jump cooldown to 1

#### Test Steps
1. Set `game.jump_cooldown[chess.WHITE] = 1`
2. Call `game.jump_info_text()`
3. Assert the result equals `"Jump: 3  (cooldown 1)"`

#### Owner
Team 11

---

### TC-33 — Status Text Shows Stalemate Draw

#### Description
Verify that the status display shows the correct game-over message when the game ends in a draw by stalemate.

#### Test Inputs
- Board FEN: `"7k/5Q2/7K/8/8/8/8/8 b - - 0 1"`

#### Expected Results
- `game.status_text() == "Game over: STALEMATE — Draw"`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set the board to a stalemate position

#### Test Steps
1. Call `game.board.set_fen("7k/5Q2/7K/8/8/8/8/8 b - - 0 1")`
2. Call `game.status_text()`
3. Assert the result equals `"Game over: STALEMATE — Draw"`

#### Owner
Team 11

---

### TC-34 — Status Text Shows Black Checkmate Win

#### Description
Verify that the status display correctly shows a Black victory when the game ends in checkmate.

#### Test Inputs
- Board FEN: `"7K/6q1/6k1/8/8/8/8/8 w - - 0 1"`

#### Expected Results
- `game.status_text() == "Game over: CHECKMATE — Black wins"`

#### Dependencies
- `python-chess` library  
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance  
- Set the board to a checkmate position with Black winning

#### Test Steps
1. Call `game.board.set_fen("7K/6q1/6k1/8/8/8/8/8 w - - 0 1")`  
2. Call `game.status_text()`  
3. Assert the result equals `"Game over: CHECKMATE — Black wins"`

#### Owner
Team 11

---
### TC-35 — Board Resets to Starting Position

#### Description
Verify that calling `new_game()` restores the chess board to the initial starting position.

#### Test Inputs
- A move: `e4`

#### Expected Results
- `game.board.fen()` equals `chess.STARTING_FEN`

#### Dependencies
- `python-chess` library  
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.board.push_san("e4")`
2. Call `game.new_game()`
3. Assert `game.board.fen() == chess.STARTING_FEN`

#### Owner
Team 11

---

### TC-36 — Turn Resets to White

#### Description
Verify that a new game resets the turn to White.

#### Test Inputs
- Moves played before reset: `e4`, `e5`

#### Expected Results
- `game.board.turn == chess.WHITE`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.board.push_san("e4")`
2. Call `game.board.push_san("e5")`
3. Call `game.new_game()`
4. Assert `game.board.turn == chess.WHITE`

#### Owner
Team 11

---

### TC-37 — Move History Cleared After Reset

#### Description
Verify that all previous moves are cleared after calling `new_game()`.

#### Test Inputs
- Moves played before reset: `e4`, `e5`

#### Expected Results
- `len(game.board.move_stack) == 0`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.board.push_san("e4")`
2. Call `game.board.push_san("e5")`
3. Call `game.new_game()`
4. Assert `len(game.board.move_stack) == 0`

#### Owner
Team 11

---

### TC-38 — Freeze State Resets Completely

#### Description
Verify that all Freeze spell state is cleared after a new game starts.

#### Test Inputs
- Active freeze cast on `E5`

#### Expected Results
- `freeze_effect_color` is `None`
- `freeze_effect_squares == set()`
- `freeze_effect_plies_left == 0`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.cast_freeze(chess.E5)`
2. Call `game.new_game()`
3. Assert `game.freeze_effect_color` is `None`
4. Assert `game.freeze_effect_squares == set()`
5. Assert `game.freeze_effect_plies_left == 0`

#### Owner
Team 11

---

### TC-39 — Freeze Charges Reset to 5

#### Description
Verify that Freeze charges reset to the starting value of 5.

#### Test Inputs
- Modified values: `freeze_remaining[WHITE] = 2`, `freeze_remaining[BLACK] = 1`

#### Expected Results
- Both sides have 5 charges after reset

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Set `game.freeze_remaining[chess.WHITE] = 2`
2. Set `game.freeze_remaining[chess.BLACK] = 1`
3. Call `game.new_game()`
4. Assert `game.freeze_remaining[chess.WHITE] == 5`
5. Assert `game.freeze_remaining[chess.BLACK] == 5`

#### Owner
Team 11

---

### TC-40 — Jump Charges Reset to 3

#### Description
Verify that Jump charges reset to the starting value of 3.

#### Test Inputs
- Modified values: `jump_remaining[WHITE] = 0`, `jump_remaining[BLACK] = 1`

#### Expected Results
- Both sides have 3 charges after reset

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Set `game.jump_remaining[chess.WHITE] = 0`
2. Set `game.jump_remaining[chess.BLACK] = 1`
3. Call `game.new_game()`
4. Assert `game.jump_remaining[chess.WHITE] == 3`
5. Assert `game.jump_remaining[chess.BLACK] == 3`

#### Owner
Team 11

---

### TC-41 — Cooldowns Reset to 0

#### Description
Verify that all spell cooldowns reset to zero after starting a new game.

#### Test Inputs
- Modified cooldown values: `freeze_cooldown[WHITE] = 2`, `jump_cooldown[WHITE] = 1`, etc.

#### Expected Results
- All cooldowns equal 0

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Set `game.freeze_cooldown[chess.WHITE] = 2`
2. Set `game.jump_cooldown[chess.WHITE] = 1`
3. Call `game.new_game()`
4. Assert all `freeze_cooldown` and `jump_cooldown` values are 0

#### Owner
Team 11

---

### TC-42 — Spell Cast Flags Reset

#### Description
Verify that per-turn spell flags are reset after starting a new game.

#### Test Inputs
- Flags set to `True`: `spell_casted_this_turn`, `jump_casted_this_turn`, `freeze_targeting`

#### Expected Results
- All flags are `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Set `game.spell_casted_this_turn = True`
2. Set `game.jump_casted_this_turn = True`
3. Set `game.freeze_targeting = True`
4. Call `game.new_game()`
5. Assert all flags are `False`

#### Owner
Team 11

---

## Module 5: Move Lifecycle

### TC-43 — Move Switches Turn

#### Description
Verify that a valid move correctly switches the turn to the opposite player.

#### Test Inputs
- Move: `e2` → `e4`

#### Expected Results
- Turn changes from White to Black

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Assert `game.board.turn == chess.WHITE`
2. Call `game.make_move(chess.E2, chess.E4)`
3. Assert `game.board.turn == chess.BLACK`

#### Owner
Team 11

---

### TC-44 — Move Updates Board State

#### Description
Verify that a moved piece appears on the destination square.

#### Test Inputs
- Move: `e2` → `e4`

#### Expected Results
- A white pawn exists at `e4`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.make_move(chess.E2, chess.E4)`
2. Assert piece exists at `chess.E4`
3. Assert piece type is `PAWN` and color is `WHITE`

#### Owner
Team 11

---

### TC-45 — Illegal Move Rejected

#### Description
Verify that invalid chess moves are rejected and not applied.

#### Test Inputs
- Move: `b1` → `b3` (illegal knight move)

#### Expected Results
- `make_move()` returns `False`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `result = game.make_move(chess.B1, chess.B3)`
2. Assert `result is False`
3. Assert `game.board.piece_at(chess.B3)` is `None`

#### Owner
Team 11

---

### TC-46 — Cannot Move Opponent Piece

#### Description
Verify that a player cannot move the opponent's pieces.

#### Test Inputs
- Move: `e7` → `e5` (White tries to move Black's pawn)

#### Expected Results
- Move is rejected

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance (White to move)

#### Test Steps
1. Call `result = game.make_move(chess.E7, chess.E5)`
2. Assert `result is False`
3. Assert destination square `chess.E5` remains empty

#### Owner
Team 11

---

### TC-47 — Move History Exists After Move

#### Description
Verify that successful moves are recorded in the move stack.

#### Test Inputs
- Move: `e2` → `e4`

#### Expected Results
- Move stack length increases by 1

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Call `game.make_move(chess.E2, chess.E4)`
2. Assert `len(game.board.move_stack) == 1`

#### Owner
Team 11

---

### TC-48 — Check State Detected

#### Description
Verify that the system correctly detects check during gameplay.

#### Test Inputs
- Scholar’s mate sequence

#### Expected Results
- `game.board.is_check() == True`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance

#### Test Steps
1. Play sequence: `e4`, `e5`, `Qh5`, `Nc6`, `Bc4`, `Nf6`, `Qxf7`
2. Assert `game.board.is_check()` is `True`

#### Owner
Team 11

---
### TC-49 — En Passant Execution

#### Description
Verify that the En Passant capture works correctly, moving the capturing pawn to the destination and removing the captured pawn from the board.

#### Test Inputs
- Board FEN: `rnbqkbnr/ppp1p1pp/8/3pPp2/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3`
- Move: `e5` → `d6` (En Passant)

#### Expected Results
- `make_move(chess.E5, chess.D6)` returns `True`
- White Pawn exists at `d6`
- Black Pawn at `d5` is removed (`None`)

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set board to En Passant setup FEN

#### Test Steps
1. Call `game.board.set_fen("rnbqkbnr/ppp1p1pp/8/3pPp2/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3")`
2. Call `result = game.make_move(chess.E5, chess.D6)`
3. Assert `result is True`
4. Assert `game.board.piece_at(chess.D6).piece_type == chess.PAWN`
5. Assert `game.board.piece_at(chess.D5)` is `None`

#### Owner
Team 11

---

### TC-50 — Pawn Promotion to Queen

#### Description
Verify that a pawn reaching the 8th rank is correctly promoted to a Queen.

#### Test Inputs
- Board FEN: `8/P7/8/8/8/8/8/k6K w - - 0 1` (White Pawn on a7)
- Move: `a7` → `a8` (Promotion to Queen)

#### Expected Results
- Piece at `a8` is a `QUEEN`
- Piece color is `WHITE`

#### Dependencies
- `python-chess` library
- `SpellChessGame` from `spell_logic.py`

#### Initialization
- Create a new `SpellChessGame` instance
- Set board to promotion setup FEN

#### Test Steps
1. Call `game.board.set_fen("8/P7/8/8/8/8/8/k6K w - - 0 1")`
2. Push promotion move: `chess.Move(chess.A7, chess.A8, promotion=chess.QUEEN)`
3. Call `game.after_move_pushed()`
4. Assert piece at `chess.A8` is not `None`
5. Assert piece type is `chess.QUEEN`
6. Assert piece color is `chess.WHITE`

#### Owner
Team 11
---
# Defect Summary

| Defect # | TC(s) | Location in Code | Description |
|----------|-------|------------------|-------------|
| D-01 | TC-01 | `cast_freeze` line 150 | `freeze_effect_color` set to caster (`turn`) instead of opponent (`not turn`) |
| D-02 | TC-02 | `cast_freeze` missing line | `freeze_remaining[turn]` never decremented after a successful cast |
| D-03 | TC-04 | `cast_freeze` line 154 | Freeze cooldown set to `2` instead of spec value `3` |
| D-04 | TC-06 | `on_turn_start` lines 221–222 | `freeze_cooldown` is never decremented; only `jump_cooldown` is |
| D-05 | TC-07 | `cast_freeze` missing line | `spell_casted_this_turn` never set to `True` (masked in practice by cooldown) |
| D-06 | TC-08, TC-08b, TC-09, TC-11 | `squares_in_3x3` lines 48–50 | Guard `if df==0 and dr==0: continue` excludes the center square from the area |
| D-07 | TC-13 | `squares_in_jump_range` lines 63–64 | `range(-3, 4)` computes Chebyshev distance ≤ 3 instead of spec value 2 |
| D-08 | TC-17 | `cast_jump` line 187 | Jump cooldown set to `1` instead of spec value `2` |
| D-09 | TC-21 | `cast_jump` | Missing check to prevent the King from being jumped |
| D-10 | TC-22 | `cast_jump` | Missing check to ensure destination square is empty |
| D-11 | TC-35 | `new_game` | Board fails to reset to `STARTING_FEN`; likely `self.board.reset()` is missing |
| D-12 | TC-37 | `new_game` | `self.board.move_stack` is not cleared/reset during game initialization |
| D-13 | TC-40 | `new_game` | `jump_remaining` values are not being reset to the starting value of 3 |
| D-14 | TC-43 | `make_move` | Turn logic failing to swap `self.board.turn` after a successful move |
| D-15 | TC-48 | `make_move` | System fails to detect check state after a move sequence | 
| D-16 | TC-49 | `make_move` | En passant move rejected as illegal; logic likely missing `board.has_pseudo_legal_en_passant()` check |