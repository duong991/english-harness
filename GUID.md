# Hướng dẫn sử dụng English Learning Harness

## Repo này là gì?

Đây là một **hệ thống ghi nhớ và điều phối việc học tiếng Anh cho AI agent**, không phải ứng dụng học tiếng Anh.

- AI agent là người chọn bước học phù hợp.
- Các file Markdown là trí nhớ bền vững.
- Learner tạo ra câu trả lời, tự nhận ra vấn đề và tự sửa.
- Mọi bài học phải nối được với mục tiêu thật và bước tiếp theo.

Repo không có database, scheduler, thuật toán SRS hay analytics. Agent là runtime; Markdown là source of truth. Bạn có thể dùng tiếng Việt để trao đổi với agent, còn lượng tiếng Anh trong bài sẽ được điều chỉnh theo evidence hiện có.

## Bắt đầu

1. Mở repo bằng **Antigravity**, **Codex**, **Claude Code**, **Cursor** hoặc một AI agent tương tự.
2. Trong Antigravity/Codex, gọi `$learn`. Ở agent khác, chỉ cần nói: “Hãy giúp tôi học tiếng Anh.”
3. Tiếp tục dùng cùng một lệnh hoặc yêu cầu tự nhiên cho các buổi sau.

Lần đầu, bạn chỉ cần cung cấp ba input chính: việc cụ thể muốn làm bằng tiếng Anh, deadline, và số buổi/phút có thể học cùng lịch ưu tiên. Agent tự draft conditions, acceptance criteria và evidence để bạn xác nhận. Khi thực tế cho phép, buổi đầu cũng có một micro-diagnostic hoặc micro-practice 3–5 phút; nó không chỉ là một cuộc phỏng vấn lập kế hoạch.

Bạn không cần nhớ các lệnh riêng cho onboarding, diagnostic, study, review hay assessment. `$learn` tự chọn mode phù hợp:

```text
mục tiêu còn thiếu?          → onboarding
baseline chưa đủ?            → diagnostic thích ứng (rubric 5 chiều 0–2)
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
- Chu kỳ, skill plan, vocabulary cycle và các session cụ thể tuần này là gì?
- Listening/Reading tuần này dùng item hoặc excerpt cụ thể nào, và tại sao?
- Evidence nào đã có?
- Việc nhỏ nhất cần làm tiếp theo là gì, mất bao lâu và tại sao?

Agent mới vào repo chỉ cần đọc dashboard cùng các file learner liên quan là có thể tiếp tục đúng hướng.

## Các file chính

| File | Vai trò |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Luật bắt buộc cho agent. |
| [learner/PROFILE.md](learner/PROFILE.md) | Bối cảnh, giới hạn và sở thích tương đối ổn định. |
| [learner/LEARNING_STATE.md](learner/LEARNING_STATE.md) | Goal contract, baseline, skill/vocabulary plan, lịch session, material tuần này và next action. |
| [learner/VOCABULARY.md](learner/VOCABULARY.md) | Chunk/collocation, verification provenance và evidence theo từng kênh. |
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
→ weekly frequency theo kỹ năng → session + material cụ thể → next task
```

Nếu agent chỉ trả về “Bạn khoảng A2” rồi dừng, diagnostic chưa hoàn thành.

## Một buổi học hằng ngày & English Task Card

Trước khi bắt đầu buổi học tương tác, agent và learner thiết lập **English Task Card** để giới hạn rõ vai trò của AI:

- **AI may (Được phép):** Gợi ý tối thiểu khi tắc, đặt câu hỏi phản biện/làm rõ, chỉ ra lỗi sai, tạo bài tập song song.
- **AI may not (Bị cấm):** Trả lời thay, tự hoàn thiện câu của learner, viết lại toàn bộ bài (wholesale rewrite), tự bịa nguồn.

```text
retrieve chunk đến hạn
  → nghe hoặc đọc để hiểu
  → sửa một vài gap quan trọng (phân loại rào cản)
  → đóng source
  → nói lại hoặc viết cho tình huống thật
  → tự nhận xét
  → feedback ngắn (tối đa 2-3 điểm)
  → learner tự thử lại
```

Agent không ép buổi nào cũng phải đủ cả bốn kỹ năng. Evidence vẫn phải được ghi đúng kênh thay vì kết luận chung chung “hôm nay học tốt”.

## Material Selection + Evidence Contract

Với Listening hoặc Reading, agent phải chọn một item cụ thể hoặc một excerpt chính xác. Agent không được giao: “hãy tự tìm podcast B1”, cũng không dump nhiều link.

Material được chọn theo sáu yếu tố:

- phục vụ goal hiện tại;
- vừa level, challenging nhưng finishable;
- vừa session time;
- có chunk/language value đáng học;
- có transcript/captions/text để kiểm tra khi task cần;
- hợp topic, domain hoặc sở thích.

Trước task, agent đưa material/link, duration hoặc reading time, intensive/extensive mode, lý do chọn, difficulty và evidence cần tạo. Nếu source quá dài, agent phải chỉ rõ excerpt. Intensive listening không có transcript/captions đáng tin thì không dùng.

`LEARNING_STATE.md` lưu material của tuần để tránh nhảy nguồn ngẫu nhiên. `PROFILE.md` giữ một source pool nhỏ: topic, format và nguồn đã phù hợp trước đó.

Chỉ xem hết video hoặc đọc hết bài không có nghĩa task hoàn thành:

- Intensive Listening cần gist lần đầu, details, vị trí chưa chắc, error classification và retelling khi đã đóng transcript.
- Intensive Reading cần gist lần đầu, structure/sequence, reconstruction không nhìn bài và bảng kiểm chứng 3 cột.
- Extensive Listening/Reading chỉ cần gist hoặc reaction ngắn và một note về material fit; không biến hoạt động thưởng thức thành homework chi tiết.

Khi hữu ích, agent dùng score 0–2 nhẹ để chọn next task, không phải gamification. Delayed check dùng material mới có độ khó và capability demand tương tự, không chỉ bật lại source cũ.

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

### Chu kỳ 4 lần tiếp xúc (4 Encounters)

Để một chunk từ vựng trở nên `Usable`, quy trình chuẩn cần 4 lần tiếp xúc trải dài:

| Thời điểm | Hành động | Bằng chứng kỳ vọng |
| --- | --- | --- |
| **Day 0** | Nhớ nghĩa từ văn cảnh và đọc to câu chứa chunk | Nghĩa chính xác và ghi âm phát âm rõ ràng |
| **Day 1** | Đóng source, điền từ vào chỗ trống + tự đặt 1 câu cá nhân | Khả năng tự truy xuất và đúng cấu trúc |
| **Day 3** | Chọn đúng collocation trong một chủ đề/ngữ cảnh mới | Chuyển giao ngữ cảnh (Transfer) |
| **Day 7** | Sử dụng tự nhiên trong bài nói 60s hoặc đoạn văn ngắn | Ứng dụng tự nhiên dưới áp lực nhận thức |

Với item quan trọng, agent phải kiểm tra sense, pronunciation, collocation và register bằng learner dictionary, trusted source hoặc real corpus. Một collocation do AI tạo ra chỉ là candidate; nếu chưa kiểm tra, item phải ghi `Unverified`.

`VOCABULARY.md` chỉ lưu knowledge/evidence. Khi một item cần test lại, nó liên kết tới `reviews/QUEUE.md`; chỉ queue lưu due date, prompt và acceptance criteria.

## Recipe chính

### Listening: Gist → Inspect → Repair → Retell

1. **Nghe lần một** không transcript/subtitles để nắm ý chính (Gist) và các chi tiết nhớ được.
2. **Nghe lần hai** đánh dấu các mốc thời gian (timestamps) bị miss hoặc chưa chắc.
3. **Phân loại vào 5 rào cản nghe:**
   - **Unknown language:** Từ vựng, cụm từ hoặc ngữ pháp chưa từng học.
   - **Known but not heard:** Nhìn mặt chữ thì biết, nhưng tai không nhận ra âm thanh ở tốc độ nói thật.
   - **Connected speech & rhythm:** Nối âm, nuốt âm, trọng âm câu, biến âm, ngắt cụm (chunking).
   - **Attention & load:** Câu quá dài, nhiều thông tin dồn dập, quá tải trí nhớ ngắn hạn.
   - **Background knowledge:** Thiếu kiến thức chuyên ngành hoặc bối cảnh văn hóa của chủ đề.
4. Mở transcript để **repair đúng chỗ**.
5. Đóng transcript, nghe lại và **retell/respond**.
6. Dùng audio tương tự ở buổi sau để kiểm tra transfer.

### Reading: Structure → Blockers → Reasoning → Reconstruction

1. **First pass:** Đọc lướt không dùng từ điển, nắm ý chính và đánh dấu blocker.
2. **Second pass:** Tra cứu chỉ những từ/chunk then chốt ảnh hưởng đến lập luận.
3. Đóng bài đọc và từ điển, **tự tái cấu trúc (reconstruct)** nội dung.
4. Với bài đọc B1+ nâng cao, lập **Bảng kiểm chứng 3 cột (3-Column Verification Table)** kèm trích dẫn đoạn/dòng:
   - **Văn bản hỗ trợ rõ ràng (Explicitly Supported):** Dữ kiện/luận điểm nêu trực tiếp trong bài.
   - **Suy luận hợp lý (Reasonable Inference):** Kết luận logic dựa trên manh mối của bài.
   - **Không có căn cứ (Unsupported / False):** Giả định không được bài viết chứng minh.

### Speaking: IPA/Phonics & Giao thức 6 vòng phản xạ

#### Bảng tra nhanh Phonics / IPA cơ bản

- **15 Nguyên âm:**
  - `/ɑ/` (cop, father), `/ə/` (the - không nhấn), `/ʌ/` (cup, sun - có nhấn)
  - `/u/` (boot), `/ʊ/` (book), `/i/` (beat), `/ɪ/` (bit)
  - `/eɪ/` (make), `/e/` (head), `/æ/` (had, cat), `/ɔ/` (law)
  - `/aʊ/` (now), `/aɪ/` (bite), `/ɔɪ/` (boy), `/oʊ/` (go)
- **Phụ âm cần lưu ý:**
  - Cặp âm: `/f/` vs `/v/`, `/s/` vs `/z/`, `/θ/` (thanks) vs `/ð/` (them)
  - Âm xát/tắc xát: `/tʃ/` (check), `/dʒ/` (just), `/ʃ/` (she), `/ʒ/` (Asia)
  - Cụm âm: `/tr/`, `/dr/`, `/r/`, `/l/`, `/ŋ/` (sing)

#### Giao thức hội thoại 6 vòng (6-Round Interactive Scenario)

1. **1 phút chuẩn bị:** Nói ngắn bối cảnh, đối tượng nghe và mục tiêu (không soạn kịch bản sẵn).
2. **6 vòng tương tác:** Trao đổi 1–2 câu mỗi lượt. AI **chỉ được hỏi lại, làm rõ hoặc yêu cầu dẫn chứng** (tuyệt đối không nói thay hoặc sửa câu hộ trong lúc đang hội thoại).
3. **2 phút trình bày liên tục:** Nói một mạch về chủ đề đó và lưu file ghi âm raw.
4. **3 phút tự đánh giá (Self-review):** Nghe lại ghi âm, đánh dấu các chỗ ngập ngừng (`Yeah... yeah...`), các chunk bị sượng và chọn 1 lỗi phát âm IPA quan trọng nhất để sửa.

> **💡 Tool ghi âm Native tích hợp sẵn trong repo:**
> Bạn hoặc AI có thể kích hoạt công cụ ghi âm trực tiếp bằng lệnh:
> ```bash
> ./.agents/skills/learn/scripts/record.sh -d 60 -t project-intro
> ```
> Script sẽ đếm ngược 60s, hiển thị tiến độ trực tiếp và tự lưu file vào `artifacts/audio/`. Bạn có thể bấm `Enter` bất cứ lúc nào để kết thúc ghi âm sớm.
> 
> **📞 Gemini Live (Hội thoại bằng giọng nói 2 chiều Real-Time):**
> Để gọi điện thoại luyện nói trực tiếp với Gemini Live (nói qua mic, nghe qua loa với độ trễ <0.5s):
> 1. Chuẩn bị `GEMINI_API_KEY` (lấy từ Google AI Studio) và cài `pip install -r .agents/skills/learn/scripts/requirements.txt`.
> 2. Chạy lệnh:
> ```bash
> ./.agents/skills/learn/scripts/live.sh -t "Project Delay Discussion" -d 5
> ```
> Gemini sẽ trò chuyện cùng bạn theo ngữ cảnh của repo, và tự động ghi log buổi nói vào `sessions/` khi kết thúc!

### Writing: Draft → Layered Review → Learner Revision

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

## Weekly Review & Nghiệm thu chu kỳ 12 tuần

Cuối mỗi tuần học, agent xem xét bằng chứng theo 4 chiều (0–2 điểm): **Completion, Quality, Retention, Transfer**.

### Mười câu hỏi tự vấn trước khi nghiệm thu chu kỳ 12 tuần

Trước khi tuyên bố hoàn thành một chu kỳ hoặc nghiệm thu năng lực:

1. Tôi có thể giải thích các kết luận chính mà không cần nhìn lịch sử chat hay gợi ý của AI không?
2. Tôi có luôn làm bài thử unaided (không AI) trước khi nhận trợ giúp không?
3. Các từ vựng/chunk mới học có được chủ động sử dụng trong ngữ cảnh mới không?
4. Các lỗi nghe có được phân loại vào 5 rào cản cụ thể thay vì chỉ nói "không nghe kịp" không?
5. Các buổi luyện nói có lưu lại ghi âm raw, transcript và bản tự thử lại không?
6. Các nhận định đọc hiểu có trích dẫn đúng đoạn/dòng trong bài gốc không?
7. Các bản sửa bài viết có do chính tôi tự viết lại và giải thích được không?
8. Sản phẩm tiếng Anh có được gửi đến người nghe/người đọc thật trong công việc/cuộc sống không?
9. Dữ liệu mật và thông tin riêng tư có được bảo vệ hoàn toàn không?
10. Tôi có thực hiện được nhiệm vụ mục tiêu với ít sự trợ giúp từ AI hơn hẳn so với tuần đầu tiên không?

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
