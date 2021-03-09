# BINGO
파이썬 기반 가상머신 컨셉 OS

Android에서 실행되게 만들었습니다. Pydroid3앱으로 실행을 권장드립니다.

# 규칙
1. 기본 프로그램은 pgm폴더에 저장해야 한다.
2. pgm폴더 안에 있는 파일은 위치 상관없이 실행할 수 있어야 한다.
3. sys폴더에는 프로그램/OS가 읽어드릴 TXT파일이 저장된다.
4. 명령어는 command.py에 함수로 추가한다.
5. pip 설치가 필요한 라이브러리를 사용할시 이슈에 라이브러리명을 적는다.
6. 버전 넘버링은 수정하지 않는다.

# Windows 이식하기
이 OS는 Android에서 작동되게 제작하였기 때문에 Windows에선 실행이 안됩니다.
리눅스 이식도 할것입니다. 이식하려면 모든 파일을 수정해야 합니다.

# pip 설치가 필요한 라이브러리
1. getmac (pip install getmac)
2. cpuinfo (pip install pycpuinfo)

# 사용된 라이브러리
1. time
2. os
3. cpuinfo
4. platform
5. psutil
6. shutil
7. random
8. socket
9. subprocess
10. getmac

# 참여하신 분들
