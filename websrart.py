#Django start
 1. Python 설치
   사이트에서 다운로드
   (폴더생성 : c:\python\python36)
   설치 -> Customer(두번째것선택)
        ㅁ체크박스선택 Add Python 3.X to PATH
        다음-> 디렉토리 직접선택
        c:\python\python36으로 -> install

  # 준비
  # 컴멘드 라인 사용법 숙지
  # Python 문법 숙지

 2. Code Editor 설치
    atom.io에서 다운받아 설치
    Atom 은 GitHub에서 만든 오픈소스에디터
       #권장 PyCharm (유료)다음에 사용해봄

 3.장고 설치
  # 시작위치 (폴더생성 C:\Python\djangogirls)
     C:\Python\djangogirls
     Site : C:\Python\djangogirls\mysite

     cd C:\Python\djangogirls 폴더 위치 변경후 아래 실행.

  # 가상환경설치
     python -m venv myvenv

  # virtualenv 활성화
     myvenv\Scripts\activate - 활성화
     myvenv\Scripts\deactivate - 할성화종료

  #장고설치
     pip install --upgrade pip #pip 최신버전확인
     pip install django~=1.11.0 #장고설치

  #-----------장고프로젝트---------------
   #사이트 생성
     django-admin.py startproject mysite .
     #설정변경
       mysite/settings.py
         TIME_ZONE = 'Asia/Seoul'
         STATIC_URL = '/static/'
         STATIC_ROOT = os.path.join(BASE_DIR, 'static')
         ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com'] #배포할때

   #데이터베이스 생성
     python manage.py migrate

   # Web Server run
     python manage.py runserver
     오류나면 python manage.py runserver 0:8000

     브라우저에서 http://127.0.0.1:8000/ 실행하여 사이트 확인
                 http://127.0.0.1:8000/admin/ 관리자사이트

   # 어플리케이션(blog)생성
     python manage.py startapp blog

     mysite/settings.py 파일에 추가
       INSTALLED_APPS = [
          'blog',] # 맨아래에 추가



   # blog 글쓰기 모델 만들기
     blog/models.py 수정



        from django.db import models
        from django.utils import timezone


        class Post(models.Model):
            author = models.ForeignKey('auth.User')
            title = models.CharField(max_length=200)
            text = models.TextField()
            created_date = models.DateTimeField(
                    default=timezone.now)
            published_date = models.DateTimeField(
                    blank=True, null=True)

            def publish(self):
                self.published_date = timezone.now()
                self.save()

            def __str__(self):
                return self.title

            #_ 언더스코어, __던더(dunder더블언더스코어)

   #장고 모델에 변화가 생겼다는 걸 알게 해줘
   python manage.py makemigrations blog

   # 실제 데이터테베이스 모델추가반영 - 테이블생성
   python manage.py migrate blog

  #장고관리자
     blog/admin.py 에 내용추가
            from django.contrib import admin
            from .models import Post

            admin.site.register(Post)

   #장고관리자 admin User 생성
   python manage.py createsuperuser
   ID : usenjoy
   mail : usenjoy@naver.com
   password : P@ssword

   ------서버 재실행---------
   # Web Server run
     python manage.py runserver
     오류나면 python manage.py runserver 0:8000
   ---------------

   # Web blog 사이트 추가
     mysite/urls.py #추가
        from django.conf.urls import include

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'', include('blog.urls')), #진입하는 시점추가
        ]

    blog/urls.py #아래추가
        from django.conf.urls import url
        from . import views

        urlpatterns = [
            url(r'^$', views.post_list, name='post_list'),
        ]

    blog/views.py #아래추가
        def post_list(request):
            return render(request, 'blog/post_list.html', {})

    첫 번째 템플릿! 추가
    blog/templates/blog #폴더생성
    blog/templates/blog/post_list.html #내용추가
            <html>
                <p>Hi there!</p>
                <p>It works!</p>
            </html>

#-------------------------------------------------------------------------------

   배포하기
   1. git 설치하기
     변경사항 다섯 번째
       PATH 환경 설정(Adjusting your PATH environment)화면에서 주의하세요.
       윈도우 커맨드라인에서 Git과 유닉스 도구를 사용
       (Use Git and optional Unix tools from the Windows Command Prompt)을 선택하세요

   2. git 저장소 만들기
     git init  # C:\Python\djangogirls 에서 실행
       .gitignore 생성
     #실행이 안되면 git comman 실행프로그램 실랭 후 명령
     git config --global user.name "usenjoy"
     git config --global user.email usenjoy@naver.com

     .gitignore #github에 올리지 않을 파일 타입 생성
            *.pyc
            *~
            __pycache__
            myvenv
            db.sqlite3
            /static
            .DS_Store

     git status #상태파악
     git add --all . #전체저장
     git commit -m "My Django Girls app, first commit"



   3. GitHub 코드 배포
      계정 usenjoy, usenjoy@naver.com
       Password : park~
       site bander


       저장소 parkyongdeok/my-first-blog #https://github.com/new
       git remote add origin https://github.com/parkyongdeok/my-first-blog.git
       git push -u origin master #usenjoy@naver.com,  park~

   4. GitHub에서 PythonAnyWhere로 코드 가져오기
      #git clone https://github.com/bander/my-first-blog.git
      Site에서 bsh로 실행 #https://www.pythonanywhere.com 로그인후
      git clone https://github.com/parkyongdeok/my-first-blog.git
      tree my-first-blog

      #PythonAnywhere에서 가상환경(virtualenv) 생성하기
      cd my-first-blog
      virtualenv --python=python3.6 myvenv
      source myvenv/bin/activate

      #PythonAnywhere에서 가상환경(virtualenv) 생성하기
      배시 콘솔(Bash console)에 다음과 같이 입력하세요. :
      $ cd my-first-blog
      $ virtualenv --python=python3.6 myvenv
      $ source myvenv/bin/activate
      (myvenv) $  pip install django~=1.11.0

      #PythonAnywhere에서 데이터베이스 생성하기
      (mvenv) $ python manage.py migrate
      (mvenv) $ python manage.py createsuperuser

      #web app으로 블로그 배포하기
      domain bander.pythonanywhere.com.
      대시보드로 와서 Web을 클릭하고 Add a new web app를 선택하세요.
      도메인 이름을 확정한 후, 대화창에 수동설정(manual configuration) ("Django"옵션이 아니에요) 을 클릭하세요.
      다음, Python 3.6을 선택하고 다음(Next)을 클릭하면 마법사가 종료됩니다.

      #가상환경(virtualenv) 설정하기
      web -> Virtualenv: name 등록
      /home/bander/my-first-blog/myvenv -> 저장

      #WSGI 파일 설정하기
