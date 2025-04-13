# pyTools/__init__.py

# Import các hàm, lớp hoặc biến từ module con của thư viện.
# Ví dụ, nếu các hàm chính của bạn được định nghĩa trong file core.py:
from .core import cmb_count, debug, can_d0, report_err
from .core import help, note  # Nếu bạn có thêm các hàm này

# Đặt biến phiên bản cho thư viện
__version__ = '1.0.1'

# Nếu cần, có thể chạy một số thiết lập khởi tạo chung hoặc thông báo khi load package.
print(f"pyTools version {__version__} loaded")