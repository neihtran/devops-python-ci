# Sử dụng base image Python gọn nhẹ và bảo mật
FROM python:3.10-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cấu hình biến môi trường tối ưu cho Python trong môi trường Docker
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000

# Copy file requirements.txt trước để tận dụng Docker cache layer
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ thư mục và mã nguồn ứng dụng vào container
COPY . .

# Chạy tự động Unit Test ngay trong quá trình Build để đảm bảo code không lỗi trước khi tạo Image
RUN python -m unittest discover -s tests

# Khai báo cổng mạng mà container sẽ lắng nghe khi chạy
EXPOSE 5000

# Lệnh mặc định khởi chạy ứng dụng (in kết quả và chạy Flask API)
CMD ["python", "app/main.py"]
