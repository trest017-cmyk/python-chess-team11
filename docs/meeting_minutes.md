# Meeting Minutes — Spell Chess P4 Sprint

**Team 11** | Lee, Reznik, Trestka, Tuli  
**Sprint:** P4 Bug Verification (April 27 – May 4, 2026)

---

## Meeting 1 — Sprint Planning

**Date:** Monday, April 27, 2026  
**Time:** 8:00 PM – 9:45 PM  
**Location:** Google Meet 
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik  
**Product Owner:** Konrad Trestka

### Items Discussed

- Read through the P4 assignment brief together; confirmed two deliverable tracks: Functional (unit tests) and Process (Scrum artifacts)
- Read the `README.md` spec in full; identified five major areas to test: Freeze spell, Jump spell, new_game reset, move lifecycle, and display methods
- Read through `spell_logic.py` together; spotted several obvious issues on first pass (wrong color stored for freeze effect, no board reset in new_game)
- Discussed the "How to Document Test Cases" example format; agreed to use a markdown table in `docs/test_case_documentation.md`
- Defined roles: Konrad = Product Owner, Sophie = Scrum Master, Caleb and Nikita = primary testers

### Product Backlog Items Defined

- **PB-01** — Freeze Spell Verification (5 pts, High priority): verify cast_freeze behavior, charges, cooldown, 3×3 area, and freeze effect
- **PB-02** — Jump Spell Verification (3 pts, High priority): verify cast_jump range, charges, cooldown, King restriction, empty destination
- **PB-03** — New Game and Turn Lifecycle (3 pts, High priority): verify new_game() reset and make_move() behavior including en passant
- **PB-04** — Test Documentation and Process (5 pts, Medium priority): meeting minutes, sprint backlog, test scenarios, execution report

### Sprint Backlog Populated

- **T-01 through T-07** (Freeze tests + TS-01 scenario) → Konrad Trestka
- **T-08 through T-12** (Jump spell tests TC-12 through TC-23) → Caleb Lee
- **T-13** (Display tests TC-24 through TC-34) → Sophie Reznik
- **T-14 through T-16** (New Game + Move Lifecycle tests TC-35 through TC-50; defect table) → Nikita Tuli
- **T-17, T-18** (Meeting minutes, sprint backlog) → Sophie Reznik
- **T-19** (Test execution report) → Nikita Tuli

### Actions

- **Everyone:** Install python-chess and pytest; read through `spell_logic.py` v0.5 fully before the next stand-up
- **Caleb + Nikita:** Begin writing test stubs for assigned modules before Tuesday
- **Sophie:** Draft sprint backlog structure and meeting minutes template; start reviewing display methods in `spell_logic.py`
- **Konrad:** Finalize product backlog entries in `docs/product_backlog.md`; begin writing Freeze spell test stubs (TC-01 through TC-07)

---

## Meeting 2 — Daily Stand-up #1

**Date:** Tuesday, April 28, 2026  
**Time:** 8:00 PM – 8:15 PM  
**Location:** Google Meet 
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik

### Stand-up Updates

**Caleb Lee**
- *What did I do?* Set up test environment; read through Jump spell section of the spec and `spell_logic.py`; wrote test stubs for TC-12 through TC-16
- *What will I do?* Complete TC-17 through TC-23; document Module 2 cases in `test_case_documentation.md`
- *What's not working?* Noticed `squares_in_jump_range` uses `range(-3, 4)` which allows Chebyshev distance 3 — suspect D-07; will confirm with a test

**Sophie Reznik**
- *What did I do?* Created `meeting_minutes.md` skeleton and `sprint_backlog.md` table structure; reviewed `status_text`, `freeze_info_text`, and `jump_info_text` in `spell_logic.py`
- *What will I do?* Write TC-24 through TC-34 test methods; fill in Module 3 documentation
- *What's not working?* Nothing blocking

**Konrad Trestka**
- *What did I do?* Finalized product backlog PB-01 through PB-04 in `docs/`; drafted TC-01 through TC-07 test stubs; confirmed D-01 — `freeze_effect_color` is set to the caster's color instead of the opponent's
- *What will I do?* Complete TC-08 through TC-11b (freeze area and effect tests); draft `test_scenario.md` outline
- *What's not working?* Nothing blocking

**Nikita Tuli**
- *What did I do?* Set up test environment; read spec and `spell_logic.py` in full; started stubs for TC-35 through TC-37
- *What will I do?* Finish New Game Reset tests TC-35 through TC-42; start Move Lifecycle stubs
- *What's not working?* `new_game()` appears not to call `board.reset()` — will confirm with TC-35

### Scrum Master Notes

All members on track. Caleb and Nikita have flagged potential D-07 and D-11 early. Next stand-up Thursday April 30.
