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

---

## Meeting 3 — Daily Stand-up #2

**Date:** Thursday, April 30, 2026  
**Time:** 8:00 PM – 8:20 PM  
**Location:** Google Meet  
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik

### Stand-up Updates

**Caleb Lee**
- *What did I do?* Completed all 12 Jump spell tests (TC-12 through TC-23) and `test_case_documentation.md` Module 2; confirmed D-07 (`squares_in_jump_range` uses `range(-3, 4)` allowing distance 3), D-08 (jump cooldown set to 1 not 2), D-09 (King not blocked), D-10 (no check that destination is empty)
- *What will I do?* Review Konrad's Freeze tests for consistency; help finalize defect descriptions for D-07 through D-10
- *What's not working?* Nothing blocking — all Jump tests committed

**Sophie Reznik**
- *What did I do?* Completed TC-24 through TC-34 display tests and Module 3 documentation; most display tests pass
- *What will I do?* Update sprint backlog statuses for T-08 through T-13; review all process docs for submission consistency
- *What's not working?* Nothing blocking

**Konrad Trestka**
- *What did I do?* Completed TC-08 through TC-11b (freeze area and effect tests); documented D-02 through D-06; drafted `test_scenario.md` with step-by-step procedure and V-01 through V-08 verification checks
- *What will I do?* Finalize `test_scenario.md` with defect traceability section; review defect descriptions with Nikita
- *What's not working?* Nothing blocking

**Nikita Tuli**
- *What did I do?* Completed TC-35 through TC-42 New Game Reset tests; confirmed D-11 (`new_game()` does not call `board.reset()`), D-12 (move stack not cleared), D-13 (`jump_remaining` not reset to 3)
- *What will I do?* Write TC-43 through TC-48 Move Lifecycle tests; draft test execution report structure
- *What's not working?* `make_move()` appears to double-flip `board.turn` after a move — will confirm with TC-43

### Scrum Master Notes

PB-01 (Freeze) and PB-02 (Jump) tests effectively complete. PB-03 in progress — Nikita on track to finish Move Lifecycle by Saturday. Sophie flagged that defect descriptions need consistent formatting before final commit.

---

## Meeting 4 — Daily Stand-up #3

**Date:** Saturday, May 2, 2026  
**Time:** 8:00 PM – 8:20 PM  
**Location:** Google Meet 
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik

### Stand-up Updates

**Caleb Lee**
- *What did I do?* Reviewed Nikita's New Game Reset tests and provided feedback; helped format defect descriptions for D-11 through D-13 in the defect summary table; final read-through of Module 2 documentation
- *What will I do?* Full read-through of `test_case_documentation.md` Modules 1 and 2 before Sprint Review Sunday
- *What's not working?* Nothing blocking

**Sophie Reznik**
- *What did I do?* Updated sprint backlog task statuses (T-01 through T-13 marked Completed); finalized meeting minutes through Meeting 3; verified all header dates are consistent across documents
- *What will I do?* Write Sprint Review notes after Sunday's meeting; do a final pass on all process artifacts for submission
- *What's not working?* Nothing blocking

**Konrad Trestka**
- *What did I do?* Finalized `test_scenario.md` including the defect traceability table (defects D-01, D-02, D-03, D-06 mapped to scenario steps); reviewed D-01 through D-10 descriptions for accuracy against `spell_logic.py`
- *What will I do?* Support Nikita on Move Lifecycle tests; review final defect summary once D-14 through D-16 are added
- *What's not working?* Nothing blocking

**Nikita Tuli**
- *What did I do?* Completed TC-43 through TC-48 Move Lifecycle tests; confirmed D-14 (`make_move()` does not flip `board.turn` correctly) and D-15 (check detection fails when chaining moves via `make_move()` because of D-14); added TC-49 en passant test stub (pending commit)
- *What will I do?* Finish TC-50 (pawn promotion); add D-14 through D-16 to defect summary; write test execution report
- *What's not working?* D-14 turn-flip bug makes chaining moves unreliable in TC-48 — using `board.push_san()` directly as a workaround in that test

### Scrum Master Notes

TC-49 and TC-50 identified as late-sprint additions covering edge cases missed in planning. All PB items on track for Sprint Review Sunday May 3. Nikita to commit TC-49/50 and the execution report by end of day Sunday.

---

## Meeting 5 — Sprint Review

**Date:** Sunday, May 3, 2026  
**Time:** 8:00 PM – 9:00 PM  
**Location:** Google Meet 
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik  
**Product Owner:** Konrad Trestka

### Sprint Goal Review

**Goal:** Write a comprehensive unit test suite for `spell_logic.py` (v0.5), identify all defects by comparing behavior against the specification in `README.md`, and produce complete Scrum process documentation by the Monday deadline.

**Outcome:** Goal met. 60 tests written across 5 modules (Freeze, Jump, Display, New Game Reset, Move Lifecycle). 16 unique defects identified and documented (D-01 through D-16). All Scrum process artifacts are complete or in final review.

### Completed Product Backlog Items

- **PB-01 — Freeze Spell Verification:** 20 tests (TC-01 through TC-11b); 6 defects found (D-01 through D-06). 8 of 20 tests expose implementation bugs; 12 pass.
- **PB-02 — Jump Spell Verification:** 12 tests (TC-12 through TC-23); 4 defects found (D-07 through D-10). 5 of 12 tests expose bugs; 7 pass.
- **PB-03 — New Game and Turn Lifecycle:** 28 tests (TC-24 through TC-50); 6 defects found (D-11 through D-16). 6 of 28 tests expose bugs; 22 pass.
- **PB-04 — Test Documentation and Process:** All artifacts complete — `test_case_documentation.md`, `test_execution_report.md`, `meeting_minutes.md`, `sprint_backlog.md`, `test_scenario.md`.

### New Product Backlog Items Created

None. The project scope is complete.

### Discussion

Team confirmed that all 19 test failures map cleanly to documented defects D-01 through D-16. The highest-impact defect is D-14 (`make_move()` turn-flip) because it cascades into TC-43 and TC-48 and makes multi-move test sequences unreliable. D-06 (center square excluded from freeze area) also cascades, causing TC-08, TC-08b, TC-09, and TC-11 to fail. Two demo tests provided with the assignment also fail — they cover the same root causes as D-01 and D-11.

---

## Meeting 6 — Sprint Retrospective

**Date:** Sunday, May 4, 2026  
**Time:** 9:00 PM – 9:45 PM  
**Location:** Google Meet 
**Attendees:** Caleb Lee, Sophie Reznik, Konrad Trestka, Nikita Tuli  
**Scrum Master:** Sophie Reznik

### What Went Well

- Dividing modules by person at the start of sprint planning allowed parallel development with no merge conflicts
- Writing tests strictly against the spec (before running them) kept everyone objective — defects emerged naturally from test failures rather than from code inspection
- Early stand-ups surfaced D-07 and D-11 before they could block other work
- Using separate git branches per module made the PR history traceable and kept reviews focused

### What Did Not Go Well

- The D-14 turn-flip bug in `make_move()` made chaining moves unreliable, forcing us to use `board.push_san()` as a workaround in several Move Lifecycle tests — this created inconsistency in test style across the file
- TC-49 (en passant) and TC-50 (pawn promotion) were discovered late on Saturday and had to be added in a last-minute commit; a more thorough review of the spec's edge-case sections during sprint planning would have caught these earlier
- Sprint backlog statuses were not updated in real time — they were backfilled at the end of the sprint, which reduced the board's value as a daily tracking tool

### Next Time Let's Try To...

- Update sprint backlog task statuses immediately after each task is completed rather than batching at the end of the sprint
- Include an explicit "spec edge case review" step during sprint planning to surface tests like TC-49 and TC-50 before they become last-minute additions
- Schedule a team-wide read-through of all test modules before the Sprint Review so every member understands the full defect picture, not just their own module
