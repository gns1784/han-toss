# 2024.06.25 교육

## han-toss
git push from VScode
### 위에 파일에 동그라미 표시가 되어 있으면 저장이 되지 않은 상태

git push

- 부득이하게 홈페이지 내에서 수정할 경우 -- vscode 터미널창에서 git pull 명령어 실행
- github 홈페이지에서 작업하지 말 것 -- 동기화되지 않았기 때문에 에러가 무조건 발생하게 됨

## 해결하는 방법
1. 파일 빽업
2. 파일 전체 삭제
3. git bash 관리자 작업 환경에서 git clone "주소" 다시 실행하기
4. 빽업했던 파일 다시 복사해서 붙여넣기

--> vscode에서 git add . --> git commit -m "git push from VScode" --> git push하면
다시 전체 다 올라감

## 부득이하게 홈페이지에서 작업할 경우
git pull 명령어 실행

## 홈페이지나 VScode에서 작업 후에 error 발생 시, git bash에서 다시 실행
1. git status
2. git reset --soft HEAD~1 # 커밋이 하나가 걸려있다면 ~1, 두개라면 ~2
3. git pull
4. git add . --> git commit -m "git push from VScode"
5. git push

## 주요 명령어 정리
pwd : 현재 파일 경로 확인
cd han-toss/ : 파일 경로 han-toss/로 새로 설정
ls : 경로 안에 있는 파일 확인
ls -al : 숨겨진 파일까지 모두 확인 가능
git add . : 모든 파일 추가
git commit -m "TEST" : commit 메세지 남기기
git push

-- 만약 안된다면 --
git config --global user.email "your@gmail.com"
git config --global user.name "yourname"

--실행 후 다시 위와 같은 코드 실행
--> 이래도 오류가 발생한다면
git push
histroy : 내가 한 작업 확인

#  local pc에 python 개발환경 설정

## Windows PowerShell 보안 해제하는 방법 - 개발환경 설치 시 오류 발생 방지
1. windows powershell 관리자 권한으로 실행
2. 보안 문제 오류 발생 시 Get-ExecutionPolicy 명령어 실행
3. Set-ExecutionPolicy -ExecutionPolicy Unrestricted 실행
4. 마지막으로 Get-ExecutionPolicy 실행하였을 때 Unrestricted가 나오면 완료
5. 앞에 (base)가 나오게 되면 아나콘다 가상환경 설정 확인

## 가상환경을 왜 할까?
웹 개발, GUI(옵션 창 같은 것) 개발, 게임 개발(pygame), 영상처리 등등 가능
--> 사용하는 라이브러리마다 버전 충돌이 발생할 수도 있음
--> conda, venv 등 가상환경 설정하는 방법은 여러 가지 존재

## vscode 터미널 창에서 이제 설치
1. pip install virtualenv
2. virtualenv venv
--> 시스템이 아니라 han-toss 안에서 실행해야함
--> 해당 프로젝트 내에서 실행해야함
- git bash/powershell 어디에서든 동작이 되어야 함, 한 군데라도 안된다면 제대로 설치가 되지 않은 것


--> 만약 virtualenv 설치 에러 발생 시 종료 후 PowerShell 관리자 권한 실행 후 밑에 코드 진행
- pip uninstall virtualenv # 저장 취소
- conda init powershell
- 재부팅
- conda install pip
- pip install virtualenv # 다시 설치

--> 맥락적으로 보았을 땐 라이브러리 관리하는 양식이 virtualenv와 conda가 다름
- conda는 MLOps할 때 관리하는 것이 좀 더 편함
- 개발하는 것은 virtualenv가 좀 더 편함

## 가상환경에 접속하는 방법
han-toss 폴더 창에서 git bash 관리자 권한으로 실행
1. cd han-toss/
2. ls 실행 --> venv/ 파일이 있는지 확인
-- main이라 적혀있는 경우 접속이 아직 안됨
3. source venv/Scripts/activate # 가상환경 접속하는 명령어
--> /을 타이핑하지 말고 tab을 눌러서 파일이 존재하는지 확인
4. 위의 명령어 실행 후 (venv)이 나오면 가상환경 접속 완료
5. which python
- 경로상에 han-toss(프로엔터 폴더)가 있는지 확인
--> deactivate : 가상환경에서 빠져나와서 일반 세팅으로 변경하는 명령어

## 라이브러리 설치
ex) pip install pingouin
--> python 실행

## VScode에서 새로운 파일 생성
1. 가상환경 접속 확인
2. 설치

### 20분동안 다시 복기해보기
1. 깃허브 레파지토리 생성, 이름은 알아서 만들기
2. git clone으로 끌고오기
3. 간단한 테스트 진행 (git add . --> git commit --> git push)
4. 가상환경 설정(virtualenv)
5. 가상환경 접속
6. 마지막으로 주요 라이브러리 설치

## main.py 파일 생성
import pingouin as pg 

print(pg.__version__)
print("Hello World!")
-- 이후 터미널 창에서 python main.py 실행 후 python 코드에 대한 결과가 나오는지 확인 --

## 패키지 설치
requirements.txt 파일 생성 후 다음과 같이 입력
numpy == 1.26.4
pandas <= 2.2.6
pip install -r requirements.txt # 텍스트 파일 안에 있는 패키지들이 설치

## jupyter 실행 및 창 띄우기
1. pip install numpy scipy pandas matplotlib seaborn plotly jupyterlab
2. jupyter lab 실행 --> jupyter 화면에 나오게 됨