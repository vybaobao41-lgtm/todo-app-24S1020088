# Biến lưu trữ dữ liệu: Mỗi task là một dict {'content': '...', 'status': '...'}
tasks = []

def add_task():
    content = input("Nhập nội dung công việc: ")
    # Thêm task dưới dạng dictionary
    tasks.append({'content': content, 'status': 'Pending'})
    print(f"Đã thêm công việc: '{content}' [Pending].")

def view_tasks():
    # Bắt đầu code cho Feature 2
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    if not tasks:
        print("Danh sách công việc trống.")
        return

    for index, task in enumerate(tasks):
        # Duyệt qua danh sách và in ra định dạng: 1. Học bài [Pending]
        print(f"{index + 1}. {task['content']} [{task['status']}]")

def mark_task_done():
    # Hiển thị danh sách để người dùng chọn
    view_tasks() 

    if not tasks:
        return # Thoát nếu danh sách trống

    try:
        # Nhập số thứ tự (index) từ người dùng
        task_index = int(input("Nhập số thứ tự công việc muốn đánh dấu HOÀN THÀNH: ")) - 1

        # Kiểm tra index hợp lệ
        if 0 <= task_index < len(tasks):
            # Cập nhật status của task đó thành "Done"
            tasks[task_index]['status'] = 'Done'
            print(f"Đã đánh dấu công việc số {task_index + 1} là [Done].")
        else:
            print("Lỗi: Số thứ tự không hợp lệ.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số.")

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