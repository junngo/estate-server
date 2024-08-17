# 베이스 이미지로 Python 3.10.12 사용
FROM python:3.10.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 장고 명령어 실행을 위한 기본 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
