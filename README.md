# Kmeans
<img width="61" height="80" alt="Screen Shot 2025-09-22 at 10 44 04" src="https://github.com/user-attachments/assets/53b46f58-a4df-4ccf-9bf3-85ca28cc75cd" />
<img width="256" height="554" alt="Screen Shot 2025-09-22 at 10 43 58" src="https://github.com/user-attachments/assets/649732ce-e034-4b86-8358-b6f7260365c8" />
Ứng dụng phân cụm khách hàng với K-Means
Đây là một ứng dụng web đơn giản được xây dựng bằng Streamlit, giúp trực quan hóa và thực hiện thuật toán phân cụm K-Means trên bộ dữ liệu khách hàng. Ứng dụng này cho phép người dùng tương tác để chọn số cụm và xem kết quả phân loại một cách trực quan.

Các tính năng chính
Tương tác trực quan: Sử dụng thanh trượt để chọn số cụm (k).

Phân cụm tức thì: Áp dụng thuật toán K-Means và hiển thị kết quả phân loại ngay lập tức.

Trực quan hóa dữ liệu: Hiển thị biểu đồ phân cụm (cluster plot) với các điểm dữ liệu được tô màu theo cụm và tâm cụm.

Hiển thị dữ liệu: Bảng dữ liệu đầu vào và kết quả phân cụm được hiển thị rõ ràng.

Cách chạy ứng dụng
Chuẩn bị tệp: Đặt tệp app.py, Customers.csv, và KMeans_MallCustomers.py vào cùng một thư mục.

Cài đặt thư viện: Mở terminal và chạy lệnh sau để cài đặt các thư viện cần thiết:

Bash

pip install streamlit pandas scikit-learn matplotlib
Chạy ứng dụng: Sau khi cài đặt xong, hãy chạy lệnh sau trong terminal tại thư mục chứa các tệp:

Bash

streamlit run app.py
Ứng dụng sẽ tự động mở trên trình duyệt web của bạn.

Các tệp trong dự án
app.py: Mã nguồn chính của ứng dụng web Streamlit.

Customers.csv: Bộ dữ liệu được sử dụng để phân cụm.

KMeans_MallCustomers.py: Tệp mã nguồn gốc chứa logic phân cụm K-Means.
