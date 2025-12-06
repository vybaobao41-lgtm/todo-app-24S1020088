# Biến lưu trữ dữ liệu: Mỗi task là một dict {'content': '...', 'status': '...'}
tasks = []

def add_task():
    content = input("Nhập nội dung công việc: ")
    # Thêm task dưới dạng dictionary
    tasks.append({'content': content, 'status': 'Pending'})
    print(f"Đã thêm công việc: '{content}' [Pending].")

def view_tasks():
    # Sẽ được thêm code ở Bước 4
    print("Chức năng xem danh sách.")
    pass

def mark_task_done():
    # Sẽ được thêm code ở Bước 5
    print("Chức năng đánh dấu hoàn thành.")
    pass

def main():
    while True:
        print("\n--- TODO LIST ---")
        print("1. Thêm công việc")
        print("2. Xem danh sách")
        print("3. Đánh dấu hoàn thành")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break

if __name__ == "__main__":
    main()