# 1. Hàm nhập điểm có kiểm tra
def nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Nhập điểm {mon} (0–10): "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("❌ Điểm phải từ 0 đến 10. Nhập lại!")
        except ValueError:
            print("❌ Nhập sai định dạng! Nhập lại!")

# 2. Nhập điểm từng môn
toan = nhap_diem("Toán")
ly = nhap_diem("Lý")
hoa = nhap_diem("Hóa")

# 3. Tính điểm trung bình
diem_tb = (toan + ly + hoa) / 3

# 4. Xếp loại
if diem_tb >= 8.5:
    loai = "Giỏi"
elif diem_tb >= 6.5:
    loai = "Khá"
else:
    loai = "Trung bình"

# 5. In kết quả
print(f"Điểm trung bình: {round(diem_tb, 2)}")
print(f"Xếp loại: {loai}")

# 6. Ghi kết quả vào file diem_tb.txt
with open("diem_tb.txt", "w", encoding="utf-8") as file:
    file.write(f"Điểm Toán: {toan}\n")
    file.write(f"Điểm Lý: {ly}\n")
    file.write(f"Điểm Hóa: {hoa}\n")
    file.write(f"Điểm trung bình: {round(diem_tb, 2)}\n")
    file.write(f"Xếp loại: {loai}\n")

# 7. Thông báo đã ghi kết quả
print("✅ Đã lưu kết quả vào file 'diem_tb.txt'")