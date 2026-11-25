# 팀 협업 규칙

## 작업 순서 (매번 반복)

```bash
git checkout main
git pull                          # 1. 최신 내용 받기
git checkout -b feat/<역할>        # 2. 내 브랜치 만들기
# ... 코드 작성 ...
git add .
git commit -m "무엇을 했는지 한 줄"  # 3. 작게, 자주 커밋
git push -u origin feat/<역할>     # 4. 내 브랜치 올리기
```

5. GitHub에서 **Pull Request** 만들기 → 팀장(김동진)이 확인 후 merge
6. merge되면 다른 팀원은 `git pull`로 받기

## 규칙

- main 브랜치에 직접 push하지 않기
- 브랜치 이름: `feat/viz`(김동진), `feat/data`(김민재), `feat/train`(백찬호), `feat/eval`(김동찬)
- 커밋 메시지는 한글로 한 줄 (예: "혼동행렬 그리기 추가")
- 데이터 파일(.pkl, .npz)과 모델 파일은 절대 커밋하지 않기
- 각자 맡은 파일 위주로 수정하기 (충돌 방지)

## 처음 한 번만: 내 GitHub 계정 연결 확인

제출할 때 **본인 아이디가 보이는 커밋 스크린샷**이 필요해서, 커밋이 내 계정으로 기록되는지 꼭 확인하세요.

```bash
git config --global user.name "내 GitHub 아이디"
git config --global user.email "GitHub에 등록한 이메일"
```

## 일정 (마감 2026-12-13 23:59)

| 날짜 | 내용 |
| --- | --- |
| 12/1 (월) | 중간 점검 1 — 데이터 완성, npz 공유 |
| 12/7 (월) | 중간 점검 2 — 학습·평가 결과 확인 |
| 12/11 (금) | 코드 동결 — 모든 PR merge 완료 |
| 12/12 (토) | 새로 clone해서 실행 테스트 |
| 12/13 (일) | 오후까지 4명 모두 개인 제출, 이후 push 금지 |
