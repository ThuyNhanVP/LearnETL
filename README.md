# Dự Án nhỏ về ETL 

## Mô tả
- Dự án này thực hiện quy trình ETL (Extract - Transform - Load) với dữ liệu dạng CSV. Mục đích là đọc dữ liệu từ file CSV nguồn, xử lý biến đổi dữ liệu theo yêu cầu, sau đó ghi lại dữ liệu đã xử lý ra file CSV mới.

## Các bước thực hiện
- Extract : Đọc dữ liệu từ file CSV đầu vào.
- Transform : Thực hiện các bước biến đổi dữ liệu như lọc, chuyển đổi định dạng, tính toán trường mới,...
- Load : Ghi dữ liệu đã biến đổi ra file CSV đầu ra.

## Công nghệ sử dụng
- Python (phiên bản 3.x)
- Thư viện pandas để xử lý dữ liệu CSV

## Cách sử dụng
1. Clone repository về máy:
    ```bash
     git clone https://github.com/ThuyNhanVP/webdaygiep_Laravel.git](https://github.com/ThuyNhanVP/LearnETL.git
2. Cài đặt các thư viện cần thiết:
    ```bash
    pip install pandas
3. Chạy file ETL chính:
    ```bash
    python LearnETL.py

## Ghi chú
- Đảm bảo file CSV đầu vào nằm đúng vị trí hoặc đặt lại đường dẫn trong mã nguồn.
- Tùy chỉnh logic biến đổi dữ liệu trong phần Transform theo yêu cầu cụ thể của bạn.
