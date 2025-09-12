# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
한양대 MBA 2025년 9월 학기 통합 저장소. 4개 과목의 과제와 프로젝트를 관리하며, 각 과목별로 체계적인 폴더 구조를 유지합니다.

## Common Commands

### Environment Setup
```bash
# Virtual environment activation (always required before any Python work)
# Windows
venv\Scripts\activate
# Mac/Linux  
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Jupyter Notebook (for data analysis tasks)
jupyter notebook
```

### Testing
```bash
# Run tests if available
pytest
# With coverage report
pytest --cov=.
```

### Code Quality
```bash
# Run linting (if configured)
python -m pylint *.py
# Type checking (if mypy is configured)
python -m mypy *.py
```

### Git Workflow
```bash
# Check status before committing
git status
# Stage and commit changes
git add .
git commit -m "과목명: 작업 내용 설명"
git push origin main
```

## Architecture

### Course Structure
Each course follows a consistent folder pattern:
- `01_assignments/` - 과제 submissions and work
- `02-07_[topic_folders]/` - Course-specific content areas
- `08_resources/` - Reference materials and documentation

### Key Technology Stack by Course

**01_Marketing_Management_A**
- Web scraping: requests, beautifulsoup4, selenium, scrapy, playwright
- Data analysis: pandas==2.3.2, numpy==2.3.2
- Visualization: matplotlib, seaborn, plotly
- AI/ML: openai==1.55.3, transformers==4.46.3, langchain==0.3.9

**02_Business_Strategy**
- Strategic frameworks: pandas, numpy, scipy==1.14.1
- Data validation: pydantic==2.10.2, cerberus==1.3.5
- Visualization: plotly==5.24.1, networkx==3.4.2 (for strategic diagrams)
- Document generation: python-pptx==1.0.2, python-docx==1.1.2

**03_Digital_Business_Model_and_New_Business_Development**
- MVP tools: streamlit==1.39.0, gradio==5.8.0, fastapi==0.115.5
- Prototyping: flask==3.1.0, django==5.1.3
- Visualization: matplotlib, seaborn
- AI ideation: openai, langchain

**04_Smart_IT_Service**
- Web/app: flask, fastapi, streamlit, django, uvicorn==0.32.1
- Databases: pymongo==4.10.1, sqlalchemy==2.0.36, redis==5.2.1
- ML: transformers
- API: httpx==0.28.1, pydantic
- Testing: pytest==8.3.4, pytest-cov==6.0.0

### Important Data Files
- Business model templates: `03_Digital_Business_Model_and_New_Business_Development/01_assignments/business_model_data.py`
  - Contains: BUSINESS_MODEL_CANVAS, DESIGN_THINKING, MVP_DEVELOPMENT structures
  - Use these data structures when creating business model analyses

### Working with Course Assignments

#### Marketing Analysis Tasks
```python
# Common pattern for web scraping and analysis
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Use existing scraped data in 01_Marketing_Management_A/03_market_analysis/
```

#### Business Strategy Frameworks
```python
# Use networkx for strategic diagrams
import networkx as nx
import plotly.graph_objects as go

# Reference existing analyses in 02_Business_Strategy/02_strategic_analysis/
```

#### MVP Development
```python
# Use Streamlit for quick prototypes
import streamlit as st

# Templates in 03_Digital_Business_Model/04_mvp_development/
```

### Shared Resources
- `shared_resources/` - Common assets across all courses
- `collaboration_tools/` - Team collaboration utilities
- `requirements.txt` - All Python dependencies with specific versions (last updated: 2025-09)

## Course-Specific Notes

### Quiz Management (02_Business_Strategy) - 16 Week Course
- **Quiz Structure**: Weekly quizzes for 16 weeks (exam preparation)
- Quiz images stored in: `02_Business_Strategy/09_quizzes/week_XX/quiz_questions/`
- Answer files: 
  - `02_Business_Strategy/09_quizzes/week_XX/quiz_answers.md`
  - `02_Business_Strategy/09_quizzes/week_XX/quiz_complete_analysis_bilingual.md` (Korean + Traditional Chinese)
- Quiz helper script: `02_Business_Strategy/quiz_helper.py`
- Course tracker: `02_Business_Strategy/COURSE_TRACKER.md`

#### Quiz Processing Workflow
1. Save quiz screenshots to `week_XX/quiz_questions/`
2. Use Claude to analyze images and extract questions
3. Generate bilingual answers (Korean/Traditional Chinese)
4. Track progress in COURSE_TRACKER.md

#### Quick Commands for Business Strategy
```python
# Run quiz helper script
python 02_Business_Strategy/quiz_helper.py

# Process quiz images with Claude
# Use Read tool on multiple images in quiz_questions folder
# Generate bilingual analysis for better understanding
```

### Market Analysis (01_Marketing_Management_A)
- Competitor analyses in: `01_Marketing_Management_A/03_market_analysis/competitor_analysis/`
- Example: `coffee_industry_analysis_2025.md` with source links

### Digital Business Models (03_Digital_Business_Model)
- Business model canvas analysis: `08_resources/business_model_canvas_analysis_final.md`
- Project progress tracking: `project_progress_report.md`

## Development Workflow

### For Data Analysis Tasks
1. Always activate virtual environment first
2. Check for existing datasets in `*/05_data_analysis/datasets/`
3. Use Jupyter notebooks for exploratory work
4. Save final scripts to `*/05_data_analysis/python_scripts/`

### For Web Scraping Tasks
1. Check `robots.txt` and terms of service
2. Use existing scraping patterns from course folders
3. Save raw data to appropriate `datasets/` folder
4. Document sources in accompanying `.txt` or `.md` files

### For MVP/Prototype Development
1. Start with Streamlit for quick prototypes
2. Use templates from `business_model_data.py`
3. Deploy test versions before final submission
4. Document user testing in `04_mvp_development/user_testing/`

## Business Strategy Course Management

### Quiz Management (16-week course)
```bash
# Run quiz analyzer tool
cd "02_Business_Strategy"
python quiz_analyzer.py

# Create new week structure
python -c "from quiz_analyzer import QuizAnalyzer; QuizAnalyzer().create_week_structure([week_number])"
```

### Quiz Analysis Workflow
1. **Quiz Image Capture**: Save screenshots to `09_quizzes/week_XX/quiz_questions/`
2. **Quiz Analysis**: Use Claude to analyze images and extract questions
3. **Answer Documentation**: Create detailed analysis in `quiz_complete_analysis.md`
4. **Study Notes**: Update course tracker and create study materials

### Article Reading Management
- Track all articles in `ARTICLE_TRACKER.md`
- Save article summaries in `08_resources/articles/week_XX/`
- Use article summary template for consistent note-taking

### Team Project Structure
```
07_team_projects/
├── TEAM_PROJECT_MANAGER.md     # Main project management file
├── 01_research/                # Research materials
├── 02_analysis/               # Framework analysis (SWOT, Porter's 5 Forces)  
├── 03_presentation/           # PPT and presentation materials
└── 04_meetings/              # Meeting notes and action items
```

### Key Strategic Analysis Tools
```python
# Porter's Five Forces visualization
import networkx as nx
import plotly.graph_objects as go

# SWOT Matrix creation  
import pandas as pd
import matplotlib.pyplot as plt

# Business Model Canvas
# Use data structures from business_model_data.py
```

### Business Strategy Course Files
- **Course Progress**: `COURSE_TRACKER.md` (16-week overview)
- **Quiz System**: `quiz_analyzer.py` (automated quiz management)
- **Article Tracker**: `ARTICLE_TRACKER.md` (reading assignments)
- **Team Projects**: `TEAM_PROJECT_MANAGER.md` (collaboration tool)

### Weekly Study Routine
1. Pre-class: Read assigned articles and create summaries
2. During class: Take notes and identify quiz-worthy concepts
3. Post-class: Complete quiz analysis and update progress trackers
4. Weekly review: Update course tracker and prepare for next week