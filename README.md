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
1. Pick up your Trello card and move it to **In Progress**.
2. Work on a branch: `git checkout -b w2-eda-correlations`.
3. Open a pull request using the template; your review pair approves it.
4. Merge, then move the Trello card to **Done**.
5. Never push directly to `main`.

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
