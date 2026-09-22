---
id: zh-tw-style-profiles
title: "Taiwan Traditional Chinese Style Profiles"
applies_when:
  - Taiwan localization layer is active
companion_files:
  - ZH_TW_LOCALIZATION_AND_WRITING_RULES.md
  - ZH_TW_TERM_GLOSSARY.md
  - ZH_TW_QUALITY_CHECKLIST.md
version: 2.0.0
profile_count: 15
---

# Taiwan Traditional Chinese Style Profiles

These profiles are reusable writing-style presets. The router selects one based on workflow type, audience, and channel. Authors may override at the workflow level through `localization.locale_style_profile_overrides.zh-TW` in the workflow frontmatter (see [../templates/WORKFLOW_TEMPLATE.md](../templates/WORKFLOW_TEMPLATE.md)).

Every profile uses this schema:

```yaml
id:
locale:
best_for:
tone:
formality:
directness:
sentence_rhythm:
first_person_policy:
second_person_policy:
rhetorical_question_policy:
evidence_standard:
punctuation_notes:
avoid:
preferred_patterns:
ending_style:
```

Every profile also has a short sample paragraph in Taiwan Traditional Chinese.

---

## 1. `zh-tw-conversational-help`

Default conversational reply to a Taiwan user's question.

```yaml
id: zh-tw-conversational-help
locale: zh-TW
best_for: 對話式預設、簡短協助
tone: 友善、平實
formality: 低至中
directness: 中
sentence_rhythm: 短至中等，長度交錯
first_person_policy: 偶爾使用「我可以幫你…」
second_person_policy: 直接稱「你」，不要「您」（除非對方明顯偏好）
rhetorical_question_policy: 少用
evidence_standard: 輕
punctuation_notes:
  - 句末句號優先用全形「。」
  - 引號用「」而非 ""
  - 列表項目不需每行加句號
avoid:
  - 「在這個時代…」
  - 「這非常重要」「這很關鍵」
  - 重複的問句開頭
preferred_patterns:
  - 先說結論，再展開
  - 用具體例子替代抽象描述
  - 用「我們」描述工作方法
ending_style: 一句可操作的建議或下一步
```

**Sample**

收到，你貼的這段重複出錯的原因是迴圈內每次都重新初始化同一個 list。改成在迴圈外宣告一次就好，下面這段是修正後的版本，跑了三次都正確。

---

## 2. `zh-tw-friendly-professional`

Internal team updates, neutral business writes.

```yaml
id: zh-tw-friendly-professional
locale: zh-TW
best_for: 團隊週報、內部更新、不需要行銷渲染的商業寫作
tone: 溫暖、專業
formality: 中
directness: 中至高
sentence_rhythm: 中等為主，長短交錯
first_person_policy: 偶爾使用
second_person_policy: 「你」或「團隊」皆可，避免過度尊稱
rhetorical_question_policy: 少用
evidence_standard: 中
punctuation_notes:
  - 段落以句號或單換行收束
  - 條列以「-」或「1.」皆可，但全篇一致
avoid:
  - 對外廣告式的渲染詞
  - 大段技術 jargon
preferred_patterns:
  - 開頭一句總結
  - 條列三到五點變化
  - 結尾點一個具體動作
ending_style: 一個實際的接續動作
```

**Sample**

這週主要處理兩件事：一是客服信分類模型從五欄減到三欄，理由是「付款問題」與「帳務問題」常被誤判為同一類；二是把錯誤信的回覆路徑縮短成兩步。下一週重點是把這個改進寫進 SOP，給夜班客服一份 runbook。

---

## 3. `zh-tw-business-consulting`

Strategy memos, deck content, analytical writing.

```yaml
id: zh-tw-business-consulting
locale: zh-TW
best_for: 策略備忘錄、諮詢簡報、分析報告
tone: 分析、清晰
formality: 中至高
directness: 高
sentence_rhythm: 中等結構化，段落引導
first_person_policy: 機構式（我們團隊判斷…／我方認為…）
second_person_policy: 多用「貴公司」或「您的團隊」，書面體
rhetorical_question_policy: 偶爾用於開場框架問題
evidence_standard: 高
punctuation_notes:
  - 中英夾雜時不刻意補空格（保留自然節奏）
  - 數字與單位間保留半形空格（如「18 億美元」）
avoid:
  - 個人情緒用語
  - 含糊的「大幅提升」
preferred_patterns:
  - 先描述事實
  - 再展開選項與權衡
  - 最後提出建議與假設
ending_style: 一段明確的建議 + 假設清單
```

**Sample**

這個市場在 2024 年的規模約 18 億美元，年增 6%，主要驅動力是中小企業的內部搜尋需求。競爭者集中在三家公司，其中兩家以深度模型取勝，第三家靠低價。我們建議以「企業內部搜尋」為切入點，搭配可下載的驗證包，三個月內對兩個產業做出可比較的結果。

---

## 4. `zh-tw-threads-insightful`

Threads platform posts that aim for a considered, shareable observation.

```yaml
id: zh-tw-threads-insightful
locale: zh-TW
best_for: Threads（Meta）平台上的觀察文、串文
tone: 思考後的銳利感
formality: 低至中
directness: 高
sentence_rhythm: 短至中等，段落節奏緊湊
first_person_policy: 開放使用「我」
second_person_policy: 直接稱「你」
rhetorical_question_policy: 一則最多一個，置於開頭
evidence_standard: 中
punctuation_notes:
  - 短句多換行，營造可滑動節奏
  - 「…」在 Threads 上可用，但每則最多一個
  - 不結尾用「。」讓平台判定為未完
avoid:
  - 「各位朋友大家好」「在這個時代」
  - 全篇 emoji 裝飾
  - 純粹的自我宣傳
preferred_patterns:
  - 開頭拋出反直覺觀察
  - 中段展開一個可驗證的例子
  - 結尾留下可辯駁的下一句
ending_style: 一句留給讀者反芻的開放結論
```

**Sample**

重新整理待辦清單時，把「今天要做什麼」分成「今天可以完成什麼」兩份。貼一份在螢幕前，一份留給自己。第一份的內容通常長 5 倍，第二份才是真正會消失的。

---

## 5. `zh-tw-instagram-casual`

Instagram captions and stories.

```yaml
id: zh-tw-instagram-casual
locale: zh-TW
best_for: Instagram 貼文、限時動態
tone: 隨性、生活感
formality: 低
directness: 中
sentence_rhythm: 短、斷句多、節奏快
first_person_policy: 開放使用
second_person_policy: 直接稱「你」，避免尊稱
rhetorical_question_policy: 偶爾，置於貼文末以提高互動
evidence_standard: 輕
punctuation_notes:
  - 換行符號即節奏
  - emoji 適量（每則 1–3 個）
  - 不寫滿；視覺素材本身已是訊息
avoid:
  - 過度感性渲染
  - 直接廣告話術
  - 標籤堆砌（除非該平台演算法仍偏好）
preferred_patterns:
  - 一個場景開始
  - 一個具體動作或物品
  - 一句結尾的小體悟或邀請互動
ending_style: 一句輕鬆的收束或互動邀請
```

**Sample**

本週最划算的一次消費：一雙 1,200 元的雨鞋，把我從「濕襪子悲劇」裡救出來三次。如果你也常被午後雷陣雨突襲，這筆帳很划算。

---

## 6. `zh-tw-linkedin-professional`

LinkedIn posts, considered takes for professional audiences.

```yaml
id: zh-tw-linkedin-professional
locale: zh-TW
best_for: LinkedIn 個人或公司帳號發文、專業觀點
tone: 思考後、銳利但不張揚
formality: 中
directness: 高
sentence_rhythm: 短至中等，段落引導
first_person_policy: 開放使用，但克制
second_person_policy: 「你」優先
rhetorical_question_policy: 一則最多一個，置於開頭框架
evidence_standard: 中
punctuation_notes:
  - 中英夾雜時保留自然節奏，不刻意補空格
  - 條列以「-」為主
avoid:
  - 「深度好文」「乾貨滿滿」
  - 結尾套話
  - 誇張形容詞
preferred_patterns:
  - 開頭拋出反直覺或具體觀察
  - 中段展開一個實例或個人經驗（必須為真實或假設）
  - 結尾一句可辯駁的觀點
ending_style: 一句話提出下一個討論方向或邀請回應
```

**Sample**

大家都以為新創的瓶頸是找到客戶，其實是建立「拒絕」的流程。沒有清楚的拒絕話術，sales 會把每位 lead 都當成機會；等真有人來買時，流程已經分不清楚誰是誰。如果你只接過五個客戶，現在還不需要拒絕話術。超過 50 個，就不能不寫。

---

## 7. `zh-tw-email-professional`

B2B email, professional outreach.

```yaml
id: zh-tw-email-professional
locale: zh-TW
best_for: 業務郵件、合作邀請、外聯
tone: 尊重、簡潔
formality: 中至高
directness: 高
sentence_rhythm: 短至中等，偶爾一句一行
first_person_policy: 開放但禮貌
second_person_policy: 「您」優先於「你」，收件人是具名對方時用「X 經理您好」
rhetorical_question_policy: 偶爾用於澄清
evidence_standard: 高
punctuation_notes:
  - 開頭稱謂獨立成行
  - 結尾署名獨立成行
  - 簽名檔使用全形標點
avoid:
  - 自吹自擂的形容詞
  - 給對方太多作業
  - 多個 CTA 競逐同一封信
preferred_patterns:
  - 開頭就說為什麼寄這封信
  - 一段針對對方的具體觀察
  - 一句可選的時間
ending_style: 一個具體的時段或下一步
```

**Sample**

陳經理您好，我是歐陽書寧。看到貴公司最近把人資系統升級到新版，想了解一下內部最頭痛的環節是哪一塊。我手上有一個針對面試流程的評估方法，週四下午三點半小時方便嗎？如果時段不對，告訴我您方便的時段。

---

## 8. `zh-tw-sales-clear`

Short sales copy, offer pages, pitch snippets.

```yaml
id: zh-tw-sales-clear
locale: zh-TW
best_for: 銷售文案短篇、offer page 內段、銷售信內文
tone: 自信、平實
formality: 中
directness: 高
sentence_rhythm: 短句多，長短交錯
first_person_policy: 開放使用
second_person_policy: 「你」為主
rhetorical_question_policy: 僅當問題真的有助於賣點
evidence_standard: 中（每篇至少一個可驗證的事實）
punctuation_notes:
  - 短句不需全形句號時可省略，但全篇風格一致
  - 數字使用阿拉伯數字（除年/月）
avoid:
  - 「革命性」「顛覆」「全面賦能」
  - 套話式 CTA：「立即購買」「馬上取得」
preferred_patterns:
  - 描述一個具體情境
  - 給出時間或金錢上的差異
  - 點出驗證方式（demo、試用、回饋）
ending_style: 明確的下一步行動
```

**Sample**

每月花 6 小時整理客戶回信？我們的做法把這段時間壓到 1.5 小時，且整段流程仍由你的客服主管覆核。下面 12 分鐘的示範走過一遍真實的客服案例，看完再決定要不要約 30 分鐘試用。

---

## 9. `zh-tw-landing-page-clear`

Full landing page, hero + sections + CTA.

```yaml
id: zh-tw-landing-page-clear
locale: zh-TW
best_for: 完整著陸頁（首頁 / 銷售頁）
tone: 結果導向、平實
formality: 中
directness: 高
sentence_rhythm: 段落節奏明確，每段一個重點
first_person_policy: 開放使用
second_person_policy: 「你」為主
rhetorical_question_policy: 限於開場鉤子
evidence_standard: 中（每頁至少一個可驗證指標）
punctuation_notes:
  - 標題與副標題用較大字級時仍維持全形標點
  - 條列項目以「-」統一
avoid:
  - 抽象形容詞
  - 無具體時間或金額的「大幅提升」
  - 假見證
preferred_patterns:
  - 鉤子：對目標讀者的具體痛點
  - 證據：一個可驗證的數字或時間
  - 結構：痛點 → 解法 → 證據 → CTA
ending_style: 最終 CTA，明確告訴使用者下一步
```

**Sample**

把客服信件從每週 6 小時壓到 1.5 小時，整段流程由你的客服主管覆核，不需要改你既有的信件平台。三分鐘示範會走過一封真實投訴信的處理過程，下面可以看更多客戶的真實使用前後比較。

---

## 10. `zh-tw-long-form-article`

Long-form blog posts, articles, considered pieces.

```yaml
id: zh-tw-long-form-article
locale: zh-TW
best_for: 部落格長文、深度文章、媒體投稿
tone: 思考後、節制
formality: 中
directness: 中至高
sentence_rhythm: 中等為主，長短交錯
first_person_policy: 開放使用
second_person_policy: 開放使用「你」或「讀者」
rhetorical_question_policy: 開頭可一，內文不再用
evidence_standard: 中
punctuation_notes:
  - 段落分明，每段一個論點
  - 引用以「」區隔內文
  - 數字與單位間保留半形空格
avoid:
  - 「值得我們深入探討」
  - 結尾套話
preferred_patterns:
  - 開頭快速建立情境
  - 中段以三到五個段落推進
  - 結尾提出一個具體的延伸行動或思考
ending_style: 一個延伸思考或下一步的邀請
```

**Sample**

> 把客服信分類模型從五欄減到三欄的過程中，最有價值的發現不是模型的準確率提升了 4 個百分點，而是當我們真的去讀那些被分錯的信件時，才發現客戶最常抱怨的根本不是「退款」，而是「流程不清楚」。分類欄位只是表面，欄位背後的客戶心理才是真的產品線索。

---

## 11. `zh-tw-research-precise`

Research reports, decision briefs, fact-finding outputs.

```yaml
id: zh-tw-research-precise
locale: zh-TW
best_for: 研究報告、決策摘要、調查結果
tone: 正式、中立
formality: 高
directness: 高（精確陳述優先）
sentence_rhythm: 結構化、每段有主題句
first_person_policy: 極少
second_person_policy: 以讀者為主，少用「你」
rhetorical_question_policy: 少用
evidence_standard: 嚴格
punctuation_notes:
  - 引用以 [1]、[2] 編號
  - 數字統一為阿拉伯數字
  - 段落結尾用句號
avoid:
  - 行銷語氣
  - 推測代替事實
  - 「據說」「可能」
preferred_patterns:
  - 量化結論
  - 引用來源
  - 在結尾列出待驗證項目
ending_style: 一段總結 + 一個限制條件清單
```

**Sample**

在 2024 Q1 至 Q4 之間，台灣電子支付使用率由 39.2% 上升至 46.1%（金管會 2025-01 發布）。地區差異明顯，北部為 51%，中南部為 39%。本研究範圍未涵蓋 65 歲以上族群，建議後續以問卷補足。

---

## 12. `zh-tw-technical-clear`

Technical docs, API guides, system explanations.

```yaml
id: zh-tw-technical-clear
locale: zh-TW
best_for: 技術文件、API 說明、系統文件
tone: 技術、簡潔
formality: 中至高
directness: 非常高
sentence_rhythm: 短、密
first_person_policy: 罕用
second_person_policy: 罕用；以「使用者」「工程師」為對象
rhetorical_question_policy: 避免
evidence_standard: 嚴格
punctuation_notes:
  - 程式碼區塊前後保留空行
  - 中英夾雜時不刻意補空格
  - 全形標點僅用於敘述句
avoid:
  - 銷售用語
  - 比喻裝飾過頭
preferred_patterns:
  - 先說明目的
  - 列步驟與命令
  - 提供可驗證的範例
ending_style: 一個驗證步驟或下一步指令
```

**Sample**

`POST /v1/jobs` 啟動一個分類任務。請求主體需要 `text` 與 `categories`。回傳包含 `job_id` 與 `status`。可用 `GET /v1/jobs/{job_id}` 取得最新狀態。建議在 polling 間距設為 5 秒，避免 429。

---

## 13. `zh-tw-sop-direct`

SOPs, runbooks, checklists.

```yaml
id: zh-tw-sop-direct
locale: zh-TW
best_for: SOP、操作手冊、runbook、清單
tone: 程序化、就事論事
formality: 中
directness: 命令句
sentence_rhythm: 短命令句
first_person_policy: 罕用；用命令句
second_person_policy: 罕用；用命令句
rhetorical_question_policy: 避免
evidence_standard: 嚴格
punctuation_notes:
  - 編號步驟使用阿拉伯數字
  - 例外處理另起子節
avoid:
  - 「你可能想…」「你可以試試…」
  - 開放式結尾
preferred_patterns:
  - 編號步驟
  - 明確的例外處理
  - 結尾的檢查清單
ending_style: 一段品質檢查或回報條件
```

**Sample**

1. 開啟「自動回覆」分頁。
2. 將「啟用時段」設定為 09:00-18:00。
3. 選擇「客服類」→「付款問題」範本。
4. 預覽後送出。
例外：若客服主管要求夜間啟用，需填寫「加班核准單」後重複步驟 2。
品質檢查：每日 18:00 系統自動產生當日啟用報表。

---

## 14. `zh-tw-agent-spec-precise`

AI agent task specifications and prompt specifications.

```yaml
id: zh-tw-agent-spec-precise
locale: zh-TW
best_for: AI agent task 規格、prompt 規格、API 整合規格
tone: 規格、精準
formality: 中至高
directness: 非常高
sentence_rhythm: 短、密集
first_person_policy: 罕用
second_person_policy: 罕用；以「工程師」「整合者」為對象
rhetorical_question_policy: 避免
evidence_standard: 嚴格
punctuation_notes:
  - 欄位名稱保留英文
  - 程式碼區塊保留原樣
  - 全形標點僅用於敘述句
avoid:
  - 模糊語意詞
  - 「通常」「可能」
preferred_patterns:
  - 明確的 objective、inputs、outputs、acceptance、non-goals
  - 結構化欄位
  - 可驗證的 acceptance criteria
ending_style: 一段測試計畫或驗證步驟
```

**Sample**

目標：寫一個 Python 腳本，給定一段 `support_emails.json`（包含 `id`、`subject`、`body`、`received_at`），輸出 `classifications.json`（每封信加上 `category` ∈ {billing, bug, feature, other} 與 `confidence` ∈ [0, 1]）。Acceptance：所有信件都有分類，confidence 平均 ≥ 0.7，且類別分布不要全部都落在 billing。Non-goals：不串接實際信件 API；不做多語分類；不處理附件。

---

## 15. `zh-tw-customer-support`

User-facing support replies.

```yaml
id: zh-tw-customer-support
locale: zh-TW
best_for: 客服回覆、客戶信件、社群客服
tone: 溫暖、解方導向
formality: 中
directness: 高
sentence_rhythm: 短，長短交錯
first_person_policy: 以團隊身份發言（「我們」「客服團隊」）
second_person_policy: 「您」優先於「你」，正式信件用「您」
rhetorical_question_policy: 少用
evidence_standard: 嚴格（不虛構補償或承諾）
punctuation_notes:
  - 開頭稱呼獨立成行
  - 結尾署名獨立成行
avoid:
  - 「非常感謝您的耐心」「我們深感抱歉」
  - 模糊的「我們會盡快處理」
preferred_patterns:
  - 確認問題
  - 給出明確的動作
  - 提供升級路徑
ending_style: 一句話點出如果失敗該怎麼辦
```

**Sample**

收到了，這次出貨確實漏了附件，我再寄一次給您。附件就是上一封信裡提到的對照表。打開如果還是空白，請回信告訴我，我會直接請倉庫重新寄出，並更新您的物流單號。

---

## How to choose a profile

The router uses this decision flow:

```text
1. Read the workflow category and output channel.
2. Check the workflow's `localization.locale_style_profile_overrides.zh-TW` if present.
3. Otherwise pick a default by category:

   - content creation, communication     → zh-tw-friendly-professional or zh-tw-social-*
   - business, sales, marketing          → zh-tw-business-consulting or zh-tw-sales-clear / zh-tw-landing-page-clear
   - research, data, system              → zh-tw-research-precise or zh-tw-technical-clear
   - workflow, project, sop              → zh-tw-sop-direct
   - technical (agent spec, prompts)     → zh-tw-agent-spec-precise or zh-tw-technical-clear
   - support, customer-facing reply      → zh-tw-customer-support
   - social: Threads                     → zh-tw-threads-insightful
   - social: Instagram                   → zh-tw-instagram-casual
   - social: LinkedIn                    → zh-tw-linkedin-professional
   - long-form article                   → zh-tw-long-form-article
   - default conversational fallback     → zh-tw-conversational-help

4. Refine based on the user's stated tone (formal, casual, professional).
5. Record the choice in the context ledger.
6. Apply the profile only to the prose; never to protected content.
7. Choose editing intensity:
   - default: standard
   - legal / medical / financial / security / compliance / regulated: strict_precision
   - structured / technical: light
```

When the user requests a different register mid-conversation, update the context ledger and switch for the next deliverable.
