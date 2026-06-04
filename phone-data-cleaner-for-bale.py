import pandas as pd
import math
import os
import re

# ==========================================
# تنظیمات
# ==========================================

MAX_ROWS_PER_FILE = 9999

# ==========================================
# مسیر فایل اسکریپت
# ==========================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# پیدا کردن فایل CSV
# ==========================================

csv_files = [
    f for f in os.listdir(SCRIPT_DIR)
    if f.lower().endswith(".csv")
    and "_clean" not in f.lower()
    and "_part" not in f.lower()
]

if not csv_files:
    raise FileNotFoundError(
        f"هیچ فایل CSV در کنار اسکریپت پیدا نشد.\n\nمسیر بررسی شده:\n{SCRIPT_DIR}"
    )

if len(csv_files) > 1:
    print("چند فایل CSV پیدا شد:")
    for i, file in enumerate(csv_files, start=1):
        print(f"{i}. {file}")

    choice = int(input("\nشماره فایل موردنظر را وارد کنید: "))
    selected_file = csv_files[choice - 1]
else:
    selected_file = csv_files[0]

INPUT_FILE = os.path.join(SCRIPT_DIR, selected_file)

# ==========================================
# تابع استانداردسازی شماره
# ==========================================

def normalize_phone(phone):
    """
    تبدیل شماره‌ها به فرمت:
    989xxxxxxxxx
    """

    if pd.isna(phone):
        return None

    phone = str(phone)

    # حذف هر چیزی غیر از عدد
    phone = re.sub(r"\D", "", phone)

    if not phone:
        return None

    # تبدیل 0912... به 98912...
    if phone.startswith("0"):
        phone = "98" + phone[1:]

    # فقط شماره‌های شروع شده با 98
    if not phone.startswith("98"):
        return None

    # طول دقیق
    if len(phone) != 12:
        return None

    # موبایل ایران
    if not phone.startswith("989"):
        return None

    return phone

# ==========================================
# شروع پردازش
# ==========================================

print("=" * 60)
print("Iran Phone Processor")
print("=" * 60)

print(f"فایل انتخاب شده: {selected_file}")

try:

    # خواندن CSV
    df = pd.read_csv(
        INPUT_FILE,
        header=None,
        dtype=str
    )

    total_rows = len(df)

    print(f"\nتعداد کل ردیف‌ها: {total_rows}")

    if total_rows == 0:
        raise Exception("فایل خالی است.")

    df.columns = ["phone"]

    valid_numbers = []

    invalid_count = 0
    converted_count = 0

    print("\nدر حال پردازش شماره‌ها...")

    for phone in df["phone"]:

        phone_str = str(phone)

        if phone_str.strip().startswith("0"):
            converted_count += 1

        normalized = normalize_phone(phone)

        if normalized:
            valid_numbers.append(normalized)
        else:
            invalid_count += 1

    # حذف شماره‌های تکراری
    unique_numbers = list(dict.fromkeys(valid_numbers))

    duplicate_count = len(valid_numbers) - len(unique_numbers)

    output_df = pd.DataFrame(
        unique_numbers,
        columns=["phone"]
    )


    valid_count = len(output_df)

    print("\n" + "=" * 60)
    print("گزارش پردازش")
    print("=" * 60)

    print(f"کل ردیف‌ها: {total_rows}")
    print(f"تبدیل شده از 0 به 98: {converted_count}")
    print(f"شماره‌های نامعتبر حذف شده: {invalid_count}")
    print(f"شماره‌های تکراری حذف شده: {duplicate_count}")
    print(f"شماره‌های معتبر نهایی: {valid_count}")

    # ==========================================
    # ذخیره فایل تمیز شده
    # ==========================================

    base_name = os.path.splitext(selected_file)[0]

    clean_file = os.path.join(
        SCRIPT_DIR,
        f"{base_name}_clean.csv"
    )

    output_df.to_csv(
        clean_file,
        index=False,
        header=False,
        encoding="utf-8-sig"
    )

    print("\nفایل تمیز شده ذخیره شد:")
    print(clean_file)

    # ==========================================
    # تقسیم فایل
    # ==========================================

    if valid_count <= MAX_ROWS_PER_FILE:

        print(
            f"\nتعداد شماره‌ها کمتر از {MAX_ROWS_PER_FILE} است."
        )
        print("نیازی به تقسیم فایل نیست.")

    else:

        num_parts = math.ceil(
            valid_count / MAX_ROWS_PER_FILE
        )

        print(
            f"\nدر حال تقسیم فایل به {num_parts} قسمت..."
        )

        for i in range(num_parts):

            start = i * MAX_ROWS_PER_FILE
            end = start + MAX_ROWS_PER_FILE

            chunk = output_df.iloc[start:end]

            output_file = os.path.join(
                SCRIPT_DIR,
                f"{base_name}_part{i + 1}.csv"
            )

            chunk.to_csv(
                output_file,
                index=False,
                header=False,
                encoding="utf-8-sig"
            )

            print(
                f"ذخیره شد: {os.path.basename(output_file)}"
                f" | تعداد: {len(chunk)}"
            )

    print("\n" + "=" * 60)
    print("عملیات با موفقیت پایان یافت")
    print("=" * 60)

except Exception as e:
    print("\nخطا:")
    print(e)

input("\nبرای خروج کلید Enter را فشار دهید...")