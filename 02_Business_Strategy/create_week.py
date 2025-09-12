#!/usr/bin/env python3
"""
Simple script to create weekly quiz structures
간단한 주차별 퀴즈 구조 생성 스크립트
"""

import sys
import os
from pathlib import Path
from datetime import datetime

def create_week_structure(week_num):
    """Create folder structure for a specific week"""
    base_path = Path("09_quizzes")
    week_folder = base_path / f"week_{week_num:02d}"
    
    # Create directories
    directories = [
        week_folder / "quiz_questions",
        week_folder / "class_notes",
        week_folder / "articles"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {directory}")
    
    # Create quiz template
    quiz_template = f"""# Week {week_num} 퀴즈 답안

## 📅 날짜: {datetime.now().strftime('%Y-%m-%d')}

## 문제 및 답안

### 문제 1
**질문**: 
**정답**: 
**해설**: 

### 문제 2
**질문**: 
**정답**: 
**해설**: 

---

## 핵심 개념
1. 
2. 
3. 

## 복습 노트
- 

---
*Created with Claude Code*
"""
    
    # Save template
    template_file = week_folder / "quiz_answers.md"
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(quiz_template)
    
    print(f"✅ Created quiz template: {template_file}")
    
    # Create study guide
    study_guide = f"""# Week {week_num} Study Guide

## 학습 목표
- 

## 필수 읽기 자료
1. [ ] 교재 챕터: 
2. [ ] 아티클: 

## 핵심 개념
- 

## 수업 노트
- 

## 체크리스트
- [ ] 퀴즈 완료
- [ ] 아티클 읽기
- [ ] 복습 완료

---
*Created: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    study_file = week_folder / "study_guide.md"
    with open(study_file, 'w', encoding='utf-8') as f:
        f.write(study_guide)
    
    print(f"✅ Created study guide: {study_file}")
    
    return week_folder

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python create_week.py [week_number]")
        print("Example: python create_week.py 2")
        return
    
    try:
        week_num = int(sys.argv[1])
        if week_num < 1 or week_num > 16:
            print("Week number must be between 1 and 16")
            return
            
        print(f"Creating structure for Week {week_num}...")
        folder = create_week_structure(week_num)
        print(f"\n🎉 Week {week_num} structure created successfully!")
        print(f"📁 Location: {folder.absolute()}")
        
        # Instructions
        print(f"\n📋 Next steps:")
        print(f"1. Save quiz screenshots to: {folder}/quiz_questions/")
        print(f"2. Edit quiz answers in: {folder}/quiz_answers.md")
        print(f"3. Update study guide: {folder}/study_guide.md")
        
    except ValueError:
        print("Please provide a valid week number (1-16)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()