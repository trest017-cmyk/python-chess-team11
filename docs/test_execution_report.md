# Test Execution Report — Spell Chess P4

**Team 11** | Lee, Reznik, Trestka, Tuli  
**Date of execution:** May 3, 2026  
**Command:** `pytest test_spell_logic.py -v`  
**Python:** 3.14.3 | **pytest:** 9.0.3  
**System under test:** `spell_logic.py` version 0.5

---

## Summary

| Total Tests | Passed | Failed | Pass Rate |
|-------------|--------|--------|-----------|
| 60 | 41 | 19 | 68.3% |

---

## Full Output

```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/konradtrestka/python-chess-team11
collected 60 items

test_spell_logic.py::TestFreezeTarget::test_freeze_affects_opponent_not_caster FAILED
test_spell_logic.py::TestNewGameResetsBoard::test_board_resets_after_moves FAILED
test_spell_logic.py::TestFreezeCharges::test_freeze_initial_charges_white PASSED
test_spell_logic.py::TestFreezeCharges::test_freeze_initial_charges_black PASSED
test_spell_logic.py::TestFreezeCharges::test_freeze_decrements_charge_on_cast FAILED
test_spell_logic.py::TestFreezeCharges::test_freeze_blocked_at_zero_charges PASSED
test_spell_logic.py::TestFreezeCharges::test_freeze_returns_true_on_success PASSED
test_spell_logic.py::TestFreezeCooldown::test_freeze_cooldown_set_to_three_after_cast FAILED
test_spell_logic.py::TestFreezeCooldown::test_freeze_blocked_while_on_cooldown PASSED
test_spell_logic.py::TestFreezeCooldown::test_freeze_cooldown_decrements_on_caster_turn_start FAILED
test_spell_logic.py::TestFreezeCooldown::test_freeze_can_cast_after_cooldown_zero PASSED
test_spell_logic.py::TestFreezeOncePerTurn::test_freeze_blocked_on_second_cast_same_turn PASSED
test_spell_logic.py::TestFreezeArea::test_freeze_area_includes_center_square FAILED
test_spell_logic.py::TestFreezeArea::test_freeze_area_has_nine_squares_for_interior_center FAILED
test_spell_logic.py::TestFreezeArea::test_freeze_area_corner_has_fewer_squares PASSED
test_spell_logic.py::TestFreezeArea::test_freeze_area_edge_has_fewer_squares PASSED
test_spell_logic.py::TestFreezeArea::test_freeze_area_includes_all_eight_neighbours PASSED
test_spell_logic.py::TestFreezeEffect::test_frozen_piece_excluded_from_legal_moves FAILED
test_spell_logic.py::TestFreezeEffect::test_freeze_effect_clears_after_frozen_side_moves PASSED
test_spell_logic.py::TestFreezeEffect::test_is_frozen_true_for_opponent_square_in_area FAILED
test_spell_logic.py::TestFreezeEffect::test_is_frozen_false_for_caster_color PASSED
test_spell_logic.py::TestJumpRange::test_jump_range_valid PASSED
test_spell_logic.py::TestJumpRange::test_jump_range_invalid FAILED
test_spell_logic.py::TestJumpCharges::test_jump_initial_charges_white PASSED
test_spell_logic.py::TestJumpCharges::test_jump_decrements_charge_on_cast PASSED
test_spell_logic.py::TestJumpCharges::test_jump_blocked_at_zero_charges PASSED
test_spell_logic.py::TestJumpCooldown::test_jump_cooldown_set_to_two_after_cast FAILED
test_spell_logic.py::TestJumpCooldown::test_jump_blocked_while_on_cooldown PASSED
test_spell_logic.py::TestJumpCooldown::test_jump_cooldown_decrements_on_caster_turn_start PASSED
test_spell_logic.py::TestJumpOncePerTurn::test_jump_blocked_on_second_cast_same_turn PASSED
test_spell_logic.py::TestJumpRestrictions::test_jump_king_is_blocked FAILED
test_spell_logic.py::TestJumpRestrictions::test_jump_destination_must_be_empty FAILED
test_spell_logic.py::TestJumpRestrictions::test_jump_must_be_own_piece PASSED
test_spell_logic.py::TestNewGameReset::test_board_resets_to_starting_position FAILED
test_spell_logic.py::TestNewGameReset::test_turn_resets_to_white PASSED
test_spell_logic.py::TestNewGameReset::test_move_history_cleared_after_reset FAILED
test_spell_logic.py::TestNewGameReset::test_freeze_state_reset PASSED
test_spell_logic.py::TestNewGameReset::test_freeze_charges_reset PASSED
test_spell_logic.py::TestNewGameReset::test_jump_charges_reset FAILED
test_spell_logic.py::TestNewGameReset::test_cooldowns_reset PASSED
test_spell_logic.py::TestNewGameReset::test_spell_cast_flags_reset PASSED
test_spell_logic.py::TestMoveLifecycle::test_move_switches_turn FAILED
test_spell_logic.py::TestMoveLifecycle::test_move_updates_board_state PASSED
test_spell_logic.py::TestMoveLifecycle::test_illegal_move_rejected PASSED
test_spell_logic.py::TestMoveLifecycle::test_cannot_move_opponent_piece PASSED
test_spell_logic.py::TestMoveLifecycle::test_move_history_exists_after_move PASSED
test_spell_logic.py::TestMoveLifecycle::test_check_state_detected FAILED
test_spell_logic.py::TestMoveLifecycle::test_en_passant_execution FAILED
test_spell_logic.py::TestMoveLifecycle::test_pawn_promotion PASSED
test_spell_logic.py::TestGameStateDisplay::test_status_text_shows_white_turn_at_start PASSED
test_spell_logic.py::TestGameStateDisplay::test_status_text_shows_black_turn PASSED
test_spell_logic.py::TestGameStateDisplay::test_status_text_shows_check PASSED
test_spell_logic.py::TestGameStateDisplay::test_status_text_shows_checkmate_game_over PASSED
test_spell_logic.py::TestGameStateDisplay::test_freeze_info_text_initial_white PASSED
test_spell_logic.py::TestGameStateDisplay::test_freeze_info_text_shows_cooldown PASSED
test_spell_logic.py::TestGameStateDisplay::test_freeze_info_text_shows_frozen_area_message PASSED
test_spell_logic.py::TestGameStateDisplay::test_jump_info_text_initial_white PASSED
test_spell_logic.py::TestGameStateDisplay::test_jump_info_text_shows_cooldown PASSED
test_spell_logic.py::TestGameStateDisplay::test_shows_stalemate_draw PASSED
test_spell_logic.py::TestGameStateDisplay::test_shows_black_checkmate_win PASSED

======================== 19 failed, 41 passed in 0.21s =========================
```

---

## Failed Tests — Key Failure Messages

| TC ID | Test | Failure Message |
|-------|------|-----------------|
| TC-01 (demo) | `TestFreezeTarget::test_freeze_affects_opponent_not_caster` | `assert chess.WHITE == chess.BLACK` — `freeze_effect_color` is caster (WHITE), not opponent → D-01 |
| TC-35 (demo) | `TestNewGameResetsBoard::test_board_resets_after_moves` | FEN after reset does not match `chess.STARTING_FEN` → D-11 |
| TC-02 | `test_freeze_decrements_charge_on_cast` | `assert 5 == 4` — charge count unchanged after cast → D-02 |
| TC-04 | `test_freeze_cooldown_set_to_three_after_cast` | `assert 2 == 3` — cooldown set to 2 instead of 3 → D-03 |
| TC-06 | `test_freeze_cooldown_decrements_on_caster_turn_start` | `assert 3 == 2` — `on_turn_start()` does not decrement freeze cooldown → D-04 |
| TC-08 | `test_freeze_area_includes_center_square` | `assert chess.E4 in area` — center square absent from returned set → D-06 |
| TC-08b | `test_freeze_area_has_nine_squares_for_interior_center` | `assert 8 == 9` — only 8 squares returned (center excluded) → D-06 |
| TC-09 | `test_frozen_piece_excluded_from_legal_moves` | `assert chess.E7 not in legal_origins` — E7 still present in legal moves → D-01 + D-06 |
| TC-11 | `test_is_frozen_true_for_opponent_square_in_area` | `assert False is True` — `is_frozen()` returns False for frozen square → D-01 + D-06 |
| TC-13 | `test_jump_range_invalid` | `assert True is False` — distance-3 jump accepted; `squares_in_jump_range` uses range(-3,4) → D-07 |
| TC-17 | `test_jump_cooldown_set_to_two_after_cast` | `assert 1 == 2` — jump cooldown set to 1 instead of 2 → D-08 |
| TC-21 | `test_jump_king_is_blocked` | `assert True is False` — King jump accepted; no King check in `cast_jump` → D-09 |
| TC-22 | `test_jump_destination_must_be_empty` | `assert True is False` — jump onto occupied square accepted → D-10 |
| TC-35 | `test_board_resets_to_starting_position` | FEN after `new_game()` does not match `chess.STARTING_FEN` → D-11 |
| TC-37 | `test_move_history_cleared_after_reset` | `assert len(move_stack) == 0` — move stack not cleared by `new_game()` → D-12 |
| TC-40 | `test_jump_charges_reset` | `assert 0 == 3` — `jump_remaining` not reset by `new_game()` → D-13 |
| TC-43 | `test_move_switches_turn` | `assert True == False` — turn remains WHITE after `make_move(E2, E4)` → D-14 |
| TC-48 | `test_check_state_detected` | `assert False` — board not in check after Scholar's mate via `make_move()` (cascades from D-14) → D-15 |
| TC-49 | `test_en_passant_execution` | `assert False is True` — en passant move rejected as illegal by `make_move()` → D-16 |
