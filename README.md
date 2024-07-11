# SSAFY-Album-Downloader
삼성 청년 SW 아카데미 수료 앨범 다운로드

---

## Feature
- 모든 앨범 이미지 다운로드
- 책자 형태의 PDF본 다운로드

---

## Environment

- Linux
- Windows
- Python 3.12.4

---

## Installation
- 자동실행을 원한다면, 아래의 Usage로 이동 (별도 패키지 설치 필요 없음)
- 수동실행을 원한다면, 아래의 패키지를 설치
- 필요시 파이썬 가상환경에서 실행

```bash
# Linux Terminal
$ python -m venv venv
$ source venv/bin/activate
```
```bash
# Windows Command Prompt
$ python -m venv venv
$ cd venv\Scripts
$ activate
```
```bash
# Install Packages
$ pip install -r requirements.txt
```

---

## Usage

- [Settings](#settings) 설정 후 [Run](#run) 

---

### Settings
- 수료 기수에 따라 아래의 4개 변수 수정
- 필요에 따라 `SAVE_DIR`, `TEMP_DIR` 수정
```python
BASE_URL = '문자로 안내받은 수료앨범 링크주소'
ENDPOINT = 'assets/page-images/page-hashcode-hashcode'
FILENAME = '20XX 삼성 청년 SW 아카데미 N기 PHOTO ALBUM'
END_PAGE = 300
```
```python
SAVE_DIR = os.path.join(os.getcwd(), 'downloads')
TEMP_DIR = os.path.join(os.getcwd(), 'temp')
```

---

### Run
- 실행환경에 따라 파일 실행
```bash
# Linux
$ run.sh

# Windows
$ run.bat

# Manual
$ python run.py
```
