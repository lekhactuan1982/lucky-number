"""Ví dụ Python đơn giản: Tìm số may mắn"""

import random


def so_may_man(ten: str) -> int:
    """Tạo số may mắn dựa trên tên người dùng."""
    tong = sum(ord(c) for c in ten)
    random.seed(tong)
    return random.randint(1, 100)


def main():
    print("=== Chương trình Số May Mắn ===")
    ten = input("Nhập tên của bạn: ")
    so = so_may_man(ten)
    print(f"Số may mắn của {ten} là: {so}")

    # Danh sách số may mắn cho nhiều người
    nguoi_dung = ["An", "Bình", "Chi", "Dũng"]
    print("\nSố may mắn của mọi người:")
    for nguoi in nguoi_dung:
        print(f"  {nguoi}: {so_may_man(nguoi)}")


if __name__ == "__main__":
    main()
