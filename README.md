# 🚀 DevOps Python Multiply App - Bài Thực Hành Số 1

Ứng dụng Python thực hiện phép toán nhân cơ bản kèm theo **Flask API nâng cao**, giao diện web **Calculator** hiện đại, hệ thống **Unit Test** chặt chẽ, đóng gói bằng **Docker**, và tự động tích hợp liên tục (CI) qua **GitHub Actions**.

---

## 📁 Cấu Trúc Thư Mục Dự Án

```text
d:\VTC\DevOps\
├── .github/
│   └── workflows/
│       └── ci.yml             # Luồng tự động chạy test trên GitHub Actions
├── app/
│   ├── templates/
│   │   └── index.html         # Giao diện Calculator Web (glassmorphism đẹp mắt)
│   ├── calculator.py          # Module nghiệp vụ chính chứa hàm multiply(a, b)
│   └── main.py                # Server Flask API, in kết quả terminal khi khởi động
├── tests/
│   └── test_calculator.py     # Bộ kiểm thử Unit Test cho hàm multiply
├── Dockerfile                 # File đóng gói ứng dụng thành container
├── requirements.txt           # Danh sách thư viện Python cần thiết
└── README.md                  # Hướng dẫn sử dụng dự án này
```

---

## 🛠️ Hướng Dẫn Cài Đặt Cục Bộ (Local)

Để chạy thử ứng dụng và kiểm thử trực tiếp trên máy của bạn:

1. **Khởi tạo và kích hoạt môi trường ảo (Khuyên dùng):**
   ```bash
   python -m venv venv
   # Trên Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # Trên Linux/macOS:
   source venv/bin/activate
   ```

2. **Cài đặt các thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy Unit Test cục bộ:**
   ```bash
   python -m unittest discover -s tests -v
   ```

4. **Khởi chạy ứng dụng Flask:**
   ```bash
   python app/main.py
   ```
   *Khi khởi chạy, bạn sẽ thấy kết quả của phép toán `multiply(3, 4)` được in trực tiếp ngay trên terminal!*
   *Sau đó, bạn có thể truy cập `http://localhost:5000` trên trình duyệt để sử dụng giao diện web.*

---

## 🐳 Hướng Dẫn Sử Dụng Với Docker

Ứng dụng đã được cấu hình tối ưu để đóng gói bằng Docker. Quá trình đóng gói sẽ tự động chạy unit test để đảm bảo an toàn.

1. **Build Docker Image:**
   ```bash
   docker build -t devops-multiply-app .
   ```

2. **Khởi chạy Container:**
   ```bash
   docker run -p 5000:5000 --name my-multiply-container devops-multiply-app
   ```
   *Bạn sẽ lập tức thấy log in kết quả phép nhân `multiply(3, 4)` trên terminal:*
   ```text
   ============================================================
       KHỞI CHẠY ỨNG DỤNG DEVOPS - BÀI THỰC HÀNH SỐ 1
   ============================================================
   Thực hiện phép tính kiểm thử yêu cầu: multiply(3, 4)
   ==> KẾT QUẢ TRÊN TERMINAL: 3 * 4 = 12
   ==> TRẠNG THÁI: THÀNH CÔNG (multiply(3, 4) == 12)
   ============================================================
   ```

3. **Truy cập Giao diện Web & API qua Container:**
   - **Giao diện Web:** Truy cập [http://localhost:5000](http://localhost:5000)
   - **Thử API nhân số khác:** [http://localhost:5000/api/multiply?a=5&b=6](http://localhost:5000/api/multiply?a=5&b=6)

---

## ⚙️ Tự Động Hóa Với GitHub Actions CI

Khi bạn push code lên kho lưu trữ GitHub của mình (nhánh `main`, `master` hoặc `develop`), luồng GitHub Actions cấu hình trong `.github/workflows/ci.yml` sẽ tự động:
1. Tạo môi trường ảo chạy hệ điều hành Ubuntu mới nhất.
2. Cài đặt Python 3.10 và khôi phục cache pip.
3. Cài đặt các thư viện trong `requirements.txt`.
4. Chạy toàn bộ các unit test để kiểm tra logic hàm `multiply`.
