# pipeline_config.py
# ── All pipeline settings in one place ────────────────────────────────────
# Edit this file to configure the pipeline without touching run_pipeline.py

import os

# ── Paths ──────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE        = os.path.join(BASE_DIR, "inputs", "new_export.xlsx")
INPUT_SHEET       = "Sheet"

MASTER_FILE       = os.path.join(BASE_DIR, "data", "master.xlsx")
PROCESSED_IDS     = os.path.join(BASE_DIR, "data", "processed_ids.csv")
TAGS_FILE         = os.path.join(BASE_DIR, "data", "tags.csv")
MANUAL_TAGS_FILE  = os.path.join(BASE_DIR, "data", "manuallytagged_complete.csv")

MODELS_DIR        = os.path.join(BASE_DIR, "models")
SVM_MODEL         = os.path.join(MODELS_DIR, "svm_final_model.pkl")
SVM_ENCODER       = os.path.join(MODELS_DIR, "svm_final_label_encoder.pkl")

OUTPUTS_LATEST    = os.path.join(BASE_DIR, "outputs", "latest")
OUTPUTS_ARCHIVE   = os.path.join(BASE_DIR, "outputs", "archive")
LOGS_DIR          = os.path.join(BASE_DIR, "logs")

# ── Column names ───────────────────────────────────────────────────────────
COL_RESPONDENT_ID = "Respondent ID"
COL_FEEDBACK      = "Feedback"
COL_FEEDBACK_CLEAN = "Feedback_clean"
COL_RATING        = "Rating"
COL_DATE          = "Start Date"
COL_FEEDBACK = "Is there anything you would like to tell us about your experience?"
COL_FEEDBACK_CLEAN = "Feedback_clean"

# ── SVM settings ───────────────────────────────────────────────────────────
EMBEDDING_MODEL   = "all-mpnet-base-v2"
MIN_SAMPLES       = 8
SVM_C             = 5
PRIMARY_THRESHOLD   = 0.3
SECONDARY_THRESHOLD = 0.15

# ── ABSA settings ──────────────────────────────────────────────────────────
ABSA_MODEL        = "yangheng/deberta-v3-base-absa-v1.1"
ABSA_MIN_WORDS    = 2       # skip reviews shorter than this
ABSA_MAX_ASPECTS  = 3       # max aspects to check per review

# ── Summarisation settings ─────────────────────────────────────────────────
SUMMARY_MODEL     = "facebook/bart-large-cnn"
SUMMARY_MIN_REVIEWS = 5     # minimum reviews per group to summarise
SUMMARY_MAX_REVIEWS = 80    # sample size for large groups

# ── Entity extraction settings ─────────────────────────────────────────────
SPACY_MODEL       = "en_core_web_sm"
MIN_ENTITY_COUNT  = 3       # minimum mentions to include in aggregations

# ── Output settings ────────────────────────────────────────────────────────
AUDIENCE_OUTPUTS = {
    "research":    ["master", "entities", "absa_detail"],
    "product":     ["summaries", "entity_analysis", "priority_matrix"],
    "leadership":  ["executive_summary"],
}