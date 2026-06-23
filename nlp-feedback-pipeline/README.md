# NLP Feedback Analysis Pipeline

Automated Python pipeline processing 50+ daily user feedback responses, combining 
topic modelling, sentiment analysis, and entity extraction to surface insights 
at scale.

## Overview

At TerraQuest, we collect ~50 user feedback responses daily across multiple 
product lines. Manually synthesising 200+ monthly responses took 3-4 days. 
This pipeline automates that process, enabling real-time insights.

## The Problem

- **Volume**: 50+ daily responses across products
- **Complexity**: Each response has ratings + qualitative comments
- **Latency**: 3-4 day manual synthesis meant insights arrived after priorities shifted
- **Bottleneck**: Research became a constraint, not an accelerator

## The Solution

Built an automated pipeline processing feedback through:

### 1. **Topic Modelling**
Identify what users are talking about most (e.g., "supporting documents" 
in 40% of feedback)

### 2. **Multi-Label Classification (SVM)**
Tag each response with 1-3 relevant categories
- Uses scikit-learn SVM with keyword boosting
- Handles multi-issue feedback intelligently

### 3. **Aspect-Based Sentiment Analysis**
Understand *why* feedback matters, not just sentiment polarity
- Uses DeBERTa v3 model
- Pairs sentiment with specific features/products

### 4. **Entity Extraction**
Flag which products/features/systems mentioned
- Uses spaCy + regex patterns
- Enables cross-product pattern detection

### 5. **Automated Summarisation**
Condense key points for different audiences
- Researchers: full detail
- Product: prioritised by impact
- Leadership: trends

### 6. **Database & Reporting**
- SQLite backend for structured data storage
- Monthly dashboards tailored to different audiences
- Searchable insight repository in Dovetail

## Impact

| Metric | Result |
|--------|--------|
| Actionable insights increase | 3x |
| User satisfaction improvement | 22% (56% → 68% NSAT) |
| Synthesis time reduction | 3-4 days → automated daily |
| Coverage | 50 responses/day, 100% tagged |

## Technical Stack

- **Language**: Python 3.9+
- **ML/NLP**: scikit-learn (SVM), transformers (DeBERTa v3), spaCy
- **Data**: SQLite
- **Dashboards**: Chart.js, Streamlit
- **Data source**: SurveyMonkey exports

## Project Structure
