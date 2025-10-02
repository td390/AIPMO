#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Đọc file
with open('/workspace/dev', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Tìm và thay thế dòng chứa button cũ
for i, line in enumerate(lines):
    if 'class="back"' in line and 'menu PMO' in line:
        # Thay thế dòng này bằng header mới
        lines[i] = '''  <!-- Header đồng bộ -->
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
  </header>
'''

# Ghi file
with open('/workspace/dev', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Đã cập nhật header thành công!")