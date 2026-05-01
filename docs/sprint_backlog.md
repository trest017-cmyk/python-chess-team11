# Sprint Backlog — Spell Chess P4 Sprint

**Team 11** | Lee, Reznik, Trestka, Tuli  
**Sprint Dates:** April 27 – May 4, 2026  
**Scrum Master:** Sophie Reznik  
**Product Owner:** Konrad Trestka

---

## Sprint Goal

Write a comprehensive unit test suite for `spell_logic.py` (v0.5), identify all defects
by comparing behavior against the specification in `README.md`, and produce complete
Scrum process documentation by the Monday deadline.

---

## Sprint Backlog

Tasks are derived from Product Backlog items PB-01 through PB-04.
Each task has a clear definition of done (DoD) and a status.

---

### From PB-01: Freeze Spell Verification

| Task ID | Description | Assignee | DoD | Status |
|---------|-------------|----------|-----|--------|
| T-01 | Write TC-01 — freeze targets opponent, not caster | Konrad Trestka | Test in `test_spell_logic.py`; case documented in Module 1 | Completed |
| T-02 | Write TC-02, TC-03a–d — freeze charge behavior | Konrad Trestka | Tests pass or fail with documented defect; case documented | Completed |
| T-03 | Write TC-04, TC-05, TC-05b, TC-06 — freeze cooldown | Konrad Trestka | Tests pass or fail with documented defect; case documented | Completed |
| T-04 | Write TC-07 — freeze once per turn | Konrad Trestka | Test in `test_spell_logic.py`; case documented | Completed |
| T-05 | Write TC-08, TC-08b–e — freeze area (squares_in_3x3) | Konrad Trestka | Tests pass or fail with documented defect; case documented | Completed |
| T-06 | Write TC-09, TC-10, TC-11, TC-11b — freeze effect and is_frozen | Konrad Trestka | Tests pass or fail with documented defect; case documented | Completed |
| T-07 | Write test scenario TS-01 end-to-end | Konrad Trestka | `docs/test_scenario.md` complete with steps, checks, and defect table | In Progress |

---

### From PB-02: Jump Spell Verification

| Task ID | Description | Assignee | DoD | Status |
|---------|-------------|----------|-----|--------|
| T-08 | Write TC-12, TC-13 — jump range (squares_in_jump_range) | Caleb Lee | Tests pass or fail with documented defect; case documented | Completed |
| T-09 | Write TC-14, TC-15, TC-16 — jump charge behavior | Caleb Lee | Tests pass or fail with documented defect; case documented | Completed |
| T-10 | Write TC-17, TC-18, TC-19 — jump cooldown | Caleb Lee | Tests pass or fail with documented defect; case documented | Completed |
| T-11 | Write TC-20 — jump once per turn | Caleb Lee | Test in `test_spell_logic.py`; case documented | Completed |
| T-12 | Write TC-21, TC-22, TC-23 — jump restrictions (king, empty dest, own piece) | Caleb Lee | Tests pass or fail with documented defect; case documented | Completed |

---

### From PB-03: New Game and Turn Lifecycle

| Task ID | Description | Assignee | DoD | Status |
|---------|-------------|----------|-----|--------|
| T-13 | Write TC-24 through TC-34 — game state display methods | Sophie Reznik | Tests in `test_spell_logic.py`; Module 3 documented | Completed |
| T-14 | Write TC-35 through TC-42 — new_game() reset behavior | Nikita Tuli | Tests in `test_spell_logic.py`; Module 4 documented | Completed |
| T-15 | Write TC-43 through TC-50 — make_move() lifecycle | Nikita Tuli | Tests in `test_spell_logic.py`; Module 5 documented | In Progress |
| T-16 | Compile defect summary table (D-01 through D-16) | Nikita Tuli | Defect table appended to `docs/test_case_documentation.md` | In Progress |

---

### From PB-04: Test Documentation and Process

| Task ID | Description | Assignee | DoD | Status |
|---------|-------------|----------|-----|--------|
| T-17 | Write and maintain meeting minutes for all 6 meetings | Sophie Reznik | `docs/meeting_minutes.md` complete with all 6 meetings | Not Started |
| T-18 | Maintain sprint backlog throughout sprint | Sophie Reznik | `docs/sprint_backlog.md` up-to-date with final statuses | Not Started |
| T-19 | Write test execution report | Nikita Tuli | `docs/test_execution_report.md` complete with pytest output and failure analysis | Not Started |

---

## Initial State (April 27 — Sprint Start)

| PB Item | Tasks | Not Started | In Progress | Completed |
|---------|-------|-------------|-------------|-----------|
| PB-01 (Freeze Verification) | 7 | 7 | 0 | 0 |
| PB-02 (Jump Verification) | 5 | 5 | 0 | 0 |
| PB-03 (New Game / Move) | 4 | 4 | 0 | 0 |
| PB-04 (Documentation / Process) | 3 | 3 | 0 | 0 |
| **Total** | **19** | **19** | **0** | **0** |

## Final State (May 4 — Sprint End)

| PB Item | Tasks | Not Started | In Progress | Completed |
|---------|-------|-------------|-------------|-----------|
| PB-01 (Freeze Verification) | 7 | — | — | — |
| PB-02 (Jump Verification) | 5 | — | — | — |
| PB-03 (New Game / Move) | 4 | — | — | — |
| PB-04 (Documentation / Process) | 3 | — | — | — |
| **Total** | **19** | **—** | **—** | **—** |
