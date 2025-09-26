---
layout: archive
title: "CV/Resume"
permalink: /cv/
hideAuthor: true
ShowToc: false
ShowReadingTime: false
ShowWordCount: false
hideTags: true
redirect_from:
  - /resume
---

<section class="cv-root">
  <header class="cv-header">
    <h1 id="cvName">Suyog Garg</h1>
    <p id="cvTagline">Gravitational-wave astrophysics • Computational methods • Data analysis</p>
    <div class="cv-contacts">
      <span class="cv-chip" id="cvWeb" aria-label="Website"><i class="fa fa-globe"></i><a id="cvWebLink" rel="me noopener" target="_blank"></a></span>
      <!-- Sensitive: assembled client-side, opt-in reveal -->
      <span class="cv-chip sens" id="cvEmailWrap" data-nosnippet hidden>
        <i class="fa fa-envelope"></i><a id="cvEmailLink" rel="nofollow"></a>
      </span>
      <span class="cv-chip sens" id="cvAddrWrap" data-nosnippet hidden>
        <i class="fa fa-location-dot"></i><span id="cvAddress"></span>
      </span>
      <span class="cv-chip sens" id="cvDobWrap" data-nosnippet hidden>
        <i class="fa fa-cake-candles"></i><span id="cvDob"></span>
      </span>
      <button id="revealBtn" class="cv-btn" aria-expanded="false" aria-controls="cvEmailWrap cvAddrWrap cvDobWrap">
        <i class="fa fa-eye"></i> Reveal contact details
      </button>
    </div>
  </header>

  <main class="cv-grid">
    <section>
      <h2>Affiliations</h2>
      <ul id="affNow" class="cv-list"></ul>
      <details>
        <summary class="cv-subtle">Past affiliations</summary>
        <ul id="affPast" class="cv-list"></ul>
      </details>
    </section>
    <section>
      <h2>Education</h2>
      <ul id="eduList" class="cv-list"></ul>
    </section>
    <section>
      <h2>Employment & Experience</h2>
      <ul id="expList" class="cv-list"></ul>
    </section>
    <section>
      <h2>Honours & Awards</h2>
      <ul id="awardsList" class="cv-list"></ul>
    </section>
    <section>
      <h2>Extracurricular</h2>
      <ul id="extraList" class="cv-list"></ul>
    </section>
  </main>

  <footer class="cv-foot">
    <small id="cvNote" class="cv-note"></small>
  </footer>
</section>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
/* === CV layout (light/dark + print) =================================== */
.cv-root{--bg:#fff;--fg:#1f2328;--muted:#57606a;--hair:#d0d7de;--chip:#fff;--chip-b:#d0d7de;--pill:#f6f8fa}
@media (prefers-color-scheme: dark){
  .cv-root{--bg:#0d1117;--fg:#c9d1d9;--muted:#8b949e;--hair:#30363d;--chip:#161b22;--chip-b:#30363d;--pill:#161b22}
}
html.dark .cv-root, :root[data-theme="dark"] .cv-root, body.dark .cv-root{
  --bg:#0d1117;--fg:#c9d1d9;--muted:#8b949e;--hair:#30363d;--chip:#161b22;--chip-b:#30363d;--pill:#161b22
}

.cv-root{background:var(--bg); color:var(--fg); padding:0 .5rem}
.cv-header{max-width:980px;margin:0 auto 1rem auto;padding:1rem 0 0 0;border-bottom:1px dashed var(--hair)}
.cv-header h1{margin:0; font-size:2rem; line-height:1.1}
.cv-header p{margin:.25rem 0 .8rem 0; color:var(--muted)}
.cv-contacts{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.cv-chip{display:inline-flex;gap:.4rem;align-items:center;background:var(--chip);border:1px solid var(--chip-b);border-radius:999px;padding:.25rem .6rem}
.cv-chip a{color:inherit;text-decoration:none}
.cv-chip a:hover{text-decoration:underline}
.cv-btn{margin-left:auto;border:1px solid var(--chip-b);background:var(--chip);color:inherit;border-radius:.5rem;padding:.35rem .6rem;cursor:pointer}
.cv-btn:hover{background:var(--pill)}

.cv-grid{max-width:980px;margin:1.1rem auto;display:grid;grid-template-columns:1fr;gap:1.1rem}
.cv-grid h2{margin:.25rem 0 .4rem 0;font-size:1.15rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.cv-list{margin:.2rem 0 .6rem 1.1rem}
.cv-list li{margin:.2rem 0 .35rem 0}
.cv-role{font-weight:600}
.cv-meta{color:var(--muted)}
.cv-subtle{color:var(--muted);cursor:pointer}
.cv-note{color:var(--muted); font-family:mistral;}

@media print{
  #revealBtn{display:none}
  .cv-root{padding:0}
  .cv-chip{border-color:#bbb}
}

/* Small helpers */
.sens[hidden]{display:none !important}
</style>

<script>
/** ===== Config ===== **/
const RESUME_JSON_PATH = "/files/resume.json"; // put under /static/json/
const SENSITIVE_KEYS = ["email","address","dob"];  // keys we won't render until user reveals

/** ===== Fallback sample (edit/replace via /json/resume.json) ===== **/
const SAMPLE_RESUME = {
  "basics":{
    "name":"Suyog Garg",
    "tagline":"PhD candidate • Gravitational-wave Astrophysics, Computational Methods",
    "website":"https://suyoggarg.com",
    "email":"gargsuyog@resceu.s.u-tokyo.ac.jp",
    "address":"7-3-1 Hongo, Bunkyo-ku, Tokyo 113-0033, Japan",
    "dob":"1998-05-20",
    "citizenship":"India"
  },
  "affiliations":{
    "current":[
      "Department of Physics, The University of Tokyo, Bunkyo-ku, Tokyo 113-0033, Japan",
      "Research Centre for Early Universe (RESCEU), The University of Tokyo, Bunkyo-ku, Tokyo 113-0033, Japan"
    ],
    "previous":[
      "2021–2023: Institute of Cosmic Ray Research (ICRR), Kashiwa-shi, Chiba 277-8582, Japan"
    ]
  },
  "education":[
    {"degree":"PhD in Physics","org":"The University of Tokyo, Japan","years":"2023 – 2026","advisor":"Kipp Cannon"},
    {"degree":"MSc in Physics","org":"The University of Tokyo, Japan","years":"2021 – 2023","advisor":"Masatake Ohashi"},
    {"degree":"BTech (Mechanical Eng., Design & Manufacturing)","org":"IIITDM Kancheepuram, Chennai","years":"2016 – 2020"},
    {"degree":"High School","org":"Montfort Senior Secondary School, Mandla","years":"2002 – 2016"}
  ],
  "experience":[
    {"role":"Visiting Research Student","org":"OzGrav, Monash University, Australia","when":"Mar & Aug 2025"},
    {"role":"Google Summer of Code Participant (Astropy)","org":"Astropy Project","when":"Jun – Aug 2021"},
    {"role":"Visiting Student (remote)","org":"IIT-BHU, Varanasi","when":"May – Jul 2021"},
    {"role":"Project Student (remote)","org":"Massachusetts Institute of Technology, USA","when":"Dec 2020 – Jun 2021"},
    {"role":"Visiting Student (remote)","org":"TIFR, Mumbai","when":"Nov 2020 – May 2021"},
    {"role":"Visiting Student","org":"IUCAA, Pune","when":"Aug – Oct 2019"},
    {"role":"Physics Summer Research Intern","org":"The Institute of Mathematical Sciences, Chennai","when":"May – Aug 2019"}
  ],
  "awards":[
    "Invited to address 2025 batch of MEXT scholars at Embassy of Japan in India (2025)",
    "Graduate Research Abroad Program (UTokyo) — visit to Seoul National University (2025)",
    "ULVAC–Hayashi Seed Funding between MIT and UTokyo — research featured (2024–25)",
    "Embassy-recommended MEXT Scholarship, Japan (2021–2023; 2023–2026)",
    "Provisional admission to SOKENDAI Graduate Program (2020)",
    "Vacations Student Program, IUCAA, Pune (2020)",
    "CBSE Distinction Certificate (2016)"
  ],
  "activities":[
    "Teaching Assistant, Gravitational-Wave Physics (2023, 2024, 2025)",
    "Secretary, University of Tokyo Indian Student Association (UTISA) (Jul 2022 – Jun 2023)",
    "Content writer, BrightBegins.com (Sep – Nov 2020)",
    "Contributing Editor, Margdarshan Magazine, IIITDM Kancheepuram (Jan 2017 – Apr 2018)",
    "Social Service Volunteer, VIDHAI (2017 – 2018)"
  ],
  "note":"Live life in such a way that life itself has a crush on you! — unknown (2025-09-15)"
};

/** ===== DOM els ===== **/
const E = sel => document.querySelector(sel);
const els = {
  name: E('#cvName'), tagline: E('#cvTagline'),
  webLink: E('#cvWebLink'),
  emailWrap: E('#cvEmailWrap'), emailLink: E('#cvEmailLink'),
  addrWrap: E('#cvAddrWrap'), address: E('#cvAddress'),
  dobWrap: E('#cvDobWrap'), dob: E('#cvDob'),
  revealBtn: E('#revealBtn'),
  affNow: E('#affNow'), affPast: E('#affPast'),
  eduList: E('#eduList'), expList: E('#expList'),
  awardsList: E('#awardsList'), extraList: E('#extraList'),
  note: E('#cvNote')
};

/** ===== Helpers ===== **/
const safe = s => (s??"").toString();
function li(html){ const li=document.createElement('li'); li.innerHTML=html; return li; }
function obfEmailClear(email){
  // Convert to "mailto:" on demand
  const [u,d]=email.split('@'); return {text:`${u} [at] ${d}`, href:`mailto:${u}@${d}`};
}
function setSensitiveVisible(on){
  [els.emailWrap,els.addrWrap,els.dobWrap].forEach(x=>{ if(!x) return; x.hidden = !on; });
  if(els.revealBtn){
    els.revealBtn.setAttribute('aria-expanded', String(on));
    els.revealBtn.innerHTML = on
      ? '<i class="fa fa-eye-slash"></i> Hide contact details'
      : '<i class="fa fa-eye"></i> Reveal contact details';
  }
}

/** ===== Render ===== **/
function renderCV(cv){
  const b = cv.basics || {};
  // Header
  if(b.name) els.name.textContent = b.name;
  els.tagline.textContent = safe(b.tagline || ''); 
  if(b.website){ els.webLink.textContent = b.website.replace(/^https?:\/\//,''); els.webLink.href = b.website; }

  // Sensitive (not shown until reveal)
  if(b.email){
    const {text, href} = obfEmailClear(b.email);
    els.emailLink.textContent = text; els.emailLink.href = href;
  }
  if(b.address){ els.address.textContent = b.address; }
  if(b.dob){ els.dob.textContent = b.dob; }

  // Affiliations
  (cv.affiliations?.current||[]).forEach(t => els.affNow.appendChild(li(`<span class="cv-role">Present:</span> <span class="cv-meta">${safe(t)}</span>`)));
  (cv.affiliations?.previous||[]).forEach(t => els.affPast.appendChild(li(`<span class="cv-meta">${safe(t)}</span>`)));

  // Education
  (cv.education||[]).forEach(e=>{
    const adv = e.advisor ? ` <span class="cv-meta">(advisor: ${safe(e.advisor)})</span>` : '';
    els.eduList.appendChild(li(`<span class="cv-role">${safe(e.degree)}</span>, ${safe(e.org)} <span class="cv-meta">— ${safe(e.years)}</span>${adv}`));
  });

  // Experience
  (cv.experience||[]).forEach(x=>{
    els.expList.appendChild(li(`<span class="cv-role">${safe(x.role)}</span>, ${safe(x.org)} <span class="cv-meta">— ${safe(x.when)}</span>`));
  });

  // Awards
  (cv.awards||[]).forEach(a=>els.awardsList.appendChild(li(safe(a))));

  // Extras
  (cv.activities||[]).forEach(e=>els.extraList.appendChild(li(safe(e))));

  // Note
  els.note.textContent = safe(cv.note||'');
}

/** ===== Boot ===== **/
async function boot(){
  let data = null;
  try{
    const url = new URL(RESUME_JSON_PATH, document.baseURI).href;
    const res = await fetch(url, {cache:'no-store'});
    if(res.ok){ data = await res.json(); }
  }catch(e){ /* ignore */ }
  if(!data) data = SAMPLE_RESUME;

  renderCV(data);
  setSensitiveVisible(false);

  // Toggle reveal
  els.revealBtn?.addEventListener('click', ()=>{
    const on = els.emailWrap.hidden; setSensitiveVisible(on);
  });
}

if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
</script>



<!--
<object data="/files/acadSummary-Nov2023.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="/files/acadSummary-Nov2023.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://www.suyog7130.github.io/files/acadSummary-Apr2024-no-contact.png">Download PDF</a></p>
    </embed>
</object>
-->

<!--<span style="text-align:center">
<img src="/files/acadSummary-Apr2024-no-contact.png" alt="acadSummary-Apr2024" style="height:100%; width:71%;dpi:300;"/>
</span>-->



<!--

Education
======
* B.S. in GitHub, GitHub University, 2012
* M.S. in Jekyll, GitHub University, 2014
* Ph.D in Version Control Theory, GitHub University, 2018 (expected)

Work experience
======
* Summer 2015: Research Assistant
  * Github University
  * Duties included: Tagging issues
  * Supervisor: Professor Git

* Fall 2015: Research Assistant
  * Github University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams

-->
