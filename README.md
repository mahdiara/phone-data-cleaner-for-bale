# تمیزکننده شماره تلفن برای بله

ابزار Phone Data Cleaner For Bale یک اسکریپت پایتون برای پاکسازی، اعتبارسنجی و آماده‌سازی شماره تلفن‌های ایرانی جهت استفاده در ارسال پیام انبوه در بله است.

## قابلیت‌ها

- تبدیل شماره‌های 09xxxxxxxxx به فرمت استاندارد 989xxxxxxxxx
- حذف شماره‌های نامعتبر
- حذف شماره‌های تکراری
- حذف کاراکترهای اضافی و غیرعددی
- تشخیص خودکار فایل CSV ورودی
- تقسیم خودکار فایل‌های بزرگ به بخش‌های حداکثر 9999 شماره‌ای
- تولید فایل خروجی تمیز و آماده استفاده

## نمونه ورودی

```csv
09123456789
989351234567
test
abc
09121234567
```

## نمونه خروجی

```csv
989123456789
989351234567
989121234567
```

## نحوه استفاده

1. فایل CSV حاوی شماره تلفن‌ها را در کنار فایل `phone-data-cleaner-for-bale.py` قرار دهید.
2. اسکریپت را اجرا کنید.
3. برنامه به صورت خودکار شماره‌ها را پردازش می‌کند.
4. فایل‌های خروجی در همان پوشه ایجاد می‌شوند.

## فایل‌های خروجی

- `*_clean.csv` : شامل تمامی شماره‌های معتبر و تمیز شده
- `*_part1.csv`
- `*_part2.csv`
- `*_part3.csv`
- ...

در صورتی که تعداد شماره‌ها بیشتر از 9999 باشد خروجی به چند فایل تقسیم خواهد شد.

## کاربرد

این ابزار برای آماده‌سازی بانک شماره تلفن جهت ارسال پیام انبوه از طریق ربات‌ها، سامانه‌های اطلاع‌رسانی و سرویس بله طراحی شده است.



# Phone Data Cleaner For Bale

A simple Python utility for preparing Iranian mobile phone numbers for bulk messaging in Bale.

## Features

- Converts 09xxxxxxxxx to 989xxxxxxxxx
- Removes invalid numbers
- Removes duplicates
- Cleans unwanted characters
- Splits large files into chunks of 9999 rows
- Automatically detects CSV files next to the script

## Input Example

```csv
09123456789
989351234567
test
abc
```

## Output Example

```csv
989123456789
989351234567
```

## Usage

1. Place your CSV file next to the script.
2. Run:

```bash
python phone-data-cleaner-for-bale.py
```

3. The script creates:
   - *_clean.csv
   - *_part1.csv
   - *_part2.csv
   - ...

## Target Use Case

Preparing phone number lists for Bale bot bulk messaging.

## License

MIT
