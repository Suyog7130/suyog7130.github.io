---
permalink: /
title: "News"
math: true
hideAuthor: true
ShowWordCount: false
ShowToc: false
ShowReadingTime: false
hideTags: true
redirect_from: 
  - /news/
---



<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
.news-shell{
  --news-bg:#fff;
  --news-card:#fff;
  --news-fg:#24292f;
  --news-muted:#57606a;
  --news-border:#d0d7de;
  --news-soft:#f6f8fa;
  --news-blue:#0969da;
  --news-green:#1a7f37;
  --news-brown:#8b5e34;
  --news-red:#cf222e;
  display:grid;
  gap:1rem;
  margin:1rem 0;
  color:var(--news-fg);
}

.news-toolbar{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  gap:.55rem;
  padding:.8rem;
  border:1px solid var(--news-border);
  border-radius:14px;
  background:var(--news-card);
  box-shadow:0 2px 8px rgba(0,0,0,.05);
}

.news-search{
  flex:1 1 220px;
  border:1px solid var(--news-border);
  border-radius:999px;
  padding:.45rem .75rem;
  background:var(--news-bg);
  color:var(--news-fg);
  font:inherit;
}

.news-catbar{
  display:flex;
  flex-wrap:wrap;
  gap:.35rem;
}

.news-cat-filter,
.news-clear{
  border:1px solid var(--news-border);
  border-radius:999px;
  padding:.28rem .62rem;
  background:var(--news-bg);
  color:var(--news-fg);
  font:inherit;
  cursor:pointer;
}

.news-cat-filter.is-active{
  border-color:currentColor;
  font-weight:800;
}

.news-clear{
  color:var(--news-muted);
}

.news-count{
  margin-left:auto;
  color:var(--news-muted);
  font-size:.9rem;
}

.news-section{
  border:1px solid var(--news-border);
  border-radius:16px;
  padding:.6rem .75rem .8rem;
  background:var(--news-card);
  box-shadow:0 2px 8px rgba(0,0,0,.05);
}

.news-section > summary{
  cursor:pointer;
  font-weight:900;
  font-size:1.08rem;
  margin:.2rem 0 .7rem;
}

.news-list{
  display:grid;
  gap:.75rem;
}

.news-card{
  border:1px solid var(--news-border);
  border-radius:14px;
  padding:.85rem 1rem;
  background:linear-gradient(180deg, var(--news-card), var(--news-soft));
  box-shadow:0 2px 8px rgba(0,0,0,.045);
}

.news-head{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  gap:.45rem .6rem;
  margin-bottom:.35rem;
}

.news-tag{
  display:inline-flex;
  align-items:center;
  gap:.3rem;
  border:1px solid currentColor;
  border-radius:999px;
  padding:.12rem .5rem;
  font-size:.78rem;
  font-weight:900;
  line-height:1.25;
}

.news-tag.academic{color:var(--news-blue)}
.news-tag.paper,
.news-tag.talk,
.news-tag.poster{color:var(--news-green)}
.news-tag.award,
.news-tag.honour,
.news-tag.career{color:var(--news-brown)}
.news-tag.part-time{color:var(--news-blue)}
.news-tag.other{color:var(--news-muted)}

.news-date{
  display:inline-flex;
  align-items:center;
  gap:.3rem;
  color:var(--news-muted);
  font-size:.9rem;
}

.news-year{
  margin-left:auto;
  color:var(--news-muted);
  font-size:.82rem;
  border:1px dashed var(--news-border);
  border-radius:999px;
  padding:.08rem .45rem;
}

.news-text{
  line-height:1.65;
}

.news-text a{
  text-decoration:none;
  font-weight:700;
}

.news-text a:hover{
  text-decoration:underline;
}

.news-links{
  display:flex;
  flex-wrap:wrap;
  gap:.4rem;
  margin-top:.45rem;
}

.news-link-chip{
  display:inline-flex;
  align-items:center;
  gap:.35rem;
  border:1px solid var(--news-border);
  border-radius:999px;
  padding:.22rem .58rem;
  font-size:.86rem;
  text-decoration:none;
  color:inherit;
  background:var(--news-bg);
}

.news-empty{
  color:var(--news-muted);
  font-style:italic;
  margin:.4rem 0;
}

@media (prefers-color-scheme: dark){
  .news-shell{
    --news-bg:#0d1117;
    --news-card:#161b22;
    --news-fg:#c9d1d9;
    --news-muted:#8b949e;
    --news-border:#30363d;
    --news-soft:#0d1117;
  }

  .news-card,
  .news-section,
  .news-toolbar{
    box-shadow:0 2px 10px rgba(0,0,0,.28);
  }

  .news-tag{
    color:inherit !important;
    opacity:.95;
  }
}
</style>


<!-- Section Headings -->

<div class="news-shell">
  <div class="news-toolbar">
    <input id="newsSearch" class="news-search" type="search" placeholder="Search news..." aria-label="Search news">
    <div id="newsCatbar" class="news-catbar"></div>
    <button id="newsClear" class="news-clear" type="button">Clear</button>
    <span id="newsCount" class="news-count"></span>
  </div>

  <details class="news-section" open>
    <summary>Recent News</summary>
    <div id="newsRecent" class="news-list"></div>
  </details>

  <details class="news-section">
    <summary>Older News</summary>
    <div id="newsOlder" class="news-list"></div>
  </details>
</div>

<!-- Actual Data -->

<script type="text/plain" id="newsData">
# group | category | date | text | links

recent | Paper | 2026年06月12日 | PhD paper accepted in PRD |
recent |  Talk | 2026年05月xx日 | Joined [APRIM](https://aprim2026.org/) in Hong Kong for a talk |
recent | Academic | 2026年02月18-28日 | Visited Prof. Otto's GW group at CUHK, Hong Kong. |
recent | Academic | 2025年11月18日 | Presented a [Gravitational Waves Data Analysis tutorial](https://suyoggarg.com/ewha/) at Ewha Womans University, Seoul. |
recent | Paper | 2025年11月 | Two new papers up on Arxiv this month! |

older | Academic | 2025年10月 | Volunteered for the LVK Rapid Response Team level-0 shifter, for the third time! We had [one significant BBH detection](https://gracedb.ligo.org/superevents/S251021u/view/) during my shift. |
older | Academic | 2025年10月 ー 2025年11月 | Visiting Prof HM Lee and group at Seoul National University, Korea! |
older | Talk | 2025年10月08日 | Invited talk at Osaka Metropolitan University (online). |
older | Academic | 2025年10月 ー 2026年02月 | Serving as a Teaching Assistant for the graduate-level "Gravitational-Wave Physics" Course! (third time's the charm :) |
older | Honour | 2025年09月11日 | I am addressing the incoming batch of embassy-recommended MEXT scholars at the Embassy of Japan in India (online). |
older | Talk | 2025年09月05日 | Presented a talk at the RESCEU Summer School, Hirono, Fukushima. |
older | Academic | 2025年09月02-03日 | Hosting Deep Chatterjee @ MIT at RESCEU |
older | Academic | 2025年08月06-30日 | Visited Paul Lasky and Eric Thrane's group at OzGrav, Monash university, Melbourne (again ;) |
older | Award | 2025年08月 | Selected for the graduate research abroad (GRASP) program by the University of Tokyo for trip to Korea later this year! |
older | Poster | 2025年07月15-25日 | Presenting a Poster at the ICRC 2025 in Geneva, Swizz! |
older | Talk | 2024年08月02日 | Spoke at the KAGRA International Workshop 12 in Shanghai, China! |
older | Poster | 2025年03月24-28日 | Presenting a Poster at the LVK Meeting in Monash university, Melbourne. |
older | Academic | 2025年03月08-29日 | Visited Paul Lasky and Eric Thrane's group at OzGrav, Monash university, Melbourne. |
older | Academic | 2025年01月 ー 2025年09月 | Enrolled in the MITx Statistics and Data Science MicroMasters Programs. Crediting four courses in the Methods track. |


older | Academic | 2024年10月 ー 2025年02月 | I serve as a Teaching Assistant for the Graduate-level "Gravitational-Wave Physics" Course! (once again :) |
older | Talk | 2024年08月02日 | Gave an invited talk at the "Eccentric Seminar" at Tokyo City University | slides:fa-file-pdf:https://www.dropbox.com/scl/fi/pamxd525b7lg1o9vjiaxs/eccentric-seminar-240802-talk-v1.pdf?rlkey=slz51bn7jgyfgpzu6io3b0b95&dl=0
older | Talk | 2024年07月06日 | Presentation at the Department of Physics Open House for prospective International student at UTokyo | slides:fa-file-pdf:https://www.dropbox.com/scl/fi/m49tb46fregudg8s8rmua/UTokyo-Phys-Dept-Open-House-240706.pdf?rlkey=jnzbhoxyq8kyc7r1ng9mg3rvh&dl=0
older | Talk | 2024年06月20日 | Gave a talk at RESCEU-UTAP Thursday Seminar | slides:fa-file-pdf:https://www.dropbox.com/scl/fi/d7rvscuzuf3462wbtirog/thurs-seminar-240620-talk.pdf?rlkey=pxnfixmqqaplledvruua56du6&dl=0
older | Academic | 2024年04月〜 | I will be hosting the RESCEU-UTAP Thursday seminars starting next term! |
older | Poster | 2024年03月11ー14日 | I will be participating in the [LVK collaboration meeting](https://www.lsu.edu/physics/lvkmeeting/index.php) at Louisiana State Univesity, Baton Rouge. |
older | Academic | 2024年01月16ー28日 | Visited Prof Gopu's lab in the Department of Astronomy at TIFR, Mumbai! |
older | Academic | 2023年12月〜 | I am be one of the [reviewers](https://git.ligo.org/waveforms/reviews/nrtidalv3/-/wikis/home#review-checks-and-review-documentation) for the [NRTidalv3](https://dcc.ligo.org/G2302143) waveform model! My contributions will be on _Time Domain Behavior_ and _Documentation_. |
older | Part-time | 2023年12月07ー15日 | Serving as a part-time worker during the RESCEU-NBIA workshop in the Hongo campus! |
older | Talk | 2023年12月07ー15日 | I plan to submit present a talk on X-Ray Observations in the [RESCEU-NBIA GW Workshop](https://indico2.cns.s.u-tokyo.ac.jp/event/286/overview), at UTokyo, Hongo campus! |
older | Talk | 2023年12月04ー06日 | Have a talk at the [Gakujutsu-Henkaku Conference](https://multimessenger.jp/en/events/annualconf-1/) in Gero Onsen Sumeikan, Gifu! |
older | Poster | 2023年11月13ー18日 | I will present a Poster in the [MLPhys Conference](https://mlphys.scphys.kyoto-u.ac.jp/ic_mlphys/) at YITP, Kyoto University. |
older | Part-time | 2023年11月06ー09日 | Tomonokai Junior High School Program at Mitaka! |
older | Talk | 2023年10月31日 | I have a contributed talk at the [RESCEU Symposium](https://www.resceu.s.u-tokyo.ac.jp/symposium/resceu_sympo2023/), UTokyo, Hongo. |
older | Academic | 2023年10月ー2024年02月 | I serve as a Teaching Assistant for the Graduate-level "Gravitational-Wave Physics" Course! (my first TAship :) |
older | Career | 2023年10月01日 | Started PhD with Kipp-san at [RESCEU](https://www.resceu.s.u-tokyo.ac.jp/top.php), The University of Tokyo |
</script>

<!-- Scripts -->

<script>
(function(){
  const dataEl = document.getElementById("newsData");
  const recentEl = document.getElementById("newsRecent");
  const olderEl = document.getElementById("newsOlder");
  const searchEl = document.getElementById("newsSearch");
  const catbarEl = document.getElementById("newsCatbar");
  const clearEl = document.getElementById("newsClear");
  const countEl = document.getElementById("newsCount");

  if(!dataEl || !recentEl || !olderEl) return;

  const state = {
    q:"",
    cats:new Set()
  };

  function esc(s){
    return String(s || "").replace(/[&<>"']/g, c => ({
      "&":"&amp;",
      "<":"&lt;",
      ">":"&gt;",
      '"':"&quot;",
      "'":"&#39;"
    }[c]));
  }

  function splitRow(line){
    return line.split("|").map(x => x.trim());
  }

  function catClass(cat){
    const k = String(cat || "").toLowerCase();
    if(k.includes("academic")) return "academic";
    if(k.includes("paper")) return "paper";
    if(k.includes("talk")) return "talk";
    if(k.includes("poster")) return "poster";
    if(k.includes("award")) return "award";
    if(k.includes("honour") || k.includes("honor")) return "honour";
    if(k.includes("career")) return "career";
    if(k.includes("part")) return "part-time";
    return "other";
  }

  function normalGroup(raw){
    const g = String(raw || "recent").toLowerCase();
    if(["older","old","past","previous"].includes(g)) return "older";
    return "recent";
  }

  function yearFromDate(date){
    const m = String(date || "").match(/(19|20)\d{2}/);
    return m ? m[0] : "";
  }

  function mdInline(text){
    const parts = [];
    let last = 0;
    const rx = /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g;
    let m;

    while((m = rx.exec(text || ""))){
      parts.push(esc(text.slice(last, m.index)));
      parts.push(`<a href="${esc(m[2])}" target="_blank" rel="noopener">${esc(m[1])}</a>`);
      last = rx.lastIndex;
    }
    parts.push(esc(String(text || "").slice(last)));

    return parts.join("")
      .replace(/_([^_]+)_/g, "<em>$1</em>");
  }

  function parseLinks(raw){
    return String(raw || "")
      .split(";")
      .map(x => x.trim())
      .filter(Boolean)
      .map(x => {
        const parts = x.split(":");
        const label = parts.shift() || "link";
        const icon = parts.shift() || "fa-up-right-from-square";
        const url = parts.join(":");
        return {label, icon, url};
      })
      .filter(x => x.url);
  }

  function loadRows(){
    return dataEl.textContent
      .split(/\r?\n/)
      .map(x => x.trim())
      .filter(x => x && !x.startsWith("#"))
      .map(line => {
        const cols = splitRow(line);
        return {
          group: normalGroup(cols[0]),
          cat: cols[1] || "Other",
          date: cols[2] || "",
          text: cols[3] || "",
          links: parseLinks(cols.slice(4).join(" | ")),
          year: yearFromDate(cols[2] || "")
        };
      })
      .filter(x => x.text);
  }

  const allItems = loadRows();

  function buildCatbar(){
    const cats = [...new Set(allItems.map(x => x.cat))].sort((a,b) => a.localeCompare(b));
    catbarEl.innerHTML = cats.map(cat => {
      const n = allItems.filter(x => x.cat === cat).length;
      return `<button class="news-cat-filter ${catClass(cat)}" type="button" data-cat="${esc(cat)}">${esc(cat)} (${n})</button>`;
    }).join("");

    catbarEl.querySelectorAll("button").forEach(btn => {
      btn.addEventListener("click", () => {
        const cat = btn.dataset.cat;
        if(state.cats.has(cat)) state.cats.delete(cat);
        else state.cats.add(cat);
        render();
      });
    });
  }

  function passes(item){
    const q = state.q.trim().toLowerCase();
    const catOK = !state.cats.size || state.cats.has(item.cat);
    const textBlob = `${item.cat} ${item.date} ${item.text}`.toLowerCase();
    const qOK = !q || textBlob.includes(q);
    return catOK && qOK;
  }

  function card(item){
    const links = item.links.map(l =>
      `<a class="news-link-chip" href="${esc(l.url)}" target="_blank" rel="noopener"><i class="fa ${esc(l.icon)}"></i>${esc(l.label)}</a>`
    ).join("");

    return `
      <article class="news-card">
        <div class="news-head">
          <span class="news-tag ${catClass(item.cat)}">${esc(item.cat)}</span>
          <span class="news-date"><i class="fa fa-paper-plane"></i>${esc(item.date)}</span>
          ${item.year ? `<span class="news-year">${esc(item.year)}</span>` : ""}
        </div>
        <div class="news-text">${mdInline(item.text)}</div>
        ${links ? `<div class="news-links">${links}</div>` : ""}
      </article>
    `;
  }

  function render(){
    const visible = allItems.filter(passes);
    const recent = visible.filter(x => x.group === "recent");
    const older = visible.filter(x => x.group === "older");

    recentEl.innerHTML = recent.map(card).join("") || `<p class="news-empty">No recent news matching this filter.</p>`;
    olderEl.innerHTML = older.map(card).join("") || `<p class="news-empty">No older news matching this filter.</p>`;

    document.querySelectorAll(".news-section").forEach(section => {
      const list = section.querySelector(".news-list");
      const key = list && list.id === "newsOlder" ? "older" : "recent";
      const n = key === "older" ? older.length : recent.length;
      const summary = section.querySelector("summary");
      if(summary){
        if(!summary.dataset.baseTitle) summary.dataset.baseTitle = summary.textContent.trim().replace(/\s*\(\d+\)\s*$/, "");
        summary.textContent = `${summary.dataset.baseTitle} (${n})`;
      }
    });

    catbarEl.querySelectorAll("button").forEach(btn => {
      btn.classList.toggle("is-active", state.cats.has(btn.dataset.cat));
    });

    countEl.textContent = `Showing ${visible.length} of ${allItems.length}`;
  }

  searchEl.addEventListener("input", () => {
    state.q = searchEl.value || "";
    render();
  });

  clearEl.addEventListener("click", () => {
    state.q = "";
    state.cats.clear();
    searchEl.value = "";
    render();
  });

  buildCatbar();
  render();
})();
</script>








<!-- Old Styles legacy -->





<!-- News -->
<!-- <h2><p style="text-align:center; font-family:mistral;"> News </p></h2>
-->


<!-- <i class="fa fa-clock"></i>
<i class="ai ai-google-scholar"></i>
<a href="https://scholar.google.com/citations?hl=en&amp;user=FtzrMYwAAAAJ" class="icon-link" target="_blank" rel="noopener" data-original-href="https://scholar.google.com/citations?hl=en&amp;user=FtzrMYwAAAAJ"><i class="ai ai-google-scholar"></i> Google Scholar</a> -->

<!-- <div style="text-align: center">
<a href="https://sensr.net/auth/users/sign_up">
<button style="background-color:#a4d61e;margin-top:6px;margin-bottom:16px;border-radius:4px;font-size:1.6em;padding:8px 20px;    font-family: "GibsonSemibold", "Helvetica Neue", Helvetica, Arial, sans-serif;float:none !important;text-shadow:0 1px 1px rgba(0,0,0,0.2)">
Sign up for free!
</button>
</a>
</div>
-->

<!--{{% button href="https://gohugo.io/" %}}Get Hugo{{% /button %}}
{{% button href="https://gohugo.io/" style="warning" icon="dog" %}}Get Hugo{{% /button %}}-->

<!--
<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2026年02月18-28日
</br>
Visited Prof. Otto's GW group at CUHK, Hong Kong.

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年11月18日
</br>
Presented a [Gravitational Waves Data Analysis tutorial](https://suyoggarg.com/ewha/) at Ewha womans university, Seoul.

<span style="color:green; font-weight:bold">[Paper]</span> 
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年11月
<br/>
Two new papers up on Arxiv this month!

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年10月
</br>
Volunteered for the LVK Rapid Response Team level-0 shifter, for the third time! We had [one significant BBH detection](https://gracedb.ligo.org/superevents/S251021u/view/) during my shift.

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年10月 ー 2025年11月
</br>
Visiting Prof HM Lee and group at Seoul National University, Korea!

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年10月08日
<br/>
Invited talk at Osaka Metropolitan University (online).
<br/>

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年10月 ー 2026年02月
</br>
Serving as a Teaching Assistant for the graduate-level "Graviational-Wave Physics" Course ! (third time's the charm :)

<span style="color:brown; font-weight:bold">[Honour]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年09月11日
</br>
I am addressing the incoming batch of embassy-recommended MEXT scholars at the Embassy of Japan in India (online). 

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年09月05日
<br/>
Presented a talk at the RESCEU Summer School, Hirono, Fukushima.
<br/>
$\rightarrow$ <i class="fa fa-file-pdf">&nbsp;</i>

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年09月02-03日
</br>
Hosting Deep Chatterjee @ MIT at RESCEU

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年08月06-30日
</br>
Visited Paul Lasky and Eric Thrane's group at OzGrav, Monash university, Melbourne (again ;)

<span style="color:brown; font-weight:bold">[Award]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年08月
</br>
Selected for the graduate research abroad (GRASP) program by the University of Tokyo for trip to Korea later this year!

<span style="color:green; font-weight:bold">[Poster]</span> 
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年07月15-25日
<br/>
Presenting a Poster at the ICRC 2025 in Geneva, Swizz!

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年08月02日
<br/>
Spoke at the KAGRA International Workshop 12 in Shanghai, China!
<br/>
$\rightarrow$ <i class="fa fa-file-pdf">&nbsp;</i>

<span style="color:green; font-weight:bold">[Poster]</span> 
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年03月24-28日
<br/>
Presenting a Poster at the LVK Meeting in Monash university, Melbourne.

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年03月08-29日
</br>
Visited Paul Lasky and Eric Thrane's group at OzGrav, Monash university, Melbourne.

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2025年01月 ー 2025年09月
</br>
Enrolled in the MITx Statistics and Data Science MicroMasters Programs. Crediting four courses in the Methods track.

    
<!-- Older News -->

<!--

<details>
	<summary style="font-family: mistral; text-align:center; font-size: 24px">
	Older News
	</summary>


<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年10月 ー 2025年02月
</br>
I serve as a Teaching Assistant for the Graduate-level "Graviational-Wave Physics" Course ! (once again :)

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年08月02日
<br/>
Gave an invited talk at the "Eccentric Seminar" at Tokyo City University 
<br/>
$\rightarrow$ <i class="fa fa-file-pdf">&nbsp;</i>
<a href="https://www.dropbox.com/scl/fi/pamxd525b7lg1o9vjiaxs/eccentric-seminar-240802-talk-v1.pdf?rlkey=slz51bn7jgyfgpzu6io3b0b95&dl=0">slides</a>

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年07月06日
<br/>
Presentation at the Department of Physics Open House for prospective International student at UTokyo
$\rightarrow$ <i class="fa fa-file-pdf">&nbsp;</i>
<a href="https://www.dropbox.com/scl/fi/m49tb46fregudg8s8rmua/UTokyo-Phys-Dept-Open-House-240706.pdf?rlkey=jnzbhoxyq8kyc7r1ng9mg3rvh&dl=0">slides</a>

<span style="color:green; font-weight:bold">[Talk]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年06月20日
<br/>
Gave a talk at RESCEU-UTAP Thursday Seminar
$\rightarrow$ <i class="fa fa-file-pdf">&nbsp;</i>
<a href="https://www.dropbox.com/scl/fi/d7rvscuzuf3462wbtirog/thurs-seminar-240620-talk.pdf?rlkey=pxnfixmqqaplledvruua56du6&dl=0">slides</a>

<span style="color:darkblue; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年04月〜
<br/>
I will be hosting the RESCEU-UTAP Thursday seminars starting next term ! 

<span style="color:green; font-weight:bold">[Poster]</span> 
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年03月11ー14日
<br/>
I will be participating in the [LVK collaboration meeting](https://www.lsu.edu/physics/lvkmeeting/index.php) at Louisiana State Univesity, Baton Rouge.

<span style="color:darkgreen; font-weight:bold">[Academic]</span>
&nbsp;
<i class="fa fa-paper-plane"></i>
2024年01月16ー28日
<br/>
Visited Prof Gopu's lab in the Department of Astronomy at TIFR, Mumbai !	

<i class="fa fa-paper-plane">&nbsp;</i>
2023年12月$\sim$
<br/>
<span style="color:darkgreen; font-weight:bold">[Academic]</span> 
I am be one of the [reviewers](https://git.ligo.org/waveforms/reviews/nrtidalv3/-/wikis/home#review-checks-and-review-documentation) for the [NRTidalv3](https://dcc.ligo.org/G2302143) waveform model ! My contributions will be on _Time Domain Behavior_ and _Documentation_. 

- <span style="color:blue; font-weight:bold">[Part-time]</span> 2023年12月07ー15日
<br/> Serving as a part-time worker during the RESCEU-NBIA workshop in the Hongo campus !

- <span style="color:green; font-weight:bold">[Talk]</span> 2023年12月07ー15日
<br/> I plan to submit present a talk on X-Ray Observations in the [RESCEU-NBIA GW Workshop](https://indico2.cns.s.u-tokyo.ac.jp/event/286/overview), at UTokyo, Hongo campus !

- <span style="color:green; font-weight:bold">[Talk]</span> 2023年12月04ー06日
<br/> Have a talk at the [Gakujutsu-Henkaku Conference](https://multimessenger.jp/en/events/annualconf-1/) in Gero Onsen Sumeikan, Gifu !

- <span style="color:green; font-weight:bold">[Poster]</span> 2023年11月13ー18日
<br/> I will present a Poster in the [MLPhys Conference](https://mlphys.scphys.kyoto-u.ac.jp/ic_mlphys/) at YITP, Kyoto University.

- <span style="color:blue; font-weight:bold">[Part-time]</span> 2023年11月06ー09日
<br/> Tomonokai Junior High School Program at Mitaka !

- <span style="color:green; font-weight:bold">[Talk]</span> 2023年10月31日
<br/> I have a contributed talk at the [RESCEU Symposium](https://www.resceu.s.u-tokyo.ac.jp/symposium/resceu_sympo2023/), UTokyo, Hongo.

- <span style="color:darkblue; font-weight:bold">[Academic]</span> 2023年10月ー2024年02月
<br/> I serve as a Teaching Assistant for the Graduate-level "Graviational-Wave Physics" Course ! (my first TAship :)

- <span style="color:brown; font-weight:bold">[Career]</span> 2023年10月01日
<br/> Started PhD with Kipp-san at [RESCEU](https://www.resceu.s.u-tokyo.ac.jp/top.php), The University of Tokyo

</details>
-->