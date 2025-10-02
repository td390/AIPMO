#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Đọc file
with open('/workspace/dev', 'r', encoding='utf-8') as f:
    content = f.read()

# Thay thế button cũ bằng header mới - sử dụng regex để tìm pattern
import re

# Pattern để tìm button cũ
pattern = r'<a class="back" href="/">.*?menu PMO</a>'
replacement = '''<!-- Header đồng bộ -->
  <header class="top">
    <div class="row">
      <div class="brand">
        <div class="logo">
          <img src="https://z-cdn-media.chatglm.cn/files/1a1ab789-5429-451f-bb53-65e73a39e4bd_pasted_image_1758225809744.png"
               alt="BIDV" onerror="this.style.display='none'">
        </div>
        <h1 class="title">Công cụ AI cho PMO</h1>
      </div>
      <nav class="nav">
        <a href="/"><i class="fa-solid fa-home"></i>&nbsp;Trang chủ</a>
        <a href="/meetingnote"><i class="fa-solid fa-microphone-lines"></i>&nbsp;Meeting Note</a>
        <a href="/risk"><i class="fa-solid fa-triangle-exclamation"></i>&nbsp;Risk Management</a>
        <a href="/chatbot"><i class="fa-solid fa-robot"></i>&nbsp;Chat Bot</a>
      </nav>
    </div>
  </header>'''

# Thay thế
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Thay thế button trong chatbot page
old_button2 = '<a href="/" class="btn ghost"><i class="fa-solid fa-house"></i>Về menu PMO</a>'
new_button2 = '<a href="/" class="btn ghost"><i class="fa-solid fa-house"></i>Trang chủ</a>'
content = content.replace(old_button2, new_button2)

# Ghi file
with open('/workspace/dev', 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã cập nhật header thành công!")