---
permalink: /
title: "About"
math: true
ShowAuthor: false
ShowToc: false
ShowReadingTime: true
hideTags: true
redirect_from: 
  - /about/
  - /about.html
---

![](/images/suyog-ueno-dslr-pic-by-vivi-cropped.jpeg)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Tangerine&color=&background=8A8A8A00&size=50&duration=5500&width=600&height=75&center=true&repeat=true&lines=Heya!+This+is+Suyog!;I'm+an+aspiring+Astrophysicist!;I+love+Books!;I'm+an+avid+Traveller!)](https://git.io/typing-svg)

<!--$$f(x) = \alpha$$-->

<h3> Here's some fun facts about me: </h3>

&nbsp;&nbsp;👋&nbsp;&nbsp; My name is Suyog and I am a scientist!
	
&nbsp;&nbsp;👀&nbsp;&nbsp; I love Astrophysics, Books, Places and People.
	
&nbsp;&nbsp;🌱&nbsp;&nbsp; My research is on using Machine Learning for Gravitational-Wave Detections.
	
&nbsp;&nbsp;💻&nbsp;&nbsp; I have experience in Data Analysis, Numerical Solvers and Deep Neural Networks.
	
&nbsp;&nbsp;💞️&nbsp;&nbsp; It would be awesome to collaborate on a computational project together :)
	
&nbsp;&nbsp;📫&nbsp;&nbsp; Catch up about my work on this website ~


<!-- More Details -->


<div style="object-position:center; text-align:center">
<details>
	<summary>
	<p style="text-align:center; font-family:mistral; font-size:24px">
	  A Bit More Detail
	</p>
	</summary>
Heya, this is Suyog. Currently, I am a second year PhD candidate at the Department of Physics, the University of Tokyo (UTokyo). I am a member of the Research Center for Early Universe (RESCEU) and primarily focus on detection and data analysis methods for Gravitional-Waves. At UTokyo, I am supported by the MEXT Scholarship and the ASPIRE-GW program. 

My research and other interests are broad and indiscriminate. And so are my hobbies and experiences, ranging from dabbling in cutting-edge Machine Learning research to masquerading as a wannabe writer. You can find more about these on this website.

Prior to RESCEU, I was a master's student at the Intitute of Cosmic Ray Research in Kashiwanoha. My undergraduate degree is in Mechanical Engineering with specialization in Design and Manufacturing, from IIITDM Kancheerpuram, Chennai. I was born and raised in a quaint little town called Mandla in the heart of India, amidst a pleasant life full of stories, warm summers, trees, and books.
</br></br>
</details>
</div>




<!-- Wobble Text -->
<style type="text/css" media="screen">
.wobble {
  font-size: 20px;
  color: #A52A2A;
  font-weight: bold;
  display: inline-block;
}

@keyframes wobb {
  0%, 100%   {transform: translateY(0px)}
  25%  {transform: translateY(-3px)}
  75%  {transform: translateY(3px)}
}

.wobble span {
  animation-name: wobb;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
  animation-duration: 400ms;
  display: inline-block;
  transform: translateY(0px);
}

.spacer {
  height: 100px;
}

.text {
	padding: 0.5rem;
	vertical-align: middle;
	display: inline-block;
}
</style>

<!-- wobble class needs to be defined before the JS code that makes the text wobble, and there seems to be a problem with the word spacing with,
Okay, I slightly modified the JS code to have word wobbling instead of individual letters and then added spacing between the returned wobbling words.
See and experiment: https://codepen.io/queenadreena/pen/oKGyYq
hmm... the hyperlink doesn't work when wobbling :(
okay, I did plethora of things, but on webpage upload the wobbling stops and it doens't seem to be a `table` env problem. So, let's not have this up on the webpage for now.
And also, perhaps, having this manual public isn't the best of the ideas, that Ueda-san can be nasty, when she wants to be, haha!
-->
<!--
<div class="wobble_container">
<div class="wobble">RESCEU  Admin  Manual  (English)</div>
<div class="text">
	<span style="font-size:50px;"> &#9758; </span>
</div>
<div class="text">
	<a style="font-size: 30px;" href="https://www.dropbox.com/scl/fi/99f7j738igzathsmx80fx/RESCEU-Adminitrative-Procedure-Manual-English.pdf?rlkey=2pbwv4jpqwul0kppqsowkw77k&dl=0">click here!</a>
</div>
<script>
// Create array of any elements with "wobble" class
const all = document.querySelectorAll('.wobble');
// Iterate through each "wobble"
all.forEach(el => {
  // Get the text content of the element
  let text = el.textContent;
  // Create an array of separate letters
  text = text.split("");
  // Iterate through each letter and give it its own span element and individual animation delay offset
  const textCode = text.map((x, idx) => {
    let delay = (idx + 1) * 50;
    return `<span style="animation-delay: ${delay}ms">${x}</span>`;
  })
  // replace the element's html with our dynamically created html
  el.innerHTML = textCode.join(" ");
});
</script>
</div>
-->


<!-- Timeline -->

<div style="object-position:center; text-align:center">
<details>
	<summary>
	<p style="text-align:center; font-family:mistral; font-size:24px">
	  Timeline
	</p>
	</summary>

<style type="text/css" media="screen">
   @import url(https://fonts.googleapis.com/css?family=Raleway:400,900);

body{
  font-family: 'Raleway', sans-serif;
  color: black;
}

header h1{
  text-align: center;
  font-weight: bold;
  margin-top: 0;
}
  
 header p{
   text-align: center;
   margin-bottom: 0;
 }

.hexa{
  border: 0px;
  float: left;
  text-align: center;
  height: 35px;
  width: 60px;
  font-size: 22px;
  background: #973939;
  color: #973939;
  position: relative;
  margin-top: 15px;
}

.hexa:before{
  content: ""; 
  position: absolute; 
  left: 0; 
  width: 0; 
  height: 0;
  border-bottom: 15px solid #973939;
  border-left: 30px solid transparent;
  border-right: 30px solid transparent;
  top: -15px;
}

.hexa:after{
  content: ""; 
  position: absolute; 
  left: 0; 
  width: 0; 
  height: 0;
  border-left: 30px solid transparent;
  border-right: 30px solid transparent;
  border-top: 15px solid #973939;
  bottom: -15px;
}

.timeline {
  position: relative;
  padding: 0;
  width: 100%;
  margin-top: 20px;
  list-style-type: none;
}

.timeline:before {
  position: absolute;
  left: 50%;
  top: 0;
  content: ' ';
  display: block;
  width: 2px;
  height: 100%;
  margin-left: -1px;
  background: rgb(213,213,213);
  background: -moz-linear-gradient(top, rgba(213,213,213,0) 0%, rgb(213,213,213) 8%, rgb(213,213,213) 92%, rgba(213,213,213,0) 100%);
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(30,87,153,1)), color-stop(100%,rgba(125,185,232,1)));
  background: -webkit-linear-gradient(top, rgba(213,213,213,0) 0%, rgb(213,213,213) 8%, rgb(213,213,213) 92%, rgba(213,213,213,0) 100%);
  background: -o-linear-gradient(top, rgba(213,213,213,0) 0%, rgb(213,213,213) 8%, rgb(213,213,213) 92%, rgba(213,213,213,0) 100%);
  background: -ms-linear-gradient(top, rgba(213,213,213,0) 0%, rgb(213,213,213) 8%, rgb(213,213,213) 92%, rgba(213,213,213,0) 100%);
  background: linear-gradient(to bottom, rgba(213,213,213,0) 0%, rgb(213,213,213) 8%, rgb(213,213,213) 92%, rgba(213,213,213,0) 100%);
  z-index: 5;
}

.timeline li {
  padding: 2em 0;
}

.timeline .hexa{
  width: 16px;
  height: 10px;
  position: absolute;
  background: #973939;
  z-index: 5;
  left: 0;
  right: 0;
  margin-left:auto;
  margin-right:auto;
  top: -30px;
  margin-top: 0;
}

.timeline .hexa:before {
  border-bottom: 4px solid #973939;
  border-left-width: 8px;
  border-right-width: 8px;
  top: -4px;
}

.timeline .hexa:after {
  border-left-width: 8px;
  border-right-width: 8px;
  border-top: 4px solid #973939;
  bottom: -4px;
}

.direction-l,
.direction-r {
  float: none;
  width: 100%;
  text-align: center;
}

.flag-wrapper {
  text-align: center;
  position: relative;
}

.flag {
  position: relative;
  display: inline;
  background: rgb(255,255,255);
  font-weight: 600;
  z-index: 15;
  padding: 6px 10px;
  text-align: left;
  border-radius: 5px;
}

.direction-l .flag:after,
.direction-r .flag:after {
  content: "";
  position: absolute;
  left: 50%;
  top: -15px;
  height: 0;
  width: 0;
  margin-left: -8px;
  border: solid transparent;
  border-bottom-color: rgb(255,255,255);
  border-width: 8px;
  pointer-events: none;
}

.direction-l .flag {
  -webkit-box-shadow: -1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
  -moz-box-shadow: -1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
  box-shadow: -1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
}

.direction-r .flag {
  -webkit-box-shadow: 1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
  -moz-box-shadow: 1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
  box-shadow: 1px 1px 1px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.15);
}

.time-wrapper {
  display: block;
  position: relative;
  margin: 4px 0 0 0;
  z-index: 14;
  line-height: 1em;
  vertical-align: middle;
  color: #fff;
}

.direction-l .time-wrapper {
  float: none;
}

.direction-r .time-wrapper {
  float: none;
}

.time {
  background: #973939;
  display: inline-block;
  padding: 8px;
}

.desc {
  position: relative;
  margin: 1em 0 0 0;
  padding: 1em;
  background: rgb(254,254,254);
  -webkit-box-shadow: 0 0 1px rgba(0,0,0,0.20);
  -moz-box-shadow: 0 0 1px rgba(0,0,0,0.20);
  box-shadow: 0 0 1px rgba(0,0,0,0.20);
  z-index: 15;
}

.direction-l .desc,
.direction-r .desc {
  position: relative;
  margin: 1em 1em 0 1em;
  padding: 1em;
  z-index: 15;
}

@media(min-width: 768px){
  .timeline {
    width: 660px;
    margin: 0 auto;
    margin-top: 20px;
  }

  .timeline li:after {
    content: "";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
  }
  
  .timeline .hexa {
    left: -28px;
    right: auto;
    top: 8px;
  }

  .timeline .direction-l .hexa {
    left: auto;
    right: -28px;
  }

  .direction-l {
    position: relative;
    width: 310px;
    float: left;
    text-align: right;
  }

  .direction-r {
    position: relative;
    width: 310px;
    float: right;
    text-align: left;
  }

  .flag-wrapper {
    display: inline-block;
  }
  
  .flag {
    font-size: 18px;
  }

  .direction-l .flag:after {
    left: auto;
    right: -16px;
    top: 50%;
    margin-top: -8px;
    border: solid transparent;
    border-left-color: rgb(254,254,254);
    border-width: 8px;
  }

  .direction-r .flag:after {
    top: 50%;
    margin-top: -8px;
    border: solid transparent;
    border-right-color: rgb(254,254,254);
    border-width: 8px;
    left: -8px;
  }

  .time-wrapper {
    display: inline;
    vertical-align: middle;
    margin: 0;
  }

  .direction-l .time-wrapper {
    float: left;
  }

  .direction-r .time-wrapper {
    float: right;
  }

  .time {
    padding: 5px 10px;
  }

  .direction-r .desc {
    margin: 1em 0 0 0.75em;
  }
}

@media(min-width: 992px){
  .timeline {
    width: 800px;
    margin: 0 auto;
    margin-top: 20px;
  }

  .direction-l {
    position: relative;
    width: 380px;
    float: left;
    text-align: right;
  }

  .direction-r {
    position: relative;
    width: 380px;
    float: right;
    text-align: left;
  }
}
</style>

<ul class="timeline">
  <li>
    <div class="direction-r">
      <div class="flag-wrapper">
        <span class="hexa"></span>
        <span class="flag"> 
          The University of Tokyo </span>
        <span class="time-wrapper"><span class="time">
          2023 ~ </span></span>
      </div>
      <div class="desc">
      	  PhD in Physics at RESCEU
      </div>
    </div>
  </li>

  <li>
    <div class="direction-l">
      <div class="flag-wrapper">
        <span class="hexa"></span>
        <span class="flag"> 
          The University of Tokyo </span>
        <span class="time-wrapper"><span class="time">
          2021 – 2023 </span></span>
      </div>
      <div class="desc">
      	  MSc in Physics at ICRR
      </div>
    </div>
  </li>
  
  <li>
    <div class="direction-r">
      <div class="flag-wrapper">
        <span class="hexa"></span>
        <span class="flag"> 
          TIFR, Mumbai </span>
        <span class="time-wrapper"><span class="time">
          2020/11 – 2021/04 </span></span>
      </div>
      <div class="desc">
      	  Project Associate in the Helioseismology lab
      </div>
    </div>
  </li>

  <li>
    <div class="direction-l">
      <div class="flag-wrapper">
        <span class="hexa"></span>
        <span class="flag"> 
          IIITDM Kancheepuram, Chennai </span>
        <span class="time-wrapper"><span class="time">
          2016 – 2020 </span></span>
      </div>
      <div class="desc">
      	  BTech in Mechanical Engineering, Design and Manufacturing
      </div>
    </div>
  </li>

  <li>
    <div class="direction-r">
      <div class="flag-wrapper">
        <span class="hexa"></span>
        <span class="flag"> 
          Montfort School, Mandla </span>
        <span class="time-wrapper"><span class="time">
          2002 – 2016 </span></span>
      </div>
      <div class="desc">
      	 High School Graduation, majoring in Science      
      </div>
    </div>
  </li>
</ul>


</details>
</div>

---


<h3> <p style="text-align: center;"> Thank you for visiting my page! :) </p> </h3>

