"""
Unit tests for Spell Chess game logic.

Run with:
    pytest test_spell_logic.py -v

These tests verify the Spell Chess rules described in SPELL_CHESS_RULES.md (README.md).
Each test is identified by a TC-XX ID, documented in docs/test_case_documentation.md.

Test classes are organized by feature:
    Freeze Spell  — TestFreezeTarget, TestFreezeCharges, TestFreezeCooldown,
                    TestFreezeOncePerTurn, TestFreezeArea, TestFreezeEffect
    Jump Spell    — TestJumpRange, TestJumpCharges, TestJumpCooldown,
                    TestJumpOncePerTurn, TestJumpRestrictions
    New Game      — TestNewGameReset
    Move Rules    — TestMoveLifecycle
    Display       — TestGameStateDisplay

Traceability: each test docstring cites the relevant README section or
P2 EARS requirement number.
"""

import chess
from spell_logic import SpellChessGame, squares_in_3x3, squares_in_jump_range


# ------------------------------------------------------------------ #
#  Demo tests — provided to students as examples                      #
# ------------------------------------------------------------------ #

class TestFreezeTarget:
    """Casting Freeze should mark the opponent's color as frozen."""

    def test_freeze_affects_opponent_not_caster(self):
        game = SpellChessGame()
        # White casts freeze
        game.cast_freeze(chess.E5)
        # The frozen color should be Black (the opponent), not White
        assert game.freeze_effect_color == chess.BLACK


class TestNewGameResetsBoard:
    """Calling new_game() should bring the board back to the starting position."""

    def test_board_resets_after_moves(self):
        game = SpellChessGame()
        game.board.push_san("e4")
        game.new_game()
        assert game.board.fen() == chess.STARTING_FEN


# ------------------------------------------------------------------ #
#  YOUR TESTS GO BELOW                                                #
#  Write tests that check the rules from SPELL_CHESS_RULES.md.        #
#  If a test fails, you've found a bug — document it!                 #
# ------------------------------------------------------------------ #

# ================================================================== #
#  Freeze Spell — Charges                                            #
# ================================================================== #

class TestFreezeCharges:
    """Each side starts with 5 freeze charges; each successful cast costs 1."""

    def test_freeze_initial_charges_white(self):
        """TC-03a | Spec: 'Each side begins the game with 5 freeze charges.' (White)"""
        game = SpellChessGame()
        assert game.freeze_remaining[chess.WHITE] == 5

    def test_freeze_initial_charges_black(self):
        """TC-03b | Spec: 'Each side begins the game with 5 freeze charges.' (Black)"""
        game = SpellChessGame()
        assert game.freeze_remaining[chess.BLACK] == 5

    def test_freeze_decrements_charge_on_cast(self):
        """
        TC-02 | Spec: 'Each cast costs 1 charge.'
        Expected: freeze_remaining[WHITE] drops from 5 to 4 after one cast.
        DEFECT: freeze_remaining is never decremented inside cast_freeze.
        """
        game = SpellChessGame()
        game.cast_freeze(chess.E5)
        assert game.freeze_remaining[chess.WHITE] == 4

    def test_freeze_blocked_at_zero_charges(self):
        """TC-03c | Spec: 'When a player has 0 charges remaining, they cannot cast Freeze.'"""
        game = SpellChessGame()
        game.freeze_remaining[chess.WHITE] = 0
        result = game.cast_freeze(chess.E5)
        assert result is False

    def test_freeze_returns_true_on_success(self):
        """TC-03d | cast_freeze must return True when all conditions are satisfied."""
        game = SpellChessGame()
        result = game.cast_freeze(chess.E5)
        assert result is True


# ================================================================== #
#  Freeze Spell — Cooldown                                           #
# ================================================================== #

class TestFreezeCooldown:
    """After casting Freeze the caster enters a 3-turn cooldown."""

    def test_freeze_cooldown_set_to_three_after_cast(self):
        """
        TC-04 | Spec table: 'Freeze cooldown after casting: 3 turns.'
        Expected: freeze_cooldown[WHITE] == 3 immediately after cast.
        DEFECT: cast_freeze sets cooldown to 2 instead of 3.
        """
        game = SpellChessGame()
        game.cast_freeze(chess.E5)
        assert game.freeze_cooldown[chess.WHITE] == 3

    def test_freeze_blocked_while_on_cooldown(self):
        """TC-05 | Spec: 'The caster cannot cast Freeze again until the cooldown reaches 0.'"""
        game = SpellChessGame()
        game.freeze_cooldown[chess.WHITE] = 2
        result = game.cast_freeze(chess.E5)
        assert result is False

    def test_freeze_cooldown_decrements_on_caster_turn_start(self):
        """
        TC-06 | Spec: 'The cooldown decrements by 1 at the start of each of the caster's turns.'
        Action: manually call on_turn_start() with White to move.
        Expected: freeze_cooldown[WHITE] drops by 1.
        DEFECT: on_turn_start() only decrements jump_cooldown, never freeze_cooldown.
        """
        game = SpellChessGame()
        game.freeze_cooldown[chess.WHITE] = 3
        game.board.turn = chess.WHITE
        game.on_turn_start()
        assert game.freeze_cooldown[chess.WHITE] == 2

    def test_freeze_can_cast_after_cooldown_zero(self):
        """TC-05b | Freeze may be cast again once cooldown is 0 (and charges remain)."""
        game = SpellChessGame()
        game.freeze_cooldown[chess.WHITE] = 0
        game.freeze_remaining[chess.WHITE] = 3
        result = game.cast_freeze(chess.D4)
        assert result is True


# ================================================================== #
#  Freeze Spell — Once Per Turn                                      #
# ================================================================== #

class TestFreezeOncePerTurn:
    """A player may cast Freeze at most once per turn."""

    def test_freeze_blocked_on_second_cast_same_turn(self):
        """
        TC-07 | Spec: 'A player may cast Freeze once per turn.'
        Setup: cast Freeze once successfully.
        Action: attempt a second cast on the same turn.
        Expected: second cast returns False.
        DEFECT: cast_freeze never sets spell_casted_this_turn = True,
                so the guard never fires and the second cast succeeds.
        """
        game = SpellChessGame()
        game.cast_freeze(chess.E5)
        result = game.cast_freeze(chess.D4)
        assert result is False


# ================================================================== #
#  Freeze Spell — Area                                               #
# ================================================================== #

class TestFreezeArea:
    """The 3×3 freeze area is centred on the chosen square and includes that square."""

    def test_freeze_area_includes_center_square(self):
        """
        TC-08 | Spec: 'The player selects any square… as the center of a 3×3 area.'
                The area must include the center.
        DEFECT: squares_in_3x3 skips df==0 and dr==0, excluding the center.
        """
        center = chess.E4
        area = squares_in_3x3(center)
        assert center in area

    def test_freeze_area_has_nine_squares_for_interior_center(self):
        """
        TC-08b | Spec: 'up to 9 squares in the middle of the board.'
        An interior center (E4) must produce exactly 9 squares.
        DEFECT: only 8 returned because center is excluded.
        """
        area = squares_in_3x3(chess.E4)
        assert len(area) == 9

    def test_freeze_area_corner_has_fewer_squares(self):
        """TC-08c | Spec: 'fewer on edges/corners.' Corner A1 must yield < 9 squares."""
        area = squares_in_3x3(chess.A1)
        assert len(area) < 9

    def test_freeze_area_edge_has_fewer_squares(self):
        """TC-08d | Spec: 'fewer on edges/corners.' Edge A4 must yield < 9 squares."""
        area = squares_in_3x3(chess.A4)
        assert len(area) < 9

    def test_freeze_area_includes_all_eight_neighbours(self):
        """TC-08e | All 8 surrounding squares of E4 must be in the area."""
        area = squares_in_3x3(chess.E4)
        neighbours = {
            chess.D3, chess.E3, chess.F3,
            chess.D4,           chess.F4,
            chess.D5, chess.E5, chess.F5,
        }
        for sq in neighbours:
            assert sq in area


# ================================================================== #
#  Freeze Spell — Effect                                             #
# ================================================================== #

class TestFreezeEffect:
    """Frozen pieces cannot be moved; the effect lasts exactly 1 of the opponent's turns."""

    def test_frozen_piece_excluded_from_legal_moves(self):
        """
        TC-09 | Spec: 'All opponent pieces whose square falls inside the frozen area
        cannot be moved on the opponent's next turn.'
        State set manually so Black's e7 pawn square is frozen.
        Expected: E7 absent from get_legal_moves() when it is Black's turn.
        """
        game = SpellChessGame()
        game.freeze_effect_color = chess.BLACK
        game.freeze_effect_squares = squares_in_3x3(chess.E7)
        game.freeze_effect_plies_left = 1
        game.board.turn = chess.BLACK
        legal_origins = {m.from_square for m in game.get_legal_moves()}
        assert chess.E7 not in legal_origins

    def test_freeze_effect_clears_after_frozen_side_moves(self):
        """
        TC-10 | Spec: 'Duration: the freeze lasts for exactly 1 of the opponent's turns.'
        Setup: Black is frozen with plies_left=1.
        Action: Black makes a move; after_move_pushed() is called.
        Expected: freeze_effect_color is None and plies_left == 0.
        """
        game = SpellChessGame()
        game.freeze_effect_color = chess.BLACK
        game.freeze_effect_squares = {chess.E7}
        game.freeze_effect_plies_left = 1
        game.board.turn = chess.BLACK
        game.board.push_san("d5")   # push directly to bypass make_move bugs
        game.after_move_pushed()
        assert game.freeze_effect_plies_left == 0
        assert game.freeze_effect_color is None

    def test_is_frozen_true_for_opponent_square_in_area(self):
        """
        TC-11 | is_frozen(sq, color) must return True when that color is frozen
        and sq is inside the frozen area.
        State is set manually to isolate from cast_freeze bugs.
        """
        game = SpellChessGame()
        game.freeze_effect_color = chess.BLACK
        game.freeze_effect_squares = squares_in_3x3(chess.E5)
        game.freeze_effect_plies_left = 1
        assert game.is_frozen(chess.E5, chess.BLACK) is True

    def test_is_frozen_false_for_caster_color(self):
        """TC-11b | is_frozen must return False for the caster's color (WHITE)."""
        game = SpellChessGame()
        game.freeze_effect_color = chess.BLACK
        game.freeze_effect_squares = squares_in_3x3(chess.E5)
        game.freeze_effect_plies_left = 1
        assert game.is_frozen(chess.E5, chess.WHITE) is False

# ================================================================== #
#  Jump Spell — Range                                                #
# ================================================================== #

class TestJumpRange:
    """A piece can jump up to 2 squares in any direction."""

    def test_jump_range_valid(self):
        """TC-12 | Spec: 'within Chebyshev distance 2'"""
        game = SpellChessGame()
        # White knight on b1 jumps to b3 (distance 2, unobstructed)
        # We need an empty square. b3 is empty.
        result = game.cast_jump(chess.B1, chess.B3)
        assert result is True

    def test_jump_range_invalid(self):
        """
        TC-13 | Spec: 'at most 2 squares in any direction'
        Expected: A jump of distance 3 should return False.
        DEFECT: squares_in_jump_range uses range(-3, 4) which allows distance 3.
        """
        game = SpellChessGame()
        # White rook on a1 jumps to a4 (distance 3). a4 is empty.
        result = game.cast_jump(chess.A1, chess.A4)
        assert result is False


# ================================================================== #
#  Jump Spell — Charges                                              #
# ================================================================== #

class TestJumpCharges:
    """Each side starts with 3 jump charges; each successful cast costs 1."""

    def test_jump_initial_charges_white(self):
        """TC-14 | Spec: 'Each side begins the game with 3 jump charges.' (White)"""
        game = SpellChessGame()
        assert game.jump_remaining[chess.WHITE] == 3

    def test_jump_decrements_charge_on_cast(self):
        """TC-15 | Spec: 'Each cast costs 1 charge.'"""
        game = SpellChessGame()
        game.cast_jump(chess.B1, chess.B3)
        assert game.jump_remaining[chess.WHITE] == 2

    def test_jump_blocked_at_zero_charges(self):
        """TC-16 | Spec: 'When a player has 0 charges remaining, they cannot cast Jump.'"""
        game = SpellChessGame()
        game.jump_remaining[chess.WHITE] = 0
        result = game.cast_jump(chess.B1, chess.B3)
        assert result is False


# ================================================================== #
#  Jump Spell — Cooldown                                             #
# ================================================================== #

class TestJumpCooldown:
    """After casting Jump the caster enters a 2-turn cooldown."""

    def test_jump_cooldown_set_to_two_after_cast(self):
        """
        TC-17 | Spec table: 'Jump cooldown after casting: 2 turns.'
        Expected: jump_cooldown[WHITE] == 2 immediately after cast.
        DEFECT: cast_jump sets cooldown to 1 instead of 2.
        """
        game = SpellChessGame()
        game.cast_jump(chess.B1, chess.B3)
        assert game.jump_cooldown[chess.WHITE] == 2

    def test_jump_blocked_while_on_cooldown(self):
        """TC-18 | Spec: 'The caster cannot cast Jump again until the cooldown reaches 0.'"""
        game = SpellChessGame()
        game.jump_cooldown[chess.WHITE] = 1
        result = game.cast_jump(chess.B1, chess.B3)
        assert result is False

    def test_jump_cooldown_decrements_on_caster_turn_start(self):
        """TC-19 | Spec: 'The cooldown decrements by 1 at the start of each of the caster's turns.'"""
        game = SpellChessGame()
        game.jump_cooldown[chess.WHITE] = 2
        game.board.turn = chess.WHITE
        game.on_turn_start()
        assert game.jump_cooldown[chess.WHITE] == 1


# ================================================================== #
#  Jump Spell — Once Per Turn                                        #
# ================================================================== #

class TestJumpOncePerTurn:
    """A player may cast Jump at most once per turn."""

    def test_jump_blocked_on_second_cast_same_turn(self):
        """TC-20 | Spec: 'A player may cast Jump once per turn.'"""
        game = SpellChessGame()
        game.cast_jump(chess.B1, chess.B3)
        # Try to jump another piece in the same turn
        result = game.cast_jump(chess.G1, chess.G3)
        assert result is False


# ================================================================== #
#  Jump Spell — Restrictions                                         #
# ================================================================== #

class TestJumpRestrictions:
    """Jump has restrictions: King cannot jump, destination must be empty, must be own piece."""

    def test_jump_king_is_blocked(self):
        """
        TC-21 | Spec: 'The King cannot be jumped — only non-King pieces may be selected.'
        Expected: Jumping the King returns False.
        DEFECT: cast_jump does not check if the piece is a King.
        """
        game = SpellChessGame()
        result = game.cast_jump(chess.E1, chess.E3)
        assert result is False

    def test_jump_destination_must_be_empty(self):
        """
        TC-22 | Spec: 'The piece can only land on an empty square — it cannot capture via Jump.'
        Expected: Jumping onto an occupied square returns False.
        DEFECT: cast_jump does not check if the destination square is empty.
        """
        game = SpellChessGame()
        # White rook on a1 jumps to a2 (occupied by White pawn)
        result = game.cast_jump(chess.A1, chess.A2)
        assert result is False

    def test_jump_must_be_own_piece(self):
        """TC-23 | Spec: 'player selects one of their own pieces'"""
        game = SpellChessGame()
        # White tries to jump Black's pawn on a7
        result = game.cast_jump(chess.A7, chess.A5)
        assert result is False

# ================================================================== #
#  New Game Reset                                                    #
# ================================================================== #

class TestNewGameReset:

# ================================================================== #
#  Move Lifecycle                                                    #
# ================================================================== #

class TestMoveLifecycle:

# ================================================================== #
#  Game State Display                                                #
# ================================================================== #

class TestGameStateDisplay:
