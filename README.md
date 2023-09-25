# projrct_I
2023 2학기 캡스톤디자인 프로젝트
## git기본 설정
### **잘못해서 설명 쓰다가 싹다 날렸음**
**설치나 이런거는 유튜브에 '코딩애플git' 검색하면 다 할 수 있습니다. 이거는 참고 정도만 해주세요.**

먼저 git을 다운로드 합니다.
### https://git-scm.com/downloads
![image](https://github.com/TU-Yoon/projrct_I/assets/88664877/953c95cc-703d-4d8d-bfdc-0e04737e27b5)
위 사진처럼 설치할 때 체크 한번 해주세요.

설치가 끝나면 git폴더로 쓸 로컬폴더를 하나 만듭니다.

그러고 나서 해당 폴더 우클릭 -> 터미널 열기(Powershell열기) 열리면
```cmd
git config --global user.email "홍길동@gmail.com"
git config --global user.name "홍길동"
```
이렇게 두개 입력해줍니다. 이게 깃에서 쓸 아이디랑 닉네임 같은거에요.(이메일은 저는 안헷갈리게 깃허브랑 같은거 했습니다.)

그다음 VSCode를 열어서 'ctrl + o'를 눌러 아까 만든 폴더를 엽니다.

하단에 터미널에다가
```cmd
git init
```
입력해서 해당 폴더에서 git을 쓸 수 있게합니다.

그러면 폴더가
![image](https://github.com/TU-Yoon/projrct_I/assets/88664877/3243ace6-1fc4-4fdb-b866-34575d04eab6)에서
![image](https://github.com/TU-Yoon/projrct_I/assets/88664877/5a55c086-861d-4e26-b31d-b3d780a632c9)이렇게 체크 표시가 날겁니다.

그러면 정상적으로 된거에요.
## 로컬폴더를 깃허브랑 연결하기
이 폴더를 깃허브에 연결 할 겁니다.
```cmd
git remote -v
```
로 연결된 원격저장소가 있는지 확인합니다. 아마 아무것도 안나올거에요.

그러면
### git remote add [원격저장소 이름] [원격저장소 주소]
```cmd
git remote add origin https://github.com/TU-Yoon/projrct_I.git
```
이렇게 코드를 입력합니다.

이름은 대부분 origin 쓴다고 하고 깃허브 주소는
### https://github.com/TU-Yoon/projrct_I.git
```cmd
https://github.com/TU-Yoon/projrct_I.git
```
입니다. 복사하면 돼요.

그러면 해당 폴더랑 깃허브랑 연결이 되었습니다.
```cmd
git remote -v
```
로 fetch 주소랑 push 주소가 정상적으로 나오는지 확인해보세요.

잘 나왔으면 먼저 깃허브 파일을 가져와볼겁니다. test.py랑 new.txt 두개를 가져올거에요.
### git pull [원격저장소 이름] [가져올 브랜치]
```cmd
git pull origin main
```
이 명령어는 원격저장소에서 main 브랜치를 가져오는 명령어입니다.

그러면 설정한 git폴더에
![image](https://github.com/TU-Yoon/projrct_I/assets/88664877/c002738a-07c4-45b3-81fd-f8b306b1723d)

이런식으로 파일들을 가져옵니다. 쉽죠?

## git 기본문법
**이제 우리는 연결도 하고 파일도 내려받을 수 있어요. 그러면 이제 작성을 하고 다시 올려야겠죠?**
폴더 내에서 파일을 작성하고 저장을 합니다. (ctrl + s 그거 맞습니다.)

터미널 탭으로 가서
```cmd
git add .          # 폴더 내 모든파일 staging
git add [파일이름]  # 해당파일 staging
```
명령어를 입력합니다. 여기서 staging은 commit 전에 잠시 대기하는 상태로 보면 됩니다.
```cmd
git commit -m 'commit할 내용'
```
이 명령어로 여기서 올리기 전에 바뀐코드나 내용을 간략하게 적습니다.

그 다음
```cmd
git push origin main # 또는
git push -u origin main
```
으로 깃허브에 업로드 합니다.
### 여기서 오류가 날수도 있어요.
에러메세지에 'not found git/heads/main'이런거 적혀있으면
```cmd
git branch
```
해서 '* main'인지 확인해보세요. 만약 main이 아니라 master, 혹은 다른거 적혀있으면 위 push 코드에서 'main -> 해당 브랜치 이름'으로
바꾸면 됩니다.

그러면 깃허브에 올라갔을겁니다.

혹시나 안보인다면 branch 탭 한번 보세요. 이름달라서 다른 브랜치로 생성됐을수도 있습니다.

그러면 제가 수정할게요 그건

나머지 알아두면 좋은 것들은
```cmd
git status  # 파일의 상태를 확인합니다. staging 된 파일을 확인하거나 commit해야할 파일이 있는지 확인합니다.
git remote -v # 해당 폴더랑 연결됭 원격저장소를 확인합니다. fetch랑 push 두개 보일겁니다.
```
정도 있습니다.
### 사실 VSCode 확장도구가 좋아서 여러분은 그걸 주로 사용할겁니다.
코딩애플 채널에서 git다룬 것도 있고 다른사람들도 올린게 많아서 참고하셔서 확장도구 사용해도 괜찮아요.

굳이 터미널에다가 힘들게 명령어 입력 안해도 됩니다.

**여기 관리는 제가 주로 할테니 여러분은 만들고 맘껏 올려주세요.**
# 그럼 다들 캡스톤디자인 화이팅 하시고 힘내봅시다!
