📌 Task Management Backend

Backend API cho hệ thống quản lý Task, viết bằng FastAPI + SQLAlchemy + PostgreSQL.
Hỗ trợ authentication bằng JWT, quản lý project, task, comment, attachment (upload file), báo cáo.

🚀 Yêu cầu hệ thống

Windows 10/11

Python 3.12+

PostgreSQL 16+

⚙️ Cài đặt

1. Clone source code

Mở Command Prompt (CMD) hoặc PowerShell:

git clone https://github.com/manhdao1006/be-assignment.aug-2025.git
cd task-management

2. Tạo virtual environment
   python -m venv venv
   venv\Scripts\activate

Sau khi chạy lệnh trên, sẽ thấy (venv) xuất hiện trong CMD/PowerShell.

3. Cài dependencies
   pip install -r requirements.txt

4. Tạo database

Mở pgAdmin hoặc psql, chạy lệnh:

CREATE DATABASE task_management;

5. Chạy migration
   alembic upgrade head

▶️ Chạy server

Trong CMD/PowerShell (vẫn trong virtualenv):

uvicorn app.main:app --reload

API chạy ở: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📂 Upload file

File đính kèm được lưu trong thư mục uploads/

Giới hạn: tối đa 5MB / file, 3 file / task

✅ Test nhanh API

Mở http://127.0.0.1:8000/docs

Đăng nhập, lấy JWT token

Thử gọi API: Project, Task, Comment, Attachment…
