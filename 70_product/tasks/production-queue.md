---

id: production-queue

type: queue

status: active

updated_at: 2026-07-04T18:30:00+00:00

reviewed_by: 娆ч槼閿?

owner: 鐜嬭瀚?

audience: 鑰侀〗绔?/ 娆ч槼閿?/ 榛勮嵂甯?/ 鐢ㄦ埛

---



# 鐢熶骇闃熷垪锛氳€侀〗绔ラ鍙?/ 娆ч槼閿嬪鏍?



> 鏈枃浠舵槸 KDO 鐭ヨ瘑宸ュ巶鐨?*缁熶竴鐢熶骇闃熷垪**銆?

> 鑰侀〗绔ユ寜闃熷垪椤哄簭棰嗗彇浠诲姟锛屼竴娆″彧鍋氫竴浠讹紱娆ч槼閿嬫寜闃熷垪椤哄簭瀹℃牳銆?

> 浠诲姟鏉ユ簮锛氬巻鍙叉壒閲忓伐鍗曘€佹柊鍩熻瘖鏂换鍔°€佽法鍩熸ˉ鎺ヤ换鍔°€?



---



## 闃熷垪瑙勫垯



1. **鍗曞疄渚嬪崟绾跨▼棰嗗彇**锛氭瘡涓€侀〗绔ュ疄渚嬫瘡娆″彧鑳介鍙栦竴涓?`queued` 浠诲姟锛屾妸鐘舵€佹敼涓?`claimed-<瀹炰緥鏍囪瘑>`锛堝 `claimed-hermes`銆乣claimed-kimi`锛夈€俙pending_review` 鐘舵€佺殑鏉＄洰涓哄闃呴」锛岀敱娆ч槼閿嬬洿鎺ュ鏍革紝鑰侀〗绔ヤ笉棰嗗彇銆?

2. **澶氬疄渚嬪苟琛?*锛氬綋闃熷垪涓瓨鍦?鈮? 涓棤渚濊禆鐨?`queued` 浠诲姟鏃讹紝鍙惎鍔ㄥ涓€侀〗绔ュ疄渚嬪苟琛岄鍙栥€傚悓涓€浠诲姟榛樿鐢卞崟瀹炰緥瀹屾垚锛涘闇€澶氬疄渚嬪崗浣滃悓涓€浠诲姟锛岀敱鐢ㄦ埛鎴栫帇璇鍦ㄤ换鍔″崟涓槑纭媶鍒嗐€?

3. **瀹屾垚鍚庢彁浜?*锛氳€侀〗绔ュ畬鎴愮敓浜у苟鎶?`kdo pre-submit` 杈撳嚭璐村埌浠诲姟鏂囦欢鍚庯紝灏嗙姸鎬佹敼涓?`pending_review`銆?

4. **鎸夊簭瀹℃牳**锛氭闃抽攱鎸夐槦鍒楅『搴忓鏍?`pending_review` 浠诲姟锛岄€氳繃鍚庢敼涓?`reviewed`锛涚帇璇璺熻釜浠诲姟鐘舵€侊紝蹇呰鏃舵敼涓?`done`銆?

5. **闃诲澶勭悊**锛氳嫢浠诲姟琚樆濉烇紝鍦ㄣ€岀姸鎬併€嶅垪鏍囨敞 `blocked` 骞跺啓鏄庨樆濉炲師鍥狅紱闃诲瑙ｅ喅鍚庢仮澶嶄负 `queued`銆?

6. **浼樺厛绾ц皟鏁?*锛氱敤鎴峰彲闅忔椂璋冩暣闃熷垪椤哄簭锛涜皟鏁存椂鐢辩帇璇鏇存柊鏈枃浠讹紝骞跺湪 `.agent/context.md` 涓悓姝ャ€?

7. **鏂颁换鍔″叆闃?*锛氱帇璇璇婃柇瀹屾垚鍚庯紝鏂颁换鍔￠粯璁よ繘鍏ラ槦鍒楁湯灏撅紱鐢ㄦ埛鍙寚瀹氭彃闃熴€?

8. **馃啎 鎵€鏈夌姸鎬佸彉鏇村繀椤婚€氳繃 `queue_transition.py`**锛?

   - 鑰侀〗绔ラ鍙栵細`python 90_control/scripts/queue_transition.py claim <task-id> --instance <瀹炰緥鏍囪瘑>`

   - 鑰侀〗绔ュ畬鎴愭彁浜わ細`python 90_control/scripts/queue_transition.py complete <task-id> --instance <瀹炰緥鏍囪瘑>`

   - 鑰侀〗绔ラ噴鏀撅細`python 90_control/scripts/queue_transition.py release <task-id> --instance <瀹炰緥鏍囪瘑>`

   - 娆ч槼閿嬬粓瀹￠€氳繃锛歚python 90_control/scripts/queue_transition.py review <task-id> --verdict pass --reviewer 娆ч槼閿媊

   - 娆ч槼閿嬬粓瀹′笉閫氳繃锛歚python 90_control/scripts/queue_transition.py review <task-id> --verdict fail --reviewer 娆ч槼閿媊

9. **馃啎 绂佹鎵嬪姩淇敼鐘舵€?*锛氫换浣曡鑹蹭笉寰楃洿鎺ョ紪杈戞湰鏂囦欢鎴栦换鍔″崟 frontmatter 涓殑 `status` / `reviewed_by` / `review_date`銆傛墍鏈夌姸鎬佸彉鏇寸敱鑴氭湰鑷姩瀹屾垚锛岃剼鏈唴缃?gate銆侀攣銆佺姸鎬佹満鏍￠獙锛岄槻姝㈡姠璺戝拰鐘舵€佷笉涓€鑷淬€?



---



## 褰撳墠闃熷垪



| 闃熷垪搴忓彿 | 浠诲姟 ID | 浠诲姟鍚嶇О | 鐘舵€?| 棰嗗彇浜?| 棰勮鍗℃暟 | 闃诲/渚濊禆 | 鏉ユ簮鏂囦欢 | 澶囨敞 |

|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|

| 1 | `laowantong-batch-2026-06-20-wave1` | 鑰侀〗绔ユ壒閲忓伐鍗曠 1 娉細闂ㄧ蹇€熸竻鐞?| reviewed | 鑰侀〗绔?WorkBuddy) | 18 | 鏃?| `review_20260628_ouyangfeng-wave1.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?8/18 寮犲崱 status 鏇存柊涓?reviewed锛宺eviewed_by: 娆ч槼閿嬶紝review_date: 2026-06-28 |

| 2 | `task_20260627_laowantong-deliberate-practice-cards` | 鍏冭兘鍔?鍒绘剰缁冧範鍩熷崱鐗囧寲锛堝惈 AI 鍗忎綔妗ユ帴鍗★級 | reviewed | - | 11 | 鏃狅紙鍙笌 wave1 骞惰锛?| `60_feedback/tasks/task_20260627_laowantong-deliberate-practice-cards.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?1 寮犲崱 status 鏇存柊涓?reviewed锛宖rontmatter 宸茶ˉ review_date |

| 3 | `task_20260627_laowantong-channel-growth-cards` | 娓犻亾澧為暱鍩熷崱鐗囧寲锛堝惈 2 寮犺法鍩熸ˉ鎺ュ崱锛?| reviewed | - | 25 | 鏃狅紙鍙笌 wave1 骞惰锛?| `review_20260628_ouyangfeng-channel-growth.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?5/25 寮犲崱 status 鏇存柊涓?reviewed锛宺eviewed_by: 娆ч槼閿嬶紝review_date: 2026-06-28锛涘凡鐭ラ仐鐣欙細13 寮?case 鍗＄己 lint 鏍囧噯 section锛堝叏灞€ case section 鍊哄姟锛夈€? 寮?dk 鐩綍鏈榻愩€? 寮?concept 鐩綍鏈榻愶紝宸茶褰曚负鍚庣画娓呯悊浠诲姟 |

| 4 | `task_20260627_laowantong-lanyi-panproduct-organization` | 鍏版瘏娉涗骇鍝佺粍缁囧寲 + 娉涗骇鍝佽璁″煙鍗囩骇 | reviewed | - | 12 | 鏃?| `task_20260627_laowantong-lanyi-panproduct-organization.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?2/12 寮犲崱 status 鏇存柊涓?reviewed锛宺eviewed_by: 娆ч槼閿嬶紝review_date: 2026-06-28锛涘鏌ヤ腑淇 3 寮?case section + 5 涓洰褰曠Щ鍔?|

| 5 | `laowantong-batch-2026-06-20-wave2` | 鑰侀〗绔ユ壒閲忓伐鍗曠 2 娉細P0 杩斿伐 | reviewed | 鑰侀〗绔?WorkBuddy) | 16 | 鏃?| `laowantong-batch-2026-06-20.md` | 娆ч槼閿嬪瓙浠ｇ悊缁堝閫氳繃锛?6/16 寮犲崱 `kdo pre-submit` 閫氳繃锛宻tatus 鏇存柊涓?reviewed锛宍reviewed_by: 娆ч槼閿媊锛宍review_date: 2026-06-28`锛涗粛鏈?frontmatter domain/related/tags/query_triggers `src_unknown` 鍗犱綅鍙婂皯閲忓唴瀹瑰尯鍗犱綅锛屽凡璁板綍涓?wave2 娈嬬暀椤癸紝寤鸿鐢辩帇璇/鑰侀〗绔ュ湪鍚庣画娓呯悊浠诲姟涓ˉ榻?|

| 6 | `laowantong-batch-2026-06-20-wave3` | 鑰侀〗绔ユ壒閲忓伐鍗曠 3 娉細P1 娣卞害琛ュ叏 | reviewed | 娆ч槼閿?| 14 | 渚濊禆 wave2 瀹屾垚锛堝凡 reviewed锛岃В閿侊級 | `review_20260628_ouyangfeng-wave3.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?4/14 寮犲崱 status 鏇存柊涓?reviewed锛涘鏌ヤ腑娓呯悊 14 寮犲崱 frontmatter 涓?domain/related/tags 鐨?src_unknown 鍗犱綅锛涘叏搴?lint ERROR 闄嶈嚦 533锛涘凡瑙ｉ攣 wave4 鍜岀鍏壒 dk 娓呴浂 |

| 7 | `task_20260628_laowantong-dark-knowledges-batch8` | dark-knowledges 绗叓鎵规竻闆讹細琛ラ綈 10 寮犻棶棰?dk 鍗?| reviewed | 娆ч槼閿?| 10 | 渚濊禆 wave3 瀹屾垚锛堝凡 reviewed锛岃В閿侊級 | `task_20260628_laowantong-dark-knowledges-batch8.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?0/10 寮?dk 鍗?status 鏇存柊涓?reviewed锛沗dark-knowledges/` 鐩綍 lint ERROR 褰掗浂锛涘鏌ヤ腑淇 4 寮犲崱鏍煎紡闂锛泈ave4 宸插畬鍏ㄨВ閿?|

| 8 | `laowantong-batch-2026-06-20-wave4` | 鑰侀〗绔ユ壒閲忓伐鍗曠 4 娉細鏂板煙寤鸿 | reviewed | Hermes 鑰侀〗绔?| 15 | 宸茶В閿侊紙wave3 + 绗叓鎵瑰潎 reviewed锛?| `review_20260628_ouyangfeng-wave4.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?5/15 寮犲崱 status 鏇存柊涓?reviewed锛宺eviewed_by: 娆ч槼閿嬶紝review_date: 2026-06-28锛涘鏌ヤ腑淇 4.1 source_refs 18 澶勩€?.2 domain 鍗犱綅 7 澶勫強姝ｆ枃 src_unknown 鍗犱綅 30+ 澶勶紱wave4 宸茶В閿?wave5 |

| 9 | `laowantong-batch-2026-06-20-wave5` | 鑰侀〗绔ユ壒閲忓伐鍗曠 5 娉細澶栭儴鎺㈢储涓変釜鏂扮洸鍖?| reviewed | WorkBuddy 鑰侀〗绔?| 12 | 渚濊禆 wave4 瀹屾垚锛堝凡 reviewed锛岃В閿侊級 | `review_20260628_ouyangfeng-wave5.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?2/12 寮犲崱 `kdo pre-submit` 閫氳繃锛涘鏌ヤ腑淇 12 寮犲崱 frontmatter锛堣ˉ `status: reviewed`銆佺粺涓€ `reviewed_by: 娆ч槼閿媊銆佹洿鏂?`updated_at`锛夛紱wave5 宸茶В閿?|

| 10 | `task_20260628_hermes-lint-baseline-cleanup-batch1` | Hermes lint 鍩虹嚎娓呯悊 Batch 1锛氭満姊版€?frontmatter 淇 | reviewed | Hermes 鑰侀〗绔?| 784锛堝畨鍏ㄦ満姊颁慨澶嶏紝鍚鏌ヨ拷鍔?125锛?| 鏃?| `60_feedback/tasks/task_20260628_hermes-lint-baseline-cleanup-batch1.md` | Hermes 宸插畬鎴愶細frontmatter parse 绫?ERROR 娓呴浂锛沗kdo lint` 浠?690鈫?90 鏄洜涓?frontmatter 淇ソ鍚庡師琚帇鍒剁殑鍗＄墖鏆撮湶鏇村 section/source_refs 閿欒锛?90 涓唴瀹圭骇閿欒鐢?Batch 2-A/B/C 鎵挎帴锛汬ermes 鑰侀〗绔ュ緟鍛?|

| 11 | `task_20260628_wangyuyan-cleanup-channel-growth-residuals` | 娓犻亾澧為暱鍩熺粓瀹￠仐鐣欓棶棰樻竻鐞嗭紙P2+P3 宸插畬鎴愶紝P1 宸叉媶鍒嗭級 | done | 榛勮嵂甯?| 0锛堟竻鐞嗕换鍔★級 | 鏃?| `task_20260628_wangyuyan-cleanup-channel-growth-residuals.md` | 榛勮嵂甯堝凡瀹屾垚 dk/concept 鐩綍绉诲姩 + 鍏ㄥ簱 related 閾炬帴鏇存柊 + 椤烘墜淇 3 寮?case 鍗★紱P1 鍓╀綑 10 寮?case + 1 寮?dk section 璋冩暣宸叉媶鍒嗕负鐙珛浠诲姟 #12 |

| 12 | `task_20260628_laowantong-case-section-standardization` | 娓犻亾澧為暱鍩?10 寮?case + 1 寮?dk section 鏍囧噯鍖?| reviewed | 娆ч槼閿?| 11 | 鏃?| `task_20260628_laowantong-case-section-standardization.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?1/11 鏂囦欢 `kdo lint` 0 ERROR锛? 澶勬爣棰樺簭鍙烽棶棰樺凡鐜板満淇 |

| 13 | `task_20260628_laowantong-lint-batch2-case-sections` | lint Batch 2-A锛歝ase section 鏍囧噯鍖栬ˉ鍏紙130 鏂囦欢锛?| reviewed | WorkBuddy 鑰侀〗绔?| 130 | 鏃?| `60_feedback/tasks/task_20260628_laowantong-lint-batch2-case-sections.md` | 娆ч槼閿嬪鏍搁€氳繃锛氱敵璇夋垚绔嬶紝130/130 case 鏂囦欢宸茬湡瀹炰慨鏀瑰苟 commit锛宍kdo lint` Case section ERROR 娓呴浂锛涗箣鍓?`git diff HEAD` 妫€鏌ュけ鏁堟牴鍥犳槸 vault backup 鑷姩 commit |

| 14 | `task_20260628_laowantong-lint-batch2-dk-sections` | lint Batch 2-B锛歞k section 鏍囧噯鍖栬ˉ鍏紙43+14 鏂囦欢锛?| reviewed | WorkBuddy 鑰侀〗绔?| 57 | 鏃?| `60_feedback/tasks/task_20260628_laowantong-lint-batch2-dk-sections.md` | 娆ч槼閿嬪鏍搁€氳繃锛氱敵璇夋垚绔嬶紝57/57 dk 鏂囦欢宸茬湡瀹炰慨鏀瑰苟 commit锛宍kdo lint` DK section ERROR 娓呴浂锛涘師 43 娓呭崟 + 14 涓?extra 鏂囦欢鍧囧鐞?|

| 15 | `task_20260628_huangyaoshi-lint-batch2-source-refs` | lint Batch 2-C锛歴ource_refs 鐪熷疄瀛樺湪鎬ф竻鐞嗭紙175 ERROR / 90 鏂囦欢锛?| reviewed | WorkBuddy 鑰侀〗绔?| 90 | 鏃?| `60_feedback/tasks/task_20260628_huangyaoshi-lint-batch2-source-refs.md` | 鐢ㄦ埛澶嶆牳鍙戠幇瑙勫垯灞傝ˉ涓佸凡涓婄嚎浣嗘暟鎹眰娓呯悊鏈畬鎴愶紱浠诲姟杞氦鑰侀〗绔ワ紱宸茬湡瀹炰慨鏀?90 涓枃浠讹紝涓?175 涓?bare source_refs 娣诲姞 `10_raw/sources/` 鍓嶇紑锛宍kdo lint` source_refs ERROR 娓呴浂锛宍kdo pre-submit` 90/90 閫氳繃锛涘緟娆ч槼閿嬬粓瀹?|

| 16 | `task_20260628_wangyuyan-wave6-blindspot-diagnosis` | Wave 6 鏂扮洸鍖烘帰绱㈣瘖鏂?| reviewed | 鐜嬭瀚?| 0 | 鏃?| `60_feedback/tasks/task_20260628_wangyuyan-wave6-blindspot-diagnosis.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛氬喅绛栫瀛﹀煙 14 reviewed + 闇€姹傚垎鏋愬煙 10-20 reviewed锛屼袱涓洸鍖鸿瘑鍒悎鐞嗭紱寤鸿鍗＄墖 ID 鏃犲啿绐侊紱#21/#22 鍙叆闃熺敓浜?|

| 17 | `task_20260628_wangyuyan-next-phase-orchestration` | 涓嬩竴闃舵浠诲姟缂栨帓寤鸿锛歐ave 6 + 琛ラ摼骞惰 | confirmed | 鐜嬭瀚?| 0 | 鏃?| `60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md` | 鐜嬭瀚ｅ凡鎷嶆澘锛歐ave 6 缁х画 #16锛岃ˉ閾炬媶涓?B1/B2/B3 浣滀负 #18/#19/#20 鍏ラ槦锛汢1 鑷姩鍐欏叆+鎶芥锛孊2 蹇呴』浜哄伐瀹℃牳锛孊3 鍗婅嚜鍔紱related 鍒嗗眰鏍囧噯涓嶆寜 鈮? 涓€鍒€鍒?|

| 18 | `task_20260628_laowantong-link-repair-b1-frontmatter-related` | B1锛歠rontmatter `related` 瀛楁 src_unknown 鍗犱綅娓呯悊 | reviewed | 鑰侀〗绔?WorkBuddy) | 256 | 鏃?| `60_feedback/tasks/task_20260628_laowantong-link-repair-b1-frontmatter-related.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?56 鏂囦欢鐪熷疄淇敼锛宺elated src_unknown 娓呴浂锛?190 pending_unknown 琛ュ叆绗﹀悎鍒嗗眰鏍囧噯锛沗kdo lint` 0 ERROR锛涙娊妫€ 4 寮犲崱 OK |

| 19 | `task_20260628_laowantong-link-repair-b2-synthesis-section` | B2锛歋ynthesis section 姝婚摼/鍗犱綅娓呯悊 | reviewed | 鑰侀〗绔?WorkBuddy) | 235 + 66 琛ュ厖 | 鏃?| `60_feedback/tasks/task_20260628_laowantong-link-repair-b2-synthesis-section.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?35 寮犲垵澶勭悊 + 66 寮犺ˉ鍏呮竻鐞嗭紝66 鏂囦欢 body src_unknown 鍏ㄩ儴娓呴浂锛沰do lint 140 ERROR 鍏ㄤ负鍘嗗彶閬楃暀锛屾棤鏂板锛沠rontmatter src_unknown 鍙﹀紑浠诲姟澶勭悊 |

| 20 | `task_20260628_laowantong-link-repair-b3-island-cards` | B3锛氬宀涘崱鐗?`kdo link-suggest` 鎵归噺鎺ㄨ崘 | reviewed | 鑰侀〗绔?WorkBuddy) | 1042 | 鏃?| `60_feedback/tasks/task_20260628_laowantong-link-repair-b3-island-cards.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?014 YAML寮曞彿淇 + 163 bare id鍖呰９ + 119鍙ュ瓙鍒犻櫎 + 33寮犲宀涜ˉ鐪熷疄wikilink + pending_unknown.md绉诲埌system/锛涘宀涘崱鐗囨竻闆讹紱lint 140 ERROR鍏ㄤ负鍘嗗彶閬楃暀鏃犳柊澧烇紱pre-submit 鎶芥5/5 PASS锛?5寮犱粛鍏╬ending涓哄凡鐭ラ檺鍒?|

| 21 | `task_20260628_laowantong-wave6-decision-science-systematization` | Wave 6-A锛氬喅绛栫瀛﹀煙绯荤粺鍖?| reviewed | 鑰侀〗绔?Hermes) | 5 | 渚濊禆 Wave 6 璇婃柇 reviewed | `60_feedback/tasks/task_20260628_laowantong-wave6-decision-science-systematization.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?/5 鍗＄墖缁撴瀯瀹屾暣锛宭int 148 ERROR 鍏ㄤ负鍘嗗彶閬楃暀鏃犳柊澧烇紱鍒犻櫎 framework-decision-quality-checklist 涓噸澶?related锛涘喅绛栫瀛﹀煙 reviewed 浠?14鈫?8 |

| 22 | `task_20260628_laowantong-wave6-demand-analysis-deepening` | Wave 6-B锛氶渶姹傚垎鏋愬煙娣卞寲 | reviewed | 鑰侀〗绔?Hermes) | 5 | 渚濊禆 Wave 6 璇婃柇 reviewed | `60_feedback/tasks/task_20260628_laowantong-wave6-demand-analysis-deepening.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?/5 鍗＄墖缁撴瀯瀹屾暣锛宑ase section 鑻辨枃鏍囬鏀逛负涓枃锛沴int 140 ERROR 鍏ㄤ负鍘嗗彶閬楃暀鏃犳柊澧烇紝涓斾慨澶?8 涓巻鍙?case section 閿欒锛? 寮犲崱鍏ㄩ儴鍔犲叆 index.md锛沺re-submit 5/5 PASS |

| 23 | `task_20260629_huangyaoshi-lint-a1-empty-source-refs` | A1锛氱┖ source_refs 娓呯悊 | reviewed | 榛勮嵂甯?| 8 | 鏃?| `60_feedback/tasks/task_20260629_huangyaoshi-lint-a1-empty-source-refs.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛?/8 鏂囦欢 source_refs 琛ヤ负 pending_archive锛沗kdo lint` empty source_refs ERROR 娓呴浂锛沺re-submit 8/8 PASS |

| 24 | `task_20260629_laowantong-lint-a2-case-section-completion` | A2锛歝ase section 缂哄け琛ュ叏 | done | 鑰侀〗绔?Hermes) | 83 | 渚濊禆 A1 鏃犲啿绐?| `60_feedback/tasks/task_20260629_laowantong-lint-a2-case-section-completion.md` | frontmatter 淇鐩爣宸插畬鎴愶紙鏃ユ湡瀛楁/parse error/title/type锛夛紱娆ч槼閿嬬粓瀹￠€氳繃锛?32 涓?`Case card missing section` 鍘嗗彶閬楃暀宸叉媶鍒嗕负鐙珛鍊哄姟浠诲姟 #24-debt |

| 25 | `task_20260629_laowantong-expand-ai-learning-concept-cards` | 鎵╁睍 AI 宸ュ叿瀛︿範鏂规硶璁哄師瀛愭蹇靛崱 | reviewed | 鑰侀〗绔?Hermes) | 7 | 鏃?| `60_feedback/tasks/task_20260629_laowantong-expand-ai-learning-concept-cards.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛? 寮犳柊鍗＄粨鏋勫畬鏁达紱淇 3 寮?tool 鍗℃爣鍑?section锛涜ˉ鍏?4 寮犳牳蹇冨崱 related 鍙屽悜閾炬帴锛沬ndex.md 宸叉敹褰曪紱lint 0 鏂板 ERROR锛沺re-submit 鏈浜у嚭鏃?ERROR锛堝叏閲?FAIL 涓哄巻鍙查仐鐣欙級 |

| 26 | `task_20260629_kimi-full-frontmatter-compliance-cleanup` | 鍏ㄥ簱 frontmatter 鍚堣淇锛堝惊鐜鐞嗙洿鍒板綊闆讹級 | reviewed | 鑰侀〗绔?Hermes) | ~88 鏂囦欢 + 22 鐩綍 | 鏃?| `60_feedback/tasks/task_20260629_kimi-full-frontmatter-compliance-cleanup.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歠rontmatter 绫汇€佺洰褰曠粨鏋勭被 ERROR 鍏ㄩ儴娓呴浂锛沗kdo pre-submit` 448/0 PASS锛沗kdo lint` 0 ERROR / 7507 WARNING锛涘墿浣?WARNING 涓哄唴瀹硅川閲忕被锛岄渶鍗曠嫭浠诲姟澶勭悊 |

| 27 | `task_20260629_kimi-lint-mechanical-noise-reduction` | lint 鏈烘绫?WARNING 鐩存帴闄嶅櫔 | reviewed | 鑰侀〗绔?Hermes) | ~2700 WARNING | 鏃?| `60_feedback/tasks/task_20260629_kimi-lint-mechanical-noise-reduction.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歭int 闃堝€艰皟鏁村凡纭锛?35 鏂囦欢 source_refs 瑙勮寖鍖栵紱1637 椤甸潰琛ュ綍 index锛?51 涓?tool 鍗¤ˉ section 楠ㄦ灦锛沗kdo lint` 浠?7507 闄嶅埌 3286 WARNING锛沗kdo lint` 0 ERROR锛沗kdo pre-submit` PASS |

| 28 | `task_20260629_kimi-lint-content-debt-by-domain` | lint 鍐呭鍊烘寜 domain 鍒嗘壒娓呯悊 | reviewed | workbuddy | ~2656 WARNING / 14 涓瓙浠诲姟 | 渚濊禆 #27 reviewed | `60_feedback/tasks/task_20260629_kimi-lint-content-debt-by-domain.md` | 娆ч槼閿嬬粓瀹￠€氳繃銆?4 鍗曞叏 PASS銆俉ARNING 鈫?2%锛屽叚澶у唴瀹圭被鍒叏娓呴浂 |

| 29 | `task_20260629_wangyuyan-goat-milk-channel-partnership-bridge` | 缇婂ザ銆屽崠鍦板浘銆嶈法鍩熸ˉ鎺ュ崱鐢熶骇 | reviewed | 鑰侀〗绔?Hermes鍒嗚韩-Claude) | 3 寮犲崱 | 鏃?| `60_feedback/tasks/task_20260629_wangyuyan-goat-milk-channel-partnership-bridge.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛? 寮犲崱宸茶ˉ褰?index銆佷慨姝?section 鏍囬銆佽ˉ鍏?Critique 澶栭儴鍙嶅鑰呬笌鍏抽敭鏈銆佽ˉ鐩搁偦鍩?related 鍥為摼锛? 寮犵洰鏍囧崱 lint 鏃?ERROR/WARNING锛沺re-submit 鐩爣鍗℃棤 ERROR锛堝叏閲?FAIL 涓?raw/ocr 涓?_dogfood 鍘嗗彶閬楃暀锛?|

| 30 | `task_20260629_vikki-info-emotion-skill-upgrade` | Vikki + 澶чΘ锛歝ontent-production-polish skill 2.0 鍗囩骇 | reviewed | 鑰侀〗绔?Kimi) | 1 涓?skill | 鏃?| `60_feedback/tasks/task_20260629_vikki-info-emotion-skill-upgrade.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歋KILL.md Core Standard 鎵╁睍涓?6 鏉?+ Step 5.5 6 椤归獙璇?+ Platform Notes 5 骞冲彴妯℃澘 + Mini Scoring Rubric 6 缁达紱human-speech-rules.md 鏂板 #13-#15 鏂规硶锛?-part 缁撴瀯 + 5 璺ㄥ煙绀轰緥锛夛紱`kdo pre-submit` 2/2 PASS锛泂hared 涓?`.claude/skills/` 妗ユ帴涓€鑷达紱瀹℃煡涓慨姝?2 澶勬枃鏈笉涓€鑷达紙4鈫? 鏍囧噯銆丮ini Scoring Rubric 6 缁达級锛沗agent澶嶇洏/Kimi/2026-06-30.md` 缂哄け璁颁负鍚庣画寰€哄姟 |

| 31 | `task_20260629_vikki-five-tag-quality-labels` | Vikki 浜旀爣绛?+ 澶чΘ鍝佺墝涓夊害 鈫?KDO 鍗＄墖璐ㄩ噺鏍囩浣撶郴 | reviewed | 鑰侀〗绔?Kimi) | 1 涓?schema + 50 寮犺瘯鐐瑰崱鐗?+ 1 寮?framework | 鍘?assignee 榛勮嵂甯堬紱schema/鑴氭湰灞傚凡鐢遍粍鑽笀瀹屾垚锛坙abel-quality-migrate.py锛夛紱鑰侀〗绔?Kimi)瀹屾垚鍐呭灞?| `60_feedback/tasks/task_20260629_vikki-five-tag-quality-labels.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歠ramework-brand-three-degree 姒傚康鍗?+ system-kdo-quality-labels 鎸囧崡閫氳繃 pre-submit锛?0 寮犺瘯鐐瑰崱鐗囨爣绛捐縼绉诲畬鎴愶紱瀹℃煡涓彂鐜板苟淇 48 寮犲崱鐗囧瓨鍦ㄩ噸澶?`quality_labels` 瀛楁鐨勯棶棰橈紱杩佺Щ鑴氭湰宸插鍔犻槻寰℃€ц烦杩囬€昏緫锛沗kdo pre-submit` 鏂板崱 2/2 PASS + 鎶芥煡 4/4 PASS锛沗.agent/laowantong-context.md` 宸叉洿鏂?quality_labels 妫€鏌ラ」 |

| 32 | `task_20260629_vikki-open-source-knowledge-boundary` | 娌夋穩銆屽紑婧愮煡璇嗕娇鐢ㄨ竟鐣屻€嶆蹇靛崱 | reviewed | 鑰侀〗绔?Kimi) | 1 寮?concept 鍗?| 鏃?| `60_feedback/tasks/task_20260629_vikki-open-source-knowledge-boundary.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歝oncept-open-source-knowledge-usage-boundary 姒傚康鍗℃鏂?300 琛岋紝鍥涘眰绾э紙瀛︿範/寮曠敤/鏀圭紪/钂搁锛? 涓夋潯杈圭晫绾?+ KDO 榛樿鍗忚寤鸿锛圕C BY-NC-SA/CC BY-NC-ND/CC BY锛? 娓镐緺浜嬩欢/Anthropic-DeepSeek 鍙屾渚?+ Critique 鍐呴儴灞€闄?+ 2 涓閮ㄦ敾鍑昏€咃紱`kdo pre-submit` 1/1 PASS锛? 涓?related 閾炬帴鍏ㄩ儴鏈夋晥锛沇ebSearch 鏉ユ簮寤鸿鍚庣画琛ュ叆 source_refs |

| 33 | `task_20260630_daxin-methodology-cards-production` | 澶чΘ鎴橀槦鏍稿績鏂规硶璁哄崱鐗囧寲 | reviewed | 鑰侀〗绔?Kimi) | 5 寮犲崱锛?30 skill 宸茶鐩栬剼鏈ā鏉匡紝鐪佺暐 tool-shortvideo-script-templates锛?| 鏃?| `60_feedback/tasks/task_20260630_daxin-methodology-cards-production.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛? 寮犵洰鏍囧崱鍏ㄩ儴 `kdo pre-submit` PASS锛沠ramework-brand-three-degree 浠?concept 鍗囩骇涓?framework 骞惰ˉ鍏?6 姝ユ搷浣滄硶锛沜ase-daxin-team-content-training-camp 璇佹嵁閾撅紙615 鏉＄兢鑱婏級+ 6 涓け璐ユā寮忓畬鏁达紱瀹℃煡涓慨姝?1 澶?`quality_labels: observed` 涓哄彈鎺ф爣绛?`cited`锛涢槦鍒楁姠璺戝紓甯稿凡鎸夎ˉ瀹℃祦绋嬪鐞?|

| 34 | `task_20260630_community-knowledge-failure-modes` | 绀剧兢鐭ヨ瘑鐢熶骇澶辫触妯″紡搴擄紙Vikki + 澶чΘ铻嶅悎锛?| reviewed | 鑰侀〗绔?Hermes) | 1 寮?framework + 1 寮犲彲閫?case | 鏃?| `60_feedback/tasks/task_20260630_community-knowledge-failure-modes.md` | 鏉ユ簮锛歏ikki缇?+ 澶чΘ鎴橀槦锛涜瀺鍚?0涓け璐ユā寮忥紝寤虹珛KDO澶欰gent鍗忎綔/绀剧兢杩愯惀鐨勫け璐ユā寮忓簱涓庢棭鏈熼璀︽寚鏍?|

| 35 | `task_20260630_kdo-state-json-sqlite-migration-mvp` | KDO state.json 鈫?SQLite MVP 杩佺Щ锛坰ources 闆嗗悎锛?| reviewed | **榛勮嵂甯?* | 1 涓泦鍚?/ 689 鏉¤褰?| 鏃狅紱鐢ㄦ埛鎸囧畾鏈懆楂樹紭鍏堢骇鍩虹璁炬柦浠诲姟 | `60_feedback/tasks/task_20260630_kdo-state-json-sqlite-migration-mvp.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛圔+锛夛細`.kdo/state.sqlite` 鐢熸垚锛宍state.json` 宸查噸鍛藉悕涓?`.migrated`锛?89 鏉?sources 涓€鑷达紱`kdo lint --summary` 0 鏂板 ERROR锛宍kdo status` 姝ｅ父锛涙柊澧?11 涓?SQLite state 鍗曞厓娴嬭瘯锛涘鏌ヤ腑淇 append 涓嶆彁浜ゃ€乺eload 涓㈠け sources銆佽法绾跨▼ finalizer銆佸鍛戒护鏈叧闂繛鎺ャ€乴int 鍩虹嚎鏈鍒?SQLite 绛?5 澶勯棶棰橈紱`kdo enrich --all --dry-run` 褰撳墠鏃?TODO 椤甸潰寰呰ˉ娴嬶紱鍏ㄩ噺 pytest 538 passed / 1 skipped / 1 failed锛坒ailed 涓洪瀛樺湪 Windows GBK 缂栫爜闂锛?|

| 36 | `task_20260630_kdo-query-label-filter` | 瀹炵幇 kdo query --label 璐ㄩ噺鏍囩杩囨护鍛戒护 | reviewed | 榛勮嵂甯?| 1 涓?CLI 鍙傛暟 | 渚濊禆 #31 reviewed锛?8 寮犻噸澶嶆爣绛鹃棶棰樺凡鐢辨闃抽攱鐜板満淇 | `60_feedback/tasks/task_20260630_kdo-query-label-filter.md` | #31 閬楃暀锛氶獙鏀舵爣鍑嗚姹?`kdo query --label actionable` 鍙繃婊わ紱褰撳墠鐢?rg 涓存椂鏇夸唬锛涢粍鑽笀瀹炵幇鍚庢洿鏂?system-kdo-quality-labels 鎸囧崡 |

| 37 | `task_20260630_kdo-cli-syntaxerror-fix` | 淇 kdo CLI SyntaxError锛坘do/commands/delivery.py:686锛?| reviewed | 榛勮嵂甯?| 1 涓?bugfix | 鏃狅紱鑰侀〗绔ュ湪 #34 鐢熶骇涓彂鐜?| `60_feedback/tasks/task_20260630_kdo-cli-syntaxerror-fix.md` | `python -m kdo pre-submit` 绛夊懡浠よЕ鍙?SyntaxError锛岄渶榛勮嵂甯堜慨澶?delivery.py 璇硶閿欒锛涗慨澶嶅悗鑰侀〗绔ュ彲鎭㈠鐩存帴浣跨敤 CLI |

| 38 | `task_20260701_kdo-index-lint-wikilink-format-alignment` | KDO index/lint wikilink 鏍煎紡瀵归綈 | reviewed | 榛勮嵂甯?| 1 涓?KDO 浠ｇ爜淇 + 1 涓祴璇?| 鏃狅紱闃诲 #28 strategy 鍩熺湡瀹炴竻闆?| `60_feedback/tasks/task_20260701_kdo-index-lint-wikilink-format-alignment.md` | 娆ч槼閿嬪缓璁彃闃燂紱鏍瑰洜锛歚kdo index --rebuild` 鐢熸垚 bare wikilink锛宍kdo lint` 鏈熸湜甯﹁矾寰?wikilink锛屽鑷?strategy 148 涓?/ 鍏ㄥ簱绾?700+ WARNING 璇姤锛涗慨澶嶅悗 strategy 鍩熷彲鐪熷疄娓呴浂锛涢璁?0.5-1 澶?|

| 39 | `task_20260701_design-domain-encoding-diagnosis` | design domain 缂栫爜鎹熷潖璇婃柇 | reviewed | 鑰侀〗绔?Kimi) | 1 浠借瘖鏂姤鍛?| 鏃狅紱闃诲 #28 design 鍩熸竻鐞?| `60_feedback/tasks/task_20260701_design-domain-encoding-diagnosis.md` | 娆ч槼閿嬪缓璁彃闃燂紱鐩爣锛氬彧璇昏瘖鏂?design 鍩熸枃浠剁紪鐮佹崯鍧忔牴鍥狅紝缁欏嚭 healthy/display-only/recoverable/corrupted 鍒嗙被鍙婂悗缁鐞嗗缓璁紱璇婃柇瀹屾垚鍓嶇姝㈡壒閲忎慨鏀?design 鏂囦欢锛涢璁?0.5-1 澶?|

| 40 | `task_20260701_wangyuyan-wobeirushen-pilot-orchestration` | 銆婂惥杈堝绁炪€嬫潯浠舵€х撼鍏?+ 3 寮犲崱 | reviewed | 鑰侀〗绔?Kimi) | 3 寮犲崱锛? concept + 1 tool + 1 concept锛?| 鏃狅紱楠岃瘉鎶ュ憡宸插畬鎴?| `60_feedback/tasks/task_20260701_wangyuyan-wobeirushen-pilot-orchestration.md` | 鐜嬭瀚ｄ环鍊煎垽鏂細B 绾х礌鏉愶紝涓嶅仛璇曠偣锛岀洿鎺ヤ骇鍑?3 寮犲崱鈥斺€擿concept-cognitive-offloading-in-ai-era`锛堝凡鏈夊垵绋匡紝闇€缁堝锛夈€乣tool-ai-use-barbell-strategy`锛堟柊寤猴級銆乣concept-abundance-paradox`锛堟柊寤猴級锛涚籂姝?BMW 85%/AGI 2029/AI 鏃犳硶鍒涢€犵瓑璇锛涘叾浣欐蹇垫湰娆′笉绾冲叆锛屽皝璐?|

| 41 | `task_20260701_wangyuyan-time-management-domain-orchestration` | 鏃堕棿绠＄悊鍩熷崌绾э細3 寮犻珮瀵嗗害妗ユ帴鍗?| reviewed | 鑰侀〗绔?Kimi) | 3 寮狅紙1 framework 妗ユ帴 + 1 tool 瀹¤寰幆 + 1 dk 鍙嶆ā寮忥級 | 鏃狅紱娲竷鍏?OCR+VLM 棰勫鐞嗗凡瀹屾垚 | `70_product/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md` | 鐜嬭瀚ｇ粡涔濆眰娣辨寲杩斿伐锛氭椂闂寸鐞?= 涓€鍫備簲姝ユ硶/IPO/鍗曞厓妯″瀷/鍐崇瓥鍗敓鍦ㄨ嚜绠＄悊鍦烘櫙鐨勫疄渚嬪寲锛? 寮犻珮瀵嗗害鍗?+ 鍙嶅悜鏇存柊 鈮?0 寮犲凡鏈夋鏋跺崱 related锛涜瑙?`diag_20260701_time-management-nine-layer-isomorphism.md` |

| 42 | `task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production` | 鏆楃煡璇嗚ˉ鎸栬瘯鐐圭敓浜э細Vikki + 澶чΘ鎴橀槦 | reviewed | 鑰侀〗绔?Kimi) | 4 寮犳柊 dk + 7-9 寮犲凡鏈夊崱琛ュ厖 | 渚濊禆鐜嬭瀚ｈ瘖鏂?`diag_20260702_vikki-daxin-dark-knowledge-extraction.md` | `60_feedback/tasks/task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production.md` | 榛勮嵂甯堣瘯鐐瑰缓璁功锛氶獙璇併€屼竴鍙ヨ瘽閲戠熆鎵弿銆嶆祦绋嬶紱鐜嬭瀚ｅ凡鎵弿 22 鏉℃殫鐭ヨ瘑锛屽缓璁?4 寮犳柊 dk锛堣倢鑲夎蹇?鍒涘浜?IP 淇′换>娴侀噺/闅愭€т环鍊间紶閫?璁插笀 vs 缇や紬绀剧兢锛夛紝鍏朵綑 18 鏉¤ˉ鍏呭埌宸叉湁鍗★紱娆ч槼閿嬫娊妫€ 鈮? 寮?|

| 43 | `task_20260702_laowantong-live81-ai-trademark-design-production` | Live81 AI 璧嬭兘鍟嗘爣璁捐锛? case + 2 tool + 1 dk | reviewed | 鑰侀〗绔?Kimi) | 4 寮狅紙1 case + 2 tool + 1 dk锛?| 鏃狅紱鐜嬭瀚ｄ節灞傛繁鎸栬瘖鏂凡瀹屾垚 | `60_feedback/tasks/task_20260702_laowantong-live81-ai-trademark-design-production.md` | 娆ч槼閿嬪鏌ラ€氳繃锛? 寮犳柊鍗?pre-submit PASS銆乴int 0 鏂板 ERROR锛涘鏌ヤ腑淇 case/dk 鍗?section 鏍囬浠ョ鍚?lint schema锛岃ˉ鍏?dk 鍗＄己澶辩殑 5 涓爣鍑?section锛涘弽鍚戞洿鏂扮害 20 寮犲凡鏈夊崱 related锛涜嚜鏀诲嚮鎶ュ憡 0 鑷村懡锛涘悓鎰忓皝璐?|

| 44 | `task_20260702_laowantong-yitang-scientific-sales-methodology-production` | 涓€鍫傜瀛﹂攢鍞柟娉曡锛? framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool锛圤PC 鏅鸿兘浣擄級 | reviewed | - | 12 寮?| 鏃狅紱鐜嬭瀚ｄ節灞傛繁鎸栬瘖鏂凡瀹屾垚锛?44 宸叉寜榛勮嵂甯堝缓璁?鐜嬭瀚ｇ嫭绔嬪垽鏂粠 6->10->12 寮犳墿灞?| `60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md` | 鐜嬭瀚ｇ嫭绔嬪垽鏂細10 寮犲凡瑕嗙洊閿€鍞柟娉曡锛屼絾缂?OPC 鍙珛鍗虫墽琛岀殑鏅鸿兘浣撹鏍煎崱鍜屽甫鏁版嵁鐨勫伐涓氬垎閿€妗堜緥锛涙墿灞曚负 12 寮狅細鏂板 `case-yitang-sales-transformation-tuliaogongsi`锛堟秱鏂欏叕鍙?10 涓?>20 S 绾э級+ `tool-opc-sales-dialogue-assistant`锛堣瀵硅瘽->鎯崇瓥鐣?>缁欒瘽鏈紝鍙洿鎺ュ綋 system prompt锛夛紱鏅鸿兘浣撳眰涓嶄竴娆℃€ч摵寮€ 8-10 寮狅紝鍏堝仛 MVP 瀵硅瘽鍔╂墜锛涘弽鍚戞洿鏂?>=28 寮犲凡鏈夊崱 related锛汷PC 鏅鸿兘浣撳啗鍥㈢敱 `opc-ai-sales-agent-architecture.md` 鎵挎帴骞惰ˉ鍏?MVP 鍚姩璺緞 |

| 45 | `task_20260702_huangyaoshi-kdo-inbox-grade` | kdo inbox --grade 鑷姩鍒嗙骇鍛戒护 | reviewed | 榛勮嵂甯?| 1 涓?CLI 鍛戒护 | 鏃狅紱Sprint 6 lake transparency 鍩哄缓 | `60_feedback/tasks/task_20260702_huangyaoshi-kdo-inbox-grade.md` | 娆ч槼閿嬪鏌ラ€氳繃锛氭柊澧?`kdo inbox --grade`锛屾寜 S/A/B/C 鑷姩缁?00_inbox/ 绱犳潗鎵撳垎锛?0104 鏂囦欢鍒嗙骇 S 2832 / A 40 / B 6559 / C 673锛沺ytest 548 passed锛涘缓璁笅涓€姝ュ姞 `--grade --ready` 杩囨护鍜?C 绾ф竻鐞嗕换鍔★紱缂?inbox grade 鍗曞厓娴嬭瘯锛岃涓哄井鍊哄姟 |

| 46 | `task_20260702_huangyaoshi-kdo-pipeline-dashboard` | kdo pipeline 绠＄嚎鍙鍖?Dashboard | reviewed | 榛勮嵂甯?| 1 涓?CLI 鍛戒护 | 鏃狅紱Sprint 6 lake transparency 鍩哄缓 | `60_feedback/tasks/task_20260702_huangyaoshi-kdo-pipeline-dashboard.md` | 娆ч槼閿嬪鏌ラ€氳繃锛氭柊澧?`kdo pipeline`锛屾寜 CAPTURE鈫扞NGEST鈫扨RODUCE鈫扴HIP鈫扺IKI 浜旀灞曠ず KDO 绠＄嚎鍋ュ悍搴︼紱鑷姩妫€娴?inbox/enrich/review 鐡堕骞剁粰寤鸿锛涗慨澶?state SQLite 杩炴帴鏈叧闂棶棰橈紱pytest 548 passed锛涚己 pipeline 鍗曞厓娴嬭瘯锛岃涓哄井鍊哄姟 |

|47|`task_20260702_laowantong-opc-sales-agent-specs-production`|OPC 閿€鍞櫤鑳戒綋鍐涘洟棣栨壒瑙勬牸鍗★細浠?#44 鏂规硶璁哄崱鐗囩紪璇?4 寮?agent-spec| reviewed | 鑰侀〗绔?Kimi) |4 寮爘渚濊禆 #44 缁堝閫氳繃|`60_feedback/tasks/task_20260702_laowantong-opc-sales-agent-specs-production.md`|KDO Agent 鍖栧璁＄粨璁猴細涓嶇己鏂规硶璁哄崱锛岀己鏅鸿兘浣撹鏍煎崱锛涙湰浠诲姟鎶?#44 涓?4 寮犳牳蹇?tool 鍗＄紪璇戞垚鍙洿鎺ュ綋 system prompt 浣跨敤鐨?agent-spec锛氬鎴峰垎绾у姪鎵?/ 鍗栫偣鐢熸垚鍔╂墜 / 閿€鍞樁娈佃拷韪姪鎵?/ 涓氱哗鐩戞帶鍔╂墜锛汚gent 鍋氬甫瀹姐€佷汉鍋氬垽鏂紱涓嶆敼鍙橀攢鍞姩浣滐紝鍙緭鍑哄缓璁紱鍙嶅悜鏇存柊 `opc-ai-sales-agent-architecture.md` 鍜?`tool-opc-sales-dialogue-assistant` related|

|49|`task_20260702_laowantong-opc-sales-agent-incremental-specs`|OPC 閿€鍞櫤鑳戒綋鍐涘洟澧為噺锛氬紑鍦?寮傝/鑷垜椹卞姩 3 寮?agent-spec| reviewed | 鑰侀〗绔?Kimi) |3 寮爘渚濊禆 #44 缁堝閫氳繃锛涘缓璁?#47 瀹屾垚鑷冲皯 2 寮犲悗鍐嶅惎鍔▅`60_feedback/tasks/task_20260702_laowantong-opc-sales-agent-incremental-specs.md`|鐢ㄦ埛鎻愬嚭銆岃竟鍋氳竟鐜┿€嶈ˉ鍏呴攢鍞櫤鑳戒綋鍐涘洟缂哄彛锛氬紑鍦?3 鍒嗛挓鍔╂墜 / 寮傝澶勭悊鍔╂墜 / 鑷垜椹卞姩鍔╂墜锛涗紭鍏堢骇 P2锛汚gent 鍋氬甫瀹姐€佷汉鍋氬垽鏂紱鍙嶅悜鏇存柊 OPC 鏋舵瀯涓庡璇濆姪鎵?related|

| 50 | `task_20260702_laowantong-opc-sales-agent-testing-wave1` | OPC 閿€鍞櫤鑳戒綋瀹炴祴 Wave 1锛? 寮?agent-spec 鐪熷疄妯″瀷楠岃瘉 | reviewed | 鑰侀〗绔?Kimi) | 7 寮?agent-spec 瀹炴祴 | 渚濊禆 #47/#49 缁堝閫氳繃 | `60_feedback/tasks/task_20260702_laowantong-opc-sales-agent-testing-wave1.md` | 娆ч槼閿?#47/#49 棣栬鏀硅繘鐐癸紱鎶?7 寮?agent-spec 鐨?System Prompt 鏀惧埌 Claude/GPT 鐪熷疄鐜璺戜竴閬嶏紱瑕嗙洊鍖昏嵂闆跺敭 B2B / SaaS / 闂ㄥ簵闆跺敭 / 浼犵粺鍒嗛攢鍥涗釜鍦烘櫙锛涙瘡寮犲崱鑷冲皯 2 涓湡瀹炲満鏅紱浜у嚭杩唬鏃ュ織 + KDO 鍥炴祦娓呭崟 + case 褰掓。锛汚gent 鍋氬甫瀹姐€佷汉鍋氬垽鏂?|

| 51 | `task_20260703_laowantong-yitang-Y-model-foundation-production` | 涓€鍫傚簳灞傞€昏緫鍩燂細Y妯″瀷 + 瀹炰簨姹傛槸 + 瑙ｆ斁鎬濇兂锛? 閲嶅啓 + 2 鏂板缓 framework + 1 tool + 1 dk + 2 case锛?| reviewed | 鑰侀〗绔?Kimi) | 7 寮?| 鏃狅紱鐜嬭瀚ｄ節灞傛繁鎸栬瘖鏂凡瀹屾垚 | `60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-foundation-production.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛? 寮犲畬鏁村崱 + 3 寮犳棫鍗¤縼绉伙紱17 寮犲凡鏈夊崱鍙嶅悜琛ラ摼锛涘叏搴?lint 0 ERROR锛泍t-decision-y-model degree 100 / top 0.24%锛涘疄浜嬫眰鏄?瑙ｆ斁鎬濇兂涓ゅ紶 framework 鍗?degree 14 / top 5.3% |

| 52 | `task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure` | Y妯″瀷鏍硅妭鐐瑰寲锛欸raphRAG rebuild + 绱㈠紩缁存姢 + pipeline 鐩戞帶 | reviewed | 榛勮嵂甯?| GraphRAG rebuild + 鐩戞帶 | 渚濊禆 #51 绾?A 瀹屾垚锛坹t-decision-y-model 閲嶅啓 + 鎵归噺 related锛?| `60_feedback/tasks/task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md` | 娆ч槼閿嬪鏌ラ€氳繃锛歩ndex/graph rebuild 鎴愬姛锛泍t-decision-y-model degree 100 / top 0.24%锛? 鏉″吀鍨嬭矾寰?2 hops锛沺ipeline 鍩虹嚎鏃?lint/閾炬帴/鏍煎紡寮傚父锛況elated 鏀逛负 bare id 鍚?GraphRAG 杈圭敓鏁堬紱7 澶╄繛缁洃鎺ф湭鍦ㄤ細璇濆唴瀹屾垚锛屽凡璁板綍涓哄悗缁瘡鏃ュ姩浣?|

| 53 | `task_20260703_laowantong-case-backfill-wobeirushen-time-management` | 妗堜緥鍗¤ˉ鎸栵細鍚捐緢濡傜 + 鏃堕棿绠＄悊鍩熺己澶?companion case锛?-6 寮狅級 | reviewed | 鑰侀〗绔?Kimi) | 4 寮?case | 渚濊禆 #40/#41 reviewed | `60_feedback/tasks/task_20260703_laowantong-case-backfill-wobeirushen-time-management.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛? 寮?companion case 鍗?+ 8 寮犻敋瀹氬崱鍙嶅悜鍥為摼锛汢MW 85% 宸茬籂鍋忎负 idle time 鈫?5%锛涘叏搴?lint 0 ERROR锛沇ARNING 浠?2581 闄嶈嚦 2542 |

| 54 | `task_20260703_wangyuyan-retroactive-case-scan-pilot` | 宸叉秷鍖栫礌鏉愭渚嬪崱琛ユ壂璇曠偣锛氱瀛﹀喅绛?/ 娉涗骇鍝佽璁?/ 鎴樼暐 | reviewed | 鑰侀〗绔?Kimi) | 3 涓煙鍊欓€夋竻鍗曪紙绉戝鍐崇瓥鈮?0 / 娉涗骇鍝佽璁♀墺30 / 鎴樼暐鈮?0锛?| 涓嶉樆濉?#42/#51/#53 | `60_feedback/tasks/task_20260703_wangyuyan-retroactive-case-scan-pilot.md` | 鐜嬭瀚ｇ嫭绔嬪垽鏂細鍋氫絾涓嶅叏閲忥紱鍏堣瘯鐐?3 涓珮浼樺厛绾у煙锛涗笉涓?#42 鍚堝苟锛涙帓闄ゅ凡鐢?#53 瑕嗙洊鐨勬椂闂寸鐞?鍚捐緢濡傜锛涘彧鎵弿鏍囪鍊欓€夛紝涓嶇洿鎺ヤ骇瀹屾暣 case 鍗?|

| 55 | `task_20260703_laowantong-yitang-Y-model-os` | Y妯″瀷 OS锛氭墍鏈?Agent 鐨勫叡浜簳灞?prompt + 鍙€?Coach 妯″紡 | reviewed | 鑰侀〗绔?Kimi) | 1 寮?system OS 鍗?+ agent-native-card-design 鏇存柊 + 1 寮犲彲閫?Coach 妯″紡 agent-spec + 1 涓煙 Agent 闆嗘垚绀轰緥 | 渚濊禆 #51 reviewed | `60_feedback/tasks/task_20260703_laowantong-agent-spec-yitang-Y-model-coach.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛欰gent 鍒嗗眰娓呮櫚锛汷S/鍩?鐢ㄦ埛涓夊眰缁撴瀯钀藉湴锛汣oach 妯″紡闈炶皟搴﹀櫒锛汷PC 閿€鍞璇濆姪鎵嬪凡鍔犺浇 OS 灞傦紱2 涓湡瀹炴ā鍨嬫祴璇曢€氳繃锛涘叏搴?lint 0 ERROR锛涙敞鎰?queue_transition.py review 浠嶆棤娉曟寜 frontmatter id 瀹氫綅鏈换鍔″崟锛岄渶榛勮嵂甯堝悓姝ヤ慨澶?|

| 56 | `task_20260703_laowantong-yitang-Y-model-stub-completion` | #51 鏀跺熬锛氬疄浜嬫眰鏄?/ 瑙ｆ斁鎬濇兂 framework 鍗¤ˉ鍏?| closed_cancelled | 鈥?| 鈥?| #51 宸插叏閮ㄥ畬鎴愶紝鏈换鍔″彇娑?| `60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-stub-completion.md` | 鍙栨秷鍘熷洜锛?51 缁堝鍓嶈€侀〗绔ュ凡琛ュ叏 2 涓?framework stub锛屾棤闇€鍗曠嫭鏀跺熬浠诲姟 |

| 57 | `task_20260703_laowantong-graphrag-orphan-reduction` | GraphRAG 鍋ュ悍搴︽彁鍗囷細璺ㄥ煙 related 琛ラ摼闄嶄綆 orphan 姣斾緥 | reviewed | 鑰侀〗绔?Kimi) | 578 寮?orphan 鍗¤ˉ閾?/ 847 鏉℃柊澧?related | 渚濊禆 #52 reviewed | `60_feedback/tasks/task_20260703_laowantong-graphrag-orphan-reduction.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歰rphan 18% (621/3468)銆乧omponents 669銆乭ealth 90/100锛屼笁椤规寚鏍囧潎杈炬爣锛?78 寮犲崱 pre-submit 鍏ㄩ儴 PASS锛涙棩蹇?`60_feedback/diagnosis/diag_20260704_graphrag-orphan-linking-log.json`锛涢儴鍒?hub 閾炬帴锛堝 tool-ai-prd-for-ai锛夐珮棰戜娇鐢紝鍚庣画鍙簿绛?|

| 58 | `task_20260703_huangyaoshi-agent-tcpr-role-layer` | Agent 鑳藉姏鍒嗗眰寮曞叆 TCPR 瑙掕壊妯″瀷锛氭墍鏈?Agent 鍗忎綔鍓嶅繀椤婚€夊畾 T/C/P/R 韬唤 | reviewed | 鑰侀〗绔?Kimi) | 1 system + 2 framework鏇存柊 + 7 agent-spec retrofit + 璁捐瑙勮寖鏇存柊 + lint 澧炲己 + retrofit 鎸囧崡 | 渚濊禆 #50 reviewed锛涘彲涓?#55 骞惰璁捐锛屾渶缁堜笌 Y妯″瀷 OS 瀵归綈锛涢粍鑽笀浠?co_architect | `60_feedback/tasks/task_20260703_huangyaoshi-agent-tcpr-role-layer.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛歛gent-os.md 宸插崌绾т负杩愯鏃?OS锛沘gent-native-card-design.md 鏂板 TCPR 绔犺妭锛? 寮?OPC agent-spec 宸茶ˉ TCPR 瀛楁涓?System Prompt 韬唤澹版槑锛沋妯″瀷 OS 绗?0 姝ュ凡瀵归綈锛沰do_lint.py 鏂板 WARNING 绾?TCPR 鏍￠獙锛況etrofit 鎸囧崡宸蹭骇鍑猴紱13 涓敼鍔ㄦ枃浠?pre-submit 鍏ㄩ儴 PASS |

| 59 | `task_20260703_huangyaoshi-agent-prompt-compiler` | Agent Prompt 缂栬瘧鍣細鎶?agent-os.md + 鍩熷崱缂栬瘧涓哄彲娉ㄥ叆鐨?system prompt | reviewed | 榛勮嵂甯?| 1 涓?CLI/skill + 1 璁捐瑙勮寖鏇存柊 + 3 涓瘯鐐圭紪璇?prompt + 1 浠戒娇鐢ㄨ鏄?| 渚濊禆 #55/#58 宸叉弧瓒?| `60_feedback/tasks/task_20260703_huangyaoshi-agent-prompt-compiler.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 60 | `task_20260703_huangyaoshi-fix-queue-transition-review-lookup` | 淇 queue_transition.py review 鎸?frontmatter id 鏌ユ壘浠诲姟鍗?| done | 榛勮嵂甯?| 1 涓?bugfix + 1 涓洖褰掓祴璇?| 鏃?| `60_feedback/tasks/task_20260703_huangyaoshi-fix-queue-transition-review-lookup.md` | 宸插畬鎴?|

| 61 | `task_20260704_laowantong-case-production-54-pilot-A-candidates` | #54 璇曠偣 A 绾у€欓€夋姇浜э細7 寮?companion case 鍗?| reviewed | 鑰侀〗绔?Kimi) | 7 寮?case 鍗?| 渚濊禆 #54 reviewed锛堝凡婊¤冻锛?| `60_feedback/tasks/task_20260704_laowantong-case-production-54-pilot-A-candidates.md` | 鐜嬭瀚ｈ拷鍔狅細鎶?#54 璇婃柇鎶ュ憡涓闃抽攱鍦堝畾鐨?7 鏉?A 绾у€欓€夎浆鍖栦负瀹屾暣 case 鍗★紱楠岃瘉鎵弿娴佺▼鐨勫€欓€夎川閲忥紱P2锛屾帓鍦?#58 涔嬪悗 |

| 62 | `task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt` | #59 寰€哄姟锛欰gent Prompt 璁捐瑙勮寖琛ュ叏涓?source 瀛楁鏍囧噯鍖?| done | 榛勮嵂甯?| 1 涓璁¤鑼冩洿鏂?+ 3+ agent-spec 鍗?frontmatter 琛ュ叏 + lint 瑙勫垯澧炲己 | 渚濊禆 #59 reviewed | `60_feedback/tasks/task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt.md` | 宸插畬鎴?|

| 63 | `task_20260704_laowantong-yihang-dual-triangle-batch2-supplement` | 涓€琛屽弻涓夎绗簩鎵规渚嬭ˉ浜э細澶╂湯/闃胯豹/鑺辨€?闄堝ぉ 4 寮?case 鍗?| done | 鑰侀〗绔?Kimi) | 4 寮犲畬鏁?case 鍗?+ 绗竴鎵?14 寮犲崱浜ゅ弶妫€鏌?| 渚濊禆鐜嬭瀚ｇ涓€鎵?14 寮犲崱 pre-submit PASS | `60_feedback/tasks/task_20260704_laowantong-yihang-dual-triangle-batch2-supplement.md` | 娆ч槼閿嬪凡缁堝閫氳繃锛涜€侀〗绔ュ彲閲婃斁璧勬簮 |

| 64 | `task_20260704_laowantong-truman-feishu-to-slide-case` | Truman銆岄涔?To slide銆峆PT 杩唬妗堜緥鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?S+ 鏍稿績 case 鍗?| 鏃狅紱鐜嬭瀚ｅ叆鍙ｆ爣娉ㄥ凡瀹屾垚 | `60_feedback/tasks/task_20260704_laowantong-truman-feishu-to-slide-case.md` | P0锛氫换鍔″崟缂栧彿宸蹭慨姝ｄ负 #64锛涘睍绀?Y妯″瀷 **杩唬鍙戝姩鏈?* 鑰岄潪闈欐€佸垎鏋愶紱蹇呴』鍚汉鐗?鍔ㄤ綔/鏃堕棿绾匡紱蹇呴』鏄犲皠鍏绱狅紱蹇呴』鍐欐竻鏈疆杩唬瀵瑰弻涓夎妗嗘灦鐨勮础鐚?|

| 65 | `task_20260704_laowantong-y-model-dual-triangle-bridge-framework` | Y妯″瀷 脳 鍙屼笁瑙掑崗鍚屽伐浣滄硶妗嗘灦鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?framework/method 鍗?| 渚濊禆 #64 妗堜緥鍗★紙鍙苟琛岋紝浣嗙粓瀹″墠闇€浜掔浉瀵圭収锛?| `60_feedback/tasks/task_20260704_laowantong-y-model-dual-triangle-bridge-framework.md` | P0锛氫换鍔″崟缂栧彿宸蹭慨姝ｄ负 #65锛涙柊澧炲绋胯姹傗€斺€斿垱閫犲姏瀹氫箟銆佺伒鎰熷尯鍒嗐€佷綋绯?妯″瀷杈圭晫鎰忚瘑锛涙妸銆屽弻涓夎鏄?Y妯″瀷 **涓€杞竴杞窇鍑烘潵鐨勬鏋舵€ц璇?*銆嶅彉鎴愬彲璋冪敤璧勪骇 |

| 66 | `task_20260704_laowantong-human-in-the-loop-dual-triangle-relation` | 浜哄湪鐜?脳 鍙屼笁瑙掑叧绯诲崱 | reviewed | 鑰侀〗绔?Kimi) | 1 寮?concept/framework 鍗?| 渚濊禆 #65 reviewed 鍚庡惎鍔?| `60_feedback/tasks/task_20260704_laowantong-human-in-the-loop-dual-triangle-relation.md` | P1锛氫换鍔″崟缂栧彿宸蹭慨姝ｄ负 #66锛涙緞娓呫€屽師鍒?鈫?鑳藉姏銆嶅叧绯伙紱浜哄湪鐜槸娌荤悊璧风偣锛屽弻涓夎鏄兘鍔涘湴鍥撅紱鐢?Truman PPT 妗堜緥灞曠ず浠庛€屼汉鍦ㄧ粏鑺傘€嶅埌銆屼汉鍦ㄦ鏋躲€嶇殑杩涘寲 |

| 67 | `task_20260704_laowantong-y-model-engine-layer-method` | Y妯″瀷 寮曟搸灞傛搷浣滄硶鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?method 鍗?| 渚濊禆 #65 reviewed 鍚庡惎鍔?| `60_feedback/tasks/task_20260704_laowantong-y-model-engine-layer-method.md` | P1锛氫换鍔″崟缂栧彿宸蹭慨姝ｄ负 #67锛涙柊澧?ROI 婊ョ敤/浠ュ亸姒傚叏闄烽槺锛涙妸 Y妯″瀷 浠庡垎鏋愭鏋堕噸瀹氫綅涓鸿凯浠ｅ彂鍔ㄦ満锛汿ruman PPT 妗堜緥鏄渶浣虫紨绀?|

| 68 | `task_20260704_laowantong-cross-domain-framework-iteration-audit` | 璺ㄥ煙瀹¤锛氭鏋舵槸鍚﹁闈欐€佸寲 | reviewed | 鑰侀〗绔?Kimi) | 1 浠藉璁℃姤鍛?+ 楂橀闄╀慨澶嶄换鍔″崟 | 渚濊禆 #64/#65 reviewed 鍚庡惎鍔?| `60_feedback/tasks/task_20260704_laowantong-cross-domain-framework-iteration-audit.md` | P2锛氫换鍔″崟缂栧彿宸蹭慨姝ｄ负 #68锛涙帓鏌?KDO 鍏朵粬鍩熸槸鍚︿篃鐘€屾妸 Y妯″瀷/妗嗘灦褰撻潤鎬佸伐鍏枫€嶇殑閿欒锛涘彲鍦?#64/#65 涔嬪悗鍚庡彴鎵ц |

| 69 | `task_20260704_wangyuyan-dual-triangle-canvas-agent-cli` | 鍙屼笁瑙掔敾甯?Agent CLI 浜や粯 | reviewed | 榛勮嵂甯?| 1 涓?CLI 宸ュ叿 + 1 涓?agent-spec v2 + 5 涓祴璇曞満鏅?| 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-canvas-agent-cli.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 70 | `task_20260704_laowantong-dual-triangle-afterclass-chat-cards` | 鍙屼笁瑙掕鍚庨棽鑱婃礊瀵熷崱鐗囧寲 | reviewed | 鑰侀〗绔?Kimi) | 11 寮犲崱 | 鏃?| `60_feedback/tasks/task_20260704_laowantong-dual-triangle-afterclass-chat-cards.md` | P1锛氬凡瑙ｉ攣銆傚惈鍒绘剰缁冧範娉?瀹＄編涓夋娉?鐭ヨ瘑鏁版嵁瑙ｈ€?鏁欒偛闈炴爣/瑙勬ā缁忔祹瀵规姉/鐮斿彂鎯呮劅浠ｄ环/鏁版嵁鍖呬俊浠昏竟鐣?鍦烘櫙鏃堕棿绾?浜旀娉曡矾绾垮浘 |

| 71 | `task_20260704_laowantong-yitang-underlying-logic-case-method-cards` | 搴曞眰閫昏緫涓夎绋嬭ˉ浜э細妗堜緥 + 鏂规硶 + 宸ュ叿鍗?| reviewed | 鑰侀〗绔?Kimi) | 33 寮狅紙13 P0 + 13 P1 + 6 P2锛?| 鏃?| `60_feedback/tasks/task_20260704_laowantong-yitang-underlying-logic-case-method-cards.md` | 娆ч槼閿嬬粓瀹￠€氳繃銆俢oncept/principle 鍗″亸钖勶紝宸茶褰曚负 P2 鍊哄姟 鈫?#95 |

| 72 | `task_20260704_laowantong-aesthetic-library-method-tool-cards` | 瀹＄編蹇€熷缓绔嬪伐浣滄硶 + 瀹＄編搴撻噰闆嗗伐鍏峰崱 | reviewed | 鑰侀〗绔?Kimi) | 3 寮狅紙1 method + 1 tool + 1 case锛?| 鏃?| `60_feedback/tasks/task_20260704_laowantong-aesthetic-library-method-tool-cards.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 73 | `task_20260704_wangyuyan-agent-card-skill-execution-pattern` | Agent 鍩轰簬 KDO 鍗＄墖/Skill 瑙ｅ喅瀹為檯闂鐨勬墽琛屾ā寮忚璁?| reviewed | 榛勮嵂甯?| 1 浠借璁℃枃妗?+ 1 寮犳鏋跺崱 + 1 涓彲杩愯鍘熷瀷 | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-agent-card-skill-execution-pattern.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 74 | `task_20260704_laowantong-ai-feature-thinking-concept` | AI 鍩烘湰鍔?Feature 鎬濈淮姒傚康鍗?+ 閲嶅埗涓ゅ紶鑽夌鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?concept + 2 寮?tool | 鏃?| `60_feedback/tasks/task_20260704_laowantong-ai-feature-thinking-concept.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 75 | `task_20260704_wangyuyan-ai-feature-inventory-research` | AI 宸ュ叿鐗规€ф竻鍗曞叏缃戣皟鐮斾笌寤鸿 | reviewed | 鐜嬭瀚?| 1 寮?tool + 2 寮犻鍩熺壒鎬у崱 | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-ai-feature-inventory-research.md` | 鎶婁笂涓嬫枃宸ョ▼/鎻愮ず璇?Codex/Hermes/榫欒櫨鎸夋渶灏忔妧鏈壒鎬у師瀛愬寲鎷嗚В |

| 76 | `task_20260704_wangyuyan-dual-triangle-degradation-spiral` | 鍙屼笁瑙掓浜￠杞?dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-degradation-spiral.md` | P1 |

| 77 | `task_20260704_wangyuyan-hITL-dual-triangle-supplement` | #66 杩借ˉ锛氫汉鍦ㄧ幆鍘嗗彶瀹氫綅 | reviewed | 鑰侀〗绔?Kimi) | 1 寮犲崱鍗曠偣淇敼 | #66 reviewed 鉁?| `60_feedback/tasks/task_20260704_wangyuyan-hITL-dual-triangle-supplement.md` | P2 |

| 78 | `task_20260704_wangyuyan-ai-native-dual-triangle-kernel` | AI 鍘熺敓鏄粨鏋滐紝鍙屼笁瑙掓槸寮曟搸 framework | reviewed | 鑰侀〗绔?Kimi) | 1 寮?framework | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-ai-native-dual-triangle-kernel.md` | P1 |

| 79 | `task_20260704_wangyuyan-framework-staticization-repair` | #68 瀹¤淇锛? 寮犳鏋跺崱寮曟搸鍖栬竟鐣屽０鏄?| reviewed | 鑰侀〗绔?Kimi) | 5 寮犲崱杩藉姞杈圭晫娈佃惤 | #68 reviewed | `60_feedback/tasks/task_20260704_wangyuyan-framework-staticization-repair.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 80 | `task_20260704_wangyuyan-report-book-learner-dk` | 鎶ュ憡涔﹀瀷瀛︿範鑰?dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-report-book-learner-dk.md` | P2 |

| 81 | `task_20260704_wangyuyan-patch-canvas-risk-judgment` | #69 淇ˉ锛氱敾甯?Agent 鍔犻闄╁垽鏂緭鍑?| done | 榛勮嵂甯?| agent-spec 鏇存柊 + CLI 鍔熻兘杩藉姞 | #69 瀹屾垚 | `60_feedback/tasks/task_20260704_wangyuyan-patch-canvas-risk-judgment.md` | 榛勮嵂甯堝凡瀹屾垚銆傜敾甯?Agent 姣忔牸鏍囨敞 [纭]/[鍋囪]/[绌虹櫧]锛岀粨鏉熻緭鍑洪闄╂憳瑕?|

| 82 | `task_20260704_wangyuyan-patch-aesthetic-boundary` | #72 淇ˉ锛氬缇庝笁绾︽潫 | reviewed | 鑰侀〗绔?Kimi) | method + tool 鍗℃洿鏂?| #72 reviewed 鉁?宸茶В閿?| `60_feedback/tasks/task_20260704_wangyuyan-patch-aesthetic-boundary.md` | P2 |

| 83 | `task_20260704_wangyuyan-patch-feature-thinking-supplement` | #74 淇ˉ锛欶eature 鎬濈淮瀹屾暣鎿嶄綔瀹氫箟 + 閬楁紡妗堜緥 | reviewed | 鑰侀〗绔?Kimi) | concept 鍗℃洿鏂?| 渚濊禆 #74 瀹屾垚 | `60_feedback/tasks/task_20260704_wangyuyan-patch-feature-thinking-supplement.md` | P2锛氬彛杩扮 L1402-1451 Feature 鎿嶄綔瀹氫箟锛堝師瀛愬寲/鍙祴/璺ㄥ伐鍏凤級+ Feature vs Skill 鍖哄垎 + 璞嗗寘绉冨ご/榫欒櫨鐖遍┈浠曟渚?|

| 84 | `task_20260704_wangyuyan-knowledge-data-decoupling-framework` | 鐭ヨ瘑灞備笌鏁版嵁灞傝В鑰?framework 鍗★紙YAI 鏋舵瀯娲炲療锛?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?framework | 鏃狅紱绱犳潗宸插氨浣嶏紙鍙ｈ堪绋?L5025-5078锛?| `60_feedback/tasks/task_20260704_wangyuyan-knowledge-data-decoupling-framework.md` | P1锛歒AI 鏍稿績鏋舵瀯鍐崇瓥鈥斺€旂郴缁熸牳蹇冭瘝锛堝缇?浣撶郴锛変笌 data pack 鍒嗗紑鐢熶骇銆佹彃浠跺紡缁勫悎銆傜洿鎺ュ鎺?#59 Prompt 缂栬瘧鍣ㄥ拰 #73 Agent 鎵ц妯″紡銆備笉绛?#70 瑙ｉ攣 |

| 85 | `task_20260704_wangyuyan-dual-triangle-ai-review-method` | 鍙屼笁瑙?AI 杈呭姪澶嶇洏娉?method 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?method | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-ai-review-method.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 86 | `task_20260704_wangyuyan-methodology-production-pipeline` | 鏂规硶璁虹敓浜ф祦姘寸嚎 concept 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?concept | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-methodology-production-pipeline.md` | P2 |

| 87 | `task_20260704_wangyuyan-dual-triangle-oral-spray-skill` | 鍙ｅ柗 Skill锛氬弻涓夎鍐呭姛 + 涔濆瓧璇€澶栧姛 | reviewed | 鑰侀〗绔?Kimi) | 1 涓?Skill + 1 寮?tool | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-oral-spray-skill.md` | P1锛氬彛杩扮 L2330-2610銆備箣鍓嶆紡鍏ラ槦 |

| 88 | `task_20260704_wangyuyan-dual-triangle-xray-deconstruct-skill` | X鍏夋媶瑙?Skill锛氬弻涓夎妗堜緥閫嗗悜宸ョ▼ | reviewed | 鑰侀〗绔?Kimi) | 1 涓?Skill + 1 寮?tool | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-xray-deconstruct-skill.md` | P1锛氬彛杩扮 L2016-2218銆備箣鍓嶆紡鍏ラ槦 |

| 89 | `task_20260704_wangyuyan-knowledge-battle-station-workflow` | 鐭ヨ瘑绔欏満寤鸿 Workflow | reviewed | 鑰侀〗绔?Kimi) | 1 寮?method + 1 涓?Workflow | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-knowledge-battle-station-workflow.md` | P1锛氬彛杩扮 L462-600銆備箣鍓嶆紡鍏ラ槦 |

| 91 | `task_20260704_wangyuyan-marathon-case-batch-production` | 鍙屼笁瑙掗┈鎷夋澗鏈叆搴撴渚嬫壒閲忕敓浜?| reviewed | 鑰侀〗绔?Kimi) | 10+ 寮?case | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-marathon-case-batch-production.md` | P0锛氭闃抽攱缁堝閫氳繃 |

| 92 | `task_20260704_wangyuyan-vlm-cases-batch-ingest` | ~~VLM 宸插鐞嗘渚嬫壒閲忓叆搴搤~ | closed_merged | 鈥?| 鈥?| 宸茶 #91/#93 鏇夸唬 | 鈥?| 鈥?|

| 93 | `task_20260704_laowantong-dual-triangle-vlm-case-enrichment` | 鍙屼笁瑙?VLM 妗堜緥鎵归噺 enrichment | reviewed | 鑰侀〗绔?Kimi) | 46 寮?draft鈫掗儴鍒?enriched | 鏃?| `60_feedback/tasks/task_20260704_laowantong-dual-triangle-vlm-case-enrichment.md` | P1锛氫粠 draft 涓寫璐ㄩ噺鏈€楂樼殑 enrich |

| 94 | `task_20260704_wangyuyan-jumi-canvas-demo-case` | 宸ㄧ背鎺ㄥ箍鍙屼笁瑙掔敾甯冧節灞傚～鍏呮紨绀?case 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?case | 鏃狅紱绱犳潗宸插氨浣?| `60_feedback/tasks/task_20260704_wangyuyan-jumi-canvas-demo-case.md` | P1锛歩nbox 涓敮涓€璧板畬涔濆眰娣辨寲鍏ㄦ祦绋嬬殑鐪熷疄婕旂ず |

| 95 | `task_20260704_wangyuyan-patch-71-concept-thin-cards` | #71 鍊哄姟锛歝oncept/principle 鍗″姞鍘?| reviewed | 鑰侀〗绔?Kimi) | 鑻ュ共寮犱慨琛?| #71 reviewed | `60_feedback/tasks/task_20260704_wangyuyan-patch-71-concept-thin-cards.md` | P2锛氭闃抽攱鍙戠幇 concept/principle 鍗″亸钖勩€傝ˉ榻愯揪鏍囧嵆鍙?|

| 96 | `task_20260704_laowantong-case-section-linter-error-cleanup` | linter 瑙勫垯鍗囩骇锛?6 寮?case 鍗℃爣鍑?section 琛ュ叏 | reviewed | 鑰侀〗绔?Kimi) | 56 寮犺ˉ section | 鏃狅紱P2 鎺掍富绾垮悗 | `60_feedback/tasks/task_20260704_laowantong-case-section-linter-error-cleanup.md` | P2锛歭inter 瑙勫垯鍙樻洿鏆撮湶鐨勫瓨閲忓€?|

| 97 | `task_20260704_wangyuyan-ai-self-xray-decomposition` | AI 鑷垜 X 鍏夋媶瑙ｄ笌杩唬 method 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?method | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-ai-self-xray-decomposition.md` | P1锛氬彛杩扮 L2118-2136鈥斺€擜I 涓诲姩瀛﹀弻涓夎鈫掓媶鑷繁銆備笌 #85 琚姩澶嶇洏涓嶅悓锛屾槸涓诲姩鑷垎瑙?|

| 98 | `task_20260704_wangyuyan-agent-self-flywheel-review` | Agent 鑷鐩橈細椋炶疆寮曟搸浠庢墜鍔ㄥ埌鑷姩鍖?| reviewed | 榛勮嵂甯?| flywheel.py --auto + 1 Agent 璇曠偣 | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-agent-self-flywheel-review.md` | 宸插畬鎴愶細Truman YAI 澶嶇洏娉曞凡鍐欏叆 agent-os.md 搂10 |

| 99 | `task_20260704_wangyuyan-agent-config-human-portrait-template` | Agent 閰嶇疆锛氫汉绫荤敾鍍?瑙勫垯鍖归厤 7 姝ユ硶 tool 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?tool | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-agent-config-human-portrait-template.md` | P1锛氬彛杩扮 L2460-2610鈥斺€旈緳铏惧姪鐞?7 姝ラ厤缃粨鏋?|

| 100 | `task_20260704_wangyuyan-canvas-preparation-method-dk` | 鍙屼笁瑙掔敾甯冪澶囦笁鍘熷垯 dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-canvas-preparation-method-dk.md` | P1锛氳姳鎬昏浆鎶?鍏堝姞娉曞悗鍑忔硶/15鍒嗛挓鍑虹杞?|

| 101 | `task_20260704_wangyuyan-dual-triangle-team-assembly-method` | 鍙屼笁瑙掑垎宸ユ嫾鍥?method 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?method | 鏃?| `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-team-assembly-method.md` | P1锛氭帹缈?浜у搧+涓氬姟+绋嬪簭鍛?鍏紡銆傞」鐩鐞喢椾汉绫讳笁瑙捗桝I涓夎銆傞」鐩粡鐞嗚京璇佸績鎬?绮惧噯绱㈠彇 |

| 102 | `task_20260705_wangyuyan-fde-ai-native-org-framework` | FDE 宸ョ▼ 脳 AI 鍘熺敓缁勭粐 framework 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?framework | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-fde-ai-native-org-framework.md` | P1锛欶DE鎰挎櫙+缁勭粐鏂囧寲銆傚叏缃戣皟鐮斾氦鍙夐獙璇?|

| 103 | `task_20260705_wangyuyan-enrich-weapon-library` | 姝﹀櫒搴撳崱 enrichment锛氳ˉ VLM 娣卞害鍒嗘瀽 5 娲炲療 | reviewed | 鑰侀〗绔?Kimi) | 1 寮?enrich | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-enrich-weapon-library.md` | P1锛氱幇鏈?draft 鍗″凡鏈?6脳4 鐭╅樀銆傝ˉ 5 娲炲療 + 5 瀹炶返鍦烘櫙 |

| 104 | `task_20260705_wangyuyan-agent-distillation-method` | Agent 钂搁鏂规硶锛氬璇濃啋绯荤粺鎻愮ず璇?5 姝ユ鏋?| reviewed | 鐜嬭瀚?| 1 浠借璁℃枃妗?| 鏄庡ぉ鎵ц | `60_feedback/tasks/task_20260705_wangyuyan-agent-distillation-method.md` | 缂濆悎璇剧▼+澶栭儴璋冪爺銆傝緭鍑哄彲鎸傝浇 system prompt |

| 105 | `task_20260705_wangyuyan-kdo-agent-design-meta-method` | KDO Agent 璁捐鍏冩柟娉曪細鐢ㄥ弻涓夎鍔犻€?Agent 寤鸿 | reviewed | 鐜嬭瀚?| 1 寮?method + 1 涓ā鏉?| 渚濊禆 #69 #97 #98 | `60_feedback/tasks/task_20260705_wangyuyan-kdo-agent-design-meta-method.md` | 鎶?Truman 鍋?partner 鐨勬柟娉曪紙鐢诲竷鈫掕凯浠ｂ啋鑷鐩橈級鍥哄寲涓?KDO Agent 寤鸿鏍囧噯 |

| 106 | `task_20260705_wangyuyan-ymodel-case-batch` | Y妯″瀷 鍙ｈ堪绋挎渚嬫壒閲忕敓浜э紙5 寮?case 鍗★級 | reviewed | 鑰侀〗绔?Kimi) | 5 寮?case | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-ymodel-case-batch.md` | 鑰侀〗绔ュ凡鎻愪氦銆傚緟娆ч槼閿嬪 |

| 107 | `task_20260705_laowantong-fix-source-refs-paths` | 淇 4 涓?source_refs 璺緞 | reviewed | 鑰侀〗绔?Kimi) | 4 涓枃浠朵慨澶?| 鏃?| `60_feedback/tasks/task_20260705_laowantong-fix-source-refs-paths.md` | P2锛? 涓崱鐗?source_refs 鎸囧悜涓嶅瓨鍦ㄧ殑鏂囦欢 |

| 108 | `task_20260705_huangyaoshi-lint-warning-infra` | lint WARNING 鍩虹璁炬柦杩唬 | reviewed | 榛勮嵂甯?| 1 浠藉垎鏋愭姤鍛?| 鏃?| `60_feedback/tasks/task_20260705_huangyaoshi-lint-warning-infra.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 109 | `task_20260705_wangyuyan-shishi-qiushi-case-batch` | 瀹炰簨姹傛槸鍗佸潙妗堜緥鍗℃壒閲忕敓浜э紙10 寮?case 鍗★級 | reviewed | 鑰侀〗绔?Kimi) | 10 寮?case | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-shishi-qiushi-case-batch.md` | P1锛氭闃抽攱缁堝閫氳繃 |

| 111 | `task_20260705_wangyuyan-canvas-agent-spec-v3-upgrade` | 鐢诲竷 Agent agent-spec v3 鍗囩骇鈥斺€旀敞鍏?YAI 钂搁鏂规硶璁?| done | 鐜嬭瀚?| 1 涓?agent-spec 鍗囩骇 | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-canvas-agent-spec-v3-upgrade.md` | 宸插畬鎴愶細agent-spec v2鈫抳3锛屾敞鍏?10 椤硅兘鍔涙ā寮?|

| 110 | `task_20260705_laowantong-fix-3-content-quality` | 淇 3 鏉″唴瀹硅川閲忛棶棰?| reviewed | 鑰侀〗绔?Kimi) | 3 涓枃浠朵慨澶?| 鏃?| `60_feedback/tasks/task_20260705_laowantong-fix-3-content-quality.md` | P2锛氭鍣ㄥ簱鍗ody/鍥涜绱犲崱鏍囬/寮€婧愮煡璇嗗崱鏍囩 |

| 112 | `task_20260705_wangyuyan-multi-ai-cross-validation-dk` | 澶?AI 浜ゅ弶姣斿楠岃瘉娉?dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-multi-ai-cross-validation-dk.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 113 | `task_20260705_wangyuyan-register-xiaohongshu-skill` | 灏忕孩涔﹀畾浣?Skill 娉ㄥ唽鍏ュ簱 | reviewed | 鑰侀〗绔?Kimi) | 1 涓?Skill 娉ㄥ唽 | 鏃?| `60_feedback/tasks/task_20260705_wangyuyan-register-xiaohongshu-skill.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 114 | `task_20260706_wangyuyan-non-expert-judgment-dk` | 闈炰笓瀹跺垽鏂浛浠ｆ硶 dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260706_wangyuyan-non-expert-judgment-dk.md` | P1锛氶潪涓撲笟鍩熷浣曢€氳繃澶欰I浜ゅ弶姣斿+瀹炶瘉楠岃瘉寤虹珛鍙敤鍒ゆ柇鍔涖€傜粨鏋勫伐绋嬪浘绾?浠ｇ爜搴撴⒊鐞嗗弻妗堜緥 |

| 115 | `task_20260706_wangyuyan-ai-false-certainty-dk` | AI 閿欒绗冨畾妯″紡 dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260706_wangyuyan-ai-false-certainty-dk.md` | P1锛欳laude鏂╅拤鎴搧璇?Windows 10鏃犺В"鈫掕拷闂皟鐮斺啋瑙ｅ喅浜嗐€侫I琚璁℃潵鍥炵瓟闂锛屾湭琚憡鐭?鎰忚瘑鍒拌嚜宸变笉鐭ラ亾" |

| 116 | `task_20260706_wangyuyan-agent-hr-role-method` | Agent HR 瑙掕壊锛堝厓 Agent锛塵ethod 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?method | 鏃?| `60_feedback/tasks/task_20260706_wangyuyan-agent-hr-role-method.md` | P1锛氫笓闂ㄥ叧娉ㄥ叾浠?Agent 琛屼负琛ㄧ幇骞惰瘎浼扮殑鍏傾gent銆傝€佹湵宸插疄璺碉紝鍙戠幇寰堟湁鏁?|

| 117 | `task_20260706_wangyuyan-technical-domain-aesthetic-dk` | 涓ユ牸鎶€鏈煙瀹＄編寤虹珛 dk 鍗?| reviewed | 鑰侀〗绔?Kimi) | 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260706_wangyuyan-technical-domain-aesthetic-dk.md` | P2锛氱數瀛愬伐绋?SaaS/鏈烘缁撴瀯鍩熲€斺€斿灏辨槸瀵归敊灏辨槸閿欍€傛鍣ㄥ簱瀹＄編鍏冪骇琛ㄤ笉閫傜敤 |

| 118 | `task_20260706_huangyaoshi-session-context-pipeline` | 浼氳瘽涓婁笅鏂囪嚜鍔ㄥ帇缂╀笌鏃堕棿搴忓垪瀛樺偍绠＄嚎 | reviewed | 榛勮嵂甯?| 1 鏉¤嚜鍔ㄥ寲绠＄嚎 | 鏃?| `60_feedback/tasks/task_20260706_huangyaoshi-session-context-pipeline.md` | 娆ч槼閿嬬粓瀹￠€氳繃 |

| 119 | `task_20260707_wangyuyan-human-self-distillation-method` | 浜轰晶钂搁鏂规硶鈥斺€旀妸闅愭€у垽鏂樉鎬у寲 method 鍗?| reviewed | 鑰侀〗绔?| 1 寮?method | 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-human-self-distillation-method.md` | P1锛氱啓鐔?钂搁鎴戣嚜宸?鈥斺€旀壘閫夐/鎷嗙垎娆?鍐欑/鏀圭鍥涙鏄炬€у寲銆備笌 #104 AI渚ц捀棣忎簰琛?|

| 120 | `task_20260707_wangyuyan-agent-workstation-design-method` | ~~Agent 宸ヤ綅璁捐~~ | closed_merged | 鈥?| 鈥?| 宸插苟鍏?#122 | 鈥?| 璺ㄥ煙铻嶅悎锛氱啓鐔欏伐浣?= #105 鍦烘櫙瑙掑叿璞″寲锛屽悎骞惰繘 method-kdo-agent-design-meta |

| 121 | `task_20260707_wangyuyan-tool-upgrade-not-system-dk` | ~~宸ュ叿鍗囩骇鈮犵郴缁熷崌绾~ | closed_merged | 鈥?| 鈥?| 宸插苟鍏?#123 | 鈥?| 璺ㄥ煙铻嶅悎锛氬伐鍏峰崌绾ч櫡闃?= #76 姝讳骸椋炶疆鍙樹綋锛屽悎骞惰繘 dk-ai-collaboration-degradation-spiral |

| 122 | `task_20260707_wangyuyan-patch-105-agent-workstation` | #105 琛ュ厖鈥斺€擜gent 宸ヤ綅璁捐 | reviewed | 鑰侀〗绔?Kimi) | 1 涓皬鑺傝拷鍔?| 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-patch-105-agent-workstation.md` | P2锛氬伐浣嶆蹇?鐔欑啓4宸ヤ綅妗堜緥鍐欏叆 method-kdo-agent-design-meta |

| 123 | `task_20260707_wangyuyan-patch-76-tool-upgrade-trap` | #76 琛ュ厖鈥斺€斿伐鍏峰崌绾ч櫡闃?| reviewed | 鑰侀〗绔?Kimi) | 1 涓€€鍖栨ā寮忚拷鍔?| 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-patch-76-tool-upgrade-trap.md` | P2锛氭柊閫€鍖栨ā寮?鐔欑啓妗堜緥鍐欏叆 dk-ai-collaboration-degradation-spiral |

| 124 | `task_20260707_wangyuyan-oscar-enrichment` | ~~OSCAR 妗嗘灦鍗¤ˉ榻悀~ | closed_merged | 鈥?| 鈥?| 骞跺叆 #127 | 鈥?| 琚涔gent铻嶅悎鏂规鏇夸唬 |

| 125 | `task_20260707_wangyuyan-write-external-exploration-sop` | ~~external-exploration-sop~~ | closed_merged | 鈥?| 鈥?| 骞跺叆 #127 | 鈥?| 琚?SOP v2 鏇夸唬 |

| 126 | `task_20260707_huangyaoshi-review-check-retrieval` | review-check.py 澧炲姞妫€绱㈣涓烘鏌?| reviewed | 榛勮嵂甯?| 1 涓姛鑳借拷鍔?| 鏃?| `60_feedback/tasks/task_20260707_huangyaoshi-review-check-retrieval.md` | P1锛歝heck_retrieval鍑芥暟+A/B/C涓夌骇闂ㄦ銆傛闃抽攱缁堝閫氳繃 |

| 127 | `task_20260707_wangyuyan-oscar-kdo-fusion` | OSCAR-KDO 铻嶅悎鈥斺€旀鏋跺崱琛ラ綈+妗ユ帴鍗?SOP v2 | reviewed | 鑰侀〗绔?| 2 寮犲崱琛ラ綈 + 1 寮犳ˉ鎺ュ崱 + SOP v2 | 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-oscar-kdo-fusion.md` | P0锛歄SCAR鍓嶈交鍚庨噸琛DO鍓嶄笁姝?|

| 128 | `task_20260707_wangyuyan-judge-skill-meta-evaluation` | Judge Skill鈥斺€擪DO Agent/Skill 鍏冭瘎浼?method 鍗?| reviewed | 鑰侀〗绔?| 1 寮?method | 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-judge-skill-meta-evaluation.md` | P1锛氳摑楸糐udge Skill鏂规硶璁衡€斺€斾簲缁村害鎵撳垎锛堟爣鍑?杈圭晫/鍧?绾︽潫/闂ㄦ帶锛夛紝30鍒嗏啋95鍒?杞凯浠?|

| 129 | `task_20260707_wangyuyan-skill-seven-elements-upgrade` | Skill/Agent-spec 涓冭绱犲崌绾?dk 鍗?| reviewed | 鑰侀〗绔?| 1 寮?dk | 鏃?| `60_feedback/tasks/task_20260707_wangyuyan-skill-seven-elements-upgrade.md` | P2锛氳摑楸糞kill涓冭绱犮€侹DO agent-spec缂虹籂閿欏拰灏忓惊鐜?|

| 130 | `task_20260707_wangyuyan-canvas-agent-v4-upgrade` | 鐢诲竷 Agent v4鈥斺€旀敞鍏?Judge Skill + 涓冭绱?+ 闆疯揪鍥?| reviewed | 鑰侀〗绔?| 1 涓?agent-spec 鍗囩骇 | 渚濊禆 #128 #129 | `60_feedback/tasks/task_20260707_wangyuyan-canvas-agent-v4-upgrade.md` | P1锛氫笁璧勪骇娉ㄥ叆鈥斺€擩udge Skill浜旂淮鑷瘎+Skill涓冭绱犲畬鏁?钃濋奔闆疯揪鍥惧彲瑙嗗寲銆倂3鈫抳4 |

| 131 | `task_20260707_wangyuyan-project-management-domain-production` | 绠￠」鐩煙 P1 鏍稿績锛?3 寮犲崱 + 椤圭洰绠＄悊鍔╂墜 agent-spec | reviewed | 鈥?| 13 | 鏃?| `70_product/tasks/task_20260707_wangyuyan-project-management-domain-production.md` | 娆ч槼閿嬬粓瀹?A-锛? concept 閲嶅啓 + 5 framework锛堝惈 ABCD锛? 4 tool + 1 skill + 1 workflow + 1 agent-spec锛涘弽鍚戞洿鏂?鈮?4 寮犲凡鏈夊崱 related |

| 132 | `task_20260707_wangyuyan-project-management-domain-phase2` | 绠￠」鐩煙 P2 琛ヤ骇涓庢繁鎸栵細绾?30 寮犲崱 | reviewed | 鈥?| 30 | 渚濊禆 #131 reviewed | `70_product/tasks/task_20260707_wangyuyan-project-management-domain-phase2.md` | 娆ч槼閿嬬粓瀹?B+锛屽凡閫氳繃 queue_transition.py 鍏抽棴锛? case + 姝﹀櫒搴撳叆鍙?+ L5/L6 dk + 69 寮犲浘鎵归噺 tool |

| 133 | `task_20260708_wangyuyan-ai-outpost-episode2-production` | AI鍓嶅摠绔欑2闆嗗崱鐗囧寲锛? 寮犲崱锛? P0 + 4 P1锛?| reviewed | 鈥?| 8 | 鏃?| `70_product/tasks/task_20260708_wangyuyan-ai-outpost-episode2-production.md` | 娆ч槼閿嬬粓瀹?A-锛汸0锛欰I鎺у埗鍙?Agent骞冲彴鍙屽舰鎬併€乀oken Capital銆佸搧鍛崇郴缁熴€丅uilder骞昏锛汸1锛氭澃鏂囨柉鎮栬銆佸紑鏀?灏侀棴鍒嗙被鍣ㄣ€佸钩鍙版渚嬨€丆odex闃熷弸agent-spec |

| 134 | `task_20260708_wangyuyan-claude-retrospective-p0-fix` | Claude 鐜嬭瀚ｅ洖婧璁?P0 淇锛氬厓鏁版嵁涓€鑷存€т笌鍏抽敭鍐呭鏍″噯 | reviewed | 鈥?| 10 涓枃浠?| 鏃?| `70_product/tasks/task_20260708_wangyuyan-claude-retrospective-p0-fix.md` | 娆ч槼閿嬬粓瀹?A锛涗慨姝?frontmatter 鏃ユ湡/鐘舵€?YAML/鍗＄墖 ID 瀵归綈/浠诲姟鍗曞幓閲?retroactive scan 缁熻璇勭骇 |

| 135 | `task_20260708_wangyuyan-claude-retrospective-p1-supplement` | Claude 鐜嬭瀚ｅ洖婧璁?P1 琛ュ叏锛歴ource_refs 琛屽彿銆佸閮ㄩ獙璇佷笌璇婃柇娣卞害 | reviewed | 鈥?| 16 涓枃浠?| 渚濊禆 #134 reviewed | `70_product/tasks/task_20260708_wangyuyan-claude-retrospective-p1-supplement.md` | 娆ч槼閿嬬粓瀹?A锛涜ˉ鍏呯簿纭?source_refs銆佸閮?URL銆佽嚜鏀诲嚮/澶辫触妯″紡銆佷氦鍙夋瘮瀵硅〃 |

| 136 | `task_20260708_wangyuyan-sales-domain-deep-dive-supplement` | 閿€鍞煙鍙ｈ堪绋夸簩娆℃繁鎸栬ˉ浜э細鎿嶄綔灞傚伐鍏峰崱 + Agent 瑙勬牸 | reviewed | 鈥?| 6 鏂板崱 + 4 鍗囩骇 + 6 agent-spec | 鏃?| `70_product/tasks/task_20260708_wangyuyan-sales-domain-deep-dive-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細琛ラ綈鍓嶄笁绉掕瘽鏈€佽亞鍚笁涓冩硶鍒欍€佸洖娆?灞ョ害 playbook 绛?P0 缂哄彛锛屽苟閰嶅 6 涓攢鍞?Agent 瑙勬牸 |

| 137 | `task_20260708_wangyuyan-pan-product-domain-supplement` | 娉涗骇鍝佽璁″煙 P0-P2 琛ヤ骇锛氭鏋跺～鑲?+ 鍙跺瓙鍗囩骇 + Agent 瑙勬牸 | reviewed | 鈥?| 12 鍗?+ 7 agent-spec | 鏃?| `70_product/tasks/task_20260708_wangyuyan-pan-product-domain-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細4 寮犱腑灞傛鏋跺崱濉倝 + 6 寮犲彾瀛愬崱鍗囩骇 + 2 寮犳柊宸ュ叿鍗?+ 7 涓硾浜у搧 Agent 瑙勬牸锛涜В鍐?30/36 寮犵墝鍙ｅ緞鍐茬獊 |

| 138 | `task_20260708_wangyuyan-product-kernel-domain-supplement` | 浜у搧鍐呮牳鍩?P0-P2 琛ヤ骇锛氭牳蹇冩蹇靛崌绾?+ 妗堜緥鍗?+ 楠岃瘉宸ュ叿 + Agent 瑙勬牸 | reviewed | 鈥?| 12 鍗?+ 7 agent-spec | 鏃?| `70_product/tasks/task_20260708_wangyuyan-product-kernel-domain-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細3 寮?concept 鍗囩骇 + 1 寮犲叚绛栫暐楠岃瘉宸ュ叿鍗?+ 4 case + 2 DK + 7 涓唴鏍?Agent 瑙勬牸锛涚粺涓€楠岃瘉/杩唬妗嗘灦鍛藉悕 |

| 139 | `task_20260708_wangyuyan-time-management-agent-supplement` | 鏃堕棿绠＄悊鍩?P1 琛ヤ骇锛氬洓寮犳ā鍨嬪浘 + 鎿嶄綔宸ュ叿 + 妗堜緥 + 涓撳睘 Agent Spec | reviewed | 鈥?| 18 鍗?+ 1 agent-spec | 鏃?| `70_product/tasks/task_20260708_wangyuyan-time-management-agent-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細1 寮?concept 鍗囩骇 + 4 寮?framework + 8 寮?tool + 5 寮?case + 1 涓椂闂寸鐞嗕笓灞?Agent Spec锛涚敤鎴锋槑纭姹傗€滄椂闂寸鐞嗕笓闂ㄧ殑 agent鈥?|

| 140 | `task_20260708_wangyuyan-demand-analysis-agent-supplement` | 闇€姹傚垎鏋愬煙 P0-P2 琛ヤ骇锛氬啺灞卞伐鍏峰崱琛ュ叏 + 澶╄姳鏉挎鏋?+ 涓撳睘 Agent Spec | reviewed | 鈥?| 17 鍗?+ 1 agent-spec | 渚濊禆 #143/#144 | `70_product/tasks/task_20260708_wangyuyan-demand-analysis-agent-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細鐭ヨ瘑宸查獙璇侊紝缂?Agent 灏佽锛? Agent Spec + 6 L1-L6 宸ュ叿鍗¤ˉ鍏?+ 澶╄姳鏉垮洓灞傛鏋?+ RAT/璇勪及/寰浣撴劅宸ュ叿锛涚敤鎴锋槑纭€滈渶姹傛槸鏋佸叾閲嶈鐨勫煙鈥?|

| 141 | `task_20260708_wangyuyan-five-step-method-orchestrator-supplement` | 涓€鍫備簲姝ユ硶鍩?P0-P2 琛ヤ骇锛氭€绘鏋跺崱 + 瀛愭鏋跺崱 + orchestrator Agent Spec | reviewed | 鈥?| 10 鍗?+ 1 agent-spec | #143 宸?reviewed | `70_product/tasks/task_20260708_wangyuyan-five-step-method-orchestrator-supplement.md` | 鐜嬭瀚ｄ簩娆℃繁鎸栵細浜旀娉曟槸鏂规硶璁轰腑鏋紝缂烘€绘鏋跺崱銆佸闀垮懆鏈?澹佸瀿妗嗘灦鍗°€乷rchestrator Agent Spec锛涢渶鎶?#136-#140 瀛愬煙浠诲姟涓叉垚鍙鑸摼璺紱**Hermes 瀹炰緥宸插畬鎴愶紝娆ч槼閿嬬粓瀹?A-** |

| 142 | `task_20260708_wangyuyan-y-model-cross-domain-fusion-and-coach-agent` | Y妯″瀷 / 瀹炰簨姹傛槸 / 瑙ｆ斁鎬濇兂 璺ㄥ煙铻嶅悎锛氭€绘鏋跺崱 + 璺ㄥ煙 Coach Agent Spec | reviewed | 鈥?| 9 鍗?+ 1 agent-spec + 5 璇婃柇鏇存柊 | #143 宸?reviewed | `70_product/tasks/task_20260708_wangyuyan-y-model-cross-domain-fusion-and-coach-agent.md` | 鐜嬭瀚ｈ法鍩熸繁鎸栵細Y妯″瀷 鏄竴鍫傝绋嬫渶搴曞眰鏈川锛岄渶鎶婇渶姹?浜у搧/浜旀娉?閿€鍞?鏃堕棿绠＄悊/AI钀藉湴绛夊煙鏄犲皠璐€氾紝褰㈡垚璺ㄥ煙鎬绘鏋朵笌璺ㄥ煙 Coach Agent锛?*Kimi Code CLI 瀹炰緥宸插畬鎴愶紝娆ч槼閿嬬粓瀹?A-** |

| 143 | `task_20260708_wangyuyan-dual-triangle-cross-domain-agent` | 璺ㄥ煙鍙屼笁瑙掕瘖鏂?Agent锛欰gent 鍐涘洟鍏ュ彛鍒嗚瘖涓庡厓妗嗘灦鏍″噯 | reviewed | 鈥?| 6 鍗?+ 1 agent-spec | #144 reviewed | `70_product/tasks/task_20260708_wangyuyan-dual-triangle-cross-domain-agent.md` | 娆ч槼閿嬬粓瀹￠€氳繃锛涘弻涓夎鏍稿績鍗℃棌宸插畬澶囷紝缂?Agent 鍐涘洟鍏ュ彛鍏冭瘖鏂?Agent锛? Agent Spec + 3 宸ュ叿鍗★紙鍚煙娉ㄥ唽鎵╁睍鍗忚锛? 2 鐜版湁鍗?related 鍗囩骇 + 1 閮ㄧ讲璺緞 runbook锛涙敮鎸佹湭鏉ョ煡璇嗗煙鍙彃鎷旀帴鍏ワ紱**宸茶В闄?#141/#142 闃诲** |

| 144 | `task_20260708_huangyaoshi-capability-hub-phase1` | P-23 鑳藉姏涓彴 Phase 1锛歏LM 鑳藉姏涓婄嚎 + Agent 鍏变韩宸ュ叿搴曞骇 | reviewed | 鈥?| 1 浠ｇ爜妯″潡 + CLI + 鍚姩搴忓垪鏇存柊 | 鏃?| `70_product/tasks/task_20260708_huangyaoshi-capability-hub-phase1.md` | 榛勮嵂甯堝仠杞﹀満 P-23锛涙墍鏈?Agent 璋冪敤 VLM/OCR/鎼滅储鐨勫叡浜簳搴э紱0.5-1 澶╃‖鍓嶇疆锛汚gent 鍚姩搴忓垪鍔犲叆 `python -m capability_hub list` |

| 145 | `task_20260709_wangyuyan-key-assumptions-business-formula-agent` | 鍏抽敭鍋囪 + 涓氬姟鍏紡鎷嗚В鍩?P0-P2 琛ヤ骇锛氫富绾挎€绘鏋跺崱 + ABCD/涓夋澘鏂?涓氬姟鍏紡璐€氬崱 + orchestrator Agent Spec | reviewed | 鑰侀〗绔ワ紙kimi) | 12 鍗★紙6 鏂?+ 6-8 鍗囩骇锛? 1 agent-spec | #141/#143/#144 reviewed | `70_product/tasks/task_20260709_wangyuyan-key-assumptions-business-formula-agent.md` | 鐜嬭瀚ｆ繁鎸栵細鍏抽敭鍋囪涓荤嚎 + ABCD 妯″瀷 + 涓夋澘鏂?+ 瀛旀簮涓氬姟鍏紡鎷嗚В鏈疮閫氾紱浣嶄簬浜旀娉曘€岄渶姹傗啋浜у搧鍐呮牳銆嶄箣闂达紝琛旀帴 #140/#138锛涘彛杩扮 2 浠?+ OCR 14 寮犲彇璇佸埌琛屽彿锛?*Kimi 瀹炰緥路鑰侀〗绔ュ凡瀹屾垚锛屾闃抽攱缁堝 A-** |

| 146 | `task_20260709_wangyuyan-personal-learning-method-agent` | 涓汉淇偧路瀛︿範鏂规硶鍩燂紙IPO + 绉戝鎻愰棶 + 鎬濈淮妯″瀷 + 鐭ヨ瘑钀冨彇锛夛細鎬绘鏋跺崱 + 4 瀛愭鏋跺崱 + orchestrator Agent Spec | reviewed | 鑰侀〗绔ワ紙hermes) | 7 鍗?+ 1 agent-spec | #142/#143/#144 reviewed | `70_product/tasks/task_20260709_wangyuyan-personal-learning-method-agent.md` | 鐜嬭瀚ｆ繁鎸栵細鏈€濂戝悎銆屾湁鍙ｈ堪绋夸絾 wiki 缂哄け銆嶏紱4 涓畬鏁村彛杩扮 + 5 OCR锛屽悇瀛愬煙浠?1-4 寮犻浂鏁ｅ崱銆佹棤鎬绘鏋讹紱鍚?IPO脳Y妯″瀷 杈圭晫锛?*Hermes 瀹炰緥路鑰侀〗绔ュ凡瀹屾垚锛屾闃抽攱缁堝 A-** |

| 147 | `task_20260709_wangyuyan-opportunity-foresight-agent` | 涓€鍫傛満浼氶鍒?/ 缁堝眬鍏夎氨鍩?P0-P2 琛ヤ骇锛氭€绘鏋跺崱 + 缁堝眬鍏夎氨鍥捐В璇?妗堜緥棰勫垽鏂规硶鍗?+ 鏁欑粌 Agent Spec | reviewed | 鑰侀〗绔ワ紙kimi) | 4 鏂板崱 + 1 agent-spec + 6-8 鍗囩骇 + OCR 鏍￠獙 | #141/#143/#144 reviewed | `70_product/tasks/task_20260709_wangyuyan-opportunity-foresight-agent.md` | 鐜嬭瀚ｆ繁鎸栵細绱犳潗鏈€涓板瘜锛? 鍙ｈ堪绋?+ 18 寮?OCR锛夛紱`yt-foresight` 宸叉垚浣撶郴锛屼絾缁堝眬鍏夎氨瑙ｈ/妗堜緥棰勫垽/鎬绘鏋舵壙閲嶅眰缂哄け锛涗笉鍏ㄩ噺琛ュ浘锛屽彧琛ヨВ璇?鏂规硶/鎬荤翰锛?*Kimi 瀹炰緥路鑰侀〗绔ュ凡瀹屾垚锛屾闃抽攱缁堝 A-** |

| 148 | `task_20260709_wangyuyan-expression-pitch-agent` | 涓汉淇偧路琛ㄨ揪鍔涗笌璁查鍗佹寚锛堝閲忥級P0-P2锛氭€绘鏋跺崱 + 鏁欑粌 Agent Spec + 鐏妯″瀷/鎵ц姝﹀櫒搴撳崱 + 鐜版湁鍗″崌绾?| reviewed | 鑰侀〗绔ワ紙hermes) | 5 鍗?+ 1 agent-spec + ~12 鍗囩骇 | #136/#143/#144 reviewed | `70_product/tasks/task_20260709_wangyuyan-expression-pitch-agent.md` | 鐜嬭瀚ｆ繁鎸栵細璁查鏈綋 5 鏈堝凡鏃╂湡鎸栬繃锛涘墠缃璁″彂鐜拌棣欏崄鎸囧彛杩扮増鍙悆鍙栥€屾湳銆嶆紡銆岄亾銆嶃€佺翰鍗℃潵婧愰敊浣嶃€佽〃杈惧姏鐏妯″瀷/姝﹀櫒搴?OCR 鏈崌姝ｅ紡鍗★紱涓嶉噸鍐?`yt-pitch-*`锛?*Hermes 瀹炰緥路鑰侀〗绔ュ凡瀹屾垚锛屾闃抽攱缁堝 A-** |

| 149 | `task_20260710_wangyuyan-business-formula-conversion-case-round` | 涓氬姟鍏紡 脳 杞寲鐜?妗堜緥杞紙杞婚噺锛夛細3 寮犺惤鍦?case + L5/L6 鍗犱綅鍥炲～锛堝皠绠/鑸炶箞/鏈嶈搴椾笁妗堜緥锛?| reviewed | 鑰侀〗绔?kimi-code) | 3 case + 1 concept 鍥炲～ | #145 reviewed | `70_product/tasks/task_20260710_wangyuyan-business-formula-conversion-case-round.md` | 鐢ㄦ埛鎻愪緵钀藉湴涔嬪绗叚鍦洪€愬瓧绋匡紱鍒ゆ柇鍏堝仛杞婚噺妗堜緥杞€佷笉绔嬪ぇ鍩燂紱pre-submit 4/4 PASS锛?*寰呮闃抽攱缁堝**锛汥 鍩燂紙杞寲鐜囬粦瀹級鏆備笉绔嬮」锛岀瓑绯荤粺璇惧埌浣嶅啀寮€ #150 |

| 150 | `task_20260711_wangyuyan-fundamentals-domain-production` | 鑻︾粌鍩烘湰鍔熷煙锛堢鐞?鍥㈤槦瀛愬煙锛塒0-P2锛氭€荤翰/鍥涘瓧璇€鎷嗗缓鎺ㄧ粌/涓夌幆鍏淮/40 宸ュ叿鍗¤惤鍦?+ 鏄ヨ悕妗堜緥 + 绠＄悊鍩?digest + 鏁欑粌 Agent Spec | reviewed | 鑰侀〗绔?kimi) | ~18 鍗?+ 1 agent-spec + 1 digest + 2 鍗囩骇 | #149 缁堝鍚?claim锛?143/#144 鍗忚 | `70_product/tasks/task_20260711_wangyuyan-fundamentals-domain-production.md` | 鐜嬭瀚ｇ紪鎺掞細4 鍙ｈ堪绋?76 鍥?OCR+VLM锛涘洓瀛楄瘈鍙栥€屾媶寤烘帹缁冦€嶃€佸崱鏁板彇瀹炵墿 6/7/7/20銆佹暟瀛楅檷绾э紱鍏堣ˉ management-domain-digest 璋冨拰鍐茬獊 |

| 151 | `task_20260711_wangyuyan-fundamentals-dual-triangle-factory-buildout` | 鍩烘湰鍔熋楀弻涓夎/cap_hub 宸ュ巶鏀归€狅紙寤哄伐鍘傜嚎锛夛細AI-鍩烘湰鍔熼《鐐规墿灞?+ cap_hub涓夌幆杩囨护鍣?+ 娈典綅鍚堝苟 + 椋炶疆琛ュ叏 | reviewed | 榛勮嵂甯?| 1 鏂板伐鍘傜粍浠跺崱 + 4 鏃㈡湁宸ュ巶鍗″崌绾?| #150 鍐呭鍗?reviewed锛堣剼鎵嬫灦鍙厛鎼紝濉厖绛?#150锛?| `70_product/tasks/task_20260711_wangyuyan-fundamentals-dual-triangle-factory-buildout.md` | 鐜嬭瀚ｅ叏灞€瑁佸畾锛氶粍鑽笀寤鸿涔︿綔璇夋眰閲囩撼銆佹暣浣撹縼绉绘柟妗堝惁鍐筹紱寤哄伐鍘?vs 浜у唴瀹瑰垎绾匡紱寮曠敤涓嶈縼绉伙紱鏈綋鐙珛+澶氬叆鍙ｇ储寮?|

| 152 | `task_20260711_wangyuyan-agent-fundamentals-cultivation` | 鍩烘湰鍔熷煙琛ュ崱锛歝oncept-涓€鍫?Agent鍩烘湰鍔熶慨鐐硷紙Agent 鍐涘洟缁冨熀鏈姛瑙嗚锛氫笁鐜瓫閫壝桲DO鎷嗗缓鎺ㄧ粌鏄犲皠 + 鑺辨€?鐜嬭瀚ｄ袱妗堜緥锛?| reviewed | 鑰侀〗绔?| 1 concept 鍗?+ #15鍗?related 鍙嶅悜 link | #150 reviewed锛堥渶 #15 鍗″瓨鍦ㄥ仛鍙屽悜 link锛?| `70_product/tasks/task_20260711_wangyuyan-agent-fundamentals-cultivation.md` | 鑰佹湵鎸囦护锛?150 宸?claimed-kimi 涓嶆敼鍔紝鍙︾珛鏈换鍔★紱KDO 宸ュ巶=agent 缁冨熀鏈姛绯荤粺锛涗笌 #151 B-1/B-2 浜掗摼 |

| 153 | `task_20260711_wangyuyan-decision-coach-agent-supplement` | 鍐崇瓥鍩熻ˉ浜э細绉戝鍐崇瓥鏁欑粌 agent-spec锛坥rchestrator锛屾寕涓夎褰?ABCD/ROI/娣卞害L1-L4/鍏辫瘑鏇茬嚎锛? 涓夎褰㈠崱鑴忔暟鎹竻鐞?| reviewed | 鑰侀〗绔?| 1 agent-spec + 1 鍗¤剰鏁版嵁娓呯悊 + digest 鍥為摼 | 鏃狅紙鍐崇瓥鍩熷崱宸?reviewed锛?| `70_product/tasks/task_20260711_wangyuyan-decision-coach-agent-supplement.md` | 鍐崇瓥鍩熸垚鐔熷害 A- 涓嶇珛澶т换鍔★紱鍞竴缂?agent-spec 鐨勫ぇ鍩燂紱棰嗗彇鑺傚鐢辫€佹湵瀹?|

| 154 | `task_20260712_wangyuyan-long-material-reading-protocol-dk` | dk 鍗★細闀跨礌鏉愬垎灞傝鍙栧崗璁紙瀵嗗害脳闀垮害閫夌瓥鐣?/ 瀛愪唬鐞嗗瀛?琛屽彿閿氱偣 / 涓夐亾闃茬嚎 + 鏆楃煡璇嗘崟鎹炴竻鍗曪級 | reviewed | 鑰侀〗绔?| 1 dk | 鏃?| `70_product/tasks/task_20260712_wangyuyan-long-material-reading-protocol-dk.md` | 鐜嬭瀚ｅ伐浣滃崗璁啗鍥㈠叡浜寲锛涙槑澶?C/D 鍩熺敓浜у嵆鐢紝寤鸿 hermes 绌烘。浼樺厛棰?|

| 155 | `task_20260712_wangyuyan-business-formula-domain-p0-skeleton` | C鍩熉蜂笟鍔″叕寮?P0 楠ㄦ灦娣卞寲锛氭€荤翰鍗囩骇 + 鍙傛暟鍐板北/閫昏緫鍏崇郴鍐板北/鍗佸ぇ鑼冨紡涓夊崱娣卞寲 + 钀藉湴绛栫暐闆?+ 鍙傛暟姝﹀櫒搴撳叏閲?+ digest + ABC鍗囩骇 | reviewed | 鑰侀〗绔?| 4 鍗囩骇 + 3 鏂板缓 + 1 digest | 鏃狅紙C鍩熺涓€娈碉紝闃诲#156-158锛?| `70_product/tasks/task_20260712_wangyuyan-business-formula-domain-p0-skeleton.md` | 鐜嬭瀚ｆ繁鎸栵細5鍙ｈ堪96涓囧瓧+5绗旇+101鍥綱LM鍏ㄩ噺澶勭悊锛涗袱浠藉畾浣嶇储寮曡惤鐩榑vlm_output锛涙棦鏈?5寮犲簳绋垮崱鍗囩骇涓嶅簾寮冿紱PEAHD/C=瀹忚鏁堢巼绛夊啿绐佸凡瑁佸畾锛涙暟瀛楅檷绾ц绋嬫渚嬪彛寰?|

| 156 | `task_20260712_wangyuyan-business-formula-domain-p1-workflow-tools` | C鍩熉蜂笟鍔″叕寮?P1 宸ヤ綔娴佷笌宸ュ叿鏃忥細涓夋宸ヤ綔娴?鏍煎紡瑙勮寖/闄嶉緳鍗佸叓鎺?PEAHD/鍋囪姹?鏀诲潥浼?鍙岀洰鏍?涓夌被鐩爣/鍏抽敭璺緞/鐩稿叧鈮犲洜鏋?鍥犳灉涓変欢濂?瀹氶噺涓夌淮搴?鍙傛暟鑰﹀悎/榄旀硶鏁板瓧/鑴辩鎴愭湰/閫掑綊鍙傛暟/榛戠洅鐧界洅/鍋囪椋炶疆/涓撳璁胯皥/鐏垫劅浜斿瓧璇€ | reviewed | 鑰侀〗绔?| ~20 鏂板缓鍗?| #155 reviewed锛堝彲涓?157骞惰锛?| `70_product/tasks/task_20260712_wangyuyan-business-formula-domain-p1-workflow-tools.md` | 鐜嬭瀚ｇ紪鎺掞細姒傚康鍗″鍙嶅父璇嗙偣锛堣劚绂绘垚鏈?瓒婂皬瓒婂叧閿?榛樿涓簡3-5鍊嶈浆鍖栫巼锛夛紝姣廲oncept鑷冲皯涓€涓弽甯歌瘑鏍囨敞锛?8鎷涢€愭嫑鏃犵己婕忓鐓у浘001759 |

| 157 | `task_20260712_wangyuyan-business-formula-domain-p2-cases` | C鍩熉蜂笟鍔″叕寮?P2 妗堜緥鏃忥細鏃楄埌8鍗★紙澶嶇洏钀ヤ簲骞?鎴戣瀹?椹媺鏉?浼氶攢鍗佸€?婕睍/鎵泲鏈?鍏礋璐ｄ汉/瑙嗛鍙凤級+ 瀛﹀憳7鍗?+ 鍚堥泦4鍗★紙浼洜鏋?榄旀硶鏁板瓧/鍒涙柊鍙傛暟/涓夎涓氾級 | reviewed | 鑰侀〗绔?| 19 妗堜緥鍗?| #155 reviewed锛堝彲涓?156骞惰锛?| `70_product/tasks/task_20260712_wangyuyan-business-formula-domain-p2-cases.md` | 鑰佹湵鍘熻瘽銆屼笉瑕侀仐婕忛噸瑕佺煡璇嗗拰妗堜緥銆嶏紱姣忓崱蹇呭惈澶辫触鍋囪锛涙壄铔嬫満浠樿垂鐜囦袱婧愬啿绐侀渶璋冨師鍥惧鏍告垨鏍噋ending_unknown |

| 158 | `task_20260712_wangyuyan-business-formula-domain-agent-spec` | C鍩熉蜂笟鍔″叕寮?agent-spec + 鍏ㄥ煙鏀跺彛锛歛gent-涓€鍫?涓氬姟鍏紡鏁欑粌锛坥rchestrator锛屽弻杞存浣嶈瘖鏂級+ digest鍥為摼 + 瀛ゅ効鍗?杈圭晫妫€鏌?| reviewed | 鑰侀〗绔?| 1 agent-spec + 鍥為摼 + 瀹屾垚鎶ュ憡 | #155/#156/#157 鍏ㄩ儴 reviewed | `70_product/tasks/task_20260712_wangyuyan-business-formula-domain-agent-spec.md` | 瑙勬牸瀵归綈#150鍩烘湰鍔熸暀缁?#153鍐崇瓥鏁欑粌锛涘弽鍚戣捀棣忥紙鑷湁涓氬姟鍏紡agent锛変笉鍦ㄦ湰浠诲姟锛屽彟绔嬬浜岄樁娈?|

| 159 | `task_20260712_wangyuyan-lint-baseline-rollback` | 鍥為摼鍊鸿涔夊垎娴?lint鍩虹嚎鍥炲嵎锛圱5瀹屾暣鏂规锛夛細闃舵0杈瑰垎绫绘爣鍑?gate)鈫掍緥澶栬惤琛?涓夐搧寰?鈫掔湡鍊哄垎鎵逛慨(鎶芥牱>90%鏀鹃噺)鈫掑熀绾块噸寤轰笁杩炲楠?| reviewed | 榛勮嵂甯?| 鏍囧噯鑽夋+渚嬪琛?manifest+澶嶉獙鎶ュ憡 | 鏃狅紙鍙嶅悜钂搁寮€浜у墠蹇呴』瀹屾垚锛涢樁娈?闇€娆ч槼閿嬪绛撅級 |

| 160 | `task_20260712_wangyuyan-y-model-fusion-backlink` | Y妯″瀷fusion鍗74琛鍩熸€荤翰閾撅紙T4锛夛細涓€琛宺elated杩藉姞+pre-submit锛岀敵鎶ュ埗 | reviewed | 鑰侀〗绔?| 琛ラ摼+闂ㄧ杈撳嚭 | 鏃狅紙椤烘墜浠朵笉鍗犵绾匡級 |

| 161 | `task_20260712_wangyuyan-c-domain-outbound-bridges` | C鍩熷煙澶栨ˉ鎺ュ寮猴細鍥捐氨瀛ょ珛淇锛堝煙澶栧嚭閾?0.3%鈫掆墺20%锛岄浂鍩熷閾惧崱鍑忓崐锛夛紝璇箟鐪熷疄浼樺厛涓嶈閫犻摼 | reviewed | 鑰侀〗绔?| related琛ラ摼+澶嶆祴鎶ュ憡 | 鏃狅紙P1涓嶉樆濉炲弽鍚戣捀棣忥級 |

| 162 | `task_20260712_wangyuyan-c-domain-backbone-direct-links` | C鍩熼骞茬洿杩烇紙娆ч槼閿嬪缓璁功浠诲姟A锛夛細6澶栭儴hub鈫擟鍩熸€荤翰鍙屽悜~12-18杈癸紝閫愯竟grep鍙ˉ缂烘柟鍚?| reviewed | 鑰侀〗绔?| 鍙屽悜杈?grep杈撳嚭 | #161浜ゅ嵎鍚庨锛堣竟娓呭崟鍘婚噸锛?|

| 163 | `task_20260712_wangyuyan-ocr-deadlink-cleanup` | ocr-*姝婚摼澶勭疆锛堜换鍔锛夛細澶勭疆娓呭崟宸茬杩囷紙6鏉′欢锛夛紝dry-run鈫抎iff鎶介獙鈮?0%鈫抋pply鈫掑閲忛浂鏂板 | reviewed | 榛勮嵂甯?| 澶嶆壂闆舵閾?manifest褰掓。 | **鏃跺簭鍗℃锛?159闃舵3鍩虹嚎閲嶅缓鍓嶅畬鎴愶紝鎴栧畬鎴愬悗绔嬪嵆閲嶅缓**锛圥2锛?|

| 164 | `task_20260712_wangyuyan-c-domain-cleanup` | C鍩熸敹灏炬竻鐞嗭細A娈礶xpert-interview鍙屽崱鍘婚噸锛堣€侀〗绔ワ級+B娈甸粍鑽笀4浠禿raft鈫抏nriched | reviewed | 鑰侀〗绔?榛勮嵂甯?| 鍙屽崱鍒嗗伐鏍囨敞+4浠秙tatus鍗囩骇 | 鏃狅紙P2浣撴閬楃暀锛?|

| 165 | `task_20260712_wangyuyan-c-domain-feedback-cards` | C鍩熷疄鎴樺弽鍝虹煡璇嗗崱6寮狅紙A缂哄け骞跺彂鐥?L1鍋囪閫夊潃鍏嶈垂/L5鎸栨硶涓夋柟鍚?楠屽洜鏋?閫昏緫L5L6姝ｅ悕/CD寰幆鎾ら攢閿?浼洜鏋滀袱浼锛?閫昏緫鍐板北鍗5/L6瀵归綈淇涓€澶?| reviewed | 鑰侀〗绔?| 6鏂板崱+1澶勪慨璁?闂ㄧ杈撳嚭 | 鏃狅紙P1锛屽彲涓?166骞惰锛涙彁妗堣60_feedback/analysis/c-domain-mastery-review-and-agent-design-2026-07-12.md 搂浜岋級 |

| 166 | `task_20260712_wangyuyan-business-formula-coach-iteration` | 涓氬姟鍏紡鏁欑粌agent杩唬鍏拤锛歅0娈典綅璇婃柇绮惧害锛圠5瀹氶噺/L6鍔ㄦ€佺閿欎綅锛?L5鎸栨帢鏈猴紙涓夋柟鍚?寮哄埗鍥犳灉妫€楠岋級+A鐩爣璇婃柇鍓嶇疆锛汸1 L1閫夊潃妫€鏌ュ櫒+CD寰幆涓诲姩鍙洖锛汸2鍏紡鐗堟湰鎰忚瘑 | reviewed | 鑰侀〗绔?| agent prompt杩唬鐗?閫愮偣钀藉疄鎶ュ憡 | 鏃狅紙P1锛屽彲涓?165骞惰锛?165鏂板崱鎸傝浇涓鸿蒋渚濊禆鍙暀TODO锛?|

| 167 | `task_20260712_wangyuyan-c-domain-audit-rework` | C鍩熻川閲忓璁¤繑宸ワ紙娆ч槼閿嬪璁÷у叚钀藉湴锛夛細P0 154鏉ource_refs姝绘枃浠朵慨澶?19鍗ection琛ラ綈+閼腐婀惧宀涘崱鏀筪omain绉诲嚭C鍩燂紙鐜嬭瀚ｅ凡瑁佸畾锛夛紱P1 Tool鍗ection+L1L6鑷鍗″叆index锛汸2 kdo姝婚摼娓呯悊 | reviewed | 鑰侀〗绔?| lint涓夊綊闆?瀛ゅ矝褰掗浂+index鍛戒腑 | **闃诲#159鍩虹嚎閲嶅缓**锛圥0瀹屾垚鍓嶄笉寰楅噸寤猴紝闃茬湡鍊哄啀琚熀绾垮惛鏀讹級锛涘彲涓?166骞惰 |

| 168 | `task_20260712_wangyuyan-graph-island-governance` | 鍥捐氨瀛ょ珛鍥㈡不鐞嗭細A娈甸粍鑽笀锛圤CR椋炲湴184鍗＄Щ鍑?0_raw[鍏堟柟妗堢瀹+ai-saas鍛藉悕涓夊彉浣撳悎骞?pending_unknown鍗犱綅199鏉″缃級锛汢娈佃€侀〗绔ワ紙浜旀娉曗啍涓氬姟鍏紡妗ユ帴[浜掗摼0鈫掆墺6锛屽崟鍏冩ā鍨嬫帴缂漖+AI绨囬骞插hub鍒嗘暎鐩磋繛+闇€姹傜皣閿氬畾浜旀娉曪級 | reviewed | 榛勮嵂甯?鑰侀〗绔?| 绛惧鏂规+dry-run+apply+澶嶆壂闂幆 / 鍙屽悜杈?閫愯竟璇箟鐞嗙敱 | A/B娈靛彲骞惰锛汢娈电瓑#167瀹屾垚鍚庨『棰嗭紱涓嶉€犻摼锛岃涔夌湡瀹炰紭鍏?|

| 169 | `task_20260712_wangyuyan-d-domain-p0-skeleton` | D鍩烶0楠ㄦ灦13鍗★紙v2鎸夎瘖鏂功搂9.3锛氭€荤翰/鐖北鍦板浘+涓夋璺ㄨ秺/涓冧慨鍏?涓夋洸绾?浣跨敤涓夊師鍒?36璁?瀵归綈鍘熷垯/12闃诲姏+搴曞眰涓夊弬鏁?闃诲姏鏂规硶璁洪鏋?12瑙︾偣+50瀛愬垎绫?瑙︾偣鏈川璁?鍏娉?鍙屾ā寮?鍏ぇ浼樺寲鍘熷垯/鍗佹寚妯″瀷/digest锛?| reviewed | 鑰侀〗绔?| 13鍗￠綈鍏?棰勬PASS+鎵獥=瀹炲姩 | #167/#168B reviewed鍚庨『棰嗭紱鏈浠ヨ瘖鏂功搂鍥?搂9.2瑁佸畾涓哄噯锛涘紩鐢ㄥ墠鏌ヂ?.1 ASR鍒悕娓呭崟 |

| 170 | `task_20260712_wangyuyan-d-domain-p1-tools` | D鍩烶1宸ュ叿鏃忕涓€鎵癸紙鍔ㄥ姏+闃诲姏渚?2鍗★細FAB+鏈川閲嶅畾涔?鍚嶅埄鏉冩儏/鍏師鍒?寮哄急瑙勫緥/蹇冪悊婵€鍔变紭鍏?12绛?闃诲姏鎸栨帢/涓夊彞璇濆績娉?椹瘏鍥涢儴鏇?浼忕瑪寮忔秷闄?涓嶇潃鎬ヤ袱绫?鍔ㄥ槾鍔ㄦ墜鍔ㄩ挶/涓冨ぇ鍦烘櫙锛?2鏃㈡湁鍗″崌绾?| reviewed | 鑰侀〗绔?| 14鍗?Tool鍥涜妭榻愬叏+棰勬PASS | #169 reviewed锛汿ool鍗″繀澶囧洓鑺傦紙#165鏁欒锛夛紱寮曠敤鍓嶆煡搂9.1 |

| 171 | `task_20260712_wangyuyan-d-domain-p2-cases-batch1` | D鍩熸渚嬫棌绗竴鎵?6鍗★紙v2.1锛氫笁澶ф棗鑸拌ˉ缁嗚妭+缁勫悎绡囦笁璐┛妗堜緥+鏅撹帀+璺嗘嫵閬撳洓鐗?鍏澂濂惰尪+瑙嗛鍙?4鈫?5%涓ょ嫭绔嬪崱+鍥涚瘒鍙ｈ堪妗堜緥搴撶储寮?涓€鍫傝嚜韬疄璺碉級 | reviewed | 鑰侀〗绔?| 16鍗?棰勬PASS+鎵獥=瀹炲姩 | #169 reviewed锛堝彲涓?170/#174骞惰锛夛紱妗堜緥涓夊眰澶勭疆鎸壜?.5 |

| 172 | `task_20260712_wangyuyan-d-domain-agent-and-closure` | D鍩焌gent-spec锛堜慨璁細瀵归綈寮曟搸鏈哄埗涓壜锋ā鍧楀埗锛岃瘽鏈寖鏈?YAI杞寲鐜囧疄褰昪ase鍗★細绮惧害浜旀。/鐩爣浠峰€奸噺鍖?閫愬彞闃诲姏鏄犲皠/娑堥櫎鏂瑰悜鍔ㄤ綔绀轰緥/鍑忔硶鎺掑簭/杈圭晫澹版槑锛?鍏ㄥ煙鏀跺彛锛坉igest鍥為摼/瀛ゅ効褰掗浂/index瀹屾暣/C鍩熶簰閾?lint鏃犳柊澧烇級 | reviewed | 鑰侀〗绔?| agent鍗″彲鐢?瀛ゅ効0+lint鏃犳柊澧?| #169-171 reviewed + #177 寮曟搸鍗忚鍗★紱缁撴瀯瀵归綈#166涓氬姟鍏紡鏁欑粌 |

| 173 | `task_20260712_wangyuyan-d-domain-p3-cases-batch2` | D鍩熸渚嬫棌绗簩鎵圭害8鍗★細瑙︾偣妗堜緥鍚堥泦3妗堜緥锛坢d閫愬瓧绋夸竴绛夌礌鏉愶細鍙舵枃褰皠绠?鏉庡垰榛勯噾涓夌増杩唬/鑼冩笣鐑樼剻锛?灏忕背鍙戝竷浼氭媶瑙?澶嶇洏鍚堥泦 | reviewed | 鑰侀〗绔?| 妗堜緥鏃忓畬鏁达紙10+8锛?| #172 reviewed锛?-13闃诲瑙ｉ櫎锛歮d閫愬瓧绋胯鐩栧叏閮ㄦ渚嬶紝鍥炴簮闄嶇骇鍙€?|

| 174 | `task_20260712_wangyuyan-d-domain-p1-tools-batch2` | D鍩烶1宸ュ叿鏃忕浜屾壒锛堣Е鐐?缁勫悎渚?3鍗★細鍥涘眰绾?浜旂淮/浜旂鎸?12鏄撴氮璐?鍑忔硶鎺掑簭/浜斿ぇ鑼冨紡/鍑嗗绯绘暟/鎻愬亣璁惧洓绛栫暐/鎺掑簭鍥涙嫑/ABACC/妗嗘灦搴?浠跨湡涓夎鐐?璁查鍙岀瓥鐣ワ級 | reviewed | 鑰侀〗绔?| 13鍗?Tool鍥涜妭榻愬叏+棰勬PASS | #169 reviewed锛堜笌#170骞跺垪鍙苟琛岋級锛泇2鏂板琛ヨ瘖鏂功閬楁紡 |

| 175 | `task_20260712_wangyuyan-c-domain-scan-fix-structure` | C鍩熸煡婕忎慨澶嶇涓€鎵癸紙缁撴瀯灞傦級锛?瀛ゅ効鍗℃帴鍏igest+digest褰掑睘淇+5瑁佸畾钀藉湴锛堥┈鎷夋澗鍙屽彛寰?浼洜鏋滄湳璇槧灏?鍥犳灉鍙ｅ緞澹版槑锛?鍘熷浘澶嶆牳3椤?6鑰佸崱鏁板瓧澶嶆牳+鍕樿琛ㄨˉ褰?Y妯″瀷琛ㄨ堪淇锛堣€佹湵瑁佸畾6锛歒=姣嶆ā鍨嬶紝ROI=鎺ㄥ浜х墿锛屽叏搴揜OI/Y鏂滄潬娓呴浂锛?| reviewed | 榛勮嵂甯?| 6鍗″彲杈?5瑁佸畾钀藉湴+3澶嶆牳鏈夌粨璁?| #168A瀹屾垚鍚庨『棰嗭紱渚濇嵁c-domain-scan-supplement璇婃柇涔︼紝瑁佸畾宸茶惤 |

| 183 | `task_20260713_wangyuyan-c-domain-evidence-recheck` | C鍩熻瘉鎹鏍告敹灏撅紙#175鎷嗗嚭锛?鍘熷浘澶嶆牳涓夋爮璇佹嵁[2瀛﹀垎/FB涓冨ぉ/鍐板北灞傛暟]+6鑰佸崱鏁板瓧澶嶆牳涓€绛夊帇浜岀瓑+鍗?绌簊ource_refs琛ラ綈锛?| reviewed | 鑰侀〗绔?| 涓夋爮璇佹嵁鍏ヨ瘖鏂功+6鍗″鏍?lint鏃犳柊澧?| 鏃狅紱鍏堜簬#169椤洪锛堝崐澶╅噺绾э級锛屽畬鎴愬悗#175鏁翠綋close |

| 184 | `task_20260713_wangyuyan-full-vault-yaml-audit` | 鍏ㄥ簱yaml.safe_load浣撴锛氳В鏋愬け璐?缁撴瀯寮傚父/鏃爁rontmatter涓夌被娓呭崟锛屼慨澶嶁憼鈶＄被锛岄殣韬崱褰掗浂 | reviewed | 榛勮嵂甯?| 鎵弿鎶ュ憡+淇+lint鏃犳柊澧?| 鏃狅紱#181鍚庨『棰?|

| 185 | `task_20260713_wangyuyan-template-placeholder-hygiene` | 妯℃澘鍗犱綅绗﹀崼鐢燂細xxx/.../wikilink绛墌130鏉＄ず渚媤ikilink鏀逛唬鐮佸潡鍖呰９锛屽浘璋辩伆鐧界偣褰掗浂锛涘巻鍙叉枃妗ｇ湡瀹炲紩鐢ㄤ笉鍔?| reviewed | 榛勮嵂甯?| 鍗犱綅绗﹀綊闆?妯℃澘鎶芥煡+lint鏃犳柊澧?| 鏃狅紱#184鍚庨『棰?|

| 186 | `task_20260713_wangyuyan-agent-spec-prompts-ingestion` | agent-spec鍗″叆鐭ヨ瘑灞傦細20寮?prompts 鍗″叆 30_wiki/tools锛堥攢鍞煙6寮犳寜#182鏄犲皠琛ㄥ姞D鍩熷洖閾?kernel绯诲垪7寮?浜у搧椤圭洰绠＄悊7寮犳寜鎵€灞炲煙鎺ワ級 | reviewed | 鑰侀〗绔?| 20姝ｅ紡鍗?lint鏃犳柊澧?| #182 reviewed鍚庨『棰?|

| 187 | `task_20260714_wangyuyan-material-gaps-tracking` | 绱犳潗缂哄彛杩借釜涓庡洖婧愮櫥璁帮紙4绫荤己鍙ｏ細澶嶇洏鍚堥泦7妗堜緥/寰佹枃鍗佺瘒+閭辨芳妗堜緥闆?鍙屼笁瑙?鍒绘剰缁冧範锛沚locked绛夎€佹湵锛?| suspended | 鑰侀〗绔?| 缂哄彛鐧昏鍗?绱犳潗鍒颁綅鍚?4h鍐呰瘎浼板叆闃?| 鑰佹湵鎻愪緵绱犳潗 |

| 188 | `task_20260714_wangyuyan-badcase-feedback-loop` | bad case反馈机制与首条记录：模板+存储路径+缺陷分类+闭环流程；首条等老朱真实使用 | reviewed | 鑰侀〗绔?| 鏈哄埗鍗?寮?棣栨潯璁板綍+context琛ヤ竵 | 鏃?|

| 176 | `task_20260712_wangyuyan-c-domain-scan-fix-assets` | C鍩熸煡婕忎慨澶嶇浜屾壒锛堣祫浜у眰锛夛細8鐙珛妗堜緥鍗★紙姹夊牎搴?缇庡洟灏忕孩鐐?鑺墖寮€鍙戞澘/鍑忔硶涓変緥/鍏紬鍙峰崟鏈堜环鍊?鍐滄満鎾悎/鍦ㄧ嚎鏁欒偛/濂宠搴椾笁鐗堬級+5鏂癲k/tool鍗★紙鍒嗗瀷閫掑綊/璺崇骇璧锋墜/杈归檯ROI/浜旀潯鏇夸唬璺緞/涓嶅彲缁熻蹇呭啓锛?鏃㈡湁鍗¤ˉ鑺傜害15椤?鍚堥泦閫熷啓琛ュ叏 | reviewed | 鑰侀〗绔?| 13鍗?琛ヨ妭鍏ㄨ惤鍦?棰勬PASS | #175 reviewed+D鍩?169鍚庨『棰嗭紙C鍩熶慨澶嶄紭鍏圖鍩烶1锛?|

| 177 | `task_20260713_wangyuyan-coach-dialogue-engine-protocol` | 鏁欑粌瀵硅瘽寮曟搸鍗忚鍗★紙鍏变韩浠?2鏉?鎺у埗鏈哄埗涓夐€変竴+韬唤杞碩CPR[鐞嗚搴曞骇=涓€鍫俆CPR鐨囧啝妯″瀷鍘熺敓锛孻AI鍥涘垎绫?鍏朵骇鍝佸寲]+闄勫姞浜у嚭TCPR妯″瀷姝ｅ紡鍗★級+YAI瀹炲綍妗堜緥鍗∶? | reviewed | 榛勮嵂甯?| 3鍗★紙鍗忚鍗?TCPR鍗?鍙屽疄褰曪級 | 鏃狅紙#168A/#175鍚庨『棰嗭級锛涢』鏃╀簬鑰侀〗绔?172/#179/#180 |

| 178 | `task_20260713_wangyuyan-decision-coach-engine-upgrade` | B鍩?153绉戝鍐崇瓥鏁欑粌spec鍗囩骇锛氬伐鍏锋竻鍗曗啋瀵硅瘽寮曟搸锛堝紩鐢ㄥ紩鎿庡崱+鐩插尯搴撹仛鍚?涓塸attern娉ㄥ叆+鍩熼棿杞粙锛夛紝鎸夐粍鑽笀寤鸿涔﹁惤鍦?| reviewed | 榛勮嵂甯?| spec鍙窇瀹孧0-M8+棰勬PASS | #177 reviewed |

| 179 | `task_20260713_wangyuyan-c-domain-coach-engine-align` | C鍩熶笟鍔″叕寮忔暀缁冧簩娆¤凯浠ｏ紙淇锛氬榻愬紩鎿庢満鍒朵簩路S0-S8闃舵鍒惰€岄潪M0-M8锛氭瘡杞笁鏍囨敞R?/S?/鏈疆鍙В鍐?鍏紡鏍戠増鏈凯浠0.x+涓嶄笅缁撹鏄庣ず锛?C鍩熷洓浠跺+#166鍏拤鍥炲綊涓嶇牬鍧?| reviewed | 鑰侀〗绔?| 寮曟搸寮曠敤+鍥涗欢濂?鍏拤鍥炲綊 | #177+#176 reviewed鍚庨『棰嗭紙杞婚噺锛?|

| 180 | `task_20260713_wangyuyan-five-step-coach-agent` | A鍩熶簲姝ユ硶鏁欑粌agent-spec鏂板缓锛坥rchestrator锛氫簲姝ユ浣嶈瘖鏂?鍋囪杞扮偢+浜旀娉曠洸鍖哄簱鍥炴寚鍩熷崱+Y妯″瀷姣嶆ā鍨嬫寕杞?鐢熸涓嶇鏁堢巼杈圭晫/鍥涘煙杞粙锛?| reviewed | 鑰侀〗绔?| 鍥涘煙鏁欑粌榻愬+杞粙涓や袱瀵归綈 | #177 reviewed+#179鍚庨『棰嗭紙闃熷垪灏鹃儴锛?|

| 181 | `task_20260713_wangyuyan-opc-sales-assistant-engine-adapt` | OPC閿€鍞璇濆姪鎵嬪紩鎿庨€傞厤锛堝弬璋嬪瀷瑁佸壀鐗堬級锛氫笁浠跺娉ㄥ叆=12闃诲姏鐩插尯杩囩瓫+纭害鏉熸樉寮忓鍛?娣卞害鍒嗙骇锛涘姞鎸侱鍩熷崱锛涗笉鎼琈0-M8涓嶆敼鍥涙缁撴瀯 | reviewed | 榛勮嵂甯?| 閫傞厤spec+瀹炴祴鏍蜂緥+棰勬PASS | #177+#169 reviewed鍚庨『棰嗭紱鐜嬭瀚ｈ瀹氾細鍙傝皨鍨嬩笉鍏ㄦ惉鏁欑粌鍨嬮噷绋嬬 |

| 182 | `task_20260713_wangyuyan-opc-sales-d-domain-linking` | OPC閿€鍞煙脳D鍩熷洖閾撅紙33鍗¤ˉ鏂规硶璁哄簳搴у紩鐢細寮€鍦虹櫧鈫掑崄鎸囨ā鍨?寮傝鈫掗樆鍔涙柟娉曡/閿€鍐犳浣嶁啋涓夋洸绾垮垎鏁扮嚎锛涙槧灏勮〃鍏堣鐜嬭瀚ｈ繃鐩悗鎵归噺锛?| reviewed | 鑰侀〗绔?| 33鍗″洖閾?lint鏃犳柊澧?| #169-171+#174 reviewed+#177锛堟槧灏勮〃鍙厛鍔級 |

| 189 | `task_20260719_wangyuyan-profit-pricing-domain` | 鍒╂鼎涓虹帇鍩熷崱鐗囧寲锛氬埄娑︿紭鍏堢粡钀ユ鏋朵笌瀹氫环鏂规硶璁?| reviewed | - | 8寮爓iki鍗?鍙€塧gent-spec | 鏃狅紱鏂板煙寮€鑽掞紝鏉ユ簮璧皵鏇悸疯タ钂欍€婄湡姝ｇ殑鍒╂鼎銆?姘存按鎷嗕功/缁忚惀璇?|

| 190 | `task_20260719_laowantong-zhu-ai-capability-roadmap` | 老朱 AI 能力建设刻意练习路线图（tool + agent-spec） | reviewed | 老顽童(kimi) | 2 张卡 | 无 | `70_product/tasks/task_20260719_laowantong-zhu-ai-capability-roadmap.md` | 基于 personal-os 已确认的「鑫港湾打工+借假修真+学习AI」策略，输出可执行路线图与个人 AI 教练智能体规格 |

| 192 | `task_20260719_laowantong-fix-touchpoint-case-library-191` | 触点篇案例库返工：跨案例规律溯源/补 related 回链/新增规律节 | pending_review | 老顽童 | 1 张 case 卡修复 | #191 欧阳锋终审 B+ 有条件通过 | `task_20260719_laowantong-fix-touchpoint-case-library-191.md` | 修复后直接 pass，不需再审 |

| 193 | `task_20260719_wangyuyan-target-goal-zhouzijing` | 目标管理域补充——周子敬《目标管理的底层逻辑与实践》卡片化 | queued | - | 7张新卡+5项已有卡补充 | 无 | `60_feedback/tasks/task_20260719_wangyuyan-target-goal-zhouzijing.md` | 非一堂体系，独立方法论补管理域L4管业务；周子敬=以太资本CEO/字节美团天使投资人 |

| 194 | `task_20260719_wangyuyan-advanced-modeling-course2` | 高阶建模第二课——流程建模实践：18组件·四步法·三案例 | queued | - | 7新卡+2dk+1bridge+8已有卡补充回链 | 无 | `60_feedback/tasks/task_20260719_wangyuyan-advanced-modeling-course2.md` | 高阶建模域实践层补充（第一课=理论·已入库）；Truman口述4097行+57张VLM |








