---
title: "Timeline"
date: 2025-03-03T23:42:31+09:00
draft: false
---





<!--the below was just non-sense !!!!-->
<style type="text/css" media="screen">
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400&display=swap');
.design-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: ;
  min-height: 100vh;
  padding: 50px 0;
  font-family: Jost;
}

.design {
  display: flex;
  align-items: center;
  justify-content: center;
}

.timeline {
  width: 80%;
  height: auto;
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}

.timeline-content {
  padding: 20px;
  background:;
  border-radius: 5px;
  color:;
  -webkit-box-shadow: 5px 5px 10px #1a1a1a, -5px -5px 10px #242424;
          box-shadow: 5px 5px 10px #1a1a1a, -5px -5px 10px #242424;
  padding: 1.75rem;
  transition: 0.4s ease;
  overflow-wrap: break-word !important;
  margin: 1rem;
  margin-bottom: 20px;
  border-radius: 6px;
}

.timeline-component {
  margin: 0px 20px 20px 20px;
}

@media screen and (min-width: 768px) {
  .timeline {
    display: grid;
    grid-template-columns: 1fr 3px 1fr;
  }
  .timeline-middle {
    position: relative;
    background-image: linear-gradient(45deg, #F27121, #E94057, #8A2387);
    width: 3px;
    height: 100%;
  }
  .main-middle {
    opacity: 0;
  }
  .timeline-circle {
    position: absolute;
    top: 0;
    left: 50%;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background-image: linear-gradient(45deg, #F27121, #E94057, #8A2387);
    -webkit-transform: translateX(-50%);
            transform: translateX(-50%);
  }
}
</style>

<style>@import url('https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400&display=swap');</style>
<!--This is the main container that contains the whole timeline.-->
<section class="design-section">
<div class="timeline">
<!--Well, The reason for this div is to fill space. 
This space is technically used for keeping dates, 
but I didn't find the need for dates. However, I'll provide 
you the styling for dates, so that you can use it if you 
wanted to. 
-->
                  <div class="timeline-empty">
                  </div>
<!--This is the class where the timeline graphics are 
housed in. Note that we have timeline-circle 
here for that pointer in timeline.-->
               <div class="timeline-middle">
                   <div class="timeline-circle"></div>
               </div>
               <div class="timeline-component timeline-content">
                <h3>HTML</h3>
                <p>Some Text</p>
           	  </div>
                <div class="timeline-component timeline-content">
                         <h3>CSS</h3>
                         <p>Some Text.</p>
                </div>
                <div class="timeline-middle">
                    <div class="timeline-circle"></div>
                </div>
                <div class="timeline-empty">
                </div>
                <div class="timeline-empty">
                </div>
               <div class="timeline-middle">
                   <div class="timeline-circle"></div>
               </div>
               <div class=" timeline-component timeline-content">
                <h3>Javascript</h3>
                <p>Some Text.</p>
                 <div class="timeline-empty">
                </div>
                <div class="timeline-empty">
                </div>
               <div class="timeline-middle">
                   <div class="timeline-circle"></div>
               </div>
               <div class=" timeline-component timeline-content">
                <h3>Javascript</h3>
                <p>Some Text.</p>
           </div>
       </div>
    </div> 
</section>

