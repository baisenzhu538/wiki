'''
Time Capsule - KDO Agent Memory Database
Lightweight SQLite store for agent contexts, memories, sessions, and shared state.
Usage: python time_capsule.py <command> [args...]
'''
import sqlite3, json, os, sys
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'time-capsule.db')

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('PRAGMA foreign_keys=ON')
    return db

def init_db():
    db = get_db()
    db.executescript('''
    CREATE TABLE IF NOT EXISTS agents (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        role_name TEXT NOT NULL,
        role_type TEXT,
        interface TEXT,
        status TEXT DEFAULT 'active',
        created_at TEXT,
        updated_at TEXT
    );
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL REFERENCES agents(id),
        key TEXT NOT NULL,
        value TEXT NOT NULL,
        category TEXT,
        created_at TEXT DEFAULT (datetime('now','localtime')),
        UNIQUE(agent_id, key)
    );
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL REFERENCES agents(id),
        started_at TEXT DEFAULT (datetime('now','localtime')),
        ended_at TEXT,
        summary TEXT,
        notes TEXT
    );
    CREATE TABLE IF NOT EXISTS shared_state (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL,
        updated_by TEXT,
        updated_at TEXT DEFAULT (datetime('now','localtime'))
    );
    CREATE TABLE IF NOT EXISTS behavior_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL REFERENCES agents(id),
        card_id TEXT NOT NULL,
        trigger_phrase TEXT,
        action TEXT,
        UNIQUE(agent_id, card_id)
    );
    ''')
    db.commit()
    db.close()

def seed():
    db = get_db()
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    agents = [
        ('laowantong', '老顽童', 'Producer', 'producer', 'claude/hermes',
         'KDO知识工厂产能主力。按队列领任务->读素材->生产卡片->pre-submit->提交review。'),
        ('wangyuyan', '王语嫣', 'Consultant + Orchestrator', 'consultant', 'kimi/feishu',
         '诊断咨询者+任务编排者+入口把关人。不碰wiki只写feedback。'),
        ('ouyangfeng', '欧阳锋', 'Architect + Reviewer', 'architect', 'claude',
         '架构者与唯一协调节点。审查全部产出、任务分配、架构决策。'),
        ('huangyaoshi', '黄药师', 'Builder + Deployer', 'builder', 'claude/codex',
         'KDO CLI/基础设施/质量门/agent三件套部署。单一实例。'),
        ('duanwangye', '段王爷', 'Publisher', 'publisher', 'hermes/feishu',
         '发布与反馈负责人。kdo ship->渠道分发、反馈收集、版本发布。'),
        ('hongqigong', '洪七公', 'Multimodal', 'multimodal', 'hermes/feishu',
         '多模态知识仲裁者。知识->视觉资产、OCR->结构化、图片->prompt。'),
        ('beikai', '北丐', 'Unconfirmed', 'unknown', 'hermes', '待确认角色。'),
        ('basic-skills-coach', 'AI基本功教练', 'Assistant (Feishu)', 'assistant', 'feishu',
         '帮助用户用Feature思维解决AI问题。'),
        ('coaching-leadership-assistant', '教练式领导力助理', 'Assistant (Feishu)', 'assistant', 'feishu',
         '管人：一对一倾听/提问/反馈/成长。TCPR=T/C/P/R，默认C。'),
        ('meeting-assistant', '科学开会助理', 'Assistant (Feishu)', 'assistant', 'feishu',
         '管一群人：该不该开会/怎么设计会议。冰山画布+十大原则。'),
    ]
    
    for (aid, name, role_name, role_type, interface, desc) in agents:
        db.execute('INSERT OR REPLACE INTO agents (id, name, role_name, role_type, interface, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (aid, name, role_name, role_type, interface, now, now))
        db.execute('INSERT OR REPLACE INTO memories (agent_id, key, value, category) VALUES (?, ?, ?, ?)',
                   (aid, 'identity', desc, 'identity'))
    
    cards = [
        ('laowantong', 'L1', '先出牌再动手', '开始写卡'),
        ('laowantong', 'L2', '先消费全量素材再写卡', '图片不重要'),
        ('laowantong', 'L3', '先深挖达标再提交', '差不多了'),
        ('laowantong', 'L4', '先pre-submit再交卷', '写完了'),
        ('laowantong', 'L5', '先跑脚本确认再声称完成', '这批完成了'),
        ('laowantong', 'L6', '先WebSearch再命名', '叫它XX吧'),
        ('laowantong', 'L7', '先查已有卡再新建', '建张新卡'),
        ('laowantong', 'L8', '子卡先写定位再写内容', '这是某框架的子卡'),
        ('wangyuyan', 'W1', '先口述稿再笔记', '笔记够了'),
        ('wangyuyan', 'W2', '先扫信号词再读内容', '口述稿太长'),
        ('wangyuyan', 'W3', '先还原过程再标注类型', '标case'),
        ('wangyuyan', 'W4', '先规划解压路径再建任务单', '建任务单'),
        ('wangyuyan', 'W5', '先查全量素材覆盖率再交付', '诊断完了'),
        ('wangyuyan', 'W6', '先跑三方法再建任务', '排任务'),
        ('wangyuyan', 'W7', '先确认frontmatter再入队', '入队'),
        ('wangyuyan', 'W8', '先找MOC再回答', 'XX是第几步'),
    ]
    for aid, cid, action, trigger in cards:
        db.execute('INSERT OR REPLACE INTO behavior_cards (agent_id, card_id, trigger_phrase, action) VALUES (?, ?, ?, ?)',
                   (aid, cid, trigger, action))
    
    shared = [
        ('active_sprint', 'Agent部署冲刺(2026-08-09~)'),
        ('queue_file', '70_product/tasks/production-queue.md'),
        ('wiki_root', '/mnt/c/Users/Administrator/Desktop/wiki'),
        ('total_cards', '2500+'),
        ('hermes_version', 'v0.20.0'),
        ('model_default', 'deepseek-v4-flash'),
    ]
    for key, value in shared:
        db.execute('INSERT OR REPLACE INTO shared_state (key, value, updated_by) VALUES (?, ?, ?)',
                   (key, value, 'huangyaoshi'))
    
    db.commit()
    db.close()
    print(f'Seeded {len(agents)} agents, {len(cards)} cards, {len(shared)} shared states.')

def cmd_list():
    db = get_db()
    for row in db.execute('SELECT id, name, role_name, status FROM agents ORDER BY role_type, name'):
        print(f'  {row["id"]:<35} {row["name"]:<12} {row["role_name"]:<30} [{row["status"]}]')
    db.close()

def cmd_show(agent_id):
    db = get_db()
    agent = db.execute('SELECT * FROM agents WHERE id=?', (agent_id,)).fetchone()
    if not agent:
        print(f'Agent "{agent_id}" not found.'); db.close(); return
    print(f'=== {agent["name"]} ({agent["role_name"]}) ===')
    print(f'  Type: {agent["role_type"]}  Interface: {agent["interface"]}  Status: {agent["status"]}')
    print('--- Memories ---')
    for m in db.execute('SELECT key, value, category FROM memories WHERE agent_id=? ORDER BY category, key', (agent_id,)):
        print(f'  [{m["category"]}] {m["key"]}: {m["value"][:120]}')
    print('--- Behavior Cards ---')
    for c in db.execute('SELECT card_id, action, trigger_phrase FROM behavior_cards WHERE agent_id=? ORDER BY card_id', (agent_id,)):
        print(f'  {c["card_id"]}: {c["action"]} (trigger: {c["trigger_phrase"]})')
    db.close()

def cmd_set(agent_id, key, value, category='context'):
    db = get_db()
    db.execute('INSERT OR REPLACE INTO memories (agent_id, key, value, category) VALUES (?, ?, ?, ?)',
               (agent_id, key, value, category))
    db.commit(); db.close()
    print(f'Set [{category}] {key} for {agent_id}')

def cmd_recover(agent_id):
    db = get_db()
    agent = db.execute('SELECT * FROM agents WHERE id=?', (agent_id,)).fetchone()
    if not agent: print(f'Not found: {agent_id}'); db.close(); return
    identity = db.execute('SELECT value FROM memories WHERE agent_id=? AND key="identity"', (agent_id,)).fetchone()
    cards = db.execute('SELECT * FROM behavior_cards WHERE agent_id=? ORDER BY card_id', (agent_id,)).fetchall()
    shared = db.execute('SELECT * FROM shared_state').fetchall()
    
    print(f'# {agent["name"]} Amnesia Recovery')
    print(f'你是 **{agent["name"]}（{agent["role_name"]}）**。')
    if identity: print(identity['value'])
    if cards:
        print('## Behavior Cards')
        for c in cards: print(f'- **{c["card_id"]}**: {c["action"]} (trigger: {c["trigger_phrase"]})')
    print('## Shared State')
    for s in shared: print(f'- {s["key"]}: {s["value"]}')
    print(f'## Startup: 1) .agent/context.md  2) production-queue.md  3) .agent/{agent_id}-context.md')
    db.close()

def cmd_shared():
    db = get_db()
    for row in db.execute('SELECT * FROM shared_state ORDER BY key'):
        print(f'  {row["key"]:<30} {row["value"]:<60}')
    db.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Time Capsule - KDO Agent Memory')
        print('  init                  Create database')
        print('  seed                  Seed with agent data')
        print('  list                  List all agents')
        print('  show <id>             Show agent details')
        print('  set <id> <key> <val>  Set memory for agent')
        print('  recover <id>          Print recovery prompt')
        print('  shared                Show shared state')
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd == 'init': init_db(); print('OK')
    elif cmd == 'seed': init_db(); seed()
    elif cmd == 'list': cmd_list()
    elif cmd == 'show' and len(sys.argv) > 2: cmd_show(sys.argv[2])
    elif cmd == 'set' and len(sys.argv) > 4: cmd_set(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else 'context')
    elif cmd == 'recover' and len(sys.argv) > 2: cmd_recover(sys.argv[2])
    elif cmd == 'shared': cmd_shared()
    else: print(f'Unknown: {cmd}')
