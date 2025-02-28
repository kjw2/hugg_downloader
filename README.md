# Hugging Face 다운로더

허깅페이스의 모델이나 데이터셋을 쉽게 다운로드할 수 있는 CLI 도구입니다.

## 설치 방법

1. 저장소를 클론합니다.
2. 의존성을 설치합니다:
```bash
pip install -r requirements.txt
```

## 사용 방법

### 전체 모델/데이터셋 다운로드
```bash
python hugg_downloader.py download bert-base-uncased
```
위 명령어를 실행하면 `downloads/bert-base-uncased` 폴더에 모델이 다운로드됩니다.

### 특정 파일만 다운로드
```bash
python hugg_downloader.py download bert-base-uncased -f config.json
```
위 명령어를 실행하면 `downloads/bert-base-uncased/config.json` 파일이 다운로드됩니다.

### 다운로드 경로 지정
```bash
python hugg_downloader.py download bert-base-uncased -o ./my_models
```
위 명령어를 실행하면 `my_models/bert-base-uncased` 폴더에 모델이 다운로드됩니다.

### 특정 브랜치/태그 다운로드
```bash
python hugg_downloader.py download bert-base-uncased -r v1.0
```

## 폴더 구조
```
downloads/
└── 모델명/
    ├── config.json
    ├── pytorch_model.bin
    └── 기타 모델 파일들...
```

## 옵션 설명

- `repo_id`: 허깅페이스 저장소 ID (필수)
- `-f, --filename`: 다운로드할 특정 파일명 (선택)
- `-o, --output-dir`: 다운로드 기본 저장 경로 (기본값: ./downloads)
- `-r, --revision`: 리비전/브랜치명 (기본값: main) 