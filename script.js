const glow=document.querySelector('.cursor-glow');
window.addEventListener('pointermove',e=>{
  if(glow){glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'}
  document.documentElement.style.setProperty('--mx',`${e.clientX}px`);
  document.documentElement.style.setProperty('--my',`${e.clientY}px`);
});
const toggle=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav-links');
toggle?.addEventListener('click',()=>nav.classList.toggle('open'));
document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.10});
document.querySelectorAll('.hero-copy,.hero-orb-wrap,.section-kicker,.teach-grid article,.session-card,.compare-card,.person,.involved-grid article,.pearls-grid>div,.impact-photo,.contact-options article,.contact-form').forEach(x=>{x.classList.add('reveal');obs.observe(x)});
if(window.matchMedia('(pointer:fine)').matches){
 document.querySelectorAll('.teach-grid article,.session-card,.person,.compare-card,.involved-grid article,.contact-options article').forEach(card=>{
  card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;card.style.transform=`perspective(900px) rotateX(${(-y*3.5).toFixed(2)}deg) rotateY(${(x*4.5).toFixed(2)}deg) translateY(-6px)`});
  card.addEventListener('pointerleave',()=>card.style.transform='');
 });
}
const orb=document.querySelector('.hero-orb');
window.addEventListener('scroll',()=>{if(!orb)return;orb.style.setProperty('--scroll-depth',`${Math.min(window.scrollY,700)}px`)});

// FormSubmit contact form. The recipient is not rendered anywhere on the page.
const form=document.getElementById('contact-form');
const status=document.getElementById('form-status');
if(form){
  form.addEventListener('submit',async e=>{
    e.preventDefault();
    const btn=form.querySelector('.form-submit');
    btn.disabled=true; btn.querySelector('span').textContent='Sending…'; status.className='form-status'; status.textContent='';
    const recipient=atob('bW9oYW1tYWRzaGFoYW4uMDI1QGdtYWlsLmNvbQ==');
    try{
      const data=new FormData(form);
      const res=await fetch('https://formsubmit.co/ajax/'+encodeURIComponent(recipient),{method:'POST',body:data,headers:{'Accept':'application/json'}});
      if(!res.ok) throw new Error('send failed');
      form.reset(); status.className='form-status success'; status.textContent='Message sent. Thanks for reaching out to AI Unbound.';
    }catch(err){
      status.className='form-status error'; status.textContent='Something went wrong. Please try again in a moment.';
    }finally{btn.disabled=false;btn.querySelector('span').textContent='Send Message'}
  });
}
