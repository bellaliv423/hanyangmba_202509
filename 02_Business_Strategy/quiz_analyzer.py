"""
Business Strategy Quiz Analyzer
이미지로 캡처한 퀴즈를 분석하고 정리하는 도구
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import pandas as pd

class QuizAnalyzer:
    """퀴즈 분석 및 관리 클래스"""
    
    def __init__(self, base_path: str = "02_Business_Strategy"):
        self.base_path = Path(base_path)
        self.quiz_path = self.base_path / "09_quizzes"
        self.quiz_data = {}
        
    def create_week_structure(self, week_num: int):
        """특정 주차의 폴더 구조 생성"""
        week_folder = self.quiz_path / f"week_{week_num:02d}"
        quiz_questions = week_folder / "quiz_questions"
        
        # 폴더 생성
        quiz_questions.mkdir(parents=True, exist_ok=True)
        
        # 기본 파일 생성
        files_to_create = [
            (week_folder / "quiz_answers.md", self._get_answer_template(week_num)),
            (week_folder / "quiz_notes.md", self._get_notes_template(week_num)),
        ]
        
        for file_path, content in files_to_create:
            if not file_path.exists():
                file_path.write_text(content, encoding='utf-8')
                
        return week_folder
    
    def _get_answer_template(self, week_num: int) -> str:
        """답안 템플릿 생성"""
        return f"""# Week {week_num} 퀴즈 정답

## 퀴즈 정보
- **날짜**: {datetime.now().strftime('%Y-%m-%d')}
- **주차**: Week {week_num}
- **문항 수**: 

## 문제별 정답

### 문제 1
**질문**: 
**정답**: 
**해설**: 

### 문제 2
**질문**: 
**정답**: 
**해설**: 

---
*Created with Claude Code*
"""

    def _get_notes_template(self, week_num: int) -> str:
        """학습 노트 템플릿 생성"""
        return f"""# Week {week_num} 학습 노트

## 주요 개념

## 오답 노트

## 복습 포인트

## 관련 아티클

---
*Created with Claude Code*
"""

    def analyze_quiz_patterns(self) -> pd.DataFrame:
        """전체 퀴즈 패턴 분석"""
        quiz_stats = []
        
        for week_folder in sorted(self.quiz_path.glob("week_*")):
            week_num = int(week_folder.name.split("_")[1])
            
            # 이미지 파일 수 계산
            image_count = len(list((week_folder / "quiz_questions").glob("*.jpg"))) + \
                         len(list((week_folder / "quiz_questions").glob("*.png")))
            
            # 답안 파일 존재 여부
            has_answers = (week_folder / "quiz_answers.md").exists()
            has_analysis = (week_folder / "quiz_complete_analysis.md").exists()
            
            quiz_stats.append({
                "Week": week_num,
                "Image Count": image_count,
                "Has Answers": has_answers,
                "Has Analysis": has_analysis,
                "Status": "Complete" if has_analysis else "Partial" if has_answers else "Empty"
            })
        
        return pd.DataFrame(quiz_stats)
    
    def create_study_guide(self, weeks: List[int]) -> str:
        """여러 주차를 통합한 학습 가이드 생성"""
        guide = f"""# Business Strategy 통합 학습 가이드

## 범위: Week {min(weeks)} - Week {max(weeks)}
생성일: {datetime.now().strftime('%Y-%m-%d')}

---

## 주차별 핵심 내용

"""
        for week in weeks:
            week_folder = self.quiz_path / f"week_{week:02d}"
            if week_folder.exists():
                guide += f"""
### Week {week}
- 퀴즈 문항 수: {len(list((week_folder / "quiz_questions").glob("*.jpg")))}
- 상태: {"완료" if (week_folder / "quiz_complete_analysis.md").exists() else "진행중"}

"""
        
        guide += """
---

## 시험 대비 체크리스트

### 개념 정리
- [ ] 핵심 학자와 이론 매칭
- [ ] 전략 학파별 특징
- [ ] 프레임워크 이해

### 문제 풀이
- [ ] 전체 퀴즈 복습
- [ ] 오답 노트 확인
- [ ] 모의 문제 연습

### 최종 점검
- [ ] 약점 보완
- [ ] 시간 관리 연습
- [ ] 핵심 암기 사항

---
*Created with Claude Code*
"""
        return guide
    
    def export_quiz_summary(self, output_file: str = "quiz_summary.json"):
        """전체 퀴즈 정보를 JSON으로 내보내기"""
        summary = {
            "course": "Business Strategy",
            "total_weeks": 16,
            "last_updated": datetime.now().isoformat(),
            "weeks": {}
        }
        
        for week_folder in sorted(self.quiz_path.glob("week_*")):
            week_num = int(week_folder.name.split("_")[1])
            
            summary["weeks"][f"week_{week_num:02d}"] = {
                "has_quiz": (week_folder / "quiz_questions").exists(),
                "has_answers": (week_folder / "quiz_answers.md").exists(),
                "has_analysis": (week_folder / "quiz_complete_analysis.md").exists(),
                "image_count": len(list((week_folder / "quiz_questions").glob("*.*")))
            }
        
        output_path = self.base_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        return output_path


def main():
    """메인 실행 함수"""
    analyzer = QuizAnalyzer()
    
    print("Business Strategy Quiz Analyzer")
    print("=" * 50)
    
    while True:
        print("\n메뉴:")
        print("1. 새 주차 폴더 생성")
        print("2. 퀴즈 현황 분석")
        print("3. 학습 가이드 생성")
        print("4. 퀴즈 정보 내보내기")
        print("5. 종료")
        
        choice = input("\n선택: ")
        
        if choice == "1":
            week = int(input("주차 번호 (1-16): "))
            folder = analyzer.create_week_structure(week)
            print(f"✅ Week {week} 폴더 생성 완료: {folder}")
            
        elif choice == "2":
            df = analyzer.analyze_quiz_patterns()
            print("\n📊 퀴즈 현황:")
            print(df.to_string(index=False))
            
        elif choice == "3":
            weeks_input = input("포함할 주차 (쉼표로 구분, 예: 1,2,3): ")
            weeks = [int(w.strip()) for w in weeks_input.split(",")]
            guide = analyzer.create_study_guide(weeks)
            
            output_file = f"study_guide_week_{min(weeks)}-{max(weeks)}.md"
            output_path = analyzer.base_path / output_file
            output_path.write_text(guide, encoding='utf-8')
            print(f"✅ 학습 가이드 생성: {output_path}")
            
        elif choice == "4":
            output = analyzer.export_quiz_summary()
            print(f"✅ 퀴즈 정보 내보내기 완료: {output}")
            
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("❌ 잘못된 선택입니다.")


if __name__ == "__main__":
    # 스크립트 직접 실행 시
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 중단되었습니다.")
    except Exception as e:
        print(f"\n오류 발생: {e}")