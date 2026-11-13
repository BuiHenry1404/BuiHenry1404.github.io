#!/usr/bin/env python3
"""Generate the bilingual static portfolio. Output is plain HTML — no runtime build step."""
import pathlib, json, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://buihenry1404.github.io'
SLUGS = ['mainframe-agent', 'sdlc-platform', 'ecommerce-analytics', 'salona']

NAV = {
 'en': dict(work='Experience', skills='Skills', contact='Contact', back='← All projects'),
 'vi': dict(work='Kinh nghiệm', skills='Kỹ năng', contact='Liên hệ', back='← Tất cả dự án'),
}


def shell(*, lang, depth, lang_home, title, desc, body, self_path, alt_path, alt_rel):
    up = '../' * depth
    n = NAV[lang]
    home = lang_home
    other = 'vi' if lang == 'en' else 'en'
    self_abs = (SITE + '/' + self_path).rstrip('/')
    alt_abs = (SITE + '/' + alt_path).rstrip('/')
    if lang == 'en':
        sw = (f'<a href="{home}" hreflang="en" aria-current="true">EN</a>'
              f'<a href="{alt_rel}" hreflang="vi">VI</a>')
    else:
        sw = (f'<a href="{alt_rel}" hreflang="en">EN</a>'
              f'<a href="{home}" hreflang="vi" aria-current="true">VI</a>')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{self_abs}">
<meta property="og:image" content="{SITE}/assets/henry.jpg">
<link rel="canonical" href="{self_abs}">
<link rel="alternate" hreflang="{lang}" href="{self_abs}">
<link rel="alternate" hreflang="{other}" href="{alt_abs}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%230B1120'/><text x='50' y='72' font-size='64' font-family='monospace' font-weight='bold' fill='%2322C55E' text-anchor='middle'>H</text></svg>">
<link rel="stylesheet" href="{up}assets/style.css">
<noscript><style>.reveal{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
<body>

<nav class="nav">
  <div class="wrap nav__inner">
    <a class="nav__home" href="{home}">~/buihenry</a>
    <div class="nav__links">
      <a href="{home}#work">{n['work']}</a>
      <a href="{home}#skills">{n['skills']}</a>
      <a href="{home}#contact">{n['contact']}</a>
      <span class="lang">{sw}</span>
    </div>
  </div>
</nav>

{body}

<footer>
  <div class="wrap">
    <span>© 2026 Bùi Henry</span>
    <span><a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=buihenry1404@gmail.com&amp;su=Opportunity%20for%20B%C3%B9i%20Henry" target="_blank" rel="noopener">buihenry1404@gmail.com</a></span>
  </div>
</footer>

<script>
(function () {{
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal');
  if (!rm && 'IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function (es) {{
      es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
    }}, {{ rootMargin: '0px 0px -10% 0px' }});
    els.forEach(function (el) {{ io.observe(el); }});
  }} else {{
    els.forEach(function (el) {{ el.classList.add('in'); }});
  }}

}})();
</script>
</body>
</html>
'''




# ---------------------------------------------------------------- index content
IDX = {
 'en': dict(
   title='Bùi Henry — AI Engineer',
   desc='AI Engineer building LLM agents for real software-development problems: multi-agent orchestration, MCP tools, retrieval, human-in-the-loop and guardrails. Python, LangChain, LangGraph.',
   role='AI ENGINEER',
   lede='I build AI agents that help software teams: reading large legacy codebases, writing project documents, and taking tasks straight from Azure DevOps. I focus on agents that give correct answers, ask before they act, and that teams keep using.',
   cta1='See the work', cta2='Get in touch',
   stats=[('50→20%', 'unsupported answers on a COBOL maintenance agent'),
          ('60→90%', 'retrieval recall on bug-fix queries for coding agents'),
          ('80–90%', 'docs usable without multiple review rounds, 9-step workflow'),
          ('4', 'projects that reached production faster with the SDLC agents')],
   work_h='Work experience',
   work_s='Three projects at FPT Software: what I built and what it improved.',
   personal_h='Personal projects',
   personal_s='Built from start to finish, outside work.',
   skills_h='Skills', skills_s='What I use most, roughly in order.',
   contact_h='Get in touch', contact_s='Open to AI Engineer roles in Ho Chi Minh City or remote.',
   skills=[('AI agents', 'LangChain, LangGraph, Microsoft AutoGen · multi-agent orchestration · tool calling · MCP (Model Context Protocol) · human-in-the-loop · guardrails · agent memory · context engineering · structured output · model routing'),
           ('Retrieval &amp; eval', 'knowledge graph · embedding search · pgvector · Neo4j · RAG · LLM evaluation · Langfuse (observability) · token / cost profiling · Azure OpenAI'),
           ('Backend', 'Python (main), Java · FastAPI · REST APIs · Socket.IO · JWT · Spring Boot · PostgreSQL / Supabase · MongoDB · Redis · MySQL · Docker'),
           ('Parsing / tooling', 'ANTLR4 (grammars, AST) · Tree-sitter · Azure DevOps REST API · Git · pytest · Claude Code, GitHub Copilot, Codex · reading-level COBOL / JCL / CopyBook — enough to write parsers for them, not to write production programs in them')],
   work_cards=[('sdlc-platform', 'FPT Software · Apr 2026 – present', 'AgentBox: AI agents for the SDLC',
           'Six AI agents and a 9-step workflow that turn a product idea into requirements, design and a mockup. Developers use them directly from Azure DevOps.',
           '~90% of docs need one review →'),
          ('ecommerce-analytics', 'FPT Software · Jun – Sep 2026', 'Multi-agent analytics for an e-commerce business',
           'An orchestrator plans each report and four agents (Retrieval, Analysis, Validation, Report) fetch, analyse, check and present the numbers as charts and slides. In daily use at the client.',
           'reporting 3 days → 1 day →'),
          ('mainframe-agent', 'FPT Software · Nov 2025 – Apr 2026', 'xMainframe: multi-agent mainframe reverse engineering',
           'ANTLR4 parsers and an AST feed a coordinator and two agents that explain COBOL at function, file and project level, backed by a Neo4j knowledge graph and MCP tools.',
           'hallucinations ~50% → ~20% →')],
   personal_cards=[('salona', 'Personal · Aug 2026 – present', 'Salona: AI booking assistant',
           'One orchestrator and three sub-agents on LangChain + LangGraph. The AI only proposes a booking, the customer approves, and code saves it. Every reply is checked in code.',
           'AI proposes, customer approves →'),
          ('https://github.com/BuiHenry1404/ai-agent-study-planning', 'Personal · Jul – Aug 2025', 'AI Study Planner',
           'Several AutoGen agents work together to turn a study goal into a schedule on Google Calendar. Conversations resume where they left off, and replies stream in real time.',
           'Source on GitHub ↗')],
 ),
 'vi': dict(
   title='Bùi Henry — AI Engineer',
   desc='AI Engineer xây dựng LLM agent cho bài toán thực tế trong phát triển phần mềm: điều phối đa agent, MCP tool, retrieval, human-in-the-loop và guardrail. Python, LangChain, LangGraph.',
   role='AI ENGINEER',
   lede='Tôi xây AI agent hỗ trợ đội phát triển phần mềm: đọc hiểu codebase cũ hàng triệu dòng, soạn tài liệu dự án, và nhận việc trực tiếp trên Azure DevOps. Tôi chú trọng agent trả lời đúng, hỏi trước khi làm, và được đội dùng lâu dài.',
   cta1='Xem dự án', cta2='Liên hệ',
   stats=[('50→20%', 'câu trả lời thiếu căn cứ của agent hỗ trợ COBOL'),
          ('60→90%', 'recall truy xuất cho truy vấn bug fix của coding agent'),
          ('80–90%', 'tài liệu dùng được, không cần nhiều vòng review, workflow 9 bước'),
          ('4', 'dự án ra production nhanh hơn nhờ các agent SDLC')],
   work_h='Kinh nghiệm làm việc',
   work_s='Ba dự án tại FPT Software: tôi đã làm gì và kết quả ra sao.',
   personal_h='Dự án cá nhân',
   personal_s='Tự làm từ đầu tới cuối, ngoài giờ làm việc.',
   skills_h='Kỹ năng', skills_s='Những công nghệ tôi dùng nhiều nhất, xếp gần theo thứ tự.',
   contact_h='Liên hệ', contact_s='Đang tìm vị trí AI Engineer tại TP.HCM hoặc remote.',
   skills=[('AI agent', 'LangChain, LangGraph, Microsoft AutoGen · điều phối đa agent · tool calling · MCP (Model Context Protocol) · human-in-the-loop · guardrail · bộ nhớ agent · context engineering · structured output · model routing'),
           ('Retrieval &amp; eval', 'knowledge graph · embedding search · pgvector · Neo4j · RAG · đánh giá LLM · Langfuse (observability) · đo token / chi phí · Azure OpenAI'),
           ('Backend', 'Python (chính), Java · FastAPI · REST API · Socket.IO · JWT · Spring Boot · PostgreSQL / Supabase · MongoDB · Redis · MySQL · Docker'),
           ('Parsing / công cụ', 'ANTLR4 (grammar, AST) · Tree-sitter · Azure DevOps REST API · Git · pytest · Claude Code, GitHub Copilot, Codex · COBOL / JCL / CopyBook ở mức đọc hiểu — đủ để viết parser cho chúng, không phải để viết chương trình production')],
   work_cards=[('sdlc-platform', 'FPT Software · 04/2026 – nay', 'AgentBox: AI agent cho quy trình phát triển',
           'Sáu AI agent và quy trình 9 bước biến ý tưởng sản phẩm thành yêu cầu, thiết kế và mockup. Developer dùng chúng ngay trên Azure DevOps.',
           '~90% tài liệu chỉ cần 1 lần review →'),
          ('ecommerce-analytics', 'FPT Software · 06 – 09/2026', 'Hệ multi-agent phân tích số liệu cho doanh nghiệp TMĐT',
           'Orchestrator lập kế hoạch cho mỗi báo cáo, bốn agent (Retrieval, Analysis, Validation, Report) lấy số, phân tích, kiểm tra rồi dựng biểu đồ và slide. Khách dùng hằng ngày.',
           'làm báo cáo 3 ngày → 1 ngày →'),
          ('mainframe-agent', 'FPT Software · 11/2025 – 04/2026', 'xMainframe: hệ multi-agent reverse engineering mainframe',
           'Parser ANTLR4 và AST cung cấp dữ liệu cho một Coordinator và hai agent giải thích COBOL theo 3 cấp function, file, project, dựa trên knowledge graph Neo4j và MCP tool.',
           'hallucination ~50% → ~20% →')],
   personal_cards=[('salona', 'Cá nhân · 08/2026 – nay', 'Salona: trợ lý AI đặt lịch',
           'Một agent điều phối và ba agent con trên LangChain + LangGraph. AI chỉ đề xuất lịch, khách duyệt, code mới lưu. Mọi câu trả lời đều được code kiểm tra.',
           'AI đề xuất, khách duyệt →'),
          ('https://github.com/BuiHenry1404/ai-agent-study-planning', 'Cá nhân · 07 – 08/2025', 'AI Study Planner',
           'Nhiều agent AutoGen phối hợp để biến mục tiêu học tập thành lịch học trên Google Calendar. Hội thoại tiếp tục đúng chỗ đang dở, câu trả lời hiện ra theo thời gian thực.',
           'Mã nguồn trên GitHub ↗')],
 ),
}


def build_index(lang):
    d = IDX[lang]
    base = '' if lang == 'en' else 'vi/'
    stats = '\n'.join(
        f'''    <div class="stat">
      <div class="stat__n">{n}</div>
      <div class="stat__l">{l}</div>
    </div>''' for n, l in d['stats'])
    def cards_for(items):
        return '\n\n'.join(
            f'''      <a class="card reveal" {('href="' + slug + '" target="_blank" rel="noopener"') if slug.startswith('http') else ('href="projects/' + slug + '.html"')}>
        <div class="card__meta">{m}</div>
        <div class="card__t">{t}</div>
        <p class="card__d">{p}</p>
        <div class="card__k">{k}</div>
      </a>''' for slug, m, t, p, k in items)
    work_cards = cards_for(d['work_cards'])
    personal_cards = cards_for(d['personal_cards'])
    skills = '\n'.join(
        f'''      <div class="skill">
        <div class="skill__k">{k}</div>
        <div class="skill__v">{v}</div>
      </div>''' for k, v in d['skills'])
    body = f'''<header class="hero">
  <div class="wrap hero__grid">
    <div>
      <h1>Bùi Henry</h1>
      <div class="hero__role">{d['role']}</div>
      <p class="hero__lede">{d['lede']}</p>
      <div class="btns">
        <a class="btn btn--primary" href="#work">{d['cta1']}</a>
        <a class="btn btn--ghost" href="#contact">{d['cta2']}</a>
      </div>
    </div>
    <picture>
      <source srcset="{'../' if lang == 'vi' else ''}assets/henry.webp" type="image/webp">
      <img class="hero__photo" src="{'../' if lang == 'vi' else ''}assets/henry.jpg" width="640" height="640" alt="Bùi Henry">
    </picture>
  </div>
</header>

<div class="wrap">
  <div class="stats reveal">
{stats}
  </div>
</div>

<section id="work">
  <div class="wrap">
    <h2 class="h2" data-n="01.">{d['work_h']}</h2>
    <p class="sub">{d['work_s']}</p>
    <div class="cards">

{work_cards}
    </div>
  </div>
</section>

<section id="personal">
  <div class="wrap">
    <h2 class="h2" data-n="02.">{d['personal_h']}</h2>
    <p class="sub">{d['personal_s']}</p>
    <div class="cards">

{personal_cards}
    </div>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <h2 class="h2" data-n="03.">{d['skills_h']}</h2>
    <p class="sub">{d['skills_s']}</p>
    <div class="skills">
{skills}
    </div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <h2 class="h2" data-n="04.">{d['contact_h']}</h2>
    <p class="sub">{d['contact_s']}</p>
    <div class="btns">
      <a class="btn btn--primary" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=buihenry1404@gmail.com&amp;su=Opportunity%20for%20B%C3%B9i%20Henry" target="_blank" rel="noopener">buihenry1404@gmail.com</a>
      <a class="btn btn--ghost" href="https://github.com/BuiHenry1404" rel="me">GitHub</a>
      <a class="btn btn--ghost" href="https://www.linkedin.com/in/b%C3%B9i-henry-936290297/" rel="me">LinkedIn</a>
    </div>
  </div>
</section>'''
    return shell(lang=lang, depth=(0 if lang == 'en' else 1), lang_home='./', title=d['title'], desc=d['desc'],
                 body=body, self_path=base, alt_path=('vi/' if lang == 'en' else ''),
                 alt_rel=('vi/' if lang == 'en' else '../'))


def build_article(lang, slug, art):
    body = f'''<article class="wrap article">
  <h1>{art['h1']}</h1>
  <div class="article__meta">{art['meta']}</div>

{art['body']}

  <a class="backlink" href="{'../' if lang == 'en' else '../'}#work">{NAV[lang]['back']}</a>
</article>'''
    self_path = (f'projects/{slug}.html' if lang == 'en' else f'vi/projects/{slug}.html')
    alt_path = (f'vi/projects/{slug}.html' if lang == 'en' else f'projects/{slug}.html')
    alt_rel = (f'../vi/projects/{slug}.html' if lang == 'en' else f'../../projects/{slug}.html')
    return shell(lang=lang, depth=(1 if lang == 'en' else 2), lang_home='../', title=art['title'], desc=art['desc'],
                 body=body, self_path=self_path, alt_path=alt_path, alt_rel=alt_rel)
