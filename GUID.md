# Hướng dẫn sử dụng English Learning Harness

## Repo này là gì?

Đây là một **hệ thống ghi nhớ và điều phối việc học tiếng Anh cho AI agent**, không phải ứng dụng học tiếng Anh.

- AI agent là người điều phối buổi học.
- Các file Markdown là trí nhớ bền vững của quá trình học.
- Learner tạo ra câu trả lời, tự nhận ra điểm chưa ổn, rồi sửa lại. AI không làm hộ.

Vì vậy, bạn có thể mở repo này trong Codex, Claude Code, Cursor hoặc một AI coding agent tương tự, rồi học trực tiếp bằng hội thoại. Bạn có thể nói tiếng Việt khi trao đổi với agent; phần luyện tập tiếng Anh sẽ dùng lượng tiếng Anh phù hợp với năng lực hiện tại.

## Bắt đầu như thế nào?

1. Mở [learner/PROFILE.md](learner/PROFILE.md) và điền những gì bạn đã biết; có thể để trống mục tiêu nếu chưa rõ.
2. Mở repo bằng AI agent.
3. Trong Codex, bắt đầu bằng `$start`. Ở agent khác, gửi một trong các yêu cầu sau:

   - “Help me start learning English.”
   - “Hãy giúp tôi bắt đầu học tiếng Anh.”
   - “Let’s practise English.”
   - “Review me.”
   - “Assess my progress.”

Lần đầu, `$start` sẽ hỏi trước: **Bạn muốn tiếng Anh giúp bạn làm được điều gì trong vài tháng tới?** Agent có thể hỏi thêm về tình huống thật, người bạn giao tiếp, kênh cần dùng và deadline. Mục tiêu có thể là công việc, học tập, kỳ thi, du lịch, định cư, giao tiếp hằng ngày, sở thích, nội dung giải trí hoặc kết hợp nhiều mục tiêu. Repo không giả định bạn là developer hay thuộc một nghề cụ thể.

Sau khi biết mục tiêu chính, agent mới lấy các mẫu nhỏ ở nghe, đọc, nói, viết qua một hoặc vài buổi. Đây là **placement**: tìm điểm bắt đầu phù hợp, không phải thi chứng chỉ.

## Repo vận hành theo vòng nào?

```text
khám phá mục tiêu và bối cảnh
  → placement nhẹ
  → hồ sơ năng lực theo từng kỹ năng
  → chọn material và lộ trình phù hợp
  → input dễ hiểu
  → retrieval / thực hành không nhìn đáp án
  → tự nhận xét
  → feedback ngắn, trọng tâm
  → learner tự thử lại
  → recall hoặc transfer ở buổi sau
  → cập nhật Markdown khi có evidence hữu ích
```

Điểm quan trọng: `placement`, học ngôn ngữ mới, luyện output, và assessment là các việc khác nhau.

| Việc | Mục đích | AI sẽ làm gì? |
| --- | --- | --- |
| Placement | Biết nên bắt đầu ở đâu | Thu thập mẫu ngắn của 4 kỹ năng; ước lượng thực tế, không cấp chứng chỉ. |
| Học ngôn ngữ mới | Hiểu và bắt đầu sở hữu chunk/cấu trúc mới | Cho input ngắn, dễ hiểu; sau đó đóng nguồn và yêu cầu bạn nhớ hoặc dùng lại. |
| Luyện retrieval / output | Dùng thứ đã hoặc đang học trong tình huống thật | Bạn thử trước, tự nhận xét, nhận 2–3 feedback quan trọng, rồi tự làm lại. |
| Assessment | Kiểm tra tiến bộ dưới điều kiện rõ ràng | Chỉ chạy khi bạn yêu cầu; không hint hay dạy trước khi bạn nộp bài. |

## AI dựa vào những file nào?

| File | Vai trò |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Luật bắt buộc cho AI agent. |
| [learner/PROFILE.md](learner/PROFILE.md) | Mục tiêu chính, tình huống thật, ưu tiên và sở thích của bạn. `$start` hoàn thiện file này trước khi placement. |
| [learner/PROGRESS.md](learner/PROGRESS.md) | Năng lực ước lượng theo nghe/đọc/nói/viết, phase hiện tại, trở ngại và buổi học kế tiếp. |
| [learner/VOCABULARY.md](learner/VOCABULARY.md) | Các chunk/collocation đang học và evidence cho việc dùng chúng. |
| [learner/ERRORS.md](learner/ERRORS.md) | Lỗi lặp lại hoặc lỗi ảnh hưởng lớn đến giao tiếp. |
| [reviews/QUEUE.md](reviews/QUEUE.md) | Các prompt cần gọi lại sau một khoảng thời gian hoặc trong bối cảnh khác. |
| [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) | Hướng chọn material và bài học theo năng lực từng kỹ năng. |
| [sessions/](sessions/) | Bản ghi nguyên vẹn của các buổi học có evidence đáng giữ. |

Không cần đọc mọi file ở mỗi buổi. Agent có trách nhiệm đọc đúng phần cần thiết trước khi chọn bài học.

## Placement nhẹ cho learner mới

Agent sẽ cố gắng có evidence riêng cho bốn kỹ năng. Chúng không cần hoàn thành trong một buổi.

| Kỹ năng | Ví dụ evidence đầu tiên |
| --- | --- |
| Nghe | Nghe audio ngắn có transcript đáng tin, nêu ý chính và vài chi tiết. |
| Đọc | Đọc đoạn vừa sức, nêu ý chính và chi tiết quan trọng. |
| Nói | Tự giới thiệu hoặc nói ngắn về chủ đề quen thuộc, tốt nhất là có recording. |
| Viết | Viết một tin nhắn hoặc mô tả ngắn cho người nhận cụ thể. |

Agent lưu practical estimate riêng cho từng kỹ năng, ví dụ “Listening: roughly A2, confidence medium”. Điều đó hữu ích hơn một nhãn trung bình như “English level: B1”. Các nhãn này không phải CEFR chính thức.

Nếu agent không có audio hoặc bạn không thể gửi recording, agent phải ghi rõ giới hạn đó. Văn bản gõ chỉ là proxy hạn chế cho nói; nó không thay thế hoàn toàn evidence nghe hoặc phát âm.

## Một buổi học thông thường diễn ra thế nào?

Một buổi có thể chỉ tập trung một kỹ năng, hoặc xoay quanh một material để nối nhiều kỹ năng:

```text
audio hoặc đoạn đọc ngắn
  → hiểu ý chính
  → chọn vài chunk thực sự hữu ích
  → recall không nhìn nguồn
  → nói lại hoặc viết trong ngữ cảnh mới
```

Khi bạn đang học **ngôn ngữ hoàn toàn mới**, agent có thể giải thích ngắn trước: nghĩa trong ngữ cảnh, cách kết hợp từ, hoặc phát âm cần thiết. Sau đó agent phải yêu cầu bạn tự nhận ra, gọi lại, hoặc dùng nó mà không nhìn nguồn.

Khi bạn đang **luyện thứ đã biết**, trình tự là:

1. Bạn làm bản đầu tiên không được AI sửa trước.
2. Bạn nói điều mình thấy khó hoặc chưa chắc.
3. Agent chỉ chọn 2–3 điểm có giá trị cao, trích từ chính câu của bạn.
4. Bạn tự thử lại.
5. Agent so sánh ngắn sự tiến bộ và chỉ lưu evidence hữu ích.

AI không nên viết lại toàn bộ câu trả lời của bạn trong buổi luyện bình thường. Bạn có thể yêu cầu rewrite riêng khi mục tiêu là hoàn thành một sản phẩm thực tế, nhưng bản rewrite đó không được coi là evidence về năng lực độc lập.

## Học từ vựng trong repo này

Repo không có vocabulary database hay thuật toán SRS. [learner/VOCABULARY.md](learner/VOCABULARY.md) chỉ giữ các chunk đang thực sự có ích:

```text
New → Learning → Usable
```

Một item tốt thường là chunk hoặc collocation, không chỉ là một cặp dịch nghĩa. Ví dụ, thay vì chỉ ghi `risk`, nên học `pose a risk to ...` trong đúng bối cảnh.

Mỗi item có thể ghi:

- nghĩa hiện tại trong material;
- pattern hoặc collocation hữu ích;
- source;
- evidence bạn đã nhận ra, gọi lại, nói hoặc viết được;
- lần recall/transfer tiếp theo.

Một item chỉ nên được giữ khi nó lặp lại, chặn hiểu ý, hoặc sắp cần trong đời sống/công việc. Không có mục tiêu đếm số từ mỗi ngày.

## Các recipe chính

### Listening

1. Nghe một lần không transcript để nắm ý chính.
2. Nghe lại để lấy một số chi tiết hoặc đánh dấu chỗ không chắc.
3. Xem transcript và xác định lý do bỏ lỡ: từ mới, biết từ nhưng không nghe ra, nối âm, câu quá dài, suy luận hoặc mất tập trung.
4. Học 3–5 chunk hoặc sound feature cần thiết.
5. Nghe lại không transcript và kể lại ngắn.

### Reading

1. Đọc không dùng từ điển và nêu ý chính.
2. Chỉ đánh dấu những từ/cụm thực sự chặn ý nghĩa hoặc nhiệm vụ.
3. Xem chúng trong ngữ cảnh, rồi đọc lại.
4. Đóng văn bản và tóm tắt từ trí nhớ.
5. Trả lời một câu transfer bằng bối cảnh, người nghe hoặc góc nhìn khác.

### Speaking

Tiến trình đi từ giới thiệu bản thân và chủ đề quen thuộc, đến mô tả hoạt động/sự kiện, hỏi làm rõ, cập nhật tình hình, giải thích một quy trình hoặc so sánh lựa chọn, rồi mới đến thảo luận và trình bày phức tạp. Nội dung cụ thể luôn theo mục tiêu bạn đã chọn. Recording và first take có giá trị hơn một bài mẫu được AI viết sẵn.

### Writing

Tiến trình đi từ câu liên kết, tin nhắn thực tế, đoạn giải thích, email/update phù hợp bối cảnh, đến proposal hoặc document theo đối tượng. Trước mỗi bài, cần xác định người đọc và mục đích; sau feedback, learner tự sửa.

Chi tiết routing theo level nằm ở [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md).

## Khi nào repo được cập nhật?

Agent chỉ cập nhật khi có thông tin bền vững và có ích:

- Buổi học có attempt/retry, assessment, hoặc delayed review đáng giữ → thêm file trong `sessions/`.
- Năng lực, phase, priority, bottleneck hoặc next action thay đổi → cập nhật `PROGRESS.md`.
- Có chunk đang học cùng evidence → cập nhật `VOCABULARY.md`.
- Lỗi lặp lại hoặc lỗi chặn giao tiếp đáng kể → cập nhật `ERRORS.md`.
- Có thứ cần gọi lại sau hoặc chuyển sang ngữ cảnh khác → cập nhật `reviews/QUEUE.md`.

Một câu hỏi nhỏ, tra nghĩa, hoặc buổi dở dang không cần tạo hồ sơ chỉ để “đủ thủ tục”. Repo ưu tiên evidence thật hơn bookkeeping.

## Bảo mật và quyền riêng tư

Không đưa vào repo hoặc gửi cho agent các thông tin nhạy cảm không cần thiết: credentials, bí mật công ty, dữ liệu khách hàng, audio/transcript chưa được phép, hoặc tài liệu nội bộ nguyên vẹn. Hãy ẩn danh hoặc rút ngắn ví dụ công việc trước khi dùng chúng để luyện tiếng Anh.

## Tài liệu dành cho agent

Nếu bạn muốn hiểu sâu cách agent ra quyết định, xem:

- [docs/METHOD.md](docs/METHOD.md): triết lý học và bằng chứng.
- [docs/WORKFLOW.md](docs/WORKFLOW.md): trình tự agent phải theo trong một session.
- [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md): cách chọn bài học theo năng lực.
- [AGENTS.md](AGENTS.md): các quy tắc không được phá vỡ.

Bạn không cần điều khiển các file này trong lúc học. Chỉ cần nói rõ mục tiêu, làm bản đầu tiên của mình, và cho agent biết khi material quá dễ, quá khó hoặc không liên quan.
