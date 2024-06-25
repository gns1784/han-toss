# han-toss

git push from VScode
### 위에 파일에 동그라미 표시가 되어 있으면 저장이 되지 않은 상태

git push

### 부득이하게 홈페이지 내에서 수정할 경우
### vscode 터미널창에서 git pull 명령어 실행

# github 홈페이지에서 작업하지 말 것
-- 동기화되지 않았기 때문에 에러가 무조건 발생하게 됨

# 해결하는 방법
1. 파일 빽업
2. 파일 전체 삭제
3. git bash 관리자 작업 환경에서 git clone "주소" 다시 실행하기
4. 빽업했던 파일 다시 복사해서 붙여넣기

--> vscode에서 git add . --> git commit -m "git push from VScode" --> git push하면
다시 전체 다 올라감

# 부득이하게 홈페이지에서 작업할 경우
git pull 명령어 실행

# 홈페이지나 VScode에서 작업 후에 error 발생 시, git bash에서 다시 실행
1. git status
2. git reset --soft HEAD~1 # 커밋이 하나가 걸려있다면 ~1, 두개라면 ~2
3. git pull
4. git add . --> git commit -m "git push from VScode"
5. git push