# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
한양대 MBA 2025년 9월 학기 통합 저장소. 4개 과목의 과제와 프로젝트를 관리하며, 각 과목별로 체계적인 폴더 구조를 유지합니다.

## Common Commands

### Environment Setup
```bash
# Virtual environment activation (always required)
# Windows
venv\Scripts\activate
# Mac/Linux  
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jupyter Notebook
jupyter notebook
```

### Testing
```bash
# Run tests if available
pytest
pytest --cov=.
```

### Git Workflow
```bash
git add .
git commit -m "작업 내용 설명"
git push origin main
```

## Architecture

### Course Structure
Each course follows the same pattern:
- `01_assignments/` - 과제 (assignments)
- `0X_[specific_folders]/` - Course-specific analysis folders
- `08_resources/` - 참고 자료 (reference materials)

### Key Technology Stack by Course

**01_Marketing_Management_A**: Web scraping (requests, beautifulsoup4, selenium, scrapy, playwright), data analysis (pandas, numpy), visualization (matplotlib, seaborn, plotly), AI/ML (openai, transformers, langchain)

**02_Business_Strategy**: Strategic analysis frameworks (pandas, numpy, scipy), data validation (pydantic, cerberus), visualization for frameworks like Porter's 5 Forces and SWOT (plotly, networkx), document generation (python-pptx, python-docx)

**03_Digital_Business_Model_and_New_Business_Development**: MVP development (streamlit, gradio, fastapi), prototyping (flask, django), design thinking visualization (matplotlib, seaborn), AI-powered ideation (openai, langchain)

**04_Smart_IT_Service**: Web/app development (flask, fastapi, streamlit, django, uvicorn), databases (pymongo, sqlalchemy, redis), machine learning (transformers), API development (httpx, pydantic), testing (pytest, pytest-cov)

### Data Files
- Business model data structures are defined in `03_Digital_Business_Model_and_New_Business_Development/01_assignments/business_model_data.py`
- Contains templates for Business Model Canvas, Design Thinking process, MVP development, and presentation structures

### Shared Resources
- `shared_resources/` - Common assets across courses
- `collaboration_tools/` - Team collaboration utilities
- `requirements.txt` - Comprehensive Python package list with version specifications