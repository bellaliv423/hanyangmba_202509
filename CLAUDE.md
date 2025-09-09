# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This appears to be a new Python project repository for "hanyangmba_202509". The repository is currently empty except for a basic README.md file.

## Development Setup
가상환경 설정 및 라이브러리 설치:
1. 가상환경 생성: `python -m venv venv`
2. 가상환경 활성화:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. 라이브러리 설치: `pip install -r requirements.txt`

## 프로젝트별 라이브러리 활용 가이드 (2025년 9월 기준)

### 01_Marketing_Management_A
- **웹 스크래핑**: requests, beautifulsoup4, selenium, scrapy, playwright, cloudscraper
- **데이터 분석**: pandas, numpy, scipy, polars
- **시각화**: matplotlib, seaborn, plotly, networkx, bokeh
- **PPT 제작**: python-pptx, openpyxl
- **AI/ML**: openai, transformers, langchain (소비자 분석용)

### 02_Business_Strategy  
- **전략 분석**: pandas, numpy, scipy
- **데이터 검증**: cerberus, marshmallow, pydantic
- **시각화**: plotly, networkx (포터 파이브 포스, SWOT 등)
- **문서 작업**: python-pptx, python-docx
- **웹 크롤링**: requests, selenium (경쟁사 분석)

### 03_Digital_Business_Model_and_New_Business_Development
- **MVP 개발**: streamlit, gradio, fastapi
- **프로토타이핑**: flask, django
- **디자인 씽킹**: matplotlib, seaborn (사용자 여정 시각화)
- **AI 활용**: openai, langchain (아이디어 생성)
- **이미지 처리**: pillow, opencv-python

### 04_Smart_IT_Service
- **웹/앱 개발**: flask, fastapi, streamlit, django, uvicorn
- **데이터베이스**: pymongo, sqlalchemy, redis
- **머신러닝**: transformers, scipy, numpy
- **API 개발**: httpx, pydantic, fastapi
- **테스팅**: pytest, pytest-cov

### 공통 유틸리티
- **문헌 분석**: nltk, spacy, textblob, wordcloud, textstat
- **이미지 처리**: pillow, opencv-python, imageio
- **스케줄링**: schedule, celery, apscheduler  
- **로깅**: loguru, rich
- **환경관리**: python-dotenv, python-decouple

## Common Commands
No specific build, test, or development commands have been established yet. Standard Python commands will apply once the project structure is created.

## Architecture
The project structure and architecture are yet to be defined.