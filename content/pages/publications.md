---
title: "Publications"
author_profile: true
hideTags: true
showTOC: false
---

<!-- =========================
     INTERACTIVE QUICK VIEW
     ========================= -->

<div class="pub-controls" role="region" aria-label="Publications controls">
  <button id="btnFilter" class="pub-btn"><i class="fa fa-filter" aria-hidden="true"></i> Filter</button>
  <button id="btnSort" class="pub-btn"><i class="fa fa-sort" aria-hidden="true"></i> Sort</button>
  <span id="countLabel" class="pub-count" aria-live="polite"></span>
</div>

<div id="activeFilters" class="active-filters" aria-live="polite"></div>

<!-- Reverse-numbered list renders here -->
<ol id="pubList" class="pub-list" reversed></ol>

<!-- Filter dialog -->
<dialog id="filterDialog" aria-label="Filter publications">
  <form method="dialog" class="dialog-form">
    <h3>Filter</h3>
    <fieldset class="filter-group">
      <legend>Type</legend>
      <div id="filterTypes" class="filter-chips"><!-- populated by JS --></div>
    </fieldset>
    <fieldset class="filter-group">
      <legend>Subset / Topic</legend>
      <div id="filterSubsets" class="filter-chips"><!-- populated by JS --></div>
    </fieldset>
    <div class="dialog-actions">
      <button value="cancel" class="pub-btn pub-btn-secondary">Close</button>
      <button id="btnResetFilters" type="button" class="pub-btn pub-btn-secondary">Reset</button>
      <button id="btnApplyFilters" type="submit" class="pub-btn pub-btn-primary">Apply</button>
    </div>
  </form>
</dialog>

<!-- Sort dialog -->
<dialog id="sortDialog" aria-label="Sort publications">
  <form method="dialog" class="dialog-form">
    <h3>Sort</h3>
    <fieldset class="filter-group">
      <legend>Order</legend>
      <label class="radio">
        <input type="radio" name="sortMode" value="year-desc" checked>
        Year — newest → oldest
      </label>
      <label class="radio">
        <input type="radio" name="sortMode" value="year-asc">
        Year — oldest → newest
      </label>
      <label class="radio">
        <input type="radio" name="sortMode" value="title-asc">
        Title — A → Z
      </label>
      <label class="radio">
        <input type="radio" name="sortMode" value="title-desc">
        Title — Z → A
      </label>
      <label class="radio">
        <input type="radio" name="sortMode" value="first-asc">
        First author — A → Z
      </label>
      <label class="radio">
        <input type="radio" name="sortMode" value="first-desc">
        First author — Z → A
      </label>
    </fieldset>
    <div class="dialog-actions">
      <button value="cancel" class="pub-btn pub-btn-secondary">Close</button>
      <button id="btnApplySort" type="submit" class="pub-btn pub-btn-primary">Apply</button>
    </div>
  </form>
</dialog>

<!-- Hover preview tooltip -->
<div id="previewTip" class="preview-tip" role="tooltip" aria-hidden="true"></div>

<!-- =========================
     STYLES (scoped, minimal)
     ========================= -->
<style>
  .pub-controls{display:flex;gap:.75rem;align-items:center;flex-wrap:wrap;margin:0 0 1rem 0}
  .pub-btn{border:1px solid var(--mm-btn-border,#d0d7de);padding:.4rem .7rem;border-radius:.5rem;background:#fff;cursor:pointer;font:inherit}
  .pub-btn:hover{background:#f6f8fa}
  .pub-btn-primary{background:#1f6feb;color:#fff;border-color:#1f6feb}
  .pub-btn-primary:hover{filter:brightness(0.95)}
  .pub-btn-secondary{background:#fff;color:#24292f}
  .pub-count{margin-left:auto;font-size:.95rem;color:#555}
  .active-filters{display:flex;flex-wrap:wrap;gap:.5rem;margin:.25rem 0 1rem 0}
  .chip{display:inline-flex;align-items:center;gap:.35rem;border:1px solid #d0d7de;border-radius:999px;padding:.2rem .55rem;font-size:.85rem;background:#fff}
  .chip button{all:unset;cursor:pointer;display:inline-flex}
  .chip .fa{font-size:.8em;color:#555}

  .pub-list{counter-reset: none; padding-left: 1.2rem}
  .pub-item{margin:0 0 .9rem 0;padding:0 0 .9rem 0;border-bottom:1px dashed #e5e7eb}
  .pub-title{font-weight:600;line-height:1.35;margin:0}
  .pub-title a{text-decoration:none}
  .pub-title a:hover{text-decoration:underline}
  .pub-meta{color:#444;margin:.15rem 0 .45rem 0;font-size:.95rem}
  .subsets{display:flex;flex-wrap:wrap;gap:.35rem}
  .subset{font-size:.78rem;border:1px solid #e5e7eb;border-radius:.4rem;padding:.05rem .4rem;background:#fafbfc}
  .actions{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.35rem}
  .btn-chip{display:inline-flex;align-items:center;gap:.35rem;border:1px solid #d0d7de;border-radius:.5rem;padding:.25rem .45rem;font-size:.85rem;background:#fff;text-decoration:none}
  .btn-chip:hover{background:#f6f8fa}
  .btn-chip .fa, .btn-chip .ai{font-size:.9em}

  dialog{border:none;border-radius:12px;padding:1rem 1rem 1.2rem 1rem;max-width:680px;width:92%;box-shadow:0 10px 30px rgba(0,0,0,.15)}
  .dialog-form h3{margin:.3rem 0 .7rem 0}
  .filter-group{margin:.6rem 0}
  .filter-chips{display:flex;flex-wrap:wrap;gap:.45rem}
  .chip-toggle{display:inline-flex;align-items:center;gap:.35rem;border:1px solid #d0d7de;border-radius:999px;padding:.25rem .6rem;background:#fff;cursor:pointer}
  .chip-toggle input{accent-color:#1f6feb}
  .radio{display:flex;gap:.5rem;align-items:center;margin:.25rem 0}
  .dialog-actions{display:flex;gap:.5rem;justify-content:flex-end;margin-top:.8rem}

  .preview-tip{position:fixed;max-width:420px;background:#111;color:#fff;padding:.5rem .65rem;border-radius:.5rem;font-size:.9rem;line-height:1.35;box-shadow:0 6px 18px rgba(0,0,0,.25);z-index:99;pointer-events:none;opacity:0;transform:translateY(4px);transition:opacity .12s ease,transform .12s ease}
  .preview-tip[data-show="true"]{opacity:1;transform:translateY(0)}
  @media (prefers-color-scheme: dark){
    .pub-btn,.chip,.chip-toggle,.btn-chip{background:#0d1117;border-color:#30363d;color:#c9d1d9}
    .pub-btn:hover,.btn-chip:hover{background:#161b22}
    .pub-item{border-color:#30363d}
    .subset{background:#0d1117;border-color:#30363d}
    dialog{background:#0d1117;color:#c9d1d9}
    .preview-tip{background:#161b22}
  }
</style>

<!-- =========================
     DATA + RENDER LOGIC
     ========================= -->
{% raw %}
<script>
/** ======= Project URL mapping (put your actual project page links here) =======
 * Keyed by publication `id`. If missing, title falls back to Paper → Preprint → DOI.
 */
const PROJECT_URL_MAP = {
  // "apj2019-waldmeier": "/projects/waldmeier-effect/",   // example
  // "rnass2019-nsbh-periastron": "/projects/nsbh-periastron/",
  // "astropy2022-v5": "/projects/astropy-v5/",
  // "einsteinpy2020": "/projects/einsteinpy/",
  // "icrc2023-cbc-gradcam": "/projects/icrc2023-cbc-gradcam/",
  // "icrc2023-ccsn-dl": "/projects/icrc2023-ccsn/",
  // "icrc2023-nsbh-cnn": "/projects/icrc2023-nsbh-cnn/",
  // "icrc2023-cw-cnn": "/projects/icrc2023-cw-cnn/",
  // "thesis2023-ms-eccentric-nsbh-cnn": "/projects/masters-eccentric-nsbh-cnn/",
  // "thesis2020-bs-fibre-strain": "/projects/fibre-strain-sensor/"
};

/** ======= Publications data (add new items here; designed to scale) ======= */
const PUBS = [
  {
    id: "apj2019-waldmeier",
    year: 2019,
    date: "2019-12",
    type: "Journal",
    title: "Waldmeier Effect in Stellar Cycles",
    shortTitle: "Waldmeier Effect in Stellar Cycles",
    authors: ["S. Garg","B. B. Karak","R. Egeland","W. Soon","S. Baliunas"],
    venue: "The Astrophysical Journal",
    venueShort: "ApJ",
    volume: "886", issue: "2", pages: "132",
    doi: "10.3847/1538-4357/ab4a17",
    arxiv: "1909.12148",
    paperUrl: "https://doi.org/10.3847/1538-4357/ab4a17",
    preprintUrl: "https://arxiv.org/abs/1909.12148",
    codeUrl: null, dataUrl: null, url: "https://doi.org/10.3847/1538-4357/ab4a17",
    abstract: "",
    subsets: ["Stellar Physics","Solar Physics"]
  },
  {
    id: "rnass2019-nsbh-periastron",
    year: 2019,
    date: "2019-09",
    type: "Journal",
    title: "A Negligible Tidal Effect in a Periastron Precession in Neutron Star–Black Hole (Stellar Mass) Binaries",
    shortTitle: "Negligible Tidal Effect in NS–BH Periastron Precession",
    authors: ["S. Garg","M. Bagchi"],
    venue: "Research Notes of the American Astronomical Society",
    venueShort: "RNAAS",
    volume: "3", issue: "9", pages: "125",
    doi: "10.3847/2515-5172/ab3fa",
    paperUrl: "https://doi.org/10.3847/2515-5172/ab3fa",
    preprintUrl: null, codeUrl: null, dataUrl: null, url: "https://doi.org/10.3847/2515-5172/ab3fa",
    abstract: "",
    subsets: ["Other topics"]
  },
  {
    id: "astropy2022-v5",
    year: 2022,
    date: "2022-08",
    type: "Journal",
    collaboration: "Astropy Collaboration",
    title: "The Astropy Project: Community Growth and the v5.0 Core Package",
    shortTitle: "Astropy: v5.0 & Community Growth",
    authors: ["A. M. Price-Whelan","et al."],
    venue: "The Astrophysical Journal",
    venueShort: "ApJ",
    volume: "935", issue: "2", pages: "167",
    doi: "10.3847/1538-4357/ac7c74",
    arxiv: "2206.14220",
    paperUrl: "https://doi.org/10.3847/1538-4357/ac7c74",
    preprintUrl: "https://arxiv.org/abs/2206.14220",
    codeUrl: null, dataUrl: null, url: "https://doi.org/10.3847/1538-4357/ac7c74",
    abstract: "",
    subsets: ["Computational","Engineering"]
  },
  {
    id: "einsteinpy2020",
    year: 2020,
    date: "2020-05",
    type: "Preprint",
    title: "EinsteinPy: A Community Python Package for General Relativity",
    shortTitle: "EinsteinPy: Python for GR",
    authors: ["S. Bapat","et al."],
    venue: "arXiv e-prints",
    venueShort: "arXiv",
    volume: "", issue: "", pages: "",
    doi: null,
    arxiv: "2005.11288",
    paperUrl: null,
    preprintUrl: "https://arxiv.org/abs/2005.11288",
    codeUrl: null, dataUrl: null, url: "https://arxiv.org/abs/2005.11288",
    abstract: "",
    subsets: ["Computational","Engineering"]
  },
  {
    id: "icrc2023-cbc-gradcam",
    year: 2023,
    date: "2023-07",
    type: "Conference",
    title: "Deep Learning for Detecting Gravitational Waves from Compact Binary Coalescences and Its Visualization by Grad-CAM",
    shortTitle: "DL for GW from CBC + Grad‑CAM",
    authors: ["S. Sasaoka","Y. Hou","D. S. Dominguez","S. Garg","N. Koyama","Y. Sakai","Y. Omae","K. Somiya","H. Takahashi"],
    venue: "PoS (ICRC2023) 444:1498",
    venueShort: "PoS (ICRC2023)",
    doi: "10.22323/1.444.1498",
    paperUrl: "https://doi.org/10.22323/1.444.1498",
    preprintUrl: null, codeUrl: null, dataUrl: null, url: "https://doi.org/10.22323/1.444.1498",
    abstract: "",
    subsets: ["Machine Learning","Gravitational waves","Computational"]
  },
  {
    id: "icrc2023-ccsn-dl",
    year: 2023,
    date: "2023-07",
    type: "Conference",
    title: "Deep Learning Application for Detecting Gravitational Waves from Core‑Collapse Supernovae",
    shortTitle: "DL for GW from CCSN",
    authors: ["S. Sasaoka","Y. Hou","D. S. Dominguez","S. Garg","N. Koyama","Y. Sakai","Y. Omae","K. Somiya","H. Takahashi"],
    venue: "PoS (ICRC2023) 444:1499",
    venueShort: "PoS (ICRC2023)",
    doi: "10.22323/1.444.1499",
    paperUrl: "https://doi.org/10.22323/1.444.1499",
    preprintUrl: null, codeUrl: null, dataUrl: null, url: "https://doi.org/10.22323/1.444.1499",
    abstract: "",
    subsets: ["Machine Learning","Gravitational waves","Computational"]
  },
  {
    id: "icrc2023-nsbh-cnn",
    year: 2023,
    date: "2023-07",
    type: "Conference",
    title: "Comparison of Training Methods for Convolutional Neural Network Model for Gravitational‑Wave Detection from Neutron Star–Black Hole Binaries",
    shortTitle: "Training Methods for CNN on GW from NS–BH",
    authors: ["S. Garg","S. Sasaoka","D. S. Dominguez","Y. Hou","N. Koyama","K. Somiya","H. Takahashi","M. Ohashi"],
    venue: "PoS (ICRC2023) 444:1536",
    venueShort: "PoS (ICRC2023)",
    doi: "10.22323/1.444.1536",
    paperUrl: "https://doi.org/10.22323/1.444.1536",
    preprintUrl: null, codeUrl: null, dataUrl: null, url: "https://doi.org/10.22323/1.444.1536",
    abstract: "",
    subsets: ["Machine Learning","Gravitational waves","Computational"]
  },
  {
    id: "icrc2023-cw-cnn",
    year: 2023,
    date: "2023-07",
    type: "Conference",
    title: "Convolutional Neural Network for Continuous Gravitational Waves Detection",
    shortTitle: "CNN for Continuous GW Detection",
    authors: ["D. S. Dominguez","S. Sasaoka","S. Garg","Y. Hou","N. Koyama","K. Somiya","H. Takahashi"],
    venue: "PoS (ICRC2023) 444:1519",
    venueShort: "PoS (ICRC2023)",
    doi: "10.22323/1.444.1519",
    paperUrl: "https://doi.org/10.22323/1.444.1519",
    preprintUrl: null, codeUrl: null, dataUrl: null, url: "https://doi.org/10.22323/1.444.1519",
    abstract: "",
    subsets: ["Machine Learning","Gravitational waves","Computational"]
  },
  {
    id: "thesis2023-ms-eccentric-nsbh-cnn",
    year: 2023,
    date: "2023-07",
    type: "Thesis",
    title: "Convolutional Neural Network Model for Detection of Gravitational Waves from Eccentric Neutron Star–Black Hole Mergers",
    shortTitle: "CNN for GW from Eccentric NS–BH (M.S. thesis)",
    authors: ["S. Garg"],
    venue: "Master’s Thesis",
    venueShort: "M.S. Thesis",
    doi: null,
    paperUrl: null, preprintUrl: null, codeUrl: null, dataUrl: null, url: null,
    abstract: "",
    subsets: ["Machine Learning","Gravitational waves","Computational"]
  },
  {
    id: "thesis2020-bs-fibre-strain",
    year: 2020,
    date: "2020-06",
    type: "Thesis",
    title: "New Sensitivity Parameter for All‑Fibre Strain Sensor",
    shortTitle: "All‑Fibre Strain Sensor (B.S. thesis)",
    authors: ["S. Garg"],
    venue: "Bachelor Thesis",
    venueShort: "B.S. Thesis",
    doi: "10.13140/RG.2.2.31106.20166",
    paperUrl: "http://dx.doi.org/10.13140/RG.2.2.31106.20166",
    preprintUrl: "http://dx.doi.org/10.13140/RG.2.2.31106.20166",
    codeUrl: null, dataUrl: null, url: "http://dx.doi.org/10.13140/RG.2.2.31106.20166",
    abstract: "",
    subsets: ["Engineering"]
  }
];

/** ======= Rendering & Behavior ======= */
const els = {
  list: document.getElementById('pubList'),
  count: document.getElementById('countLabel'),
  tip: document.getElementById('previewTip'),
  filterDlg: document.getElementById('filterDialog'),
  sortDlg: document.getElementById('sortDialog'),
  filterTypes: document.getElementById('filterTypes'),
  filterSubsets: document.getElementById('filterSubsets'),
  activeFilters: document.getElementById('activeFilters'),
  btnFilter: document.getElementById('btnFilter'),
  btnSort: document.getElementById('btnSort'),
  btnApplyFilters: document.getElementById('btnApplyFilters'),
  btnResetFilters: document.getElementById('btnResetFilters'),
  btnApplySort: document.getElementById('btnApplySort'),
};

const state = {
  sortMode: 'year-desc',
  types: new Set(),     // empty = all
  subsets: new Set(),   // empty = all
};

function uniqueSorted(arr){ return [...new Set(arr)].sort((a,b)=>a.localeCompare(b,'en',{sensitivity:'base'})); }

function initFilters(){
  const allTypes = uniqueSorted(PUBS.map(p=>p.type));
  const allSubsets = uniqueSorted(PUBS.flatMap(p=>p.subsets||[]));

  // Build type chips
  els.filterTypes.innerHTML = allTypes.map(t => `
    <label class="chip-toggle"><input type="checkbox" value="${t}"> ${t}</label>
  `).join('');

  // Build subset chips
  els.filterSubsets.innerHTML = allSubsets.map(s => `
    <label class="chip-toggle"><input type="checkbox" value="${s}"> ${s}</label>
  `).join('');
}

function authorShort(list){
  if(!list || !list.length) return '';
  if(list.length<=3) return list.join(', ');
  return `${list[0]} et al.`;
}

function firstAuthorKey(p){ return (p.authors && p.authors[0] || '').toLowerCase(); }

function sortPubs(list){
  const m = state.sortMode;
  return [...list].sort((a,b)=>{
    if(m==='year-desc') return (b.year-a.year)||a.title.localeCompare(b.title);
    if(m==='year-asc')  return (a.year-b.year)||a.title.localeCompare(b.title);
    if(m==='title-asc') return a.shortTitle.localeCompare(b.shortTitle,'en',{sensitivity:'base'});
    if(m==='title-desc')return b.shortTitle.localeCompare(a.shortTitle,'en',{sensitivity:'base'});
    if(m==='first-asc') return firstAuthorKey(a).localeCompare(firstAuthorKey(b));
    if(m==='first-desc')return firstAuthorKey(b).localeCompare(firstAuthorKey(a));
    return 0;
  });
}

function passesFilters(p){
  const tOK = state.types.size ? state.types.has(p.type) : true;
  const sOK = state.subsets.size ? (p.subsets||[]).some(s=>state.subsets.has(s)) : true;
  return tOK && sOK;
}

function linkForTitle(p){
  return PROJECT_URL_MAP[p.id] || p.paperUrl || p.preprintUrl || (p.doi ? `https://doi.org/${p.doi}` : (p.url || '#'));
}

function button(label, iconClass, url){
  if(!url) return '';
  const safe = url.replace(/"/g,'%22');
  return `<a class="btn-chip" href="${safe}" target="_blank" rel="noopener">
    <i class="${iconClass}" aria-hidden="true"></i> ${label}
  </a>`;
}

function render(){
  const filtered = PUBS.filter(p=>passesFilters(p));
  const sorted = sortPubs(filtered);

  // reverse-numbering: set start to count
  els.list.setAttribute('start', String(sorted.length));
  els.list.innerHTML = sorted.map(p=>{
    const titleUrl = linkForTitle(p);
    const abstract = (p.abstract||'').trim();
    const meta = `${authorShort(p.authors)} — ${p.venueShort || p.venue || ''}${p.year ? ' ('+p.year+')' : ''}${p.type ? ' • '+p.type : ''}`;
    const subsetChips = (p.subsets||[]).map(s=>`<span class="subset">${s}</span>`).join('');
    const actions = [
      button('Paper','fa fa-file-pdf',p.paperUrl),
      button('Preprint','fa fa-edit',p.preprintUrl),
      button('Code','fa fa-code',p.codeUrl),
      button('Data','fa fa-database',p.dataUrl),
      button('DOI','ai ai-doi', p.doi ? `https://doi.org/${p.doi}` : null),
      button('URL','fa fa-external-link-alt',p.url && (!p.paperUrl && !p.preprintUrl) ? p.url : null)
    ].join('');

    return `
      <li class="pub-item">
        <p class="pub-title">
          <a href="${titleUrl}" class="title-link" data-abstract="${abstract.replace(/"/g,'&quot;')}">
            ${p.shortTitle || p.title}
          </a>
        </p>
        <div class="pub-meta">${meta}</div>
        <div class="subsets">${subsetChips}</div>
        <div class="actions">${actions}</div>
      </li>
    `;
  }).join('');

  els.count.textContent = `Showing ${sorted.length} of ${PUBS.length}`;
  renderActiveFilters();
  wireHoverPreviews();
}

function renderActiveFilters(){
  const chips = [];
  state.types.forEach(t=>{
    chips.push(`<span class="chip">Type: ${t}<button aria-label="Remove ${t}" data-x-type="${t}"><i class="fa fa-times"></i></button></span>`);
  });
  state.subsets.forEach(s=>{
    chips.push(`<span class="chip">Topic: ${s}<button aria-label="Remove ${s}" data-x-subset="${s}"><i class="fa fa-times"></i></button></span>`);
  });
  els.activeFilters.innerHTML = chips.join('');
  els.activeFilters.querySelectorAll('button[data-x-type]').forEach(b=>{
    b.addEventListener('click',()=>{ state.types.delete(b.dataset.xType); syncDialogChecks(); render(); });
  });
  els.activeFilters.querySelectorAll('button[data-x-subset]').forEach(b=>{
    b.addEventListener('click',()=>{ state.subsets.delete(b.dataset.xSubset); syncDialogChecks(); render(); });
  });
}

function syncDialogChecks(){
  // Types
  els.filterTypes.querySelectorAll('input[type=checkbox]').forEach(cb=>{
    cb.checked = state.types.has(cb.value);
  });
  // Subsets
  els.filterSubsets.querySelectorAll('input[type=checkbox]').forEach(cb=>{
    cb.checked = state.subsets.has(cb.value);
  });
  // Sort radios
  els.sortDlg.querySelectorAll('input[name=sortMode]').forEach(r=>{
    r.checked = (r.value === state.sortMode);
  });
}

function applyFiltersFromDialog(){
  const newTypes = new Set();
  els.filterTypes.querySelectorAll('input[type=checkbox]:checked').forEach(cb=>newTypes.add(cb.value));
  const newSubs = new Set();
  els.filterSubsets.querySelectorAll('input[type=checkbox]:checked').forEach(cb=>newSubs.add(cb.value));
  state.types = newTypes;
  state.subsets = newSubs;
}

function applySortFromDialog(){
  const sel = els.sortDlg.querySelector('input[name=sortMode]:checked');
  if(sel) state.sortMode = sel.value;
}

function wireHoverPreviews(){
  document.querySelectorAll('.title-link').forEach(a=>{
    a.addEventListener('mouseenter', e=>{
      const txt = a.dataset.abstract || '';
      if(!txt) return; // only show when you add abstracts
      showTip(txt, e.clientX, e.clientY);
    });
    a.addEventListener('mousemove', e=>{
      if(els.tip.getAttribute('data-show') === 'true'){
        positionTip(e.clientX, e.clientY);
      }
    });
    a.addEventListener('mouseleave', hideTip);
  });
}

function showTip(text, x, y){
  els.tip.textContent = text;
  els.tip.setAttribute('data-show','true');
  els.tip.setAttribute('aria-hidden','false');
  positionTip(x,y);
}
function positionTip(x,y){
  const pad = 12;
  const w = els.tip.offsetWidth, h = els.tip.offsetHeight;
  let left = x + pad, top = y + pad;
  if(left + w > window.innerWidth - 8) left = x - w - pad;
  if(top + h > window.innerHeight - 8) top = y - h - pad;
  els.tip.style.left = left + 'px';
  els.tip.style.top = top + 'px';
}
function hideTip(){
  els.tip.removeAttribute('data-show');
  els.tip.setAttribute('aria-hidden','true');
}

function supportsDialog(){ return typeof HTMLDialogElement !== 'undefined'; }

function openDialog(dlg){
  if(supportsDialog()) dlg.showModal();
  else { dlg.open = true; dlg.style.display = 'block'; }
}
function closeDialog(dlg){
  if(supportsDialog()) dlg.close();
  else { dlg.open = false; dlg.style.display = 'none'; }
}

function initUI(){
  initFilters();
  syncDialogChecks();
  render();

  els.btnFilter.addEventListener('click', ()=>{ syncDialogChecks(); openDialog(els.filterDlg); });
  els.btnSort.addEventListener('click', ()=>{ syncDialogChecks(); openDialog(els.sortDlg); });

  els.btnApplyFilters?.closest('form')?.addEventListener('submit', (e)=>{
    e.preventDefault();
    applyFiltersFromDialog();
    closeDialog(els.filterDlg);
    render();
  });
  els.btnResetFilters.addEventListener('click', ()=>{
    state.types.clear(); state.subsets.clear();
    syncDialogChecks(); render();
  });

  els.btnApplySort?.closest('form')?.addEventListener('submit', (e)=>{
    e.preventDefault();
    applySortFromDialog();
    closeDialog(els.sortDlg);
    render();
  });
}

document.addEventListener('DOMContentLoaded', initUI);
</script>
{% endraw %}

---

<details>
<summary><strong>Legacy content (unchanged)</strong></summary>

## Scientific Articles

<!-- #### Journal Articles (Preprint) -->

### Journal Articles (Published)


S. Garg, B. B. Karak, R. Egeland, W. Soon, and S. Baliunas. Waldmeier Eﬀect in Stellar Cycles. ApJ, 886(2):132, Dec 2019, 1909.12148.
<span class="__dimensions_badge_embed__" data-doi="10.3847/1538-4357/ab4a17" data-hide-zero-citations="true" data-style="small_rectangle" style="white-space:nowrap;"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
<br/>
<i class="fa fa-file-pdf">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">Paper</a>
&nbsp;•&nbsp;
<i class="fa fa-edit">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">Preprint</a>
&nbsp;•&nbsp;
<i class="fa fa-code">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">Code</a>
&nbsp;•&nbsp;
<i class="fa fa-database">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">Data</a>
&nbsp;•&nbsp;
<i class="ai ai-doi">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">DOI</a>
&nbsp;•&nbsp;
<i class="fa fa-external-link-alt">&nbsp;</i>
<a href="https://doi.org/10.3847/1538-4357/ab4a17">URL</a>

- S. Garg and M. Bagchi. A Negligible Tidal Eﬀect in a Periastron Precession in Neutron Star–Black Hole (Stellar Mass) Binaries. Research Notes of the American Astronomical Society, 3(9):125, Sep 2019. [URL](https://doi.org/10.3847/2515-5172/ab3fa).

### In Collaboration

- A. M. Price-Whelan, others, Astropy Collaboration, and Astropy Project Contributors. The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package. ApJ, 935(2):167, Aug. 2022, 2206.14220. [URL](https://doi.org/10.3847/1538-4357/ac7c74).
- S. Bapat et al. EinsteinPy: A Community Python Package for General Relativity. arXiv e-prints, May 2020, 2005.11288. [URL](https://arxiv.org/abs/2005.11288).

### Conference Papers

- S. Sasaoka, Y. Hou, D. S. Dominguez, S. Garg, N. Koyama, Y. Sakai, Y. Omae, K. Somiya, and H. Takahashi. Deep Learning for Detecting Gravitational Waves from Compact Binary Coalescences and Its Visualization by Grad-CAM. In Proceedings of 38th International Cosmic Ray Conference — PoS(ICRC2023), volume 444, page 1498, 2023.
&nbsp;
<i class="ai ai-doi"></i>
<a href="https://doi.org/10.22323/1.444.1498">DOI</a>

- S. Sasaoka, Y. Hou, D. S. Dominguez, S. Garg, N. Koyama, Y. Sakai, Y. Omae, K. Somiya, and H. Takahashi. Deep Learning Application for Detecting Gravitational Waves from Core-Collapse Supernovae. In Proceedings of 38th International Cosmic Ray Conference — PoS(ICRC2023), volume 444, page 1499, 2023. [URL](https://doi.org/10.22323/1.444.1499).
- S. Garg, S. Sasaoka, D. S. Dominguez, Y. Hou, N. Koyama, K. Somiya, H. Takahashi, and M. Ohashi. Comparison of training methods for Convolutional Neural Network model for Gravitational-Wave detection from Neutron Star−Black Hole Binaries. In Proceedings of 38th International Cosmic Ray Conference — PoS(ICRC2023), volume 444, page 1536, 2023. [URL](https://doi.org/10.22323/1.444.1536).
- D. S. Dominguez, S. Sasaoka, S. Garg, Y. Hou, N. Koyama, K. Somiya, and H. Takahashi. Convolutional neural network for continuous gravitational waves detection. In Proceedings of 38th International Cosmic Ray Conference — PoS(ICRC2023), volume 444, page 1519, 2023. [URL](https://doi.org/10.22323/1.444.1519).

## Graduation Theses

- Convolutional Neural Network model for Detection of Gravitational-Waves from Eccentric Neutron Star - Black Hole mergers. July 2023. Masters Thesis.

- New Sensitivity Parameter for all-Fibre Strain Sensor. June 2020. Bachelor Thesis.
<br/>
<i class="fa fa-edit">&nbsp;</i>
<a href="http://dx.doi.org/10.13140/RG.2.2.31106.20166">Preprint</a>
&nbsp;•&nbsp;
<i class="ai ai-doi">&nbsp;</i>
<a href="http://dx.doi.org/10.13140/RG.2.2.31106.20166">DOI</a>

<!--
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
-->
</details>
