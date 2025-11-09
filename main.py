import cv2

def main():
    # Mở camera mặc định (0 là webcam mặc định, nếu có nhiều camera thì có thể dùng 1, 2,...)
    cap = cv2.VideoCapture(0)

    # Kiểm tra camera có mở được không
    if not cap.isOpened():
        print("❌ Không thể mở camera!")
        return

    print("📸 Camera đã được kích hoạt. Nhấn 'q' để thoát.")

    while True:
        # Đọc từng khung hình (frame)
        ret, frame = cap.read()
        if not ret:
            print("❌ Không thể nhận khung hình!")
            break

        # Hiển thị hình ảnh
        cv2.imshow('Camera', frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng camera và đóng cửa sổ
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
