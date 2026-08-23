# Hướng dẫn sử dụng English Learning Harness

## Repo này là gì?

Đây là một **hệ thống ghi nhớ và điều phối việc học tiếng Anh cho AI agent**, không phải ứng dụng học tiếng Anh.

- AI agent là người chọn bước học phù hợp.
- Các file Markdown là trí nhớ bền vững.
- Learner tạo ra câu trả lời, tự nhận ra vấn đề và tự sửa.
- Mọi bài học phải nối được với mục tiêu thật và bước tiếp theo.

Repo không có database, scheduler, thuật toán SRS hay analytics. Agent là runtime; Markdown là source of truth. Bạn có thể dùng tiếng Việt để trao đổi với agent, còn lượng tiếng Anh trong bài sẽ được điều chỉnh theo evidence hiện có.

## Bắt đầu

1. Mở repo bằng Codex, Claude Code, Cursor hoặc một AI agent tương tự.
2. Trong Codex, gọi `$learn`. Ở agent khác, chỉ cần nói: “Hãy giúp tôi học tiếng Anh.”
3. Tiếp tục dùng cùng một lệnh hoặc yêu cầu tự nhiên cho các buổi sau.

Lần đầu, bạn chỉ cần cung cấp ba input chính: việc cụ thể muốn làm bằng tiếng Anh, deadline, và số buổi/phút có thể học cùng lịch ưu tiên. Agent tự draft conditions, acceptance criteria và evidence để bạn xác nhận. Khi thực tế cho phép, buổi đầu cũng có một micro-diagnostic hoặc micro-practice 3–5 phút; nó không chỉ là một cuộc phỏng vấn lập kế hoạch.

Bạn không cần nhớ các lệnh riêng cho onboarding, diagnostic, study, review hay assessment. `$learn` tự chọn mode phù hợp:

```text
mục tiêu còn thiếu?          → onboarding
baseline chưa đủ?            → diagnostic thích ứng
đến hạn review tuần?         → recall ngắn nếu cần evidence, rồi weekly review
còn recall/transfer đến hạn? → delayed review
còn lại                      → bài học tốt nhất hôm nay
```

Nếu bạn nói rõ “Tôi muốn assessment”, agent sẽ chạy một bài kiểm tra có điều kiện rõ ràng và không hỗ trợ trong lúc làm.

## Goal contract: phải biết học để làm gì

“Cải thiện tiếng Anh” là lý do, chưa phải goal có thể dùng để lập plan. Trước khi tạo một chu kỳ dài hạn, agent sẽ giúp bạn xác định:

- **Context:** dùng tiếng Anh ở đâu, với ai.
- **Observable outcome:** một việc thật có thể quan sát được.
- **Conditions:** có script hay không, thời lượng, tốc độ, domain hoặc áp lực.
- **Acceptance criteria:** thế nào là đủ tốt.
- **Deadline:** khi nào cần đạt hoặc review lại.
- **Evidence:** recordings, drafts hoặc task tương đương để so sánh.
- **Time budget:** số buổi mỗi tuần, số phút mỗi buổi và giới hạn lịch học.

Time budget nên có preferred days, preferred time, timezone và fallback nếu bỏ lỡ một buổi. Khi đủ dữ liệu, next action dùng ngày/giờ cụ thể thay vì “lúc rảnh”.

Ví dụ:

```text
Trong 12 tuần, trình bày project update 5 phút
không dùng full script và trả lời ba follow-up questions.
Người nghe phải hiểu được key message, progress, blocker và next step.
Lưu recordings ở các mốc để so sánh.
```

Bạn vẫn có thể bắt đầu học hoặc làm diagnostic khi contract chưa hoàn chỉnh. Agent chỉ không được tự bịa một long-term plan khi chưa biết đích đến.

## Dashboard trung tâm

[learner/LEARNING_STATE.md](learner/LEARNING_STATE.md) trả lời các câu hỏi quan trọng nhất:

- Mục tiêu thật hiện tại là gì?
- Deadline và time budget là bao nhiêu?
- Nghe, đọc, nói, viết và vocabulary đang ở đâu?
- Gap và bottleneck nào đang chặn goal?
- Chu kỳ, skill plan theo frequency và các session cụ thể tuần này là gì?
- Evidence nào đã có?
- Việc nhỏ nhất cần làm tiếp theo là gì, mất bao lâu và tại sao?

Agent mới vào repo chỉ cần đọc dashboard cùng các file learner liên quan là có thể tiếp tục đúng hướng.

## Các file chính

| File | Vai trò |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Luật bắt buộc cho agent. |
| [learner/PROFILE.md](learner/PROFILE.md) | Bối cảnh, giới hạn và sở thích tương đối ổn định. |
| [learner/LEARNING_STATE.md](learner/LEARNING_STATE.md) | Goal contract, baseline, skill plan, lịch session tuần này và next action. |
| [learner/VOCABULARY.md](learner/VOCABULARY.md) | Chunk/collocation đang học và evidence theo từng kênh. |
| [learner/ERRORS.md](learner/ERRORS.md) | Pattern lặp lại hoặc ảnh hưởng lớn. |
| [reviews/QUEUE.md](reviews/QUEUE.md) | Source of truth duy nhất cho thời điểm, prompt và acceptance criteria của recall/transfer. |
| [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) | Diagnostic ladder, material rule và recipe theo kỹ năng. |
| [sessions/](sessions/) | Raw attempt, learner retry và evidence của các buổi có ý nghĩa. |
| [.agents/skills/learn/SKILL.md](.agents/skills/learn/SKILL.md) | Một skill duy nhất dành cho learner. |

## Diagnostic thích ứng

Agent không dùng một task B1 cố định để buộc learner A1 thất bại. Mỗi kỹ năng bắt đầu bằng một task vừa sức:

```text
learner xử lý được?
  ├── không → dừng, đơn giản hóa hoặc hạ một bậc
  └── có    → ghi evidence và tăng một yếu tố nếu cần
```

Evidence được giữ riêng:

| Kỹ năng | Evidence ví dụ |
| --- | --- |
| Listening | Audio thật: gist, details, timestamp bị miss và nguyên nhân. |
| Reading | Main idea, structure, details; ở level cao thêm claim/evidence/inference. |
| Speaking | Câu trả lời tự nói, tốt nhất có recording và follow-up. |
| Writing | Draft không hỗ trợ cho audience và purpose rõ ràng. |
| Vocabulary | Nhận ra trong nghe/đọc và retrieve trong nói/viết. |

Reading B2 không tự động có nghĩa Speaking cũng B2. Typed answer chỉ là proxy hạn chế cho speaking; văn bản viết không thể thay listening evidence. Mọi CEFR-style estimate chỉ là nhãn làm việc, không phải chứng chỉ.

Tất cả kỹ năng dùng cùng schema: `A0–A1 Foundation`, `A2 Basic`, `B1 Independent`, `B2 Flexible`, `C1+ Advanced`. Nếu host không có audio hoặc recording, agent ghi `Environment-limited` cho evidence đó và vẫn lập provisional plan từ các kỹ năng đo được; không mắc loop diagnostic vô hạn.

Diagnostic phải dẫn đến plan nhìn thấy được:

```text
skill profile → goal gap → cycle direction
→ weekly frequency theo kỹ năng → session cụ thể → next task
```

Nếu agent chỉ trả về “Bạn khoảng A2” rồi dừng, diagnostic chưa hoàn thành.

## Một buổi học hằng ngày

Trước khi bắt đầu, agent sẽ nói ngắn:

- hôm nay làm task gì;
- mất khoảng bao lâu;
- vì sao task này nối với goal hoặc focus tuần;
- evidence độc lập nào cần tạo ra.

Một buổi có thể tích hợp nhiều kỹ năng quanh một material:

```text
retrieve chunk đến hạn
  → nghe hoặc đọc để hiểu
  → sửa một vài gap quan trọng
  → đóng source
  → nói lại hoặc viết cho tình huống thật
  → tự nhận xét
  → feedback ngắn
  → learner tự thử lại
```

Agent không ép buổi nào cũng phải đủ cả bốn kỹ năng. Evidence vẫn phải được ghi đúng kênh thay vì kết luận chung chung “hôm nay học tốt”.

## Hai vòng học khác nhau

### Ngôn ngữ thật sự mới

```text
input nhỏ và dễ hiểu
  → kiểm tra hiểu
  → đóng source
  → retrieve hoặc dùng lại
```

AI được phép giải thích nghĩa, sound, collocation hoặc register vừa đủ trước. Phần giải thích và việc lặp khi còn nhìn đáp án không phải evidence độc lập.

### Ngôn ngữ đã biết hoặc đã luyện

1. Learner làm attempt đầu tiên không được sửa trước.
2. Learner tự nói điểm khó hoặc chưa chắc.
3. Agent chọn tối đa hai hoặc ba vấn đề quan trọng từ chính câu của learner.
4. Learner tự làm lại.

AI không wholesale rewrite trong practice thông thường. Nếu bạn cần AI rewrite một sản phẩm thật, bản đó không được dùng để kết luận năng lực độc lập.

## Vocabulary là foundation

Vocabulary không phải “môn thứ năm” và không phải danh sách từ–nghĩa. Repo ưu tiên chunk/collocation khi nó:

- xuất hiện lặp lại;
- chặn main task hoặc reasoning;
- kết hợp hữu ích với vốn từ hiện có;
- có khả năng dùng trong vài tuần tới;
- quan trọng với domain hoặc goal.

Ví dụ, `pose a risk to ...` thường hữu ích hơn chỉ lưu `risk`.

Mỗi item có thể có evidence riêng:

- nhận ra trong speech mới;
- hiểu trong reading context mới;
- retrieve và dùng trong speaking;
- dùng đúng form/register trong writing;
- transfer sau một khoảng delay.

Repo dùng lifecycle nhẹ `New → Learning → Usable`; không giả vờ là một SRS engine.

`VOCABULARY.md` chỉ lưu knowledge/evidence. Khi một item cần test lại, nó liên kết tới `reviews/QUEUE.md`; chỉ queue lưu due date, prompt và acceptance criteria. Trong một buổi 25–45 phút, agent thường không đưa quá 5–8 chunk hoàn toàn mới, và dùng ít hơn khi learner mới bắt đầu hoặc đã có nhiều recall đến hạn.

Khoảng review phụ thuộc performance:

- recall dễ và chính xác → lùi xa hơn;
- đúng nhưng còn gắng sức → giữ interval tương tự;
- fail lặp lại → review sớm hơn, đơn giản hóa hoặc sửa prerequisite;
- nhận ra nhưng chưa dùng được → thêm production task.

## Recipe chính

### Listening

1. Nghe lần một không transcript để lấy gist.
2. Nghe lần hai để lấy details và đánh dấu timestamp chưa chắc.
3. Phân loại nguyên nhân: từ mới, biết nhưng không nghe ra, connected speech, câu dài, attention, inference hoặc background knowledge.
4. Mở transcript để repair đúng chỗ.
5. Đóng transcript, nghe lại và retell/respond.
6. Dùng audio tương tự ở buổi sau để test transfer.

Ngoài intensive listening ngắn và inspectable, plan nên có extensive listening dài hơn, nhẹ hơn và tập trung vào ý nghĩa.

### Reading

1. First pass: hiểu purpose, structure và main idea; chỉ đánh dấu blocker.
2. Second pass: tra item recurring, domain-critical hoặc reasoning-critical.
3. Đóng dictionary và reconstruct nội dung.
4. Ở level cao, phân biệt điều text hỗ trợ, inference hợp lý và claim không được hỗ trợ; xem evidence, assumption và trade-off.

### Speaking

Progression đi từ sound/chunk rõ ràng → câu trả lời ngắn → topic quen thuộc lặp lại → explanation kết nối → follow-up, clarification và repair → interaction theo goal.

`LEARNING_STATE.md` giữ một topic bank nhỏ với trạng thái `untested`, `developing`, `stable` hoặc `transfer needed`. Recording và first take có giá trị hơn một model monologue.

### Writing

```text
audience + purpose + criteria
  → unaided draft
  → learner kiểm tra task/facts
  → structure
  → language/register
  → learner tự revise
  → parallel task về sau
```

Giữ cả draft đầu và learner revision.

## Weekly Review

Cuối mỗi tuần học, agent không chỉ đếm số giờ. Agent xem evidence theo bốn phần, mỗi phần 0–2:

- **Completion:** task quan trọng có được thực hiện không?
- **Quality:** meaning và acceptance criteria đạt đến đâu?
- **Retention:** có recall không hỗ trợ sau delay không?
- **Transfer:** có dùng được trong context khác không?

Agent cũng xem lỗi lặp lại, lỗi đang cải thiện, lỗi mới, material fit và năng lượng/recovery. Sau đó chỉ **thay đổi một điều quan trọng** cho tuần tiếp theo: difficulty, phân bổ kỹ năng, material, support, session duration hoặc review spacing.

Nếu một recall ngắn đang đến hạn có thể cung cấp retention evidence cho weekly review và vừa session budget, agent chạy recall đó trước rồi mới chấm tuần.

Một tuần tệ không tự động làm mất hiệu lực toàn bộ plan.

## Kết thúc buổi học

Mọi meaningful session phải để lại:

- next task nhỏ nhất;
- expected duration;
- material nếu đã biết;
- evidence và acceptance criteria;
- lý do task đó đứng tiếp theo;
- ngày/giờ cụ thể theo timezone khi đã có lịch ưu tiên, hoặc điều kiện delay nếu chưa thể chốt lịch.

Agent cập nhật:

- session record khi có evidence đáng giữ;
- `LEARNING_STATE.md` khi goal, baseline, skill plan, lịch tuần, bottleneck hoặc next action thay đổi;
- `VOCABULARY.md` và `ERRORS.md` chỉ khi có evidence thật; `reviews/QUEUE.md` khi timing hoặc prompt review thay đổi.

Một câu hỏi nhỏ, tra nghĩa hoặc bài bỏ dở không cần tạo hồ sơ cho đủ thủ tục.

## Reminder

Repo quyết định và lưu thời điểm học tiếp theo. Nếu môi trường đang dùng hỗ trợ reminder, agent có thể hỏi bạn có muốn được nhắc không. Việc gửi notification thuộc host; repo không xây scheduler riêng.

## Bảo mật

Không đưa credentials, bí mật công ty, dữ liệu khách hàng, recordings/transcripts chưa được phép hoặc tài liệu nội bộ nguyên vẹn vào repo. Hãy ẩn danh và rút gọn ví dụ thật trước khi dùng để học.
