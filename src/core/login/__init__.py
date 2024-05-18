import pathlib
import sys

cwd = pathlib.Path(__file__).parent

paths = []
while True:
    # 일단 현재 폴더를 경로에 추가
    paths.append(cwd)

    gitignore_file = cwd / ".gitignore"
    # 현재 폴더에 .gitignore 파일이 있는 경우,
    if gitignore_file.exists():
        # 프로젝트 폴더 최상단이므로 종료
        break
    else:
        # 아닌 경우, 상위 폴더로 이동하는 것 반복
        cwd = cwd.parent

# 경로가 기존에 등록되지 않은 경우에만 등록
for path in paths:
    if path not in sys.path:
        sys.path.append(str(path))
