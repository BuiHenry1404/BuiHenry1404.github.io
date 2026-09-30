#!/usr/bin/env python3
"""Generate the bilingual static portfolio. Output is plain HTML — no runtime build step."""
import pathlib, json, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://buihenry1404.github.io'
SLUGS = ['mainframe-agent', 'sdlc-platform', 'code-retrieval', 'salona']

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
   desc='AI Engineer building production LLM agents: grounding, retrieval, tool calling and guardrails. Python, FastAPI, LangGraph, MCP.',
   role='AI ENGINEER',
   lede='I build LLM agents in Python and FastAPI that answer from real source code: parsers and MCP tools give the model facts, and code checks its output before anything is saved.',
   cta1='See the work', cta2='Get in touch',
   stats=[('−60%', 'hallucinations on a COBOL maintenance agent'),
          ('−20–30%', 'context tokens per code lookup'),
          ('50→80%', 'documents usable on the first run, 9-step agent workflow'),
          ('2+ yrs', 'building agents at FPT Software')],
   work_h='Work experience',
   work_s='Three projects at FPT Software, each with the design decision that mattered and the number it moved.',
   personal_h='Personal project',
   personal_s='Built end to end, outside work.',
   skills_h='Skills', skills_s='What I reach for, roughly in order of how much I use it.',
   contact_h='Get in touch', contact_s='Open to AI Engineer roles in Ho Chi Minh City or remote.',
   skills=[('AI / LLM', 'LangGraph, LangChain, AutoGen · multi-agent orchestration · tool calling · MCP (Model Context Protocol) · RAG, retrieval &amp; embedding search · long-term agent memory (Neo4j + Qdrant) · prompt &amp; context engineering · structured output · guardrails · LLM evaluation · Azure OpenAI · Langfuse'),
           ('Backend', 'Python · FastAPI · REST APIs · Socket.IO · Redis · PostgreSQL / Supabase · MongoDB · Neo4j · Qdrant · pgvector · Docker'),
           ('Parsing / tooling', 'ANTLR4 (grammars, AST) · Tree-sitter · Azure DevOps REST API · Git · pytest · Claude Code, GitHub Copilot, Codex · reading-level COBOL / JCL / CopyBook — enough to write parsers for them, not to write production programs in them')],
   work_cards=[('sdlc-platform', 'FPT Software · Apr 2026 – present', 'A multi-agent SDLC platform',
           'Six SDLC agents and a 9-step workflow that turns a rough idea into requirements, design and a mockup — plus the Azure DevOps integration that puts it where developers work.',
           '50% → 80% usable on the first run →'),
          ('code-retrieval', 'FPT Software · Jun – Sep 2026', 'Retrieval for coding agents',
           'Benchmarked regex, a Tree-sitter code graph and embedding search over a 3M-line monorepo. The winner was cheaper — and measurably worse at one thing.',
           '−20–30% token cost →'),
          ('mainframe-agent', 'FPT Software · Nov 2025 – Apr 2026', 'Grounding an agent in COBOL',
           'ANTLR4 parsers turn COBOL/JCL/CopyBook into structured JSON; MCP tools let the LLM query real dependencies instead of guessing.',
           '−60% hallucinations →')],
   personal_cards=[('salona', 'Personal · Aug 2026', 'A booking agent with an architectural guardrail',
           'The agent calls seven tools to find open slots, but the write path is out of its reach: a deterministic node commits from the database, and a code guard checks every reply.',
           'No write tool for the LLM →')],
 ),
 'vi': dict(
   title='Bùi Henry — AI Engineer',
   desc='AI Engineer xây dựng LLM agent chạy production: grounding, retrieval, tool calling và guardrail. Python, FastAPI, LangGraph, MCP.',
   role='AI ENGINEER',
   lede='Tôi xây LLM agent bằng Python và FastAPI, trả lời dựa trên source code thật: parser và MCP tool đưa dữ kiện cho model, còn code kiểm tra kết quả trước khi lưu.',
   cta1='Xem dự án', cta2='Liên hệ',
   stats=[('−60%', 'hallucination của agent hỗ trợ COBOL'),
          ('−20–30%', 'token context mỗi lần tra code'),
          ('50→80%', 'tài liệu dùng được ngay lần chạy đầu, workflow 9 bước'),
          ('2+ năm', 'xây agent tại FPT Software')],
   work_h='Kinh nghiệm làm việc',
   work_s='Ba dự án tại FPT Software, mỗi dự án kèm quyết định thiết kế quan trọng nhất và con số nó thay đổi.',
   personal_h='Dự án cá nhân',
   personal_s='Tự làm từ đầu tới cuối, ngoài giờ làm.',
   skills_h='Kỹ năng', skills_s='Những thứ tôi dùng, xếp gần theo tần suất.',
   contact_h='Liên hệ', contact_s='Đang tìm vị trí AI Engineer tại TP.HCM hoặc remote.',
   skills=[('AI / LLM', 'LangGraph, LangChain, AutoGen · điều phối multi-agent · tool calling · MCP (Model Context Protocol) · RAG, retrieval &amp; embedding search · bộ nhớ dài hạn cho agent (Neo4j + Qdrant) · prompt &amp; context engineering · structured output · guardrail · đánh giá LLM · Azure OpenAI · Langfuse'),
           ('Backend', 'Python · FastAPI · REST API · Socket.IO · Redis · PostgreSQL / Supabase · MongoDB · Neo4j · Qdrant · pgvector · Docker'),
           ('Parsing / công cụ', 'ANTLR4 (grammar, AST) · Tree-sitter · Azure DevOps REST API · Git · pytest · Claude Code, GitHub Copilot, Codex · COBOL / JCL / CopyBook ở mức đọc hiểu — đủ để viết parser cho chúng, không phải để viết chương trình production')],
   work_cards=[('sdlc-platform', 'FPT Software · 04/2026 – nay', 'Nền tảng SDLC đa agent',
           'Sáu agent SDLC và quy trình 9 bước biến một ý tưởng thô thành yêu cầu, thiết kế và mockup — cùng phần tích hợp Azure DevOps đưa nó tới đúng nơi developer làm việc.',
           '50% → 80% dùng được ngay lần đầu →'),
          ('code-retrieval', 'FPT Software · 06 – 09/2026', 'Retrieval cho coding agent',
           'Benchmark regex, code graph Tree-sitter và embedding search trên monorepo 3 triệu dòng. Phương án thắng rẻ hơn — và kém hơn ở đúng một việc.',
           '−20–30% chi phí token →'),
          ('mainframe-agent', 'FPT Software · 11/2025 – 04/2026', 'Agent trả lời từ mã COBOL thật',
           'Parser ANTLR4 chuyển COBOL/JCL/CopyBook thành JSON có cấu trúc; MCP tool cho LLM tra phụ thuộc thật thay vì đoán.',
           '−60% hallucination →')],
   personal_cards=[('salona', 'Cá nhân · 08/2026', 'Agent đặt lịch có guardrail kiến trúc',
           'Agent gọi bảy tool để tìm khung giờ trống, nhưng không có quyền ghi: một node tất định mới ghi lịch từ database, và mọi câu trả lời đều qua một lớp kiểm tra bằng code.',
           'LLM không có quyền ghi lịch →')],
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
            f'''      <a class="card reveal" href="projects/{slug}.html">
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
