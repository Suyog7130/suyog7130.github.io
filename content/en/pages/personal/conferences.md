---
title: "Conferences and Workshops"
date: 2025-03-03T21:10:16+09:00
draft: false
hidetags: true
---

<!-- TODO: Maybe I can have an auto-sorted listing based on the date, into past, this-year, future. But the present looks makes it easy for me to see the grouping even in the markdown list! -->

List of most of the Conferences and Workshops I have undertaken or am going to :


<!-- CSS style blocks -->

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
.conf-section{ 
	margin:1rem 0; 
	border:1px solid var(--conf-border,#d0d7de); 
	border-radius:14px; 
	padding:.55rem .75rem .75rem; 
	background:var(--conf-bg,#fff); 
} 

.conf-section > summary{ 
	cursor:pointer; 
	font-weight:800; font-size:1.05rem; 
	margin:.15rem 0 0.7rem; 
} 

.conf-section > summary::marker{ 
	color:var(--conf-muted,#57606a); 
}

.conf-list{
  display:grid;
  gap:.85rem;
  margin:1rem 0;
}

.conf-card{
  border:1px solid var(--conf-border,#d0d7de);
  border-radius:14px;
  padding:.85rem 1rem;
  background:var(--conf-bg,#fff);
  box-shadow:0 2px 8px rgba(0,0,0,.06);
}

.conf-title{
  font-weight:700;
  font-size:1.03rem;
  margin-bottom:.35rem;
}

.conf-title a{
  text-decoration:none;
}

.conf-title a:hover{
  text-decoration:underline;
}

.conf-tags{
  display:inline-flex;
  flex-wrap:wrap;
  gap:.3rem;
  margin-left:.35rem;
  vertical-align:middle;
}

.conf-tag{
  display:inline-flex;
  align-items:center;
  border-radius:999px;
  padding:.12rem .48rem;
  font-size:.78rem;
  font-weight:700;
  border:1px solid currentColor;
  line-height:1.25;
}

.conf-tag.invited,
.conf-tag.talk,
.conf-tag.poster{ color:#238636; }

.conf-tag.registered,
.conf-tag.maybe{ color:#2e8b57; }

.conf-tag.no,
.conf-tag.missed{ color:#cf222e; }

.conf-tag.notreg{ color:#e5532d; }

.conf-meta{
  display:flex;
  flex-wrap:wrap;
  gap:.45rem .7rem;
  margin-top:.45rem;
  color:var(--conf-muted,#57606a);
  font-size:.93rem;
}

.conf-meta span{
  display:inline-flex;
  align-items:center;
  gap:.28rem;
}

.conf-meta .fa{
  opacity:.78;
}

.conf-note{
  margin-top:.4rem;
  color:var(--conf-muted,#57606a);
  font-size:.9rem;
  font-style:italic;
}

@media (prefers-color-scheme: dark){
  #confList{
    --conf-bg:#161b22;
    --conf-border:#30363d;
    --conf-muted:#c9d1d9;
  }

  .conf-card{
    box-shadow:0 2px 10px rgba(0,0,0,.32);
  }

  .conf-tag{
    color:inherit !important;
    opacity:.95;
  }
}
</style>


<!-- List section headers -->

<details class="conf-section" open> 
	<summary>Next year or later</summary> 
	<div id="confFuture" class="conf-list"></div> 
</details>

<details class="conf-section" open> 
	<summary>This year</summary> 
	<div id="confPresent" class="conf-list"></div> 
</details> 

<details class="conf-section"> 
	<summary>Past conferences</summary> 
	<div id="confPast" class="conf-list"></div>
 </details>
 

<!-- The actual data for the conference list -->

<script type="text/plain" id="confData">
# group | title | url | tags | date | institution | location | options

# -- future conferences / workshops --#

future | xx, xx | | | | | |


# -- present conferences / workshops --#

present | NeurIPS 2026 | https://neurips.cc/ | submitting?:maybe; | 2026年12月06-08 | | Sydney, Australia |

present | Asian Conference in Machine Learning (ACML 2026) | https://www.acml-conf.org/2026/ | Submitted:registered; going?:maybe; Poster?:poster | 2026年12月01-04 | | Melbourne, Australia |

present | KAGRA F2F and KIW, Shanghai | | | 2026年12月15-17,18-19 | ShanghaiTech | Shanghai, China |

present | LIGO-Virgo-KAGRA Meeting Fall 2026 | https://web.iucaa.in/ws/~lvk2026pune/index.html | Registered:registered | 2026年09月21–25 | LIGO India | IUCAA, Pune, India |

present | KAGRA F2F, Osaka | | | 2026年08月26-28 | OMU | Osaka, Japan |

present | A3net-III | https://cd3.ipmu.jp/a3n_Aug2026/ | Registered:registered; Going:maybe; Funded:yes | 2026年08月24–28 | National Taiwan University | Taipei, Taiwan |

present | RIKEN AI & Maths Symposium | https://pri.riken.jp/symposium/ai4math.html | Registered:registered; Going:maybe; Poster:poster | 2026年08月18-12 | RIKEN Tokyo Liaison office | Tokyo, Japan |

present | IAIFI Summer Workshop | https://iaifi.org/summer-workshop | Registered:registered; cannot??:maybe | 2026年08月10–14 | MIT | Boston, MA, USA |

present | ICGAC16 | https://tianqin.sysu.edu.cn/en/ICGAC16-home | Invited:invited; Registered:registered; Going?:maybe; Talk:talk | 2026年08月10–14 | SYSU | Shenzhen, China |

present | MLPhysics conference | https://mlphys.scphys.kyoto-u.ac.jp/ic_mlphys2026/ | Registered:registered; going?:maybe; Poster:poster | 2026年07月13–15 | KyotoU | Naha, Okinawa, JAPAN |

present | Cool Stars 23 | https://coolstars23.github.io/index.html | Registered:registered; Going → NA:no; Poster:poster | 2026年06月15–19 | | TOC Ariake, Tokyo | note=

present | ICML 2026 | https://icml.cc/ | not-registered:notreg; missed:missed | 2026年07月06–11 | | Seoul, Korea | strike


# -- past conferences / workshops --#

past | APRIM 2026 | https://aprim2026.org/ | Registered:registered; Going:maybe; Talk:talk | 2026年05月04–09 | HKU | HongKong | note=had a fun time

past | KAGRA I'nt Workshop 14 | https://indico.ego-gw.it/event/1040/ | Not-going:no | 2026年05月15–16 | | Perugia, Italy | strike

past | LIGO-Virgo-KAGRA Meeting Spring 2026 | | | 2026年03月 | VIRGO | Cascina, Italy | strike

past | 2nd I'nt Conference on Physics of the Two Infinities | https://indico.in2p3.fr/event/35255/ | website:maybe | 2025年11月17-21日 | UTokyo | Tokyo, Japan | strike

past | LIGO-Virgo-KAGRA Meeting Fall 2025 | | | 2025年09月 | Colorado State University | Fort Collins, CO, USA | strike; note=Most likely not attending!

past | AstroAI Asian Network (A^3 Net) | https://cd3.ipmu.jp/a3n/ | website:maybe | 2025年08月18-22日 | KIAS | Seoul, Korea | strike

past | ICRC 2025 - The Astroparticle Physics Conference | https://indico.cern.ch/event/1258933/overview | website:maybe | 2025年07月15-24日 | CICG | Geneva, Switzerland |

past | GR24 and Amaldi16 | https://iop.eventsair.com/gr24-amaldi16/ | website:maybe | 2025年07月14-18日 | Scottish Exhibition Center | Glasgow, UK | strike

past | 12th KAGRA International Workshop | https://kiw12.casconf.cn/page/1878817789607809024 | website:maybe | 2025年05月26-27日 | Shanghai Astronomical Observatory | Shangai, China |

past | From Quarks to Neutron Stars: Insights from kHz gravitational waves | https://indico2.riken.jp/event/5141/ | website:maybe | 2025年04月23-24日 | UTokyo | Tokyo, Japan |

past | LIGO-Virgo-KAGRA Meeting Spring 2025 | | | 2025年03月24-28日 | OzGrav, Monash University | Melbourne, Australia |

past | LIGO-Virgo-KAGRA Meeting Fall 2024 | | webpage:maybe; poster:poster | 2024年09月 | University | Barcelona, Spain |

past | LIGO-Virgo-KAGRA Meeting Spring 2024 | | webpage:maybe; poster:poster | 2024年03月 | Louisiana State University | Baton Rouge, LA, USA |

past | LIGO-Virgo-KAGRA Meeting Fall 2023 | | webpage:maybe; poster:poster | 2023年09月 | RESCEU, UTokyo | Toyama, Japan |

</script>


<!-- Function to render the lists -->

<script>
(function(){
  const dataEl = document.getElementById("confData");
  
  const lists = { 
	  future: document.getElementById("confFuture"), 
	  present: document.getElementById("confPresent"), 
	  past: document.getElementById("confPast") 
  };
  
	const hasAnyList = Object.values(lists).some(Boolean); if(!dataEl || !hasAnyList) return;

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

  function parseTags(raw){
    return String(raw || "")
      .split(";")
      .map(x => x.trim())
      .filter(Boolean)
      .map(t => {
        const parts = t.split(":");
        return {
          label: (parts[0] || "").trim(),
          cls: (parts[1] || "maybe").trim().toLowerCase()
        };
      });
  }

function render(){
  const targetLists = (typeof lists !== "undefined") ? lists : {
    future: document.getElementById("confFuture"),
    present: document.getElementById("confPresent"),
    past: document.getElementById("confPast")
  };

  const rows = dataEl.textContent
    .split(/\r?\n/)
    .map(x => x.trim())
    .filter(x => x && !x.startsWith("#"));

  const buckets = {
    future: [],
    present: [],
    past: []
  };

  function normalGroup(raw){
    const g = String(raw || "future").trim().toLowerCase();
    if(["future","upcoming","next","later","next-year","next year"].includes(g)) return "future";
    if(["present","active","current","now"].includes(g)) return "present";
    if(["past","previous","old"].includes(g)) return "past";
    return "future";
  }

  function optionHas(options, key){
    return String(options || "").toLowerCase().split(";").map(x => x.trim()).includes(key);
  }

  function optionValue(options, key){
    const found = String(options || "")
      .split(";")
      .map(x => x.trim())
      .find(x => x.toLowerCase().startsWith(key.toLowerCase() + "="));
    return found ? found.slice(key.length + 1).trim() : "";
  }

  rows.forEach(line => {
    const [groupRaw, title, url, tagsRaw, date, institution, location, options] = splitRow(line);
    const bucket = normalGroup(groupRaw);

    const strike = optionHas(options, "strike");
    const note = optionValue(options, "note");

    const titleText = strike ? `<s>${esc(title)}</s>` : esc(title);
    const titleHTML = url
      ? `<a href="${esc(url)}" target="_blank" rel="noopener">${titleText}</a>`
      : titleText;

    const tags = parseTags(tagsRaw).map(t =>
      `<span class="conf-tag ${esc(t.cls)}">${esc(t.label)}</span>`
    ).join("");

    const meta = [
      date ? `<span><i class="fa fa-calendar-alt"></i> ${esc(date)}</span>` : "",
      institution ? `<span><i class="fa fa-university"></i> ${esc(institution)}</span>` : "",
      location ? `<span><i class="fa fa-map-marked-alt"></i> ${esc(location)}</span>` : ""
    ].filter(Boolean).join("");

    const noteHTML = note
      ? `<div class="conf-note"><i class="fa fa-note-sticky"></i> ${esc(note)}</div>`
      : "";

    buckets[bucket].push(`
      <div class="conf-card">
        <div class="conf-title">
          ${titleHTML}
          ${tags ? `<span class="conf-tags">${tags}</span>` : ""}
        </div>
        ${meta ? `<div class="conf-meta">${meta}</div>` : ""}
        ${noteHTML}
      </div>
    `);
  });

  Object.entries(targetLists).forEach(([key, el]) => {
    if(!el) return;

    el.innerHTML = buckets[key].join("");

    const details = el.closest("details");
    if(details){
      details.style.display = buckets[key].length ? "" : "none";

      const summary = details.querySelector("summary");
      if(summary){
        if(!summary.dataset.baseTitle) summary.dataset.baseTitle = summary.textContent.trim();
        summary.textContent = `${summary.dataset.baseTitle} (${buckets[key].length})`;
	      }
	    }
	  });
	}

  render();
})();
</script>





<!-- Old Style Lists -->


<!--<details>
<summary>Next Year or Later</summary>

</details>

- NeurIPS, xx

- [18th Asian Conference in Machine Learning](https://www.acml-conf.org/2026/)
<span style="font-weight: bold; color: seagreen;">[conf-dealine:2026/06/20]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年12月01-04 &nbsp;•&nbsp;
<i class="fa fa-university"></i> ?? 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> ??

- KAGRA F2F and KIW, Shanghai
<br/><i class="fa fa-calendar-alt"></i> 2026年12月15-17,18-19 &nbsp;•&nbsp;
<i class="fa fa-university"></i> ShanghaiTech 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Shanghai, China

- [LIGO-Virgo-KAGRA Meeting Fall 2026](https://web.iucaa.in/ws/~lvk2026pune/index.html)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年09月21–25 &nbsp;•&nbsp;
<i class="fa fa-university"></i> LIGO India &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> IUCAA, Pune, India

- KAGRA F2F, Osaka
<br/><i class="fa fa-calendar-alt"></i> 2026年08月26-28 &nbsp;•&nbsp;
<i class="fa fa-university"></i> OMU 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Osaka, Japan

- [A3net](https://cd3.ipmu.jp/a3n_Aug2026/)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: green;">[Going]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年08月24–28 &nbsp;•&nbsp;
<i class="fa fa-university"></i> National Taiwan University 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Taipei, Taiwan

- [RIKEN AI & Maths Symposium](https://pri.riken.jp/symposium/ai4math.html)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: seagreen;">[Going]</span>
<span style="font-weight: bold; color: green;">[Poster]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年08月18-12 &nbsp;•&nbsp;
<i class="fa fa-university"></i> RIKEN Tokyo Liaison office 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Tokyo, Japan

- [IAIFI Summer Workshop](https://iaifi.org/summer-workshop)
<span style="font-weight: bold; color: tomato;">[Not-registered]</span>
<span style="font-weight: bold; color: tomato;">[cannot??]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年08月10–14 &nbsp;•&nbsp;
<i class="fa fa-university"></i> MIT 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Boston, MA, USA

- [ICGAC16](https://tianqin.sysu.edu.cn/en/ICGAC16-home)
<span style="font-weight: bold; color: green;">[Invited]</span>
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: seagreen;">[Going?]</span>
<span style="font-weight: bold; color: green;">[Talk]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年08月10–14 &nbsp;•&nbsp;
<i class="fa fa-university"></i> SYSU 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Shenzhen, China

- [MLPhysics conference](https://mlphys.scphys.kyoto-u.ac.jp/ic_mlphys2026/)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: green;">[going?]</span>
<span style="font-weight: bold; color: green;">[Poster]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年07月13–15 &nbsp;•&nbsp;
<i class="fa fa-university"></i> KyotoU 
&nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Naha, Okinawa, JAPAN

- [Cool Stars 23](https://coolstars23.github.io/index.html)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: red;">[Going->NA]</span>
<span style="font-weight: bold; color: green;">[Poster]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年06月15–19 &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> TOC Ariake, Tokyo

- [<s>ICML 2026</s>](https://icml.cc/)
<span style="font-weight: bold; color: tomato;">[not-registered]</span><span style="font-weight: bold; color: red;">[missed]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年07月06–11 &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Seoul, Korea

<details>
<summary>Past</summary>

- [APRIM 2026](https://aprim2026.org/)
<span style="font-weight: bold; color: seagreen;">[Registered]</span>
<span style="font-weight: bold; color: green;">[Going]</span>
<span style="font-weight: bold; color: green;">[Talk]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年05月04–09 &nbsp;•&nbsp;
<i class="fa fa-university"></i> HKU &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> HongKong

- [<s>KAGRA I'nt Workshop 14</s>](https://indico.ego-gw.it/event/1040/)
<span style="font-weight: bold; color: red;">[Not-going]</span>
<br/><i class="fa fa-calendar-alt"></i> 2026年05月15–16 &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Perugia, Italy


- <s>LIGO-Virgo-KAGRA Meeting Spring 2026</s>
<br/><i class="fa fa-calendar-alt"></i> 2026年03月 &nbsp;•&nbsp;
<i class="fa fa-university"></i> VIRGO &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Cascina, Italy

- <s>2nd I'nt Conference on Physics of the Two Infinities</s>
[[website](https://indico.in2p3.fr/event/35255/)]
<br/><i class="fa fa-calendar-alt"></i> 2025年11月17-21日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> UTokyo &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Tokyo, Japan

- <s>LIGO-Virgo-KAGRA Meeting Fall 2025</s>
<br/><i class="fa fa-calendar-alt"></i> 2025年09月 &nbsp;•&nbsp;
<i class="fa fa-university"></i> Colorado State University &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Fort Collins, CO, USA <br/> *Note: Most likely not attending!*

- <s>AstroAI Asian Network (A$^3$ Net)</s>
[[website](https://cd3.ipmu.jp/a3n/)]
<br/><i class="fa fa-calendar-alt"></i> 2025年08月18-22日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> KIAS &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Seoul, Korea

- ICRC 2025 - The Astroparticle Physics Conference
[[website](https://indico.cern.ch/event/1258933/overview)]
<br/><i class="fa fa-calendar-alt"></i> 2025年07月15-24日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> CICG &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Geneva, Switzerland

- GR24 and Amaldi16
[[website](https://iop.eventsair.com/gr24-amaldi16/)]
<br/><i class="fa fa-calendar-alt"></i> 2025年07月14-18日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> Scottish Exhibition Center &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Glasgow, UK

- 12th KAGRA International Workshop
[[website](https://kiw12.casconf.cn/page/1878817789607809024)]
<br/><i class="fa fa-calendar-alt"></i> 2025年05月26-27日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> Shanghai Astronomical Observatory &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Shangai, China


- From Quarks to Neutron Stars: Insights from kHz gravitational waves
[[website](https://indico2.riken.jp/event/5141/)]
<br/><i class="fa fa-calendar-alt"></i> 2025年04月23-24日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> UTokyo &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Tokyo, Japan


- LIGO-Virgo-KAGRA Meeting Spring 2025
<br/><i class="fa fa-calendar-alt"></i> 2025年03月24-28日 &nbsp;•&nbsp;
<i class="fa fa-university"></i> OzGrav, Monash University &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Melbourne, Australia

- LIGO-Virgo-KAGRA Meeting Fall 2024
[webpage, poster]
<br/><i class="fa fa-calendar-alt"></i> 2024年09月 &nbsp;•&nbsp;
<i class="fa fa-university"></i> University &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Barcelona, Spain

- LIGO-Virgo-KAGRA Meeting Spring 2024
[webpage, poster]
<br/><i class="fa fa-calendar-alt"></i> 2024年03月 &nbsp;•&nbsp;
<i class="fa fa-university"></i> Louisiana State University &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Baton Rouge, LA, USA

- LIGO-Virgo-KAGRA Meeting Fall 2023
[webpage, poster]
<br/><i class="fa fa-calendar-alt"></i> 2023年09月 &nbsp;•&nbsp;
<i class="fa fa-university"></i> RESCEU, UTokyo &nbsp;•&nbsp;
<i class="fa fa-map-marked-alt"></i> Toyama, Japan

</details>
-->