# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    # Lập trình viên cố gắng sao chép đơn thuốc sang ngày mới
    new_prescription = list(old_prescription)
    # Cố gắng đổi tên thuốc ở vị trí đầu tiên (index 0) từ Panadol thành Paracetamol
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    return new_prescription
    
# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
# Vì câu lệnh new_prescription = old_prescription không tạo ra danh sách mới mà chỉ tạo thêm một biến cùng tham chiếu đến một List. Do đó khi thêm phần tử vào new_prescription thì old_prescription cũng bị thay đổi.
# Để tạo một List mới không ảnh hưởng đến List gốc, có thể dùng copy(), [:] (slicing) hoặc list(). Các cách này sẽ tạo ra một bản sao riêng biệt của danh sách.
# Vì String trong Python là immutable (bất biến), phương thức replace() không sửa trực tiếp chuỗi cũ mà trả về một chuỗi mới. Chuỗi mới này không được lưu lại nên không có sự thay đổi nào xảy ra.
# Cần gán kết quả của replace() trở lại phần tử trong danh sách.