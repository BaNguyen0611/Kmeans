# app.py
# =================================================================

import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1) Tiêu đề ứng dụng
st.title("Ứng dụng phân cụm khách hàng với K-Means")
st.write("Sử dụng thuật toán K-Means để phân loại khách hàng dựa trên Thu nhập và Điểm chi tiêu.")

# 2) Đọc dữ liệu
try:
    df = pd.read_csv("Customers.csv")
except FileNotFoundError:
    st.error("Lỗi: Không tìm thấy tệp Customers.csv. Vui lòng đảm bảo tệp này nằm trong cùng thư mục.")
    st.stop()

# Đổi tên cột cho phù hợp với mã nguồn KMeans_MallCustomers.py
df.rename(columns={'Annual Income ($)': 'Annual Income (k$)'}, inplace=True)

# 3) Hiển thị dữ liệu
st.subheader("Dữ liệu đầu vào:")
st.write(df.head())

# 4) Thanh trượt để chọn số cụm (k)
st.sidebar.subheader("Cài đặt phân cụm")
num_clusters = st.sidebar.slider(
    "Chọn số cụm (k):", 
    min_value=2, 
    max_value=10, 
    value=5, 
    step=1,
    help="Số cụm để thuật toán K-Means phân loại khách hàng."
)

# 5) Chọn đặc trưng để phân cụm và chuẩn hóa dữ liệu
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 6) Huấn luyện và dự đoán với K-Means
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# 7) Hiển thị kết quả dưới dạng bảng
st.subheader(f"Kết quả phân cụm với k = {num_clusters}:")
st.dataframe(df[["CustomerID", "Annual Income (k$)", "Spending Score (1-100)", "Cluster"]])


# 8) Trực quan hóa các cụm
st.subheader("Biểu đồ phân cụm khách hàng:")
fig, ax = plt.subplots(figsize=(10, 8))

for cluster in range(num_clusters):
    cluster_points = df[df["Cluster"] == cluster]
    ax.scatter(
        cluster_points["Annual Income (k$)"],
        cluster_points["Spending Score (1-100)"],
        label=f"Cụm {cluster+1}"
    )

# Vẽ tâm cụm
centers = scaler.inverse_transform(kmeans.cluster_centers_)
ax.scatter(centers[:, 0], centers[:, 1], s=200, c='red', marker='X', label='Tâm cụm')

ax.set_title(f"Phân cụm khách hàng (k={num_clusters})")
ax.set_xlabel("Thu nhập hàng năm (k$)")
ax.set_ylabel("Điểm chi tiêu (1-100)")
ax.legend()
st.pyplot(fig)