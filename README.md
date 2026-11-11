# data-model-group-project
Group project for MSIN0143 Programming for Business Analytics (UCL, 2026/27).

**Deadline:** Wed 9 Dec 2026, 10:00 · **Internal submission target:** Tue 8 Dec

## Team
| Workstream | Owner | Reviewer | Notebook |
|---|---|---|---|
| W1 Data cleaning + feature engineering + integration | Xuan | Andrea | `notebooks/w1_data_cleaning.ipynb` |
| W2 EDA, visualisation + business framing (+ editing) | Andrea | Tomas | `notebooks/w2_eda.ipynb` |
| W3 Baseline model | Kana | Xuan | `notebooks/w3_baseline_model.ipynb` |
| W4 Advanced model + evaluation (+ PM) | Tomas | Kana | `notebooks/w4_advanced_model_evaluation.ipynb` |

Final submission: `final/group_coursework.ipynb` (merged by Xuan from 2 Dec).

## Structure
```
data/raw/         original dataset, never edited
data/processed/   outputs of the cleaning pipeline (not committed)
notebooks/        one notebook per workstream
final/            merged master notebook for submission
```

## Setup (once per person)
```bash
git clone https://github.com/tomas-trls/data-model-group-project.git
cd data-model-group-project
pip install -r requirements.txt
nbstripout --install
```
`nbstripout` removes notebook outputs on commit so merges don't conflict.

## Workflow
Every piece of work has a Trello ticket with a unique code, e.g. **[BA-0004]**.

1. Move your Trello card to **In Progress**.
2. Create a branch named after the code: `git checkout -b BA-0004-handle-missing-values`.
3. Open a pull request whose title **starts with the code**: `[BA-0004] Handle missing values`.
4. CI must pass and your review pair must approve before merging.
5. Merge, then move the Trello card to **Done**.
6. Never push directly to `main`.

## CI/CD (GitHub Actions)
| Check | When | What it does |
|---|---|---|
| **Ticket code in title** | every PR | Blocks the merge unless the title starts with `[BA-XXXX] ` |
| **Lint and run notebooks** | every PR + push to `main` | Flags syntax errors and undefined names, runs every notebook top to bottom, checks the final word count ≤ 3,000 (appendices excluded) |
| **Build submission** | push to `main` | Executes the final notebook and uploads the run `.ipynb` + HTML as a downloadable artifact |

Run the same checks locally before opening a PR:
```bash
pip install -r requirements-dev.txt
nbqa ruff notebooks final --select E9,F63,F7,F82
pytest --nbmake notebooks final
python scripts/word_count.py final/group_coursework.ipynb
```

## Key dates
| Date | Milestone |
|---|---|
| Sun 15 Nov | Dataset + business question |
| Sun 22 Nov | Cleaning + EDA |
| Sun 29 Nov | Features + both models |
| Wed 2 Dec | Code freeze |
| Fri 4 Dec | Model walkthrough |
| Sun 6 Dec | Full-team read-through |
| Tue 8 Dec | Submit on Moodle |

## Rules from the brief
- Max 3,000 words of markdown (tables, figures and captions count; code and code comments don't).
- AI use is **Assistive**: log every use on the Trello AI usage log card.
- References in Harvard **or** Vancouver, consistently.
