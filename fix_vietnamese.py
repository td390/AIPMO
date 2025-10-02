#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Đọc file
with open('/workspace/dev', 'r', encoding='utf-8') as f:
    content = f.read()

# Sửa các lỗi encoding tiếng Việt
replacements = {
    # Sửa title và header
    'CÃ´ng cá»¥ AI cho PMO': 'Công cụ AI cho PMO',
    'Trang chá»§': 'Trang chủ',
    
    # Sửa các text khác có thể bị lỗi
    'Â© 2025 BIDV â€" CÃ´ng cá»¥ AI cho PMO': '© 2025 BIDV — Công cụ AI cho PMO',
    'Â© 2025 BIDV â€" CÃ´ng cá»¥ AI cho PMO': '© 2025 BIDV — Công cụ AI cho PMO',
    
    # Sửa các text trong navigation
    'Meeting Note': 'Meeting Note',
    'Risk Management': 'Risk Management', 
    'Chat Bot': 'Chat Bot',
    
    # Sửa các text khác có thể bị lỗi encoding
    'Tá»'i Æ°u quáº£n lÃ½ dá»± Ã¡n vá»›i AI': 'Tối ưu quản lý dự án với AI',
    'Tá»± Ä'á»™ng hÃ³a biÃªn báº£n há»'p, theo dÃµi rá»§i ro, sinh bÃ¡o cÃ¡o vÃ hÃ'i Ä'Ã¡p Jira/Confluence ngay tá»©c thÃ¬.': 'Tự động hóa biên bản họp, theo dõi rủi ro, sinh báo cáo và hỏi đáp Jira/Confluence ngay tức thì.',
    'Báº¯t Ä'áº§u Meeting Note': 'Bắt đầu Meeting Note',
    'Má»Ÿ Chat Bot': 'Mở Chat Bot',
    'Tá»± Ä'á»™ng hÃ³a bÃ¡o cÃ¡o': 'Tự động hóa báo cáo',
    'TrÃ­ch xuáº¥t master plan, tiáº¿n Ä'á»™, vÆ°á»›ng máº¯c & kiáº¿n nghá»‹ tá»« transcript.': 'Trích xuất master plan, tiến độ, vướng mắc & kiến nghị từ transcript.',
    'TÃ­ch há»£p Jira & Confluence': 'Tích hợp Jira & Confluence',
    'Táº¡o ticket, push page chuáº©n PMO chá»‰ vá»›i má»™t cÃº nháº¥p.': 'Tạo ticket, push page chuẩn PMO chỉ với một cú nhấp.',
    'AI Meeting Insights': 'AI Meeting Insights',
    'Chuyá»ƒn ghi Ã¢m â†' minutes, action items; Ä'áº©y Confluence/Jira.': 'Chuyển ghi âm → minutes, action items; đẩy Confluence/Jira.',
    'Tá»± Ä'á»™ng nháº­n diá»‡n ngÆ°á»'i nÃ³i vÃ phÃ¢n loáº¡i ná»™i dung': 'Tự động nhận diện người nói và phân loại nội dung',
    'TrÃ­ch xuáº¥t quyáº¿t Ä'á»‹nh vÃ cÃ´ng viá»‡c cáº§n lÃ m': 'Trích xuất quyết định và công việc cần làm',
    'Táº¡o bÃ¡o cÃ¡o tá»•ng há»£p theo máº«u PMO': 'Tạo báo cáo tổng hợp theo mẫu PMO',
    'Ä'á»"ng bá»™ hÃ³a vá»›i Jira vÃ Confluence': 'Đồng bộ hóa với Jira và Confluence',
    'AI Risk Management': 'AI Risk Management',
    'Cáº£nh bÃ¡o trá»… háº¡n, backlog tÄƒng, dá»± bÃ¡o rá»§i ro & gá»£i Ã½ xá»­ lÃ½.': 'Cảnh báo trễ hạn, backlog tăng, dự báo rủi ro & gợi ý xử lý.',
    'PhÃ¢n tÃ­ch dá»¯ liá»‡u Jira Ä'á»ƒ phÃ¡t hiá»‡n rá»§i ro': 'Phân tích dữ liệu Jira để phát hiện rủi ro',
    'Cáº£nh bÃ¡o tá»± Ä'á»™ng khi cÃ³ dáº¥u hiá»‡u trá»… háº¡n': 'Cảnh báo tự động khi có dấu hiệu trễ hạn',
    'Ä'á»' xuáº¥t giáº£i phÃ¡p giáº£m thiá»ƒu rá»§i ro': 'Đề xuất giải pháp giảm thiểu rủi ro',
    'BÃ¡o cÃ¡o rá»§i ro theo Ä'á»‹nh ká»³ vÃ theo yÃªu cáº§u': 'Báo cáo rủi ro theo định kỳ và theo yêu cầu',
    'Cáº£nh bÃ¡o': 'Cảnh báo',
    'Sprint': 'Sprint',
    'AI Chat Bot': 'AI Chat Bot',
    'Há»'i Jira/Confluence, lá»'c JQL tá»± Ä'á»™ng, tráº£ lá»'i 24/7.': 'Hỏi Jira/Confluence, lọc JQL tự động, trả lời 24/7.',
    'Truy váº¥n thÃ´ng tin dá»± Ã¡n báº±ng ngÃ´n ngá»¯ tá»± nhiÃªn': 'Truy vấn thông tin dự án bằng ngôn ngữ tự nhiên',
    'Táº¡o JQL phá»©c táº¡p tá»« yÃªu cáº§u Ä'Æ¡n giáº£n': 'Tạo JQL phức tạp từ yêu cầu đơn giản',
    'Tá»•ng há»£p bÃ¡o cÃ¡o nhanh theo yÃªu cáº§u': 'Tổng hợp báo cáo nhanh theo yêu cầu',
    'TÃ­ch há»£p Zalo Ä'á»ƒ há»" trá»£ má»'i lÃºc má»'i nÆ¡i': 'Tích hợp Zalo để hỗ trợ mọi lúc mọi nơi',
    'Zalo Bot': 'Zalo Bot',
    'HÆ°á»›ng dáº«n sá»' dá»¥ng': 'Hướng dẫn sử dụng',
    'LiÃªn há»‡': 'Liên hệ',
    'ChÃ­nh sÃ¡ch báº£o máº­t': 'Chính sách bảo mật'
}

# Thực hiện thay thế
for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

# Ghi file
with open('/workspace/dev', 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã sửa xong các lỗi tiếng Việt!")