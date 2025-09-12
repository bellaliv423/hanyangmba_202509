"""
Business Strategy Quiz Management System
비즈니스 전략 퀴즈 관리 시스템 / 商業策略測驗管理系統

This script helps manage weekly quizzes, including:
- Creating folder structure for new weeks
- Processing quiz images
- Generating answer templates
- Creating bilingual study materials
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class QuizManager:
    def __init__(self, base_path="02_Business_Strategy"):
        self.base_path = Path(base_path)
        self.quiz_path = self.base_path / "09_quizzes"
        
    def create_week_structure(self, week_num, topic_kr="", topic_tw=""):
        """
        Create folder structure for a new week
        새로운 주차의 폴더 구조 생성 / 創建新週次的資料夾結構
        """
        week_folder = self.quiz_path / f"week_{week_num:02d}"
        
        # Create directories
        directories = [
            week_folder,
            week_folder / "quiz_questions",
            week_folder / "class_notes",
            week_folder / "articles"
        ]
        
        for dir in directories:
            dir.mkdir(parents=True, exist_ok=True)
            
        # Create template files
        self._create_quiz_template(week_folder, week_num, topic_kr, topic_tw)
        self._create_study_guide(week_folder, week_num, topic_kr, topic_tw)
        
        print(f"✅ Week {week_num} structure created / 주차 {week_num} 구조 생성됨 / 第{week_num}週結構已創建")
        return week_folder
    
    def _create_quiz_template(self, week_folder, week_num, topic_kr, topic_tw):
        """Create quiz answer template"""
        template = f"""# Week {week_num} 퀴즈 답안 / 測驗答案

## 📚 주제 / 主題
- **한국어**: {topic_kr if topic_kr else '[주제 입력]'}
- **繁體中文**: {topic_tw if topic_tw else '[主題輸入]'}

## 📅 날짜 / 日期
- **작성일 / 作成日**: {datetime.now().strftime('%Y-%m-%d')}

---

## 문제 및 답안 / 題目及答案

### 문제 1 / 題目 1
**질문 / 問題**: 
**정답 / 答案**: 
**해설 / 解析**:
- 한국어: 
- 繁體中文: 

---

### 문제 2 / 題目 2
**질문 / 問題**: 
**정답 / 答案**: 
**해설 / 解析**:
- 한국어: 
- 繁體中文: 

---

[추가 문제는 여기에 / 在此添加更多題目]

---

## 📊 요약 / 總結
- **총 문항 / 總題數**: 
- **정답률 / 正確率**: 
- **오답 문항 / 錯誤題目**: 

## 💡 핵심 개념 / 核心概念
1. 
2. 
3. 

## 📝 복습 노트 / 複習筆記
- 

---

*Created with Claude Code*
"""
        
        file_path = week_folder / "quiz_answers.md"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template)
    
    def _create_study_guide(self, week_folder, week_num, topic_kr, topic_tw):
        """Create study guide template"""
        template = f"""# Week {week_num} Study Guide / 學習指南

## 🎯 학습 목표 / 學習目標
- 한국어: {topic_kr if topic_kr else '[목표 입력]'}
- 繁體中文: {topic_tw if topic_tw else '[目標輸入]'}

## 📖 필수 읽기 자료 / 必讀資料
1. [ ] 교재 챕터 / 教材章節: 
2. [ ] 아티클 1 / 文章 1: 
3. [ ] 아티클 2 / 文章 2: 

## 🔑 핵심 개념 / 核心概念

### 개념 1 / 概念 1
- **한국어**: 
- **繁體中文**: 
- **English**: 

### 개념 2 / 概念 2
- **한국어**: 
- **繁體中文**: 
- **English**: 

## 📝 수업 노트 / 課堂筆記
- 

## 💭 토론 주제 / 討論主題
1. 
2. 

## ✅ 체크리스트 / 檢查清單
- [ ] 퀴즈 완료 / 完成測驗
- [ ] 아티클 읽기 / 閱讀文章
- [ ] 핵심 개념 정리 / 整理核心概念
- [ ] 복습 완료 / 完成複習

---

*Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
        
        file_path = week_folder / "study_guide.md"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template)
    
    def list_weeks(self):
        """List all existing week folders"""
        weeks = []
        for folder in sorted(self.quiz_path.glob("week_*")):
            if folder.is_dir():
                week_num = int(folder.name.split("_")[1])
                quiz_files = list(folder.glob("quiz_questions/*"))
                weeks.append({
                    "week": week_num,
                    "path": str(folder),
                    "has_quiz_images": len(quiz_files) > 0,
                    "quiz_count": len(quiz_files)
                })
        return weeks
    
    def create_summary_report(self):
        """Create a summary report of all quizzes"""
        report = {
            "course": "Business Strategy",
            "total_weeks": 16,
            "completed_weeks": [],
            "pending_weeks": [],
            "statistics": {}
        }
        
        for week in range(1, 17):
            week_folder = self.quiz_path / f"week_{week:02d}"
            if week_folder.exists():
                quiz_images = list(week_folder.glob("quiz_questions/*"))
                if quiz_images:
                    report["completed_weeks"].append(week)
                else:
                    report["pending_weeks"].append(week)
            else:
                report["pending_weeks"].append(week)
        
        report["statistics"] = {
            "completed": len(report["completed_weeks"]),
            "pending": len(report["pending_weeks"]),
            "completion_rate": f"{len(report['completed_weeks'])/16*100:.1f}%"
        }
        
        return report

def main():
    """
    Main function to run the quiz manager
    퀴즈 관리자 실행 메인 함수 / 執行測驗管理器的主函數
    """
    manager = QuizManager()
    
    print("=" * 50)
    print("Business Strategy Quiz Manager")
    print("비즈니스 전략 퀴즈 관리자 / 商業策略測驗管理器")
    print("=" * 50)
    
    while True:
        print("\n옵션 선택 / 選擇選項:")
        print("1. 새 주차 생성 / 創建新週次")
        print("2. 주차 목록 보기 / 查看週次列表")
        print("3. 요약 보고서 / 總結報告")
        print("4. 종료 / 退出")
        
        choice = input("\n선택 / 選擇 (1-4): ")
        
        if choice == "1":
            week = int(input("주차 번호 입력 / 輸入週次號碼 (1-16): "))
            topic_kr = input("한국어 주제 (선택) / 韓文主題 (選填): ")
            topic_tw = input("중국어 주제 (선택) / 中文主題 (選填): ")
            manager.create_week_structure(week, topic_kr, topic_tw)
            
        elif choice == "2":
            weeks = manager.list_weeks()
            print("\n📅 주차별 현황 / 週次狀況:")
            for week in weeks:
                status = "✅" if week["has_quiz_images"] else "⬜"
                print(f"{status} Week {week['week']:02d}: {week['quiz_count']} quiz images")
                
        elif choice == "3":
            report = manager.create_summary_report()
            print("\n📊 요약 보고서 / 總結報告:")
            print(f"완료된 주차 / 完成週次: {report['completed_weeks']}")
            print(f"미완료 주차 / 未完成週次: {report['pending_weeks']}")
            print(f"완료율 / 完成率: {report['statistics']['completion_rate']}")
            
        elif choice == "4":
            print("프로그램 종료 / 程式結束")
            break
        else:
            print("잘못된 선택 / 錯誤選擇")

if __name__ == "__main__":
    # If running this script directly
    # 직접 실행시 / 直接執行時
    main()