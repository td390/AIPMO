#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Đọc file
with open('/workspace/dev', 'r', encoding='utf-8') as f:
    content = f.read()

# Sửa các lỗi encoding tiếng Việt còn lại
replacements = [
    ('Cáº£nh bÃ¡o', 'Cảnh báo'),
    ('Sprint', 'Sprint'),
    ('JQL', 'JQL'),
    ('Zalo Bot', 'Zalo Bot'),
    ('Deepgram', 'Deepgram'),
    ('Grok 3 Mini', 'Grok 3 Mini')
]

# Thực hiện thay thế
for old_text, new_text in replacements:
    content = content.replace(old_text, new_text)

# Ghi file
with open('/workspace/dev', 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã sửa xong các lỗi tiếng Việt còn lại!")