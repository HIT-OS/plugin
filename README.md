![Langflow](/docs/images/hero.png)

<p align="center" style="font-size: 12px;">
    Langflow là một nền tảng low code mã nguồn mở ứng dụng trong việc xây dựng các sản phẩm ít mã nguồn cho RAG và các ứng dụng multi-agent AI. Sản phẩm này được code dựa trên Python và có thể tích hợp bất kỳ một model, API hay cơ sở dữ liệu nào khi cần thiết.
</p>

<p align="center" style="font-size: 12px;">
    <a href="https://docs.langflow.org" style="text-decoration: underline;">Docs</a> -
    <a href="https://astra.datastax.com/signup?type=langflow" style="text-decoration: underline;">Free Cloud Service</a> -
    <a href="https://docs.langflow.org/get-started-installation" style="text-decoration: underline;">Self Managed</a>

</p>

## ✨ Các tính năng nổi bật của LangFlow

1. **Dựa trên Python** và không phụ thuộc vào mô hình, API, nguồn dữ liệu hoặc cơ sở dữ liệu.
2. **Giao diện IDE trực quan** cho việc xây dựng và thử nghiệm các workflow bằng cách kéo và thả.
3. **Playground** để thử nghiệm và lặp lại các workflow ngay lập tức với điều khiển từng bước.
4. **Quản lý nhiều tác nhân** và điều phối cuộc trò chuyện, cũng như truy xuất dữ liệu.
5. **Dịch vụ đám mây miễn phí** giúp bắt đầu trong vài phút mà không cần thiết lập.
6. **Xuất bản dưới dạng API** hoặc xuất ra ứng dụng Python.
7. **Quan sát** với tích hợp LangSmith, LangFuse hoặc LangWatch.
8. **Bảo mật và khả năng mở rộng cấp doanh nghiệp** với dịch vụ đám mây Langflow miễn phí của DataStax.
9. **Tùy chỉnh workflow** hoặc tạo flow hoàn toàn chỉ bằng Python.
10. **Tích hợp hệ sinh thái** như các thành phần tái sử dụng cho bất kỳ mô hình, API hoặc cơ sở dữ liệu nào.

## **✨ Hướng dẫn sử dụng LangFlow cơ bản**
[![Getting Started](https://github.com/user-attachments/assets/f1adfbe7-3c35-43a4-b265-661f3d4f875f)](https://www.youtube.com/watch?v=kinngWhaUKM)


## Hướng Dẫn Sử Dụng Component: Wikipedia API và Speech to Text

### 1. **Wikipedia API Component**

#### Chức năng:
Component này gọi API của Wikipedia để truy vấn thông tin dựa trên từ khóa đầu vào, trả về danh sách tài liệu (text).

#### Các bước thực hiện:

1. **Cấu hình các tham số đầu vào**:
   - `input_value`: Nhập từ khóa tìm kiếm (ví dụ: "Python programming").
   - `lang`: Chọn ngôn ngữ của kết quả tìm kiếm (mặc định là "en").
   - `k`: Số lượng kết quả tối đa trả về (mặc định là 4).
   - `load_all_available_meta`: Chọn `True` nếu muốn tải toàn bộ metadata liên quan (tùy chọn nâng cao).
   - `doc_content_chars_max`: Giới hạn số ký tự của nội dung tài liệu (mặc định là 4000, tùy chọn nâng cao).

2. **Chạy Component**:
   - Gọi hàm `run_model()` để thực thi việc truy vấn và nhận danh sách kết quả.
   - Kết quả trả về là danh sách tài liệu được nối chuỗi thành một đoạn văn bản.

3. **Tích hợp làm công cụ**:
   - Sử dụng hàm `build_tool()` để xây dựng một công cụ (`Tool`) dựa trên Wrapper của Wikipedia.

#### Ví dụ mã lệnh:
```python
component = WikipediaAPIComponent()
component.input_value = "Artificial Intelligence"
component.lang = "en"
component.k = 5
component.doc_content_chars_max = 5000

# Chạy và lấy kết quả
results = component.run_model()
print("Wikipedia Results:\n", results)
```

---

### 2. **Speech to Text Component**

#### Chức năng:
Component này chuyển đổi giọng nói từ microphone thành văn bản, đồng thời lưu văn bản vào một tệp tin trên hệ thống.

#### Các bước thực hiện:

1. **Cấu hình tham số đầu vào**:
   - `save_path`: Đường dẫn nơi lưu trữ kết quả nhận dạng (mặc định là `~/.cache/langflow/speech_output.txt`).

2. **Chạy Component**:
   - Sử dụng hàm `build_output()` để bắt đầu nhận giọng nói và chuyển đổi sang văn bản.
   - Component sẽ mở microphone, lắng nghe giọng nói, nhận dạng nội dung, và lưu vào tệp tin.

3. **Xử lý lỗi**:
   - Nếu không nhận diện được giọng nói hoặc xảy ra lỗi, thông báo lỗi sẽ được ném ra.

4. **Kiểm tra kết quả**:
   - Văn bản nhận dạng được lưu ở `save_path`.
   - Trạng thái của Component (`self.status`) chứa văn bản nhận dạng.

#### Ví dụ mã lệnh:
```python
component = SpeechToTextComponent()
component.input_value = "/path/to/output.txt"

# Bắt đầu nhận giọng nói
try:
    result = component.build_output()
    print("Recognized Speech:", result.value)
except Exception as e:
    print("Error:", str(e))
```
### 3. Thực hiện thêm component mới
- Nhấn vào **New Custom Component** để thêm vào hệ thống một component mới, thực hiện đẩy code lên vào tạo ra component.
![image](/docs/images/image.png)
---

### Gợi Ý Cấu Hình Môi Trường

#### Các thư viện cần thiết:
- Cài đặt các thư viện cần thiết qua pip:
```bash
pip install langchain langflow speechrecognition platformdirs
```

#### Yêu cầu phần cứng:
- **Wikipedia API**: Chỉ cần kết nối mạng.
- **Speech to Text**: Cần một microphone hoạt động tốt.

#### Lưu ý:
- Đảm bảo microphone đã được cấp quyền truy cập nếu chạy trên hệ điều hành yêu cầu quyền (ví dụ: macOS, Windows).
- Wikipedia API có thể giới hạn số lần gọi trong một thời gian nhất định.

--- 

Bạn có thể kết hợp hai component này để xây dựng một ứng dụng hỗ trợ tìm kiếm thông tin hoặc ghi nhận các câu hỏi được nói trực tiếp từ người dùng.

#### **📬 Liên Hệ và Góp Ý**

Nếu bạn có bất kỳ câu hỏi nào hoặc muốn đóng góp cho dự án, bạn có thể liên hệ qua email hoặc GitHub Issues:
- ✉️ **Email**: 
    - Phạm Đình Tiến: phamdt203@gmail.com
    - Đặng Hoàng Phương: hoangphuong270703@gmail.com
    - Nguyễn Tiến Kiên: tienkiennropro@gmail.com
- 🐙 **GitHub Issues**: [Issue]("https://github.com/HIT-OS/SOS-CONNECT-BE/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=")

