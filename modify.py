from pathlib import Path
p=Path('/mnt/data/aiunbound_new/index.html')
s=p.read_text()
# Add hero visual elements / simplify existing copy slightly
s=s.replace('<div class="eyebrow"><span class="live-dot"></span> STUDENT-LED AI LITERACY</div>', '<div class="eyebrow"><span class="eyebrow-line"></span><span class="live-dot"></span> STUDENT-LED AI LITERACY <span class="eyebrow-pill">UAE · 2026</span></div>')
s=s.replace('<h1>Understand AI.<br><em>Use It.</em><br>Question It.</h1>', '<h1>AI should be<br><span class="hero-gradient">understood.</span><br><em>Not blindly used.</em></h1>')
s=s.replace('<p>AI Unbound helps young people move beyond simply using AI to understanding it, questioning it and applying it with purpose.</p>', '<p class="hero-lead">A student-led AI literacy initiative helping young people understand how AI works, use it effectively, question its outputs and keep human thinking at the centre.</p>')
s=s.replace('<div class="hero-meta"><span>250+ students reached</span><i></i><span>Across the UAE</span></div>', '<div class="hero-meta"><span><strong>250+</strong> students reached</span><i></i><span>Dubai · UAE</span><i></i><span>Student-led</span></div>')
s=s.replace('<div class="actions"><a class="button primary" href="#programme">Explore the Programme <span>↓</span></a><a class="button ghost" href="#involved">Partner With Us <span>↗</span></a></div>', '<div class="actions"><a class="button primary" href="#programme">Explore the Programme <span>↓</span></a><a class="button ghost" href="#involved">Start a Conversation <span>↗</span></a></div><div class="hero-proof"><span>UNDERSTAND</span><b>→</b><span>QUESTION</span><b>→</b><span>CREATE</span></div>')
# Replace involved section with form-based contact
start=s.index('<section id="involved"')
end=s.index('</section>', start)+len('</section>')
new='''<section id="involved" class="section involved">
<div class="section-kicker">09 / GET INVOLVED</div>
<div class="contact-intro"><div><h2>Let’s make AI<br><em>make sense.</em></h2><p>Schools, organisations, educators, partners and students can use this form to reach the AI Unbound team.</p></div><div class="contact-orbit"><span>AI</span><i></i><b>HUMAN</b></div></div>
<div class="contact-layout">
<div class="contact-options">
<article><span>01</span><h3>Schools</h3><p>Bring practical AI literacy sessions to your students through workshops and structured learning.</p></article>
<article><span>02</span><h3>Partners</h3><p>Explore education, technology, community and impact partnerships with AI Unbound.</p></article>
<article><span>03</span><h3>Students</h3><p>Connect around student leadership, AI literacy, media, technology and community initiatives.</p></article>
</div>
<form class="contact-form" id="contact-form">
<div class="form-top"><span>DIRECT CONNECTION</span><small>Your message goes straight to the AI Unbound team.</small></div>
<div class="form-grid"><label><span>Name</span><input required name="name" type="text" autocomplete="name" placeholder="Your name"></label><label><span>Email</span><input required name="email" type="email" autocomplete="email" placeholder="you@example.com"></label></div>
<label><span>I’m reaching out as</span><select required name="role"><option value="" selected disabled>Select one</option><option>School / Educator</option><option>Organisation / Partner</option><option>Student</option><option>Parent / Guardian</option><option>Other</option></select></label>
<label><span>Message</span><textarea required name="message" rows="5" placeholder="Tell us a little about what you have in mind..."></textarea></label>
<input type="hidden" name="_subject" value="New AI Unbound enquiry">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">
<button class="form-submit" type="submit"><span>Send Message</span><b>↗</b></button>
<div class="form-status" id="form-status" aria-live="polite"></div>
</form></div>
</section>'''
s=s[:start]+new+s[end:]
# Footer email removed
s=s.replace('<div class="footer-contact"><span>CONTACT</span><p>hello@aiunbound.org</p><p>Student-led AI literacy initiative<br>Dubai, UAE</p></div>', '<div class="footer-contact"><span>CONNECT</span><p>Schools · Partners · Students</p><p>Student-led AI literacy initiative<br>Dubai, UAE</p></div>')
p.write_text(s)
