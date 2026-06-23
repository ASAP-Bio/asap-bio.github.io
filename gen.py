import os
OUT="/sessions/busy-serene-faraday/mnt/outputs/site"
NAV=[("index.html","Home"),("about.html","About"),("partners.html","Partners"),
     ("themes.html","Themes"),("knowledge.html","Knowledge Hub"),("scholarships.html","Scholarships"),("news.html","News"),("contact.html","Contact")]

def head(title, active, desc):
    links="".join(f'<a href="{h}" class="{ "active" if h==active else ""}">{n}</a>' for h,n in NAV)
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} · ASAP-Bio</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/styles.css">
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "65d348fea968478387f8337eee0623a3"}}'></script><!-- End Cloudflare Web Analytics -->
</head><body>
<header class="nav"><div class="wrap">
  <a class="brand" href="index.html"><img src="assets/emblem.png" alt="ASAP-Bio logo">
    <span>ASAP-Bio<small>African–Danish University Partnerships</small></span></a>
  <button class="navtoggle" onclick="document.getElementById('lk').classList.toggle('open')">☰</button>
  <nav class="links" id="lk">{links}</nav>
</div></header>"""

FOOT="""<section class="funderstrip"><div class="wrap">
    <img src="assets/mfa.png" alt="Ministry of Foreign Affairs of Denmark">
    <img src="assets/dfc.jpg" alt="Danida Fellowship Centre">
    <div class="ack"><strong>The project is funded by the Ministry of Foreign Affairs of Denmark and managed by Danida Fellowship Centre.</strong><br>
    DANIDA Knowledge and Innovation Programme (KIP) 2025.</div>
</div></section>
<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div><h4>ASAP-Bio</h4><p style="color:#cfe0d0">Advancing Sustainable Animal Production and Biodiversity through Equitable African–Danish University Partnerships. A 2026–2032 partnership in Integrated Sustainable Animal Production Systems (ISAPS).</p><img class="footemblem" src="assets/emblem-trans.png" alt="ASAP-Bio emblem"></div>
    <div><h4>Explore</h4><ul>
      <li><a href="about.html">About the project</a></li><li><a href="partners.html">Partners</a></li>
      <li><a href="themes.html">Themes</a></li><li><a href="knowledge.html">Knowledge Hub</a></li>
      <li><a href="scholarships.html">Scholarships</a></li>
      <li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h4>Contact</h4>
      <p style="color:#cfe0d0">ASAP-Bio Project Coordination<br>Center for Quantitative Genetics and Genomics (QGG)<br>Aarhus University, Denmark</p>
      <p style="margin-top:8px"><a href="mailto:grum.gebreyesus@qgg.au.dk">grum.gebreyesus@qgg.au.dk</a></p>
      <p style="margin-top:8px"><a href="contact.html">See all project contacts &#8594;</a></p></div>
  </div>
  <div class="fbar"><span>© 2026 ASAP-Bio partnership. All partner institutions.</span>
  <span>Aarhus University · Debre Berhan University · Muni University · University of Nairobi · Jomo Kenyatta University of Agriculture and Technology</span></div>
</div></footer>
<script>document.querySelectorAll('nav.links a').forEach(a=>a.addEventListener('click',()=>document.getElementById('lk').classList.remove('open')));</script>
</body></html>"""

def pagehdr(t,p):
    body = ('<p>'+p+'</p>') if p else ''
    return '<div class="pagehdr"><div class="wrap"><h1>'+t+'</h1>'+body+'</div></div>'
def write(fn,body): open(os.path.join(OUT,fn),"w").write(body)

# ---------------- INDEX ----------------
index = head("Home","index.html","ASAP-Bio: a 2026–2032 African–Danish university partnership in sustainable animal production and biodiversity, funded by the Danish MFA via Danida Fellowship Centre.") + """
<section class="hero"><div class="wrap"><div class="heroinner">
    <h1>Sustainable animal production &amp; biodiversity, built on equitable partnership</h1>
    <p class="tagline">Advancing Sustainable Animal Production and Biodiversity through Equitable African–Danish University Partnerships</p>
    <div class="btnrow"><a class="btn" href="scholarships.html">Scholarships</a>
      <a class="btn ghost" href="about.html">About the project</a></div>
  </div></div>
  <div class="credit">Image: David Buule · Muni University, Uganda</div>
</section>
<div class="wrap"><div class="stats">
  <div class="stat"><div class="v">5</div><div class="l">partner universities, 4 countries</div></div>
  <div class="stat"><div class="v">28</div><div class="l">full MSc scholarships</div></div>
  <div class="stat"><div class="v">5</div><div class="l">ISAPS themes</div></div>
  <div class="stat"><div class="v">7&nbsp;yrs</div><div class="l">2026–2032 programme</div></div>
</div></div>

<section><div class="wrap">
  <div class="eyebrow">What is ASAP-Bio</div>
  <h2>One partnership, two outcomes</h2>
  <p class="lead">ASAP-Bio strengthens long-term collaboration between Aarhus University and four East African universities, addressing a shared challenge: how to make livestock systems more productive, sustainable, and biodiversity-friendly.</p>
  <div class="grid g2" style="margin-top:26px">
    <div class="card"><span class="tg">Outcome 1 · Partnership</span>
      <h3>Knowledge &amp; collaborative learning</h3>
      <p>Jointly developed MSc course modules, staff exchanges and training, a shared open-access knowledge platform, and equitable governance embedded in every partner institution.</p></div>
    <div class="card b"><span class="tg">Outcome 2 · Scholarships</span>
      <h3>People &amp; skills</h3>
      <p>Full-degree MSc scholarships, shorter research stays, and annual summer schools that bring East African and Danish students together around real ISAPS problems.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="eyebrow">Focus areas</div>
  <h2>Five partnership &amp; teaching themes</h2>
  <div class="grid g3" style="margin-top:24px">
    <div class="card"><h3>Multi-omics</h3><p>Genomics, breeding, transcriptomics, microbiomics and bioinformatics for livestock.</p></div>
    <div class="card"><h3>Digitalization and phenomics</h3><p>Precision livestock farming, sensors, AI and machine learning.</p></div>
    <div class="card"><h3>Nutrition and feed systems</h3><p>Sustainable, climate-smart feeding strategies and feed efficiency.</p></div>
    <div class="card"><h3>One Health</h3><p>Animal, human and environmental health, led with JKUAT.</p></div>
    <div class="card"><h3>Biodiversity and Breeding programs</h3><p>Biodiversity, breeding programmes, resilient production systems.</p></div>
    <div class="card gd" style="display:flex;align-items:center;justify-content:center"><a class="btn green" href="themes.html">Explore the themes →</a></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">Partners</div>
  <h2>Four countries, one network</h2>
  <p class="lead">Aarhus University (Denmark) is the contracting institution, working with three primary partners and one secondary partner across Ethiopia, Uganda and Kenya.</p>
  <div style="margin-top:18px">
    <span class="pill">🇩🇰 Aarhus University</span><span class="pill">🇪🇹 Debre Berhan University</span>
    <span class="pill">🇺🇬 Muni University</span><span class="pill">🇰🇪 University of Nairobi</span>
    <span class="pill">🇰🇪 JKUAT (secondary)</span>
  </div>
  <p style="margin-top:18px"><a class="btn green" href="partners.html">Meet the partners →</a></p>
</div></section>
""" + FOOT
write("index.html", index)

# ---------------- ABOUT ----------------
about = head("About","about.html","About ASAP-Bio: objective, outcomes, structure and funding.") + pagehdr(
  "About ASAP-Bio","A university partnership building human capital, institutional capacity and knowledge in Integrated Sustainable Animal Production Systems (ISAPS) across East Africa and Denmark.") + """
<section><div class="wrap">
  <h2>Our objective</h2>
  <p class="lead">To contribute to sustainable livestock production, food security and biodiversity conservation in East Africa by strengthening African–Danish university partnerships that generate qualified graduates, durable institutional capacity, and relevant knowledge in ISAPS.</p>
</div></section>

<section class="alt"><div class="wrap">
  <h2>How the project works</h2>
  <p class="lead">ASAP-Bio is funded under the DANIDA Knowledge and Innovation Programme and runs on two parallel components.</p>
  <div class="grid g2" style="margin-top:24px">
    <div class="card"><span class="tg">Outcome 1</span><h3>Partnership</h3>
      <p>Co-developed, cross-credited MSc course modules; staff exchanges and capacity-building workshops; a shared open-access knowledge platform; and equitable joint governance. Runs 2026–2030.</p></div>
    <div class="card b"><span class="tg">Outcome 2</span><h3>Scholarships</h3>
      <p>28 full-degree MSc scholarships, 25 shorter research stays, and six summer schools. Prepared in 2026, active from 2027, completing by mid-2032.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Implementation structure</h2>
  <p class="lead">The partnership is run through joint governance bodies and shared academic units.</p>
<div class="orgchart">
    <div class="org-box org-strat" style="max-width:580px;margin:0 auto">
      <div class="org-title">Steering Group</div>
      <div class="org-fn">Strategic oversight and governance. One high-level representative per partner university.</div>
    </div>
    <div class="org-conn"></div>
    <div class="org-row">
      <div class="org-box">
        <div class="org-title">Joint Academic Board</div>
        <div class="org-fn">Academic governance and quality assurance.</div>
      </div>
      <div class="org-box">
        <div class="org-title">Programme Management Group</div>
        <div class="org-fn">Operational oversight.</div>
      </div>
    </div>
    <div class="org-conn"></div>
    <div class="org-box org-themes">
      <div class="org-title">Five ISAPS thematic groups</div>
      <div class="org-fn">Academic delivery: joint MSc modules, the knowledge platform and summer schools.</div>
      <div class="org-chips">
        <a href="themes.html#multiomics">Multi-omics</a><a href="themes.html#phenomics">Digitalization and phenomics</a><a href="themes.html#nutrition">Nutrition and feed systems</a><a href="themes.html#onehealth">One Health</a><a href="themes.html#biodiversity">Biodiversity and Breeding programs</a>
      </div>
    </div>
    <div class="org-conn"></div>
    <div class="org-row">
      <div class="org-box">
        <div class="org-title">Support units, Aarhus University</div>
        <div class="org-fn">Admissions, scholarships and student services.</div>
      </div>
      <div class="org-box">
        <div class="org-title">Support units, partner universities</div>
        <div class="org-fn">Academic and administrative coordination.</div>
      </div>
    </div>
  </div>
  <p style="text-align:center;color:var(--grey);font-size:13px;margin-top:14px">ASAP-Bio implementation structure.</p>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Facts &amp; figures</h2>
  <table class="t"><tr><th>Item</th><th>Detail</th></tr>
    <tr><td>Programme</td><td>DANIDA Knowledge and Innovation Programme (KIP) 2025</td></tr>
    <tr><td>Managed by</td><td>Danida Fellowship Centre (DFC), Ministry of Foreign Affairs of Denmark</td></tr>
    <tr><td>Contracting institution</td><td>Aarhus University, Faculty of Technical Sciences</td></tr>
    <tr><td>Total grant</td><td>DKK 35,928,800</td></tr>
    <tr><td>Partnership period</td><td>2026 – 2030 (Outcome 1)</td></tr>
    <tr><td>Scholarship period</td><td>2027 – June 2032 (Outcome 2; prepared in 2026)</td></tr>
    <tr><td>Countries</td><td>Denmark, Ethiopia, Uganda, Kenya</td></tr>
  </table>
</div></section>
""" + FOOT
write("about.html", about)

# ---------------- PARTNERS ----------------
partners = head("Partners","partners.html","The five universities behind ASAP-Bio across Denmark, Ethiopia, Uganda and Kenya.") + pagehdr(
  "Partners","Five universities across four countries. Select any institution to visit its website.") + """
<section><div class="wrap">
  <div class="grid g2">
    <a class="card pcard" href="https://international.au.dk/" target="_blank" rel="noopener">
      <img class="plogo" src="assets/logo-au.png" alt="Aarhus University logo" onerror="this.style.display='none'">
      <span class="flag">🇩🇰 Denmark · Contracting institution</span>
      <h3>Aarhus University (AU)</h3>
      <p>Through the Center for Quantitative Genetics and Genomics (QGG) and the Department of Animal and Veterinary Sciences (ANIVET), Faculty of Technical Sciences. AU leads overall coordination, hosts the MSc scholarship students, and contributes a co-lead to every thematic group.</p>
      <span class="pvisit">Visit international.au.dk →</span></a>
    <a class="card pcard" href="https://www.dbu.edu.et/" target="_blank" rel="noopener">
      <img class="plogo" src="assets/logo-dbu.png" alt="Debre Berhan University logo" onerror="this.style.display='none'">
      <span class="flag">🇪🇹 Ethiopia · Primary partner</span>
      <h3>Debre Berhan University (DBU)</h3>
      <p>Academic partner co-implementing both the partnership and scholarship components, contributing modules grounded in the Ethiopian livestock-production context and faculty across the thematic groups.</p>
      <span class="pvisit">Visit dbu.edu.et →</span></a>
    <a class="card pcard" href="https://www.muni.ac.ug/" target="_blank" rel="noopener">
      <img class="plogo" src="assets/logo-mu.png" alt="Muni University logo" onerror="this.style.display='none'">
      <span class="flag">🇺🇬 Uganda · Primary partner</span>
      <h3>Muni University (MU)</h3>
      <p>Academic partner linking curricula to farming-community realities in northern Uganda, contributing thematic co-leads, content and faculty exchanges.</p>
      <span class="pvisit">Visit muni.ac.ug →</span></a>
    <a class="card pcard" href="https://www.uonbi.ac.ke/" target="_blank" rel="noopener">
      <img class="plogo" src="assets/logo-uon.png" alt="University of Nairobi logo" onerror="this.style.display='none'">
      <span class="flag">🇰🇪 Kenya · Primary partner</span>
      <h3>University of Nairobi (UoN)</h3>
      <p>Academic partner co-implementing the partnership and scholarship components. UoN coordinates the secondary-partner relationship with JKUAT and contributes to the veterinary and One Health themes.</p>
      <span class="pvisit">Visit uonbi.ac.ke →</span></a>
    <a class="card pcard b" href="https://www.jkuat.ac.ke/" target="_blank" rel="noopener" style="grid-column:1 / -1">
      <img class="plogo" src="assets/logo-jkuat.png" alt="JKUAT logo" onerror="this.style.display='none'">
      <span class="flag">🇰🇪 Kenya · Secondary partner (through UoN)</span>
      <h3>Jomo Kenyatta University of Agriculture and Technology (JKUAT)</h3>
      <p>Brings the <strong>One Health</strong> dimension to the curriculum, bridging animal, human and environmental health. JKUAT participates through the University of Nairobi channel.</p>
      <span class="pvisit">Visit jkuat.ac.ke →</span></a>
  </div>
</div></section>
""" + FOOT
write("partners.html", partners)

# ---------------- THEMES ----------------
themes = head("Themes","themes.html","The five ISAPS thematic groups at the heart of ASAP-Bio.") + pagehdr(
  "Research &amp; teaching themes","All academic work happens within five ISAPS thematic groups. Each is co-led by one Aarhus and one African academic, and together they form the project's Joint Academic Board.") + """
<section><div class="wrap">
  <div class="grid g2">
    <div class="card" id="multiomics"><h3>Multi-omics</h3>
      <p>Genomics and gene mapping; transcriptomics and gene expression in production traits; proteomics and metabolomics for phenotype prediction; microbiomics and metagenomics in livestock gut systems; multi-omics data integration and bioinformatics pipelines.</p></div>
    <div class="card b" id="phenomics"><h3>Digitalization and phenomics</h3>
      <p>Precision livestock farming, sensor technologies, and the application of artificial intelligence and machine learning to animal production systems.</p></div>
    <div class="card" id="nutrition"><h3>Nutrition and feed systems</h3>
      <p>Sustainable feeding strategies, feed efficiency, and climate-smart nutrition adapted to East African production environments.</p></div>
    <div class="card p" id="onehealth"><h3>One Health</h3>
      <p>The interface of animal, human and environmental health within the ISAPS curriculum. Led in partnership with JKUAT through the University of Nairobi.</p></div>
    <div class="card gd" id="biodiversity"><h3>Biodiversity and Breeding programs</h3>
      <p>Biodiversity and breeding programmes, climate resilience, value chains, socio-economics and greenhouse-gas mitigation in sustainable livestock production.</p></div>
    <div class="card" style="display:flex;flex-direction:column;justify-content:center;background:var(--soft)">
      <h3>How themes work</h3><p>Each thematic group has 4–6 members from across the partnership and acts as a work package, delivering joint MSc modules, content for the knowledge platform, and the annual summer schools.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Summer schools</h2>
  <p class="lead">Six summer schools, typically one week each, hosted by the partner universities in Denmark and Africa on a rotating basis.</p>
  <p>They are open to students enrolled in the master&rsquo;s in animal science programmes of the partner universities (including Aarhus University) and other selected applicants, subject to availability of spots. The content of each summer school is set by the ASAP-Bio Joint Academic Board and spans the five ISAPS themes.</p>
</div></section>
""" + FOOT
write("themes.html", themes)

# ---------------- SCHOLARSHIPS ----------------
scholarships = head("Scholarships","scholarships.html","ASAP-Bio scholarships: 28 full-degree MSc places at Aarhus University plus research stays and summer schools for students from Ethiopia, Uganda and Kenya.") + pagehdr(
  "Scholarships","Fully funded opportunities for students from Ethiopia, Uganda and Kenya to study and conduct research at Aarhus University, Denmark.") + """
<section><div class="wrap">
  <h2>What is on offer</h2>
  <div class="grid g3" style="margin-top:18px">
    <div class="card"><span class="tg">Output 1</span><h3>Full-degree MSc</h3>
      <p><strong>28 scholarships</strong> · 24 months · MSc Animal Science at Aarhus University. Fully funded: tuition, travel, visa, insurance, housing and a living stipend.</p></div>
    <div class="card b"><span class="tg">Outputs 2 &amp; 3</span><h3>Research stays</h3>
      <p><strong>25 stays</strong> (10 of five months, 15 of three months) at Aarhus University for students currently enrolled at a partner university, on study leave.</p></div>
    <div class="card p"><span class="tg">Output 4</span><h3>Summer schools</h3>
      <p><strong>Six summer schools</strong>, typically one week each, hosted by the partner universities in Denmark and Africa on a rotating basis. Open to students enrolled in the master&rsquo;s in animal science programmes of the partner universities (including Aarhus University) and other selected applicants, subject to availability of spots. The content of each summer school is set by the ASAP-Bio Joint Academic Board and spans the five ISAPS themes.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Full-degree intake schedule</h2>
  <table class="t"><tr><th>Cohort</th><th>New places</th><th>Notes</th></tr>
    <tr><td>2027</td><td>6</td><td>First cohort; MSc Animal Science open from autumn 2027</td></tr>
    <tr><td>2028</td><td>7</td><td>13 students cumulative</td></tr>
    <tr><td>2029</td><td>8</td><td>21 cumulative; first graduates</td></tr>
    <tr><td>2030</td><td>7</td><td>28 cumulative, final intake</td></tr>
  </table>
</div></section>

<section><div class="wrap">
  <h2>How the full-degree application works</h2>
  <p class="lead">A transparent two-step process. Being shortlisted by ASAP-Bio does not guarantee admission, every candidate must also meet Aarhus University's official requirements.</p>
  <div class="steps" style="margin-top:22px">
    <div class="step"><div class="n"></div><div><h3>Step 1, ASAP-Bio screening</h3><p>You apply to the ASAP-Bio call. The Joint Academic Board and Admissions Taskforce assess academic strength, relevance of your BSc, ISAPS thematic fit, motivation and gender balance, and produce a shortlist. Shortlisted candidates can receive funded support to take the IELTS test.</p></div></div>
    <div class="step"><div class="n"></div><div><h3>Step 2, Official AU admission</h3><p>Shortlisted candidates submit a full application through Aarhus University's official system (Studieportalen) and are ranked alongside all other applicants. AU Admissions makes the formal admission decision.</p></div></div>
    <div class="step"><div class="n"></div><div><h3>Scholarship &amp; arrival</h3><p>Once admitted, ASAP-Bio issues your scholarship agreement and supports the residence-permit, housing and pre-departure process. Studies begin in the autumn.</p></div></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Who can apply (full-degree MSc)</h2>
  <div class="grid g2">
    <div class="card"><h3>Eligibility</h3>
      <p>• National of Ethiopia, Uganda or Kenya<br>• A relevant Bachelor's degree (animal science, veterinary science, agriculture, biology or related field)<br>• Not currently enrolled in another full Master's programme<br>• Able to begin studies in Aarhus in the autumn intake</p></div>
    <div class="card"><h3>Language</h3>
      <p>An accepted English test is required, normally <strong>IELTS Academic 6.5</strong> (minimum 6.0 in each component) or equivalent. The test result must be ready in time for the official AU deadline. Funded test support is available to shortlisted candidates.</p></div>
  </div>
  <div class="callout">Calls are circulated through partner universities (DBU, MU, UoN, JKUAT), the project website and knowledge platform, and national animal-production society networks (ESAP, KSAP, APSU). Watch the <a href="news.html">News</a> page and check back for the open call.</div>
</section></div>

<section><div class="wrap" style="text-align:center">
  <h2>Interested?</h2>
  <p class="lead center">Calls open ahead of each intake. For questions about the scholarships, contact the coordination office.</p>
  <p style="margin-top:18px"><a class="btn" href="contact.html">Contact us</a></p>
</div></section>
""" + FOOT
write("scholarships.html", scholarships)

# ---------------- NEWS ----------------
news = head("News","news.html","Latest news and milestones from the ASAP-Bio partnership.") + pagehdr(
  "News","") + """
<section><div class="wrap">
  <div class="eyebrow">Featured event · Uganda · 6–7 November 2026</div>
  <h2>ASAP-Bio co-organises APSU 2026, and we want your ideas on animal-science education</h2>
  <div class="grid g2" style="margin-top:18px;align-items:start">
    <div>
      <p class="lead" style="margin-bottom:14px">ASAP-Bio is partnering with the <strong>Animal Production Society of Uganda (APSU)</strong> to co-organise its 2nd Scientific Conference and 5th Annual General Meeting, at Das Berliner Hotel, Wakiso. Together we have added an <strong>education and human-capital</strong> dimension to the conference theme, and we are opening the floor to one urgent question: is what we teach keeping pace with how livestock systems are changing?</p>
      <div class="callout gold">
        <strong>Call for abstracts: education and curriculum fit for purpose</strong>
        <p style="margin-top:6px">Climate change, disease, digitalisation and One Health are reshaping animal production faster than most curricula can follow. If you teach, research or study animal science, this is your platform. We especially welcome abstracts on:</p>
        <ul>
          <li>Curriculum innovation and fit-for-purpose programme redesign</li>
          <li>Teaching the ISAPS themes: genetics and multi-omics, phenomics and digitalisation, nutrition and feed, One Health, and sustainable production</li>
          <li>Closing the gap between what the sector needs and what graduates learn</li>
          <li>Student and early-career voices on the skills that matter most</li>
        </ul>
        <p>Bring data, a redesigned course, or a bold idea, we want to hear it. Abstract submissions close 1 November 2026.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="btn" href="https://apsu.ug/events/apsu-conference-2026/call-for-papers" target="_blank" rel="noopener">Submit your abstract →</a>
        <a class="btn green" href="https://apsu.ug/events/apsu-conference-2026/call-for-papers" target="_blank" rel="noopener">View the official call</a>
      </div>
    </div>
    <a href="https://apsu.ug/events/apsu-conference-2026/call-for-papers" target="_blank" rel="noopener" class="apsu-fig">
      <img src="assets/apsu2026.jpg" alt="APSU 2026 conference call for abstracts poster">
    </a>
  </div>

  <h3 style="margin-top:26px">The ASAP-Bio education stream at APSU 2026</h3>
  <p class="lead">Selected education abstracts will run through the programme, alongside a plenary talk and a dedicated morning of panel discussions.</p>
  <div class="grid g3" style="margin-top:16px">
    <div class="card"><span class="tg">Across both days</span><h3>Selected education abstracts</h3><p>Presentations on animal-science education, curriculum fit for purpose, and the links between the ISAPS themes and teaching, woven into the scientific programme.</p></div>
    <div class="card b"><span class="tg">Day 1 plenary</span><h3>Opening plenary talk</h3><p>A scene-setting talk for the whole conference: what does the livestock sector need from university curricula, and are we delivering it?</p></div>
    <div class="card p"><span class="tg">Day 2 morning</span><h3>Livestock Sector Education Forum</h3><p>A dedicated half-day of panel discussions between farmers, veterinary services, agribusiness and universities, with comparative voices from Ethiopia and Kenya, ending in a shared set of curriculum priorities for Uganda.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Featured coverage</h2>
  <p class="lead">ASAP-Bio in the words of its partners and funder.</p>
  <div class="grid g3" style="margin-top:18px">
    <a class="card pcard gd" href="https://dfcentre.com/stories/advancing-sustainable-animal-production-and-biodiversity/" target="_blank" rel="noopener">
      <span class="src">Danida Fellowship Centre · feature</span>
      <h3>Advancing Sustainable Animal Production and Biodiversity</h3>
      <p>An interview with project coordinator Grum Gebreyesus on co-creating agricultural education, student mobility and an open learning platform.</p>
      <span class="pvisit">Read on dfcentre.com →</span></a>
    <a class="card pcard" href="https://www.dbu.edu.et/news_details?newsID=391" target="_blank" rel="noopener">
      <span class="src">Debre Berhan University</span>
      <h3>ASAP-Bio partnership news</h3>
      <p>Coverage of the ASAP-Bio partnership from Debre Berhan University, Ethiopia.</p>
      <span class="pvisit">Read on dbu.edu.et →</span></a>
    <a class="card pcard b" href="https://muni.ac.ug/index.php/en/muni-university-joins-landmark-african%E2%80%93danish-partnership-to-transform-agriculture-and-livestock-education-in-uganda.html" target="_blank" rel="noopener">
      <span class="src">Muni University</span>
      <h3>Muni University joins landmark African&ndash;Danish partnership</h3>
      <p>Muni University, Uganda, on joining ASAP-Bio to transform agriculture and livestock education.</p>
      <span class="pvisit">Read on muni.ac.ug →</span></a>
  </div>
</div></section>
""" + FOOT
write("news.html", news)

# ---------------- CONTACT ----------------
contact = head("Contact","contact.html","Contact the ASAP-Bio coordination team and country coordinators.") + pagehdr(
  "Contact","Reach the ASAP-Bio coordination team at Aarhus University, or the local coordinator at each partner university.") + """
<section><div class="wrap">
  <div class="grid g2">
    <div class="card"><h3>Coordination office</h3>
      <p><strong>ASAP-Bio Project Coordination</strong><br>
      Center for Quantitative Genetics and Genomics (QGG)<br>
      Aarhus University, Denmark</p></div>
    <div class="card"><h3>Scholarship enquiries</h3>
      <p>For questions about the full-degree MSc scholarships, research stays or summer schools, contact the coordination team. Calls for applications are announced on the <a href="news.html">News</a> page and circulated through all partner universities and national animal-production networks.</p></div>
  </div>

  <h2 style="margin-top:42px">Project Management Group</h2>
  <div class="grid g2" style="margin-top:18px">
    <div class="card"><h3>Grum Gebreyesus Teklewold</h3>
      <p class="role">Project Coordinator</p>
      <p>Center for Quantitative Genetics and Genomics (QGG), Aarhus University, Denmark</p>
      <p><a href="mailto:grum.gebreyesus@qgg.au.dk">grum.gebreyesus@qgg.au.dk</a><br>
      <a href="https://pure.au.dk/portal/da/persons/grum.gebreyesus%40qgg.au.dk/" target="_blank" rel="noopener">University profile (PURE) &#8594;</a></p></div>
    <div class="card"><h3>Amalie Krabbe Hansen</h3>
      <p class="role">Project Manager</p>
      <p>Center for Quantitative Genetics and Genomics (QGG), Aarhus University, Denmark</p>
      <p><a href="mailto:amaliekh@qgg.au.dk">amaliekh@qgg.au.dk</a><br>
      <a href="https://www.au.dk/amaliekh@qgg.au.dk/" target="_blank" rel="noopener">University profile &#8594;</a></p></div>
    <div class="card"><h3>Tine Rousing</h3>
      <p class="role">Animal Sciences MSc Programme Manager</p>
      <p>Department of Animal and Veterinary Sciences (ANIVET), Aarhus University, Denmark</p>
      <p><a href="mailto:tine.rousing@anivet.au.dk">tine.rousing@anivet.au.dk</a><br>
      <a href="https://pure.au.dk/portal/da/persons/tine.rousing%40anivet.au.dk/" target="_blank" rel="noopener">University profile (PURE) &#8594;</a></p></div>
    <div class="card"><h3>Rikke Nielsen</h3>
      <p class="role">International Director</p>
      <p><a href="https://pure.au.dk/portal/en/organisations/16a28811-34e6-4879-a936-50e54004c49e" target="_blank" rel="noopener">AU Student Administration and Services</a>, Aarhus University, Denmark</p>
      <p><a href="mailto:rikkenielsen@au.dk">rikkenielsen@au.dk</a><br>
      <a href="https://www.au.dk/en/rikkenielsen@au.dk" target="_blank" rel="noopener">University profile &#8594;</a></p></div>
    <div class="card"><h3>Bethel Geremew</h3>
      <p class="role">Partner Coordinator &ndash; Ethiopia</p>
      <p>Debre Berhan University, Ethiopia</p>
      <p><a href="mailto:bethel@dbu.edu.et">bethel@dbu.edu.et</a></p></div>
    <div class="card"><h3>Robert Onzima</h3>
      <p class="role">Partner Coordinator &ndash; Uganda</p>
      <p>Muni University, Uganda</p>
      <p><a href="mailto:r.onzima@muni.ac.ug">r.onzima@muni.ac.ug</a></p></div>
    <div class="card"><h3>Rawlynce Bett</h3>
      <p class="role">Partner Coordinator &ndash; Kenya</p>
      <p>University of Nairobi, Kenya</p>
      <p><a href="mailto:rawlynce@uonbi.ac.ke">rawlynce@uonbi.ac.ke</a></p></div>
    <div class="card"><h3>Johnson Kinyua</h3>
      <p class="role">Partner Coordinator &ndash; JKUAT, Kenya</p>
      <p>Jomo Kenyatta University of Agriculture and Technology, Kenya</p>
      <p><a href="mailto:johnsonkinyua@jkuat.ac.ke">johnsonkinyua@jkuat.ac.ke</a></p></div>
  </div>
</div></section>
""" + FOOT
write("contact.html", contact)

# ---------------- KNOWLEDGE HUB ----------------
COURSE_CARDS = {
"biodiversity": """    <div class="coursefeat">
      <span class="tagc">Foundational course</span>
      <h4>Foundations of Animal Genetics</h4>
      <p>The entry point to the breeding track: cells and chromosomes, mitosis and meiosis, Mendelian inheritance, gene interactions and epistasis. Developed from the materials of Hulunim Gatew Tariku (Debre Berhan University).</p>
      <p class="cmeta">★ Self-paced · ⏱ ~6 hours · 🎓 BSc / early MSc · 🧬 Foundational</p>
      <a class="btn green" href="course-foundations-animal-genetics.html">Start the course →</a>
    </div>
    <div class="coursefeat">
      <span class="tagc">Foundational course</span>
      <h4>Applied Animal Breeding</h4>
      <p>The breeder&rsquo;s toolkit: traits and variation, heritability and repeatability, the breeder&rsquo;s equation, breeding-value estimation and BLUP, and mating systems including inbreeding, with worked examples. From the materials of Hulunim Gatew Tariku (Debre Berhan University).</p>
      <p class="cmeta">★ Self-paced · ⏱ ~8 hours · 🎓 MSc level · 🧮 Worked examples</p>
      <a class="btn green" href="course-applied-animal-breeding.html">Start the course →</a>
    </div>
    <div class="coursefeat">
      <span class="tagc">Foundational course</span>
      <h4>Animal Reproduction and Reproductive Biotechnology</h4>
      <p>How genetic gain reaches the herd: reproductive anatomy and hormones, the estrous cycle and gestation, artificial insemination and semen technology, estrus synchronisation and embryo transfer. From the materials of Hulunim Gatew Tariku (Debre Berhan University).</p>
      <p class="cmeta">★ Self-paced · ⏱ ~7 hours · 🎓 MSc level · 🧬 Biotech focus</p>
      <a class="btn green" href="course-animal-reproduction-biotech.html">Start the course →</a>
    </div>
    <div class="coursefeat">
      <span class="tagc">Featured course</span>
      <h4>Breeding programs with Genomic selection</h4>
      <p>A self-paced course on genomic selection: SNP chips, genomic breeding values, the accuracy equation, breeding-program design and managing genetic diversity.</p>
      <p class="cmeta">★ Self-paced · ⏱ ~5 hours · 🎓 MSc / advanced</p>
      <a class="btn green" href="course-genomic-selection-breeding.html">Start the course →</a>
    </div>
    <div class="coursefeat">
      <span class="tagc">Featured course</span>
      <h4>Breeding and Genetics</h4>
      <p>The quantitative-genetics foundations of breeding: heritability, breeding values (BLUP) and genomic prediction (GBLUP), with hands-on R practicals. By Peter Sørensen (Aarhus University, CC0).</p>
      <p class="cmeta">★ Self-paced · ⏱ ~8 hours · 🎓 MSc / advanced · 📊 R</p>
      <a class="btn green" href="course-breeding-genetics.html">Start the course →</a>
    </div>
    <div class="coursefeat">
      <span class="tagc">Featured course</span>
      <h4>Quantitative &amp; Population Genetics</h4>
      <p>Foundations of genetic variation and quantitative trait analysis: Hardy–Weinberg, drift, selection, linkage disequilibrium, heritability and the breeder's equation, with R tutorials. By Peter Sørensen (Aarhus University).</p>
      <p class="cmeta">★ Self-paced · 🎓 MSc / advanced · 🔗 External site</p>
      <a class="btn green" href="https://psoerensen.github.io/qgteach/quant-genetics/" target="_blank" rel="noopener">Start the course →</a>
    </div>
""",
"phenomics": (
'    <div class="coursefeat">\n'
'      <span class="tagc">Featured course</span>\n'
'      <h4>AI &amp; Computer Vision in Animal Breeding</h4>\n'
'      <p>A self-paced short course: big data, machine learning, image processing, deep learning and high-throughput phenotyping, with two hands-on Python labs.</p>\n'
'      <p class="cmeta">★ Self-paced &middot; ⏱ ~6 hours &middot; 🎓 MSc level &middot; 🧪 2 labs</p>\n'
'      <a class="btn green" href="course-ai-animal-breeding.html">Start the course &#8594;</a>\n'
'    </div>\n'),
"multiomics": (
'    <div class="coursefeat">\n'
'      <span class="tagc">Featured course</span>\n'
'      <h4>AI-Driven Variant Discovery &amp; Genomic Prediction</h4>\n'
'      <p>A self-paced course on how AI finds impactful DNA variants, from sequence conservation to protein language models, and uses them to sharpen genomic prediction and guide genome editing.</p>\n'
'      <p class="cmeta">★ Self-paced &middot; ⏱ ~3.5 hours &middot; 🎓 MSc / advanced</p>\n'
'      <a class="btn green" href="course-ai-genomics-breeding.html">Start the course &#8594;</a>\n'
'    </div>\n'
'    <div class="coursefeat">\n'
'      <span class="tagc">Featured course</span>\n'
'      <h4>Quantitative Genetics</h4>\n'
'      <p>Foundations of quantitative trait analysis: means and variances, additive and dominance components, heritability, and response to selection. Course and slides by Peter Sørensen (Aarhus University).</p>\n'
'      <p class="cmeta">★ Self-paced · 🎓 MSc / advanced · 🔗 External site</p>\n'
'      <a class="btn green" href="https://psoerensen.github.io/quantitative-genetics/" target="_blank" rel="noopener">Start the course &#8594;</a>\n'
'    </div>\n'
'    <div class="coursefeat">\n'
'      <span class="tagc">Featured course</span>\n'
'      <h4>Genomics, Systems Biology &amp; Bioinformatics</h4>\n'
'      <p>Molecular data integration and computational modeling: sequencing and omics technologies, GWAS and fine-mapping, multi-omics and eQTL, gene networks, and high-dimensional methods in R. By Peter Sørensen (Aarhus University).</p>\n'
'      <p class="cmeta">★ Self-paced · 🎓 MSc / advanced · 🔗 External site</p>\n'
'      <a class="btn green" href="https://psoerensen.github.io/qgteach/genomics-systems-bioinfo/" target="_blank" rel="noopener">Start the course &#8594;</a>\n'
'    </div>\n'),
}

kh_themes = [
 ("multiomics","Multi-omics","Genomics, statistical genetics, transcriptomics, proteomics, metabolomics, microbiomics, and bioinformatics pipelines for livestock."),
 ("phenomics","Digitalization and phenomics","Precision livestock farming, sensor technologies, and AI and machine-learning applications in animal production systems."),
 ("nutrition","Nutrition and feed systems","Sustainable, climate-smart feeding strategies and feed efficiency adapted to East African production environments."),
 ("onehealth","One Health","The interface of animal, human and environmental health within the ISAPS curriculum."),
 ("biodiversity","Biodiversity and Breeding programs","Biodiversity, breeding programmes, climate resilience, value chains, socio-economics and greenhouse-gas mitigation."),
]
def kh_theme(key,title,desc,n):
    return ('<details class="theme" id="t-'+key+'">\n'
      '  <summary><span class="thn">'+str(n)+'</span><span class="tht">'+title+'</span><span class="chev">▾</span></summary>\n'
      '  <div class="theme-body">\n'
      '    <p class="tdesc">'+desc+'</p>\n'+COURSE_CARDS.get(key,"")+
      '    <details class="sub" open>\n'
      '      <summary>\U0001F3AC Video lectures</summary>\n'
      '      <div class="subbody">\n'
      '        <div class="videowrap"><video controls preload="none" poster="assets/video-poster.png">\n'
      '          <source src="assets/videos/'+key+'-1.mp4" type="video/mp4">\n'
      '          Your browser does not support embedded video.\n'
      '        </video></div>\n'
            '      </div>\n'
      '    </details>\n'
      '    <details class="sub">\n'
      '      <summary>\U0001F4DA Reading list &amp; key resources</summary>\n'
      '      <div class="subbody"><p class="soon">Curated open-access readings and references for this theme will be published here as the platform is populated. In the meantime, explore related free courses on the <a href="https://elearning.fao.org/" target="_blank" rel="noopener">FAO e-learning Academy &#8594;</a></p></div>\n'
      '    </details>\n'
      '    <details class="sub">\n'
      '      <summary>\U0001F4CA Teaching materials &amp; slides</summary>\n'
      '      <div class="subbody"><p class="soon">Lecture slide decks, regional case studies and downloadable teaching materials co-developed by the partners will be shared here under an open-access licence.</p></div>\n'
      '    </details>\n'
      '  </div>\n'
      '</details>')

kh_accordions = "\n".join(kh_theme(k,t,d,i+1) for i,(k,t,d) in enumerate(kh_themes))
kh_quick = "".join('<a href="#t-'+k+'">'+t+'</a>' for k,t,d in kh_themes)

knowledge = head("Knowledge Hub","knowledge.html","The ASAP-Bio Knowledge Hub: an open-access digital platform of lectures, teaching materials and resources across five ISAPS themes, integrating the FAO e-learning Academy.") + pagehdr(
  "Knowledge Hub","An open-access digital platform for sharing lectures, teaching materials and resources across the five ISAPS themes, co-created by the partners and open to all.") + ("""
<section><div class="wrap">
  <p class="lead">The Hub is organised by ISAPS theme. Each theme opens to reveal video lectures, reading lists and teaching materials. All content is open-access and free to use.</p>
  <div class="khquick">__QUICK__</div>
</div></section>
<section class="alt"><div class="wrap">
  <h2>Browse by theme</h2>
  <p class="lead">Select a theme to expand it, then open the sections inside.</p>
  <div style="margin-top:18px">__ACC__</div>
  <div class="callout gold" style="margin-top:24px"><strong>The Hub is being built.</strong> The platform launches in pilot form in late 2026 and grows as the partnership produces content. Materials are shared under an open-access licence.</div>
</div></section>
<section><div class="wrap">
  <div class="faobox">
    <img class="faologo" src="assets/logo-fao.png" alt="FAO e-learning Academy logo" onerror="this.style.display=\'none\'">
    <div class="faotext">
      <h3>FAO e-learning Academy</h3>
      <p>ASAP-Bio partners with FAO to augment its own materials with 500+ free, multilingual, certified courses in agriculture, food security and sustainability.</p>
      <a class="btn green" href="https://elearning.fao.org/" target="_blank" rel="noopener">Visit the FAO e-learning Academy &#8594;</a>
    </div>
  </div>
</div></section>
<script>document.querySelectorAll(".khquick a").forEach(function(a){a.addEventListener("click",function(){var t=document.querySelector(a.getAttribute("href"));if(t){t.open=true;}});});</script>
""".replace("__QUICK__",kh_quick).replace("__ACC__",kh_accordions)) + FOOT
write("knowledge.html", knowledge)


# ---------------- COURSE: AI & Computer Vision in Animal Breeding ----------------
course = head("AI &amp; Computer Vision in Animal Breeding","knowledge.html","A self-paced ASAP-Bio short course on big data, machine learning, computer vision and deep learning applied to animal breeding.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Digitalization and phenomics</div>
  <h1>AI &amp; Computer Vision in Animal Breeding</h1>
  <p class="csub">From big data and machine learning to deep learning and high-throughput phenotyping, how artificial intelligence is reshaping the way we measure animals and make breeding decisions.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~6 hours</span><span>🎓 MSc level</span><span>🧪 2 hands-on Python labs</span><span>🌍 Open access</span>
  </div>
</div></section>

<section><div class="wrap">
  <div class="attrib"><strong>About this course.</strong> This self-paced course adapts a one-day intensive class delivered by <strong>Grum Gebreyesus</strong> (Center for Quantitative Genetics and Genomics, Aarhus University) under ASAP-Bio. It has been restructured for online self-study: read each module at your own pace, try the knowledge checks, and run the labs in your browser.</div>

  <h3 style="margin-top:4px">Watch: course introduction</h3>
  <div class="videowrap" style="margin:6px 0 4px">
    <video controls preload="none" poster="assets/video-poster.png">
      <source src="assets/videos/course-ai-intro.mp4" type="video/mp4">
      Your browser does not support embedded video.
    </video>
  </div>

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Explain what “big data” means in livestock and why genomic and sensor data need different statistical tools.</li>
    <li>Describe the digital-agriculture data pipeline, from sensors to on-farm decisions.</li>
    <li>Recognise the main machine-learning methods, neural networks, support vector machines and tree ensembles, and when to use them.</li>
    <li>Understand how digital images are formed and processed, and how convolution extracts information.</li>
    <li>Explain how deep learning and convolutional neural networks (CNNs) learn from images.</li>
    <li>Connect computer vision and high-throughput phenotyping to real breeding applications.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#m1">1 · Big data in livestock</a>
    <a href="#m2">2 · Digital agriculture &amp; PLF</a>
    <a href="#m3">3 · Machine learning</a>
    <a href="#m4">4 · Image processing</a>
    <a href="#m5">5 · Deep learning &amp; CNNs</a>
    <a href="#m6">6 · Phenotyping &amp; breeding</a>
    <a href="#m7">7 · Wrap-up &amp; resources</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <!-- MODULE 1 -->
  <div class="module" id="m1">
    <div class="module-head"><div class="module-num">1</div><div><h2>Big data and data science in livestock</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>State the “5 Vs” of big data and give livestock examples.</li>
      <li>Distinguish <em>tall</em> from <em>wide</em> data and explain why each needs different methods.</li>
      <li>Place breeding's classic mixed model in the modern multi-omics context.</li></ul></div>
    <p>Livestock science has become a <strong>data science</strong>. Milking robots, wearable sensors, cameras, genotyping chips and weather stations now generate streams of data on every animal, every day. “Big data” is usually described by the <strong>5 Vs</strong>: <em>Volume</em> (how much), <em>Velocity</em> (how fast it arrives), <em>Variety</em> (tabular, images, sound, sequence), <em>Veracity</em> (how trustworthy) and <em>Value</em> (what decision it supports).</p>
    <p>Not all big data is big in the same way. <strong>Tall data</strong> has many observations and relatively few variables, classical statistics works well and significance is easy to reach. <strong>Wide data</strong> is the “big <em>p</em>, small <em>n</em>” world: far more variables than animals, as when each animal carries hundreds of thousands of genetic markers. Here ordinary regression breaks down (collinearity, multiple testing, overfitting), so we turn to <strong>penalised / regularised regression</strong> and <strong>dimension-reduction</strong> techniques.</p>
    <div class="kc"><strong class="kclabel">Key concept · big p, small n</strong>When you have more predictors than observations, a model can fit the training data perfectly yet predict new animals badly. Regularisation (shrinking coefficients) and reducing dimensions are how we keep predictions honest.</div>
    <p>Animal breeding's workhorse is the <strong>mixed model</strong>, <em>y = Xβ + Zu + e</em>, separating fixed effects (e.g. herd-year-season) from random genetic merit (breeding values). Genomics made this model “wide”; multi-omics (transcriptomics, proteomics, microbiomics) is widening it further. AI does not replace this framework, it extends our ability to use messy, high-dimensional data within it.</p>
    <div class="figbox">
      <svg viewBox="0 0 720 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Data to decisions pipeline">
        <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="14" text-anchor="middle">
          <rect x="10" y="40" width="150" height="50" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="85" y="62">Descriptive</text><text x="85" y="80" font-size="11" fill="#5f6b62">what happened</text>
          <rect x="190" y="40" width="150" height="50" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="265" y="62">Predictive</text><text x="265" y="80" font-size="11" fill="#5f6b62">what will happen</text>
          <rect x="370" y="40" width="150" height="50" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="445" y="62">Prescriptive</text><text x="445" y="80" font-size="11" fill="#5f6b62">what to do</text>
          <rect x="550" y="40" width="160" height="50" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="630" y="62">Optimisation</text><text x="630" y="80" font-size="11" fill="#5f6b62">best decision</text>
          <line x1="162" y1="65" x2="186" y2="65" stroke="#2E6B3E" stroke-width="2" marker-end="url(#ar)"/>
          <line x1="342" y1="65" x2="366" y2="65" stroke="#2E6B3E" stroke-width="2" marker-end="url(#ar)"/>
          <line x1="522" y1="65" x2="546" y2="65" stroke="#2E6B3E" stroke-width="2" marker-end="url(#ar)"/>
          <text x="360" y="22" font-size="13" fill="#1F4A2B" font-weight="bold">From data to decisions</text>
        </g>
      </svg>
      <figcaption>Analytics maturity: data becomes valuable as we move from describing the past to optimising future decisions.</figcaption>
    </div>
    <details class="quiz"><summary>Check: a genomic dataset has 2,000 animals and 600,000 SNP markers. Tall or wide?</summary><div class="ans"><strong>Wide</strong>, far more variables (markers) than observations (animals). This “big p, small n” setting calls for regularised methods such as ridge/LASSO or genomic BLUP, not ordinary least squares.</div></details>
  </div>

  <!-- MODULE 2 -->
  <div class="module" id="m2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Digital agriculture &amp; precision livestock farming</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define digital agriculture and precision livestock farming (PLF).</li>
      <li>Describe the pipeline: collect → store → analyse → visualise → decide.</li>
      <li>Explain why animal identification is the foundation of on-farm computer vision.</li></ul></div>
    <p><strong>Digital agriculture</strong> combines sensors, communication networks, drones (UAVs), robotic machinery, data analytics and AI to manage farms more precisely. Applied to animals, this is <strong>precision livestock farming (PLF)</strong>: continuous, automated, individual-level monitoring.</p>
    <p>The value chain is a pipeline: <strong>collect</strong> data (wearables, cameras, milk meters), <strong>store</strong> it (structured tables and unstructured images/sound), <strong>analyse</strong> it, <strong>visualise</strong> it (dashboards, alerts), and turn it into <strong>smart decisions</strong>. Among all sensing technologies, <strong>wearable accelerometers</strong> are the most common, and animal <strong>behaviour</strong> (activity, rumination, oestrus) is the most-collected phenotype, but cameras are rising fast because a single image can be extraordinarily informative.</p>
    <div class="kc"><strong class="kclabel">Key concept · animal identification</strong>Almost every on-farm vision system must first answer “which animal is this?”. Ear tags and RFID do this today; increasingly, 2D and 3D images identify animals directly. Identification is hardest when animals share the same colour, one reason depth (3D) cameras are valuable.</div>
    <details class="quiz"><summary>Check: why is animal identification described as the foundation of computer-vision systems on farm?</summary><div class="ans">Because individual-level decisions (genetic merit, health, feeding, traceability) require linking each measurement to the right animal. Without reliable identity, an informative image can't be used for management or breeding.</div></details>
  </div>

  <!-- MODULE 3 -->
  <div class="module" id="m3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Machine learning methods</h2><div class="module-time">~55 minutes · includes a lab</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Distinguish supervised from unsupervised learning.</li>
      <li>Explain neural networks, support vector machines and tree-based ensembles at a working level.</li>
      <li>Recognise overfitting and the tools used to control it.</li></ul></div>
    <p>A charming starting point is Francis Galton's 1906 observation that the average guess of 800 fair-goers estimated an ox's weight almost perfectly, the <strong>“wisdom of crowds.”</strong> Modern <strong>ensemble methods</strong> use the same idea: many weak models combined beat any single one.</p>
    <p><strong>Supervised</strong> learning predicts a labelled outcome (e.g. body weight) from inputs; <strong>unsupervised</strong> learning finds structure without labels (e.g. clustering animals). Three families dominate:</p>
    <p><strong>Artificial neural networks (ANNs)</strong> are flexible non-linear regressions inspired by the brain: inputs feed weighted <em>hidden units</em>, an <em>activation function</em> (sigmoid, tanh, ReLU) adds non-linearity, and <em>back-propagation</em> tunes the weights. ANNs easily <strong>overfit</strong>, so we use <em>early stopping</em> and <em>weight decay</em> (regularisation).</p>
    <div class="figbox">
      <svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Neural network with one hidden layer">
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <g stroke="#bcd0c2" stroke-width="1.5">
            <line x1="90" y1="50" x2="250" y2="40"/><line x1="90" y1="50" x2="250" y2="100"/><line x1="90" y1="50" x2="250" y2="160"/><line x1="90" y1="50" x2="250" y2="200"/>
            <line x1="90" y1="115" x2="250" y2="40"/><line x1="90" y1="115" x2="250" y2="100"/><line x1="90" y1="115" x2="250" y2="160"/><line x1="90" y1="115" x2="250" y2="200"/>
            <line x1="90" y1="180" x2="250" y2="40"/><line x1="90" y1="180" x2="250" y2="100"/><line x1="90" y1="180" x2="250" y2="160"/><line x1="90" y1="180" x2="250" y2="200"/>
            <line x1="250" y1="40" x2="430" y2="115"/><line x1="250" y1="100" x2="430" y2="115"/><line x1="250" y1="160" x2="430" y2="115"/><line x1="250" y1="200" x2="430" y2="115"/>
          </g>
          <g fill="#2E6B3E"><circle cx="90" cy="50" r="16"/><circle cx="90" cy="115" r="16"/><circle cx="90" cy="180" r="16"/></g>
          <g fill="#3E7CB1"><circle cx="250" cy="40" r="16"/><circle cx="250" cy="100" r="16"/><circle cx="250" cy="160" r="16"/><circle cx="250" cy="200" r="16"/></g>
          <circle cx="430" cy="115" r="18" fill="#C8962A"/>
          <text x="90" y="210" fill="#1F4A2B">inputs (x)</text><text x="250" y="226" fill="#1F4A2B">hidden units</text><text x="430" y="150" fill="#1F4A2B">output (ŷ)</text>
        </g>
      </svg>
      <figcaption>A feed-forward neural network with one hidden layer: inputs are combined, transformed by an activation function, and mapped to a prediction.</figcaption>
    </div>
    <p><strong>Support vector machines (SVMs)</strong> find the boundary with the widest <em>margin</em> between classes; the <em>“kernel trick”</em> lets them draw curved boundaries for data that aren't linearly separable. <strong>Decision trees</strong> split data with nested if-then rules; on their own they're unstable, so we combine many: <strong>bagging</strong>, <strong>random forests</strong> (each tree sees a random subset of predictors) and <strong>boosting</strong> (each model fixes the previous one's mistakes).</p>
    <div class="kc"><strong class="kclabel">Key concept · overfitting</strong>A model that memorises the training data fails on new animals. Cross-validation, regularisation, early stopping and ensembling all exist to keep models general.</div>
    <div class="labcard">
      <h4>🧪 Lab 1, Machine learning on real cull-cow data</h4>
      <p>Using the <code>CullDairyCow</code> dataset (401 cows: lactation, health events, 305-day production, body weight and price), build and compare <strong>partial least squares</strong>, <strong>ridge regression</strong> and a <strong>neural network</strong> in Python. You'll one-hot encode variables, split train/test, tune with grid search, and evaluate predictions. Runs free in your browser, no installation.</p>
      <a class="colab" href="https://colab.research.google.com/github/GGlivePh/QG/blob/main/Lab03.ipynb" target="_blank" rel="noopener">▶ Open Lab 1 in Google Colab</a>
      <p class="cmeta" style="margin-top:10px">Dataset: <a href="assets/course/CullDairyCow_Data.csv" download>CullDairyCow_Data.csv</a></p>
    </div>
    <details class="quiz"><summary>Check: a random forest and boosting both combine many trees. What's the key difference?</summary><div class="ans">A <strong>random forest</strong> builds trees independently in parallel on bootstrap samples (with random predictor subsets) and averages them. <strong>Boosting</strong> builds trees sequentially, each one giving more weight to the cases the previous trees got wrong.</div></details>
  </div>

  <!-- MODULE 4 -->
  <div class="module" id="m4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Image processing &amp; computer vision basics</h2><div class="module-time">~45 minutes · includes a lab</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain how a digital image is formed and stored as numbers.</li>
      <li>Read an image as a matrix of pixels and channels (RGB), and bit depth.</li>
      <li>Apply point operators and linear filters, and define convolution.</li></ul></div>
    <p>Computer vision works because <strong>an organism's status, health, growth, behaviour, leaves visually distinguishable cues</strong>. Light is electromagnetic radiation; cameras (CCD or CMOS sensors with a Bayer filter) turn it into numbers. The eye sees colour through three cone types (sensitive to red, green, blue), and digital images mimic this with <strong>RGB channels</strong>.</p>
    <p>An image is simply a <strong>matrix of numbers</strong>: a black-and-white image is one binary matrix, a grayscale image one matrix of intensities, and a colour image three stacked matrices (R, G, B). <strong>Bit depth</strong> sets how many levels each pixel can take, 8-bit gives 2⁸ = 256 levels, 16-bit gives 65,536.</p>
    <div class="figbox">
      <svg viewBox="0 0 660 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Image as a matrix and convolution with a kernel">
        <defs><marker id="ar2" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <text x="80" y="22" font-weight="bold" fill="#1F4A2B">Image = pixels</text>
          <g stroke="#9bb6a3" fill="#EEF3EC">
            <rect x="20" y="35" width="30" height="30"/><rect x="50" y="35" width="30" height="30"/><rect x="80" y="35" width="30" height="30"/><rect x="110" y="35" width="30" height="30"/>
            <rect x="20" y="65" width="30" height="30"/><rect x="50" y="65" width="30" height="30" fill="#2E6B3E"/><rect x="80" y="65" width="30" height="30" fill="#2E6B3E"/><rect x="110" y="65" width="30" height="30"/>
            <rect x="20" y="95" width="30" height="30"/><rect x="50" y="95" width="30" height="30" fill="#2E6B3E"/><rect x="80" y="95" width="30" height="30" fill="#2E6B3E"/><rect x="110" y="95" width="30" height="30"/>
            <rect x="20" y="125" width="30" height="30"/><rect x="50" y="125" width="30" height="30"/><rect x="80" y="125" width="30" height="30"/><rect x="110" y="125" width="30" height="30"/>
          </g>
          <text x="290" y="22" font-weight="bold" fill="#1F4A2B">Kernel (filter)</text>
          <g stroke="#C8962A" fill="#FBF3E3"><rect x="250" y="70" width="30" height="30"/><rect x="280" y="70" width="30" height="30"/><rect x="310" y="70" width="30" height="30"/>
          <rect x="250" y="100" width="30" height="30"/><rect x="280" y="100" width="30" height="30"/><rect x="310" y="100" width="30" height="30"/>
          <rect x="250" y="130" width="30" height="30"/><rect x="280" y="130" width="30" height="30"/><rect x="310" y="130" width="30" height="30"/></g>
          <text x="295" y="180" font-size="11" fill="#5f6b62">slides across the image</text>
          <line x1="350" y1="115" x2="430" y2="115" stroke="#2E6B3E" stroke-width="2" marker-end="url(#ar2)"/>
          <text x="392" y="105" font-size="11" fill="#5f6b62">convolution</text>
          <text x="560" y="22" font-weight="bold" fill="#1F4A2B">Feature map</text>
          <g stroke="#9bb6a3" fill="#E3EEF6"><rect x="500" y="55" width="36" height="36"/><rect x="536" y="55" width="36" height="36"/><rect x="572" y="55" width="36" height="36"/>
          <rect x="500" y="91" width="36" height="36" fill="#3E7CB1"/><rect x="536" y="91" width="36" height="36" fill="#3E7CB1"/><rect x="572" y="91" width="36" height="36"/>
          <rect x="500" y="127" width="36" height="36"/><rect x="536" y="127" width="36" height="36"/><rect x="572" y="127" width="36" height="36"/></g>
          <text x="554" y="185" font-size="11" fill="#5f6b62">edges / textures highlighted</text>
        </g>
      </svg>
      <figcaption>Convolution slides a small kernel across the pixel matrix; different kernels blur, sharpen or detect edges, the same operation a CNN learns automatically.</figcaption>
    </div>
    <p>Processing an image means applying <strong>operators</strong>. A <em>point operator</em> changes each pixel on its own (e.g. brightness scaling). A <em>linear filter</em> combines each pixel with its neighbours using a small grid of weights called a <strong>kernel</strong>, this operation is <strong>convolution</strong>, and it can blur (mean filter), sharpen, or detect edges depending on the kernel. Hold onto this idea: it is the heart of the deep-learning module.</p>
    <div class="labcard">
      <h4>🧪 Lab 2, Image processing in Python</h4>
      <p>Load an image, inspect its size and pixel statistics per channel, plot RGB histograms, and apply point operators and convolution filters (brightness, blur, sharpen, edge detection) to see how kernels transform an image.</p>
      <a class="colab" href="https://colab.research.google.com/github/GGlivePh/QG/blob/main/ImageAnalysis.ipynb" target="_blank" rel="noopener">▶ Open Lab 2 in Google Colab</a>
    </div>
    <details class="quiz"><summary>Check: how many numbers represent one pixel in an 8-bit RGB image, and what is each one's range?</summary><div class="ans">Three numbers, one per channel (R, G, B), each ranging 0–255 (2⁸ levels).</div></details>
  </div>

  <!-- MODULE 5 -->
  <div class="module" id="m5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Deep learning &amp; convolutional neural networks</h2><div class="module-time">~55 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Trace the path from a single perceptron to a deep network.</li>
      <li>Explain loss, gradient descent, back-propagation and regularisation.</li>
      <li>Describe what convolutional and pooling layers do, and why CNNs suit images.</li></ul></div>
    <p>A <strong>perceptron</strong> is a single artificial neuron: it weights its inputs, sums them, and passes the result through an <strong>activation function</strong> (sigmoid, tanh, ReLU) that introduces non-linearity. Stack many neurons in many layers and you have a <strong>deep neural network</strong>.</p>
    <p>Networks <strong>learn</strong> by minimising a <strong>loss function</strong>, mean squared error for continuous traits, cross-entropy for classification. <strong>Gradient descent</strong> nudges the weights downhill on the loss surface, and <strong>back-propagation</strong> efficiently computes those gradients layer by layer. Because deep models overfit readily, we apply <strong>dropout</strong> (randomly switching off connections during training) and <strong>early stopping</strong> (halting when validation performance stops improving).</p>
    <p>For images we use <strong>convolutional neural networks (CNNs)</strong>. Instead of hand-designing filters (Module 4), a CNN <em>learns</em> the kernels from data. <strong>Convolutional layers</strong> detect local patterns (edges → textures → parts → objects); <strong>pooling layers</strong> downsample to add robustness; a final dense layer turns the learned features into a prediction.</p>
    <div class="figbox">
      <svg viewBox="0 0 720 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CNN pipeline">
        <defs><marker id="ar3" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="11.5" text-anchor="middle">
          <rect x="10" y="50" width="70" height="55" rx="6" fill="#EEF3EC" stroke="#2E6B3E"/><text x="45" y="74">Input</text><text x="45" y="90">image</text>
          <rect x="105" y="50" width="80" height="55" rx="6" fill="#E3EEF6" stroke="#3E7CB1"/><text x="145" y="74">Conv</text><text x="145" y="90" font-size="10" fill="#5f6b62">learn filters</text>
          <rect x="210" y="50" width="80" height="55" rx="6" fill="#EEF3EC" stroke="#2E6B3E"/><text x="250" y="74">Pool</text><text x="250" y="90" font-size="10" fill="#5f6b62">downsample</text>
          <rect x="315" y="50" width="80" height="55" rx="6" fill="#E3EEF6" stroke="#3E7CB1"/><text x="355" y="74">Conv</text>
          <rect x="420" y="50" width="80" height="55" rx="6" fill="#EEF3EC" stroke="#2E6B3E"/><text x="460" y="74">Pool</text>
          <rect x="525" y="50" width="80" height="55" rx="6" fill="#f0eef6" stroke="#7E6BAE"/><text x="565" y="74">Flatten +</text><text x="565" y="90">Dense</text>
          <rect x="630" y="50" width="80" height="55" rx="6" fill="#FBF3E3" stroke="#C8962A"/><text x="670" y="74">Output</text><text x="670" y="90" font-size="10" fill="#5f6b62">trait / class</text>
          <g stroke="#2E6B3E" stroke-width="2">
            <line x1="82" y1="77" x2="103" y2="77" marker-end="url(#ar3)"/><line x1="187" y1="77" x2="208" y2="77" marker-end="url(#ar3)"/>
            <line x1="292" y1="77" x2="313" y2="77" marker-end="url(#ar3)"/><line x1="397" y1="77" x2="418" y2="77" marker-end="url(#ar3)"/>
            <line x1="502" y1="77" x2="523" y2="77" marker-end="url(#ar3)"/><line x1="607" y1="77" x2="628" y2="77" marker-end="url(#ar3)"/>
          </g>
          <text x="360" y="28" font-size="12.5" font-weight="bold" fill="#1F4A2B">A convolutional neural network for image-based phenotyping</text>
        </g>
      </svg>
      <figcaption>A CNN learns its own filters: convolution and pooling layers build up from edges to whole-animal features, ending in a prediction such as body condition score.</figcaption>
    </div>
    <div class="kc"><strong class="kclabel">Key concept · learned vs hand-crafted features</strong>The big shift deep learning brought is that the model discovers the useful image features itself, instead of an expert designing them. This is why CNNs outperform classical methods on hard, unstructured images, at the cost of needing more data and GPU computing.</div>
    <details class="quiz"><summary>Check: what is the role of a pooling layer in a CNN?</summary><div class="ans">Pooling downsamples the feature maps (e.g. taking the maximum in each small region). It shrinks the data, reduces computation, and makes the network more robust to small shifts in where a feature appears in the image (translation invariance).</div></details>
  </div>

  <!-- MODULE 6 -->
  <div class="module" id="m6">
    <div class="module-head"><div class="module-num">6</div><div><h2>High-throughput phenotyping &amp; breeding applications</h2><div class="module-time">~45 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define high-throughput phenotyping (HTP) and the qualities of a good phenotype.</li>
      <li>Give concrete examples of computer vision in animal breeding.</li>
      <li>Explain enviromics and genotype-by-environment interaction (G×E).</li></ul></div>
    <p>The phenotype equation is simple to state and hard to satisfy: <strong>Phenotype = Genetics + Environment</strong>. Genomics gave us cheap genotypes; the bottleneck moved to <strong>phenotypes</strong>. <strong>High-throughput phenotyping</strong> uses cameras, wearable sensors, robots and drones to measure many animals, often and cheaply. A <em>good</em> phenotype is accurate and precise, measured non-invasively, and scalable to thousands of animals at low cost.</p>
    <p>Computer vision now delivers traits that were once subjective or labour-intensive:</p>
    <ul>
      <li><strong>Body weight &amp; growth</strong>, continuous monitoring of cattle weight and energy balance from images.</li>
      <li><strong>Body condition score</strong>, from 3-D images at &gt;90% accuracy, a key health, welfare and feed-efficiency indicator.</li>
      <li><strong>Black soldier fly larvae</strong>, automated weight and sex prediction (YOLOv8 detection) for insect production.</li>
      <li><strong>Ribeye area &amp; carcass shape</strong> in live calves from 3-D body shape.</li>
      <li><strong>Parasite detection</strong>, reading the ocular conjunctiva (FAMACHA) to flag parasitised sheep, removing human subjectivity.</li>
      <li><strong>Identification &amp; behaviour</strong>, recognising individuals and their feeding behaviour without tags.</li>
    </ul>
    <p>Sensors also describe the <strong>environment</strong>. <strong>Enviromics</strong> uses farm- and region-level environmental descriptors to study <strong>genotype-by-environment interaction (G×E)</strong>, why the best animals in one system are not the best in another, a central question for breeding programmes across the diverse environments of East Africa and Denmark.</p>
    <div class="kc"><strong class="kclabel">Why this matters for breeding</strong>Cheaper, larger-scale, more objective phenotypes mean more animals with records, novel traits (welfare, efficiency, resilience), and more accurate breeding values, the raw material of genetic progress.</div>
    <details class="quiz"><summary>Check: HTP is often called a solution to a “bottleneck.” Which bottleneck, and why?</summary><div class="ans">The <strong>phenotyping bottleneck</strong>. Genotyping became fast and cheap, so the limiting factor for genetic evaluation is now collecting enough accurate phenotypes. HTP (sensors and computer vision) relieves this by measuring many animals automatically.</div></details>
  </div>

  <!-- MODULE 7 -->
  <div class="module" id="m7">
    <div class="module-head"><div class="module-num">7</div><div><h2>Wrap-up &amp; resources</h2><div class="module-time">~10 minutes</div></div></div>
    <h3>Key takeaways</h3>
    <ul>
      <li>AI and machine learning let us use big data for prediction, interpretation and causal inference in breeding.</li>
      <li>Computer vision enables non-invasive, high-throughput phenotyping at large scale.</li>
      <li>Neural networks, SVMs and tree ensembles are the core ML tools; CNNs are the workhorse for images.</li>
      <li>The payoff for breeding is more, better and cheaper phenotypes, and therefore faster, fairer genetic progress.</li>
    </ul>
    <h3 style="margin-top:24px">Glossary</h3>
    <div class="gloss">
      <div><b>5 Vs</b>, Volume, Velocity, Variety, Veracity, Value: the dimensions of big data.</div>
      <div><b>Tall / Wide data</b>, many observations vs many variables (“big p, small n”).</div>
      <div><b>Regularisation</b>, shrinking model complexity (ridge, LASSO, weight decay) to avoid overfitting.</div>
      <div><b>Activation function</b>, non-linear transform in a neuron (sigmoid, tanh, ReLU).</div>
      <div><b>Back-propagation</b>, algorithm to compute gradients for training neural networks.</div>
      <div><b>Kernel / convolution</b>, a small weight grid slid across an image to extract features.</div>
      <div><b>CNN</b>, convolutional neural network; learns image filters automatically.</div>
      <div><b>Pooling</b>, downsampling step that adds robustness and reduces computation.</div>
      <div><b>HTP</b>, high-throughput phenotyping: measuring many animals automatically.</div>
      <div><b>Enviromics / G×E</b>, using environmental data to study genotype-by-environment interaction.</div>
    </div>
    <h3 style="margin-top:24px">Further reading &amp; resources</h3>
    <ul>
      <li>Gianola, D. &amp; Rosa, G. J. M. (2015). One hundred years of statistical developments in animal breeding. <em>Annual Review of Animal Biosciences</em> 3:19–56.</li>
      <li>Kuhn, M. &amp; Johnson, K. <em>Applied Predictive Modeling.</em> Springer.</li>
      <li>Free, certified courses on data and sustainable agriculture at the <a href="https://elearning.fao.org/" target="_blank" rel="noopener">FAO e-learning Academy</a>.</li>
    </ul>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-ai-animal-breeding.html", course)


# ---------------- COURSE 2: AI-Driven Variant Discovery & Genomic Prediction (Multi-omics) ----------------
course2 = head("AI-Driven Variant Discovery &amp; Genomic Prediction","knowledge.html","A self-paced ASAP-Bio course on how AI finds impactful DNA variants and improves genomic prediction for animal and plant breeding.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Multi-omics</div>
  <h1>AI-Driven Variant Discovery &amp; Genomic Prediction</h1>
  <p class="csub">How artificial intelligence finds the DNA changes that actually matter, and uses them to predict performance and guide next-generation breeding.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~3.5 hours</span><span>🎓 MSc / advanced</span><span>🧬 Genomics focus</span><span>🌍 Open access</span>
  </div>
</div></section>

<section><div class="wrap">
  <div class="attrib"><strong>About this course.</strong> This course is based on the lecture <em>“Discovery of impactful variants by artificial intelligence to support next-generation breeding”</em> by <strong>Guillaume Ramstein</strong> (Tenure-Track Assistant Professor, Aarhus University), with quantitative-genetics framing from the ASAP-Bio AI module by Grum Gebreyesus (QGG, Aarhus University). It is designed for self-study and pairs well with the companion course on <a href="course-ai-animal-breeding.html">AI &amp; Computer Vision in Animal Breeding</a>.</div>

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Explain why discovering <em>impactful</em> genetic variants is a bottleneck in breeding.</li>
    <li>Compare mutant screens, association testing and computational screens on accuracy, resolution and cost.</li>
    <li>Describe how genomic prediction turns marker data into breeding values.</li>
    <li>Explain evolutionary scores from sequence conservation and from biological language models.</li>
    <li>Show how evolutionary scores improve genomic prediction and could guide single-base genome edits.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#g1">1 · The variant-discovery bottleneck</a>
    <a href="#g2">2 · Genomic prediction basics</a>
    <a href="#g3">3 · Evolutionary scores: conservation</a>
    <a href="#g4">4 · Evolutionary scores: language models</a>
    <a href="#g5">5 · Better prediction &amp; genome editing</a>
    <a href="#g6">6 · Wrap-up &amp; resources</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <!-- G1 -->
  <div class="module" id="g1">
    <div class="module-head"><div class="module-num">1</div><div><h2>The variant-discovery bottleneck</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain why finding impactful variants limits biological design and breeding.</li>
      <li>Compare three discovery strategies on accuracy, resolution and cost.</li></ul></div>
    <p>A genome contains millions of variants, but only a small fraction actually change a trait. Breeding and gene editing both depend on finding those <strong>impactful variants</strong>, and that discovery is the rate-limiting step. There are three broad strategies, each with a different trade-off:</p>
    <table class="t"><tr><th>Strategy</th><th>What it does</th><th>Accuracy</th><th>Resolution</th><th>Time &amp; cost</th></tr>
      <tr><td><strong>Mutant screens</strong></td><td>Create and test mutations experimentally</td><td>High</td><td>High</td><td>High</td></tr>
      <tr><td><strong>Association testing (GWAS)</strong></td><td>Correlate existing variation with traits</td><td>Moderate</td><td>Low</td><td>Moderate</td></tr>
      <tr><td><strong>Computational screens</strong></td><td>Predict impact from sequence with AI</td><td>The question</td><td>High</td><td>Low</td></tr>
    </table>
    <p>Association testing (genome-wide association studies) is powerful but blunt: because nearby variants are inherited together, a significant signal points to a <strong>recombination bin</strong> that can span hundreds of thousands of DNA bases (often ~300&nbsp;kb), not the causal base itself. We can see <em>where</em> an effect is, but not <em>which</em> variant causes it. That missing resolution is exactly what computational, AI-based screens promise to recover, cheaply.</p>
    <div class="kc"><strong class="kclabel">Key concept · resolution</strong>“Resolution” is how precisely a method pinpoints the causal variant. GWAS has low resolution (a broad region); the goal of AI variant discovery is single-base resolution at low cost.</div>
    <details class="quiz"><summary>Check: GWAS flags a region strongly associated with milk yield. Why can't you immediately edit the causal base?</summary><div class="ans">Because of <strong>linkage</strong>: variants in the region are inherited together, so the association points to a recombination bin (potentially ~300&nbsp;kb) rather than the single causal base. You know the neighbourhood, not the exact address.</div></details>
  </div>

  <!-- G2 -->
  <div class="module" id="g2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Genomic prediction in a nutshell</h2><div class="module-time">~35 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Write the mixed model used in animal breeding and name its parts.</li>
      <li>Explain genomic prediction and why marker data are “wide”.</li>
      <li>Say why not all markers should be treated equally.</li></ul></div>
    <p>Animal breeding predicts an animal's genetic merit (its <strong>breeding value</strong>) using the mixed model <strong>y = Xβ + Zu + e</strong>: observed performance <em>y</em> is split into fixed effects <em>β</em> (herd, year, season), random genetic merit <em>u</em> (the breeding values we want), and residual <em>e</em>. <strong>Genomic prediction</strong> replaces or augments pedigree with thousands to millions of DNA markers, building a genomic relationship between animals.</p>
    <p>Marker data are <strong>“wide”</strong>: far more markers (<em>p</em>) than animals (<em>n</em>), the “big <em>p</em>, small <em>n</em>” problem. Ordinary regression fails, so we use <strong>regularised</strong> methods (genomic BLUP, Bayesian models) that shrink marker effects. Standard genomic prediction implicitly assumes every marker contributes a little. But biology says otherwise: a handful of variants matter a lot, most matter not at all. If we could tell the model <em>which</em> variants are likely impactful, predictions should improve, and that is where evolutionary scores come in.</p>
    <div class="figbox">
      <svg viewBox="0 0 720 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Genomic prediction pipeline">
        <defs><marker id="gar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="10" y="45" width="150" height="60" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="85" y="70">Genotypes +</text><text x="85" y="88">phenotypes</text>
          <rect x="210" y="45" width="180" height="60" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="300" y="70">Prediction model</text><text x="300" y="88" font-size="10.5" fill="#5f6b62">(regularised; weighted)</text>
          <rect x="440" y="45" width="120" height="60" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="500" y="70">Breeding</text><text x="500" y="88">values (GEBV)</text>
          <rect x="610" y="45" width="100" height="60" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="660" y="70">Selection /</text><text x="660" y="88">editing</text>
          <line x1="162" y1="75" x2="208" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#gar)"/>
          <line x1="392" y1="75" x2="438" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#gar)"/>
          <line x1="562" y1="75" x2="608" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#gar)"/>
          <text x="300" y="130" font-size="11" fill="#5f6b62">evolutionary scores tell the model which variants to trust</text>
        </g>
      </svg>
      <figcaption>Genomic prediction turns genotype and phenotype data into breeding values; weighting variants by their likely impact can sharpen it.</figcaption>
    </div>
    <details class="quiz"><summary>Check: what does “big p, small n” mean for a genotyping dataset, and what's the fix?</summary><div class="ans">Far more markers (p) than animals (n). Ordinary regression overfits, so we use regularised/Bayesian methods (e.g. genomic BLUP) that shrink the many small marker effects.</div></details>
  </div>

  <!-- G3 -->
  <div class="module" id="g3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Evolutionary scores I: sequence conservation</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain how evolution “labels” important positions in the genome.</li>
      <li>Define an evolutionary score from a multiple-sequence alignment.</li></ul></div>
    <p>Evolution has already run a billion-year experiment. Positions in DNA or protein that are essential are kept the same across species by <strong>negative (purifying) selection</strong>, mutations there are harmful and get removed. Positions that don't matter drift freely. So <strong>conservation is a clue to function</strong>.</p>
    <p>We quantify this with a <strong>multiple-sequence alignment (MSA)</strong>: stack the same gene from many species and look down each column. A change at a highly conserved column gets a high <strong>evolutionary score</strong>, it is “abnormal” given evolution and therefore likely impactful. Across crops, variants flagged this way are enriched for real fitness effects (shown in sorghum and potato biomass studies).</p>
    <div class="figbox">
      <svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Multiple sequence alignment with a conserved column">
        <g font-family="Consolas,monospace" font-size="16" text-anchor="middle">
          <rect x="250" y="20" width="26" height="160" fill="#FBF3E3" stroke="#C8962A"/>
          <g fill="#1f2420">
            <text x="60" y="45">A T G C A</text><text x="263" y="45">A</text><text x="380" y="45">T C T C A</text>
            <text x="60" y="75">A T G C A</text><text x="263" y="75">A</text><text x="380" y="75">T C T C A</text>
            <text x="60" y="105">A T G C A</text><text x="263" y="105">A</text><text x="380" y="105">T C T C A</text>
            <text x="60" y="135">A T G C A</text><text x="263" y="135">A</text><text x="380" y="135">T C T C A</text>
            <text x="60" y="165" fill="#b3261e">A T G C A</text><text x="263" y="165" fill="#b3261e" font-weight="bold">G</text><text x="380" y="165" fill="#b3261e">T C T C A</text>
          </g>
          <text x="263" y="14" font-size="11" fill="#8a6516">conserved</text>
          <text x="430" y="165" font-size="12" fill="#b3261e" text-anchor="start">← mutation A→G</text>
          <text x="263" y="196" font-size="11" fill="#8a6516">high evolutionary score = likely impactful</text>
        </g>
      </svg>
      <figcaption>In a multiple-sequence alignment, a change at a column that evolution has kept constant scores high, a signal that the variant matters.</figcaption>
    </div>
    <div class="kc"><strong class="kclabel">Key concept · conservation ≈ importance</strong>If many species independently keep a position identical, changing it is probably harmful. Evolutionary conservation is a free, genome-wide functional annotation.</div>
    <details class="quiz"><summary>Check: a SNP sits at a position identical across 200 species. High or low evolutionary score, and why?</summary><div class="ans"><strong>High.</strong> Strong conservation implies negative selection has removed changes there, so the position is likely functional and a new mutation is likely impactful.</div></details>
  </div>

  <!-- G4 -->
  <div class="module" id="g4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Evolutionary scores II: biological language models</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain the analogy between human-language and protein-language models.</li>
      <li>Describe how a protein language model scores a mutation.</li></ul></div>
    <p>The same large-language-model technology behind modern AI can read biological sequence. Start with language: a model trained on text learns which word is expected next. In “a small caterpillar is born hungry and ____ everything in sight,” the model assigns <em>eats</em> 70%, <em>tastes</em> 25%, <em>reads</em> 4%. A change from “eats” to “reads” is flagged as <strong>abnormal</strong>, semantically wrong.</p>
    <p><strong>Protein language models</strong> do exactly this for amino-acid sequence. Trained on millions of natural protein sequences, they learn which residue belongs at each position. At a given site the model might predict R&nbsp;80%, Q&nbsp;10%, H&nbsp;8%, L&nbsp;2%. A mutation R→L lands on a very low-probability residue, so it scores as abnormal and likely impactful, without any alignment or labelled training data.</p>
    <div class="figbox">
      <svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Protein language model residue probabilities">
        <g font-family="Segoe UI,Arial" font-size="13">
          <text x="20" y="30" font-family="Consolas,monospace" font-size="15" fill="#1f2420">MAWAAGTVEH _ CILLNASPVERPGY…</text>
          <text x="186" y="50" font-size="11" fill="#5f6b62" text-anchor="middle">model predicts this position ↑</text>
          <g text-anchor="start">
            <text x="40" y="90">R</text><rect x="60" y="78" width="260" height="16" rx="3" fill="#2E6B3E"/><text x="330" y="90" fill="#1F4A2B">80%</text>
            <text x="40" y="116">Q</text><rect x="60" y="104" width="33" height="16" rx="3" fill="#3E7CB1"/><text x="100" y="116" fill="#225277">10%</text>
            <text x="40" y="142">H</text><rect x="60" y="130" width="26" height="16" rx="3" fill="#3E7CB1"/><text x="93" y="142" fill="#225277">8%</text>
            <text x="40" y="168">L</text><rect x="60" y="156" width="8" height="16" rx="3" fill="#b3261e"/><text x="75" y="168" fill="#b3261e">2%   ← mutation R→L is abnormal</text>
          </g>
        </g>
      </svg>
      <figcaption>A protein language model gives each residue a probability; a mutation to a very unlikely residue is flagged as impactful.</figcaption>
    </div>
    <details class="quiz"><summary>Check: why is a protein language model useful even when we have no labelled “good/bad” mutation data?</summary><div class="ans">It learns the “grammar” of natural proteins from millions of unlabelled sequences. Mutations that break that grammar (low-probability residues) are flagged as likely impactful, an <em>unsupervised</em> signal, no labels required.</div></details>
  </div>

  <!-- G5 -->
  <div class="module" id="g5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Better prediction &amp; the road to genome editing</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Give evidence that evolutionary scores improve genomic prediction.</li>
      <li>Explain how they could guide single-base genome edits (new genomic techniques).</li></ul></div>
    <p>Do these scores actually help? Yes. When variants are <strong>weighted by their evolutionary scores</strong> in genomic prediction, accuracy for fitness-related traits improves across species: up to ~20% for grain yield in maize, ~10% for cassava biomass, and up to ~25% for biomass in potato. Telling the model which variants to trust beats treating all markers equally.</p>
    <p>The bigger prize is <strong>new genomic techniques (NGT)</strong> such as precise single-base editing. To edit, you must know the <em>exact</em> causal base, the resolution GWAS lacks. Evolutionary scores can prioritise candidate single-base edits <em>in silico</em>, which are then checked by <em>experimental</em> mutagenesis. Proof-of-concept work in the model grass <em>Brachypodium</em> shows that mutations with the highest evolutionary scores have the largest effects on traits such as seed weight, evidence that AI can point editors at the right base.</p>
    <div class="kc"><strong class="kclabel">Concluding remarks</strong>Computational screens address the throughput limit of mutant screens and the resolution limit of association testing. Evolutionary scores from biological language models already improve genomic prediction; whether they can reliably target single bases for editing is the active research frontier.</div>
    <details class="quiz"><summary>Check: why is single-base resolution essential for genome editing but not for ordinary marker-assisted selection?</summary><div class="ans">Editing physically changes a specific base, so you must know the exact causal nucleotide. Marker-assisted selection only needs a marker <em>linked</em> to the causal variant, it selects existing animals/plants rather than rewriting the sequence.</div></details>
  </div>

  <!-- G6 -->
  <div class="module" id="g6">
    <div class="module-head"><div class="module-num">6</div><div><h2>Wrap-up &amp; resources</h2><div class="module-time">~10 minutes</div></div></div>
    <h3>Key takeaways</h3>
    <ul>
      <li>Finding <em>impactful</em> variants, not just associated regions, is the real bottleneck in genomic breeding.</li>
      <li>Evolution conserves what matters; conservation and language-model scores turn that into a usable, genome-wide signal.</li>
      <li>Weighting variants by evolutionary scores measurably improves genomic prediction.</li>
      <li>The same scores may one day guide precise single-base edits for next-generation breeding.</li>
    </ul>
    <h3 style="margin-top:24px">Discussion questions</h3>
    <details class="quiz"><summary>1. Where might evolutionary scores fail or mislead in a breeding programme?</summary><div class="ans">Conservation reflects fitness over evolutionary time, which may not match a breeder's specific goal (e.g. high yield under intensive management). A variant can be evolutionarily “abnormal” yet desirable in a managed system, or conserved yet irrelevant to the target trait. Scores are a prior, not a verdict.</div></details>
    <details class="quiz"><summary>2. How could ASAP-Bio partners combine high-throughput phenotyping (the companion course) with variant discovery?</summary><div class="ans">Better, larger-scale phenotypes raise the power of both association testing and the validation of computationally prioritised variants, more accurate trait data means evolutionary-score predictions can be tested and refined in local breeds and environments.</div></details>
    <h3 style="margin-top:24px">Glossary</h3>
    <div class="gloss">
      <div><b>Variant / allele</b>, a difference in DNA sequence between individuals.</div>
      <div><b>Mutant screen</b>, experimentally creating and testing mutations.</div>
      <div><b>Association testing (GWAS)</b>, correlating natural variation with traits.</div>
      <div><b>Resolution</b>, how precisely a method pinpoints the causal variant.</div>
      <div><b>Recombination bin</b>, a block of co-inherited variants (low GWAS resolution).</div>
      <div><b>Evolutionary score</b>, how “abnormal” a mutation is given evolution.</div>
      <div><b>Multiple-sequence alignment</b>, same gene from many species, stacked to read conservation.</div>
      <div><b>Negative selection</b>, removal of harmful mutations; the source of conservation.</div>
      <div><b>Protein language model</b>, AI trained on protein sequences to predict residues.</div>
      <div><b>Genomic prediction / GEBV</b>, predicting breeding values from markers.</div>
      <div><b>NGT</b>, new genomic techniques, e.g. precise single-base editing.</div>
    </div>
    <h3 style="margin-top:24px">Further reading &amp; resources</h3>
    <ul>
      <li>Ramstein, G. &amp; Buckler, E. (2022). Prediction of evolutionary constraint... <em>Genome Biology.</em></li>
      <li>Long et al. (2023). <em>Frontiers in Plant Science</em>, evolutionary-score-weighted prediction in cassava.</li>
      <li>Wu et al. (2023). <em>Cell</em>, deleterious variants and prediction in potato.</li>
      <li>Gianola, D. &amp; Rosa, G. J. M. (2015). One hundred years of statistical developments in animal breeding. <em>Annual Review of Animal Biosciences</em> 3:19–56.</li>
      <li>Free courses at the <a href="https://elearning.fao.org/" target="_blank" rel="noopener">FAO e-learning Academy</a>.</li>
    </ul>
    <div class="attrib" style="margin-top:18px"><strong>Credits.</strong> Based on the lecture <em>“Discovery of impactful variants by artificial intelligence to support next-generation breeding”</em> by Guillaume Ramstein (Aarhus University), adapted for self-study under ASAP-Bio with quantitative-genetics framing by Grum Gebreyesus (QGG, Aarhus University). Reproduced for educational use within the ASAP-Bio partnership.</div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-ai-genomics-breeding.html", course2)


# ---------------- COURSE 3: Breeding programs with Genomic selection (Biodiversity & Breeding) ----------------
GS_BASE="http://vps6371.xlshosting.net/GSwageningen/datafiles/"
def gslink(label, fname):
    return '<li><a href="'+GS_BASE+fname.replace(" ","%20")+'" target="_blank" rel="noopener">'+label+'</a></li>'
gs_day1=[("Lecture: Genomic Selection in Animal Breeding, part 1","GSwageningen_2014_Monday_lecture_GS_part_1.pdf"),
 ("Lecture: Genomic Selection in Animal Breeding, part 2","GSwageningen_2014_Monday_lecture_GS_part_2.pdf"),
 ("Lecture: Matrix calculations in Excel","GSwageningen_2014_Monday_lecture_Matrices_in_Excel.pdf"),
 ("Case + solutions: Power","GSwageningen_2014_Monday_Case_Power.pdf"),
 ("Case + Excel + solutions: Winner's Curse","GSwageningen_2014_Monday_Case_Winners_Curse.pdf"),
 ("Case + Excel + solutions: Genomic Selection","GSwageningen_2014_Monday_Case_Genomic_Selection_part1.pdf")]
gs_day2=[("Lecture: Relatedness and Variation in relatedness","GSwageningen_2014_Tuesday_lecture_Relatedness.pdf"),
 ("Lecture: Genomic and Pedigree Relationships, Mendelian Inconsistencies","GSwageningen_2014_Tuesday_Genomic_vs_Pedigree_relations.pdf"),
 ("Cases + solutions: Relatedness; Variation in Relatedness","GSwageningen_2014_Tuesday_Case_Relatedness.pdf")]
gs_day3=[("Lecture: Validation of Genomic Predictions","GSwageningen_2014_Wednesday_Lecture_ValidationGenomicPrediction.pdf"),
 ("Lecture: Design of Reference Populations","GSwageningen_2014_Wednesday_Lecture_DesignReferencePopulation.pdf"),
 ("Lecture: Factors Affecting Accuracy","GSwageningen_2014_Wednesday_Lecture_FactorsAffectingAccuracy"),
 ("Lecture: Across Breed Genomic Prediction","GSwageningen_2014_Wednesday_Lecture_AcrossBreed.pdf"),
 ("Lecture: The Daetwyler equation","GSwageningen_2014_Wednesday_Lecture_The Daetwyler equation.pdf"),
 ("Case + Excel + solutions: Accuracy and Bias","GSwageningen_2014_Wednesday_Exercise_CompAccuracy.docx")]
gs_day4=[("Lecture: Phenotypes used in Genomic Selection","GSwageningen_2014_Thursday_Lecture_PhenotypesUsedInGenomicSelection.pdf"),
 ("Lecture: Imputation of Genotype data","GSwageningen_2014_Thursday_Lecture_ImputationOfGenotypeData.pdf"),
 ("Case + data: Different BLUP methods","GSwageningen_2014_Thursday_Case_EvaluateDiffBLUPs.docx"),
 ("Case (Excel): Single Step Genomic Selection","GSwageningen_2014_Thursday_Case-SS-Genomic-selection.xlsx")]
gs_day5=[("Lecture: Breeding Programs with Genomic Selection","GSwageningen_2014_Friday_Lecture_Breeding_programs_with_genomic_selection.pdf"),
 ("Lecture: Genomic Change due to Selection","GSwageningen_2014_Friday_Lecture_Genomic_Change_due_to_Selection.pdf"),
 ("Exercises + solutions: SelAction (Dairy Cattle)","GSwageningen_2014_Friday_Exercise_SelAction_Dairy_Cattle.docx"),
 ("Exercises + solutions: SelAction (Pigs)","GSwageningen_2014_Friday_Exercise_SelAction_Pigs.docx")]
def gsblock(title, items):
    return '<h4 style="margin-top:14px;color:var(--greendk)">'+title+'</h4><ul>'+"".join(gslink(l,f) for l,f in items)+'</ul>'

course3 = head("Breeding programs with Genomic selection","knowledge.html","A self-paced ASAP-Bio course on genomic selection in animal breeding, from SNP chips and genomic breeding values to accuracy, breeding-program design and managing genetic diversity.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Biodiversity and Breeding programs</div>
  <h1>Breeding programs with Genomic selection</h1>
  <p class="csub">From SNP chips and genomic breeding values to the accuracy equation, breeding-program design and the genetic-diversity questions that genomic selection raises.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~5 hours</span><span>🎓 MSc / advanced</span><span>🧮 Excel &amp; SelAction exercises</span>
  </div>
</div></section>

<section><div class="wrap">
  

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Explain why genomic selection was introduced and where it beats traditional selection.</li>
    <li>Describe how genomic breeding values (GEBVs) are estimated, by SNP-BLUP, Bayesian methods and the genomic relationship matrix (GBLUP).</li>
    <li>Use the accuracy (Daetwyler) equation to reason about reference-population size, heritability and marker information.</li>
    <li>Design a reference population and choose phenotypes for genomic evaluation.</li>
    <li>Predict response to selection in a breeding program that uses GEBVs, accounting for the Bulmer effect.</li>
    <li>Discuss the consequences of genomic selection for inbreeding and genetic diversity.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#b1">1 · Why genomic selection</a>
    <a href="#b2">2 · Estimating GEBVs</a>
    <a href="#b3">3 · Accuracy of prediction</a>
    <a href="#b4">4 · Reference populations &amp; phenotypes</a>
    <a href="#b5">5 · Breeding programs with GS</a>
    <a href="#b6">6 · Genetic change &amp; diversity</a>
    <a href="#b7">7 · Materials, credits &amp; wrap-up</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <!-- B1 -->
  <div class="module" id="b1">
    <div class="module-head"><div class="module-num">1</div><div><h2>Why genomic selection</h2><div class="module-time">~35 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Name the limits of traditional, phenotype-based selection.</li>
      <li>Explain how SNP chips and the “use all markers” idea created genomic selection.</li></ul></div>
    <p>Traditional selection depends on <strong>phenotypes</strong>. Accuracy is limited by a trait's heritability, and it struggles with traits that are lowly heritable, sex-limited (e.g. egg production), expressed late in life, or hard or expensive to measure (disease resistance, meat quality). It also cannot see <strong>Mendelian sampling</strong>: we don't know which alleles a parent actually passed on, so relatives only take us so far.</p>
    <p>Gene-detection (QTL) studies found a few large-effect genes but left most variation unexplained, the “missing heritability”: most traits are driven by very many genes of tiny effect. The breakthrough came with cheap <strong>SNP chips</strong> (genotyping 50,000 to 700,000 markers per animal). With markers blanketing the genome, at least one is in <strong>linkage disequilibrium</strong> with each causal variant. Meuwissen, Hayes and Goddard (2001) proposed using <em>all</em> markers at once to predict a <strong>genomic estimated breeding value (GEBV)</strong>, even before any phenotype is recorded on the candidate.</p>
    <div class="kc"><strong class="kclabel">Key concept · where GS helps most</strong>Genomic selection adds the most value for “difficult” traits and for selecting young animals early, because it predicts merit from DNA rather than waiting for the animal (or its progeny) to be measured.</div>
    <details class="quiz"><summary>Check: for a trait that is cheap and easy to measure early in both sexes (e.g. body weight in broilers), is genomic selection likely to be worthwhile?</summary><div class="ans">Often not, on its own. When accurate phenotypes are available early and cheaply on all candidates, traditional selection is already accurate and fast; the extra cost of genotyping buys little. GS pays off for low-heritability, sex-limited, late or expensive-to-measure traits.</div></details>
  </div>

  <!-- B2 -->
  <div class="module" id="b2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Estimating genomic breeding values</h2><div class="module-time">~45 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain why selecting only “significant” SNPs fails (the winner's curse).</li>
      <li>Describe SNP-BLUP / ridge regression, Bayesian methods, and GBLUP.</li></ul></div>
    <p>A tempting but wrong approach is to test each SNP, keep the significant ones, and add up their effects. This suffers the <strong>winner's curse</strong>: the SNPs that reach significance have over-estimated effects, and together they explain only a small slice of the variance. Meuwissen et al. showed the fix is to fit <strong>all markers simultaneously</strong>.</p>
    <p>But with tens of thousands of markers and far fewer animals, this is the <strong>“big p, small n”</strong> problem, ordinary regression cannot invert the equations. Two equivalent families of solutions are used:</p>
    <ul>
      <li><strong>SNP-BLUP / ridge regression</strong>, every marker is assumed to explain the same small variance; effects are shrunk toward zero.</li>
      <li><strong>Bayesian methods (BayesA, BayesB)</strong>, allow markers to have different variances; BayesB lets many markers have exactly zero effect, matching the biology of few large and many tiny effects.</li>
    </ul>
    <p>The third route gives the same answer as ridge regression but is easier to implement at scale: build a <strong>genomic relationship matrix (G)</strong> from the markers and use it in the standard mixed model in place of the pedigree relationship matrix A. This is <strong>GBLUP</strong>. G captures the <em>realised</em> relationships between animals, two full sibs are not always related by exactly ½, so “some animals are more equal than others”, which is extra information traditional pedigrees miss.</p>
    <div class="figbox">
      <svg viewBox="0 0 720 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="From SNP genotypes to genomic breeding values">
        <defs><marker id="bar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="10" y="45" width="160" height="60" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="90" y="70">SNP genotypes</text><text x="90" y="88" font-size="10.5" fill="#5f6b62">M (0/1/2 per marker)</text>
          <rect x="210" y="45" width="180" height="60" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="300" y="68">Genomic relationship</text><text x="300" y="86">matrix G = WW'/Σ2pq</text>
          <rect x="430" y="45" width="150" height="60" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="505" y="70">Mixed model</text><text x="505" y="88" font-size="10.5" fill="#5f6b62">y = Xb + Zu + e</text>
          <rect x="620" y="45" width="90" height="60" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="665" y="70">GEBV</text><text x="665" y="88" font-size="10.5" fill="#5f6b62">per animal</text>
          <line x1="172" y1="75" x2="208" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bar)"/>
          <line x1="392" y1="75" x2="428" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bar)"/>
          <line x1="582" y1="75" x2="618" y2="75" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bar)"/>
        </g>
      </svg>
      <figcaption>GBLUP: markers build a realised relationship matrix G that replaces pedigree in the mixed model to produce genomic breeding values.</figcaption>
    </div>
    <details class="quiz"><summary>Check: why does keeping only statistically significant SNPs give biased, disappointing predictions?</summary><div class="ans">The <strong>winner's curse</strong>: only SNPs whose effects are over-estimated by chance clear the significance threshold, so their effects are biased upward, and the few that pass capture only a small part of the genetic variance. Fitting all markers together (shrinking effects) is unbiased and captures far more.</div></details>
  </div>

  <!-- B3 -->
  <div class="module" id="b3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Accuracy of genomic prediction</h2><div class="module-time">~45 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define accuracy and how it is validated (and checked for bias).</li>
      <li>Use the Daetwyler equation to reason about what drives accuracy.</li></ul></div>
    <p>The <strong>accuracy</strong> of a GEBV is its correlation with the true breeding value. We estimate it by <strong>validation</strong>: train the prediction on a reference population, predict a separate validation set, and compare predictions with later phenotypes, checking both correlation (accuracy) and the regression slope (<strong>bias</strong>; a slope of 1 means unbiased).</p>
    <p>The <strong>Daetwyler equation</strong> captures what drives accuracy:</p>
    <p style="text-align:center;font-size:18px;margin:6px 0"><em>r</em> = &radic;( <em>N</em>h² / (<em>N</em>h² + M<sub>e</sub>) )</p>
    <p>where <em>N</em> is the number of reference animals with phenotypes, <em>h²</em> the heritability, and <em>M<sub>e</sub></em> the effective number of independent chromosome segments (larger in populations with a big effective size N<sub>e</sub> and long genome). Accuracy rises with a <strong>larger reference population</strong> and <strong>higher heritability</strong>, and falls when M<sub>e</sub> is large. The practical messages: low-heritability traits need much larger reference populations; predicting <strong>across breeds</strong> is hard because linkage disequilibrium differs; and cheap low-density genotypes can be <strong>imputed</strong> up to high density to add information at low cost.</p>
    <div class="figbox">
      <svg viewBox="0 0 520 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Accuracy rises with reference population size">
        <g font-family="Segoe UI,Arial" font-size="12">
          <line x1="60" y1="210" x2="490" y2="210" stroke="#888" stroke-width="1.5"/>
          <line x1="60" y1="210" x2="60" y2="20" stroke="#888" stroke-width="1.5"/>
          <text x="275" y="240" text-anchor="middle" fill="#5f6b62">Reference population size (N)</text>
          <text x="20" y="115" text-anchor="middle" fill="#5f6b62" transform="rotate(-90 20 115)">Accuracy</text>
          <path d="M60,200 C160,90 300,55 490,42" fill="none" stroke="#2E6B3E" stroke-width="3"/>
          <path d="M60,205 C180,160 320,135 490,120" fill="none" stroke="#3E7CB1" stroke-width="3"/>
          <text x="430" y="34" fill="#2E6B3E" font-weight="bold">high h²</text>
          <text x="430" y="138" fill="#3E7CB1" font-weight="bold">low h²</text>
          <text x="60" y="206" font-size="10" fill="#888">0</text>
        </g>
      </svg>
      <figcaption>Accuracy increases with reference-population size and saturates; low-heritability traits need many more reference animals to reach the same accuracy.</figcaption>
    </div>
    <details class="quiz"><summary>Check: two traits have h² = 0.05 and h² = 0.40. Which needs the larger reference population for the same GEBV accuracy, and why?</summary><div class="ans">The <strong>h² = 0.05</strong> trait. In the Daetwyler equation, lower heritability means each phenotype carries less genetic signal, so many more reference animals (larger N) are needed to reach the same accuracy.</div></details>
  </div>

  <!-- B4 -->
  <div class="module" id="b4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Reference populations &amp; phenotypes</h2><div class="module-time">~35 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain how relatedness between reference and candidates affects accuracy.</li>
      <li>Describe single-step evaluation and the role of phenotype quality.</li></ul></div>
    <p>Accuracy depends not just on reference size but on <strong>relatedness</strong>: predictions are most accurate for candidates closely related to the reference animals. Comparing <strong>genomic and pedigree relationships</strong> also serves as quality control, large mismatches (Mendelian inconsistencies) flag pedigree or genotype errors.</p>
    <p>The <strong>phenotypes</strong> that go into the reference matter as much as the genotypes: they should be accurate and unbiased (for dairy bulls, for example, de-regressed proofs are used). Where some animals are genotyped and others are not, <strong>single-step GBLUP</strong> combines pedigree and genomic relationships into one matrix (H), so all animals are evaluated together, no information is wasted. Different BLUP variants (pedigree BLUP, GBLUP, single-step) can be compared on the same data to see what genomic information adds.</p>
    <div class="kc"><strong class="kclabel">Key concept · single-step</strong>Single-step GBLUP blends genotyped and non-genotyped animals into one evaluation, avoiding the need to genotype everyone while still using all phenotypes and pedigree.</div>
    <details class="quiz"><summary>Check: a young candidate is only distantly related to every animal in the reference population. What happens to its GEBV accuracy?</summary><div class="ans">It drops. Genomic prediction leans heavily on relationships (shared chromosome segments) with reference animals; distant relationship means less shared information and lower accuracy. Keeping the reference population closely connected to selection candidates is part of good design.</div></details>
  </div>

  <!-- B5 -->
  <div class="module" id="b5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Breeding programs with genomic selection</h2><div class="module-time">~45 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Predict response to selection and include GEBVs in a selection index.</li>
      <li>Explain the Bulmer effect and why parent-average comparisons mislead.</li></ul></div>
    <p>Response to selection follows from the <strong>breeding goal</strong> (H = g′v), the genetic parameters, the information used for breeding-value estimation, and the selection and mating decisions (including the <strong>generation interval</strong>). Selection-index theory predicts response, and the <strong>SelAction</strong> software implements it. A GEBV enters the index as an extra information source with its own accuracy.</p>
    <p>Genomic selection helps breeding programs in two big ways: it gives accurate predictions on <strong>young animals</strong> before they have records, which <strong>shortens the generation interval</strong>, and it improves accuracy for difficult traits. Both raise the rate of genetic gain.</p>
    <p>Two cautions are essential. The <strong>Bulmer effect</strong>: selection reduces the additive genetic variance (often by around 25%) because selected parents are less variable, so realised response is lower than a naive calculation suggests, and after accounting for it, extra pedigree information adds little. And when judging the benefit of GS (for example, the value of genotyping cows), do not compare against a <strong>parent-average</strong> prediction as if it were accurate, once the parents themselves are selected, the parent average is almost useless, so honest comparisons must account for selection.</p>
    <div class="figbox">
      <svg viewBox="0 0 640 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Genomic selection shortens the generation interval">
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <text x="320" y="20" font-weight="bold" fill="#1F4A2B">Genomic selection lets you select earlier</text>
          <text x="70" y="55" fill="#5f6b62">Traditional</text>
          <rect x="120" y="42" width="180" height="26" rx="6" fill="#EEF3EC" stroke="#9bb6a3"/><text x="210" y="59" font-size="10.5">wait for progeny records</text>
          <rect x="300" y="42" width="90" height="26" rx="6" fill="#FBF3E3" stroke="#C8962A"/><text x="345" y="59" font-size="10.5">select</text>
          <line x1="120" y1="86" x2="345" y2="86" stroke="#888" stroke-dasharray="3 3"/><text x="232" y="100" font-size="10" fill="#888">long generation interval</text>
          <text x="70" y="135" fill="#5f6b62">Genomic</text>
          <rect x="120" y="122" width="70" height="26" rx="6" fill="#E3EEF6" stroke="#3E7CB1"/><text x="155" y="139" font-size="10.5">genotype</text>
          <rect x="190" y="122" width="70" height="26" rx="6" fill="#FBF3E3" stroke="#C8962A"/><text x="225" y="139" font-size="10.5">select</text>
          <line x1="120" y1="156" x2="225" y2="156" stroke="#2E6B3E"/><text x="172" y="168" font-size="10" fill="#2E6B3E">shorter interval, faster gain</text>
        </g>
      </svg>
      <figcaption>Predicting merit from DNA on young animals shortens the generation interval, a major source of the extra genetic gain from genomic selection.</figcaption>
    </div>
    <details class="quiz"><summary>Check: a scheme reports a big advantage of GEBVs over the parent average for selecting cows. Why be sceptical?</summary><div class="ans">Because the cows' parents were themselves selected, which makes the parent average far less informative than software assuming no selection reports. Comparing GEBVs against an over-optimistic parent average inflates the apparent benefit; the Bulmer effect and selection must be accounted for (as SelAction does).</div></details>
  </div>

  </div></section>

<section><div class="wrap">
<div class="goatsim">
<style>
.goatsim{border:1px solid var(--line);border-radius:14px;padding:24px;background:#fff}
.goatsim h2{margin-bottom:4px}
.goatsim .lead{margin-bottom:14px}
.goatsim .gs-grid{display:grid;grid-template-columns:300px 1fr;gap:22px;align-items:start}
.goatsim .gs-panel{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:16px}
.goatsim .gs-panel h4{color:var(--greendk);font-size:13px;text-transform:uppercase;letter-spacing:.5px;margin:0 0 8px}
.goatsim label{font-size:14px;font-weight:600;color:var(--ink);display:block;margin:12px 0 4px}
.goatsim input[type=range]{width:100%}
.goatsim .seg{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.goatsim .seg button{flex:1;min-width:54px;border:1px solid var(--line);background:#fff;border-radius:8px;padding:7px 4px;font-size:13px;font-weight:600;color:var(--ink);cursor:pointer}
.goatsim .seg button.on{background:var(--green);color:#fff;border-color:var(--green)}
.goatsim .seg.meth button{min-width:100%}
.goatsim .runbtns{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
.goatsim .runbtns button{flex:1;border:0;border-radius:8px;padding:10px 6px;font-weight:700;font-size:14px;cursor:pointer}
.goatsim .b-step{background:var(--green);color:#fff}.goatsim .b-run{background:var(--gold);color:#fff}.goatsim .b-reset{background:#fff;color:var(--ink);border:1px solid var(--line)!important}
.goatsim .chk{font-size:13.5px;font-weight:600;margin-top:14px;display:flex;align-items:center;gap:8px}
.goatsim .eq{background:#eef4f9;border:1px solid #cfe0ee;border-radius:10px;padding:12px 14px;font-size:14px;margin-top:14px}
.goatsim .eq b{color:#225277}
.goatsim .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}
.goatsim .stat{background:var(--band);border-radius:10px;padding:10px;text-align:center}
.goatsim .stat .v{font-size:20px;font-weight:800;color:var(--green);line-height:1.1}
.goatsim .stat .l{font-size:11px;color:var(--grey);margin-top:2px}
.goatsim canvas{width:100%;border:1px solid var(--line);border-radius:10px;background:#fff;display:block}
.goatsim .cap{font-size:12px;color:var(--grey);margin:5px 0 14px}
.goatsim .herd{font-size:24px;line-height:1.5;letter-spacing:2px;margin-top:6px}
.goatsim .herd span{filter:grayscale(1) opacity(.55)}
.goatsim .herd span.sel{filter:none;text-shadow:0 0 0 #000}
.goatsim .herd span.sel::after{content:"";}
@media(max-width:760px){.goatsim .gs-grid{grid-template-columns:1fr}}
</style>

<h2>Interactive: the goat selection simulator</h2>
<p class="lead">A dairy-goat breeder wants higher <strong>milk yield</strong> (start: 250 kg per lactation). Change how hard you select, how accurately you rank the goats, and how heritable the trait is, then watch genetic gain build up across generations. Everything runs on the breeder&rsquo;s equation, <em>R = i &times; r &times; &sigma;<sub>A</sub></em>.</p>

<div class="gs-grid">
  <div class="gs-panel">
    <h4>Your breeding decisions</h4>

    <label>Heritability (h&sup2;): <span id="gsH2v">0.30</span></label>
    <input type="range" id="gsH2" min="0.05" max="0.6" step="0.05" value="0.30">

    <label>Proportion of goats selected as parents</label>
    <div class="seg" id="gsProp">
      <button data-p="2">Top 2%</button>
      <button data-p="5">Top 5%</button>
      <button data-p="10" class="on">10%</button>
      <button data-p="25">25%</button>
      <button data-p="50">50%</button>
    </div>

    <label>Selection method (sets accuracy &amp; generation interval)</label>
    <div class="seg meth" id="gsMeth">
      <button data-m="mass">Mass selection &middot; own record</button>
      <button data-m="progeny">Progeny testing &middot; very accurate, slow</button>
      <button data-m="genomic" class="on">Genomic selection &middot; accurate &amp; fast</button>
    </div>

    <label class="chk"><input type="checkbox" id="gsBulmer" checked> Include the Bulmer effect (variance shrinks under selection)</label>

    <div class="runbtns">
      <button class="b-step" id="gsStep">+1 generation</button>
      <button class="b-run" id="gsRun">Run 10</button>
      <button class="b-reset" id="gsReset">Reset</button>
    </div>

    <div class="eq" id="gsEq"></div>
  </div>

  <div class="gs-viz">
    <canvas id="gsDist" width="640" height="230"></canvas>
    <div class="cap">Milk-yield distribution of the current generation. The gold area is the share you keep as parents; the dashed curve is the original population.</div>
    <div class="herd" id="gsHerd"></div>
    <div class="cap">The herd of candidates, the highlighted goats are the ones selected to breed.</div>
    <canvas id="gsGain" width="640" height="210"></canvas>
    <div class="cap">Genetic gain in milk yield across generations. A faded line is kept after Reset so you can compare strategies.</div>
    <div class="stats">
      <div class="stat"><div class="v" id="gsGen">0</div><div class="l">generation</div></div>
      <div class="stat"><div class="v" id="gsYear">0</div><div class="l">years elapsed</div></div>
      <div class="stat"><div class="v" id="gsMean">250</div><div class="l">mean yield (kg)</div></div>
      <div class="stat"><div class="v" id="gsTot">0</div><div class="l">total gain (kg)</div></div>
      <div class="stat"><div class="v" id="gsPerGen">0</div><div class="l">gain / generation</div></div>
      <div class="stat"><div class="v" id="gsPerYr">0</div><div class="l">gain / year (kg)</div></div>
    </div>
  </div>
</div>
</div>
</div></section>
<script>
(function(){
  var BASE=250, SP=60;
  var PROPS={2:{i:2.421,x:2.054,k:0.888},5:{i:2.063,x:1.645,k:0.862},10:{i:1.755,x:1.282,k:0.830},25:{i:1.271,x:0.674,k:0.759},50:{i:0.798,x:0.0,k:0.637}};
  var METH={mass:{L:2,name:'Mass selection'},progeny:{r:0.85,L:5,name:'Progeny testing'},genomic:{r:0.70,L:2,name:'Genomic selection'}};
  var h2=0.30, prop=10, meth='genomic', bulmer=true;
  var st, ghost=null, ghostName='';
  function Va0(){return h2*SP*SP;}
  function accuracy(){return meth==='mass'?Math.sqrt(h2):METH[meth].r;}
  function reset(keepGhost){
    if(keepGhost && st && st.series.length>1){ghost=st.series.slice();ghostName=METH[st.meth].name;}
    st={meanV:BASE, Va:Va0(), gen:0, meth:meth, series:[{g:0,mean:BASE,yr:0}]};
    draw();
  }
  function step(){
    var p=PROPS[prop], r=accuracy(), sA=Math.sqrt(st.Va), R=p.i*r*sA;
    st.meanV+=R; st.gen++;
    if(bulmer){ st.Va=0.5*Va0()+0.5*st.Va*(1-p.k*r*r); }
    st.series.push({g:st.gen,mean:st.meanV,yr:st.gen*METH[meth].L});
    draw();
  }
  var running=false;
  function run10(){ if(running)return; running=true; var n=0; var t=setInterval(function(){step();if(++n>=10){clearInterval(t);running=false;}},230); }

  // ---- drawing ----
  function dpr(c,H0){var r=window.devicePixelRatio||1;var w=c.clientWidth||640;c.style.height=H0+'px';c.width=Math.round(w*r);c.height=Math.round(H0*r);var ctx=c.getContext('2d');ctx.setTransform(r,0,0,r,0,0);return {ctx:ctx,w:w,h:H0};}
  function bell(ctx,x0,x1,W,H,mean,sd,col,fill,xLo,xHi){
    ctx.beginPath();var first=true,peak=0.40/sd;
    for(var px=0;px<=W;px++){var v=xLo+(xHi-xLo)*px/W;var y=Math.exp(-0.5*Math.pow((v-mean)/sd,2))/(sd*Math.sqrt(2*Math.PI));var Y=H-12-(y/peak)*(H-30);if(first){ctx.moveTo(px,Y);first=false;}else ctx.lineTo(px,Y);}
    ctx.strokeStyle=col;ctx.lineWidth=2;if(fill){ctx.setLineDash([]);}ctx.stroke();
  }
  function drawDist(){
    var c=document.getElementById('gsDist');var o=dpr(c,230),ctx=o.ctx,W=o.w,H=o.h;ctx.clearRect(0,0,W,H);
    var xLo=100,xHi=620,peak=0.40/SP;
    // axis
    ctx.strokeStyle='#ccc';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,H-12);ctx.lineTo(W,H-12);ctx.stroke();
    ctx.fillStyle='#888';ctx.font='11px Segoe UI,Arial';
    for(var v=100;v<=600;v+=100){var X=(v-xLo)/(xHi-xLo)*W;ctx.fillText(v+(v===600?' kg':''),X-8,H-2);}
    // base population (dashed)
    ctx.setLineDash([5,4]);bell(ctx,0,W,W,H,BASE,SP,'#9bb6a3',false,xLo,xHi);ctx.setLineDash([]);
    // current generation: shade selected tail
    var p=PROPS[prop], tx=st.meanV+p.x*SP;
    ctx.beginPath();
    for(var px=0;px<=W;px++){var val=xLo+(xHi-xLo)*px/W;var y=Math.exp(-0.5*Math.pow((val-st.meanV)/SP,2))/(SP*Math.sqrt(2*Math.PI));var Y=H-12-(y/peak)*(H-30);if(px===0)ctx.moveTo(px,Y);else ctx.lineTo(px,Y);}
    ctx.lineTo(W,H-12);ctx.lineTo(0,H-12);ctx.closePath();ctx.fillStyle='rgba(46,107,62,.10)';ctx.fill();
    // shaded selected area (right of tx)
    var sx=(tx-xLo)/(xHi-xLo)*W;
    ctx.save();ctx.beginPath();ctx.rect(sx,0,W-sx,H);ctx.clip();
    ctx.beginPath();
    for(var px2=0;px2<=W;px2++){var val2=xLo+(xHi-xLo)*px2/W;var y2=Math.exp(-0.5*Math.pow((val2-st.meanV)/SP,2))/(SP*Math.sqrt(2*Math.PI));var Y2=H-12-(y2/peak)*(H-30);if(px2===0)ctx.moveTo(px2,Y2);else ctx.lineTo(px2,Y2);}
    ctx.lineTo(W,H-12);ctx.lineTo(0,H-12);ctx.closePath();ctx.fillStyle='rgba(200,150,42,.55)';ctx.fill();ctx.restore();
    // current curve outline + truncation line
    bell(ctx,0,W,W,H,st.meanV,SP,'#2E6B3E',true,xLo,xHi);
    if(sx>0&&sx<W){ctx.strokeStyle='#C8962A';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(sx,8);ctx.lineTo(sx,H-12);ctx.stroke();}
    ctx.fillStyle='#1F4A2B';ctx.font='bold 12px Segoe UI,Arial';ctx.fillText('mean '+Math.round(st.meanV)+' kg',Math.min(W-90,(st.meanV-xLo)/(xHi-xLo)*W-28),16);
  }
  function drawGain(){
    var c=document.getElementById('gsGain');var o=dpr(c,210),ctx=o.ctx,W=o.w,H=o.h;ctx.clearRect(0,0,W,H);
    var allMax=BASE+10;st.series.forEach(function(d){if(d.mean>allMax)allMax=d.mean;});if(ghost)ghost.forEach(function(d){if(d.mean>allMax)allMax=d.mean;});
    var maxG=Math.max(10,st.series.length-1);if(ghost)maxG=Math.max(maxG,ghost.length-1);
    var yLo=BASE-10,yHi=allMax+15;
    function X(g){return 38+g/maxG*(W-50);}function Y(m){return H-26-(m-yLo)/(yHi-yLo)*(H-44);}
    ctx.strokeStyle='#ddd';ctx.beginPath();ctx.moveTo(38,8);ctx.lineTo(38,H-26);ctx.lineTo(W-12,H-26);ctx.stroke();
    ctx.fillStyle='#888';ctx.font='11px Segoe UI,Arial';ctx.fillText('kg',6,16);ctx.fillText('generation',W-78,H-8);
    if(ghost&&ghost.length>1){ctx.strokeStyle='rgba(120,107,174,.5)';ctx.lineWidth=2;ctx.setLineDash([4,3]);ctx.beginPath();ghost.forEach(function(d,k){var px=X(d.g),py=Y(d.mean);k?ctx.lineTo(px,py):ctx.moveTo(px,py);});ctx.stroke();ctx.setLineDash([]);ctx.fillStyle='rgba(120,107,174,.9)';ctx.fillText(ghostName,W-160,18);}
    ctx.strokeStyle='#2E6B3E';ctx.lineWidth=3;ctx.beginPath();st.series.forEach(function(d,k){var px=X(d.g),py=Y(d.mean);k?ctx.lineTo(px,py):ctx.moveTo(px,py);});ctx.stroke();
    ctx.fillStyle='#2E6B3E';st.series.forEach(function(d){ctx.beginPath();ctx.arc(X(d.g),Y(d.mean),2.5,0,7);ctx.fill();});
  }
  function drawHerd(){
    var el=document.getElementById('gsHerd');var N=24,sel=Math.max(1,Math.round(N*prop/100));var html='';
    for(var k=0;k<N;k++){html+='<span'+(k<sel?' class="sel"':'')+'>🐐</span>';}
    el.innerHTML=html;
  }
  function draw(){
    drawDist();drawGain();drawHerd();
    var p=PROPS[prop],r=accuracy(),sA=Math.sqrt(st.Va),R=p.i*r*sA,L=METH[meth].L;
    document.getElementById('gsGen').textContent=st.gen;
    document.getElementById('gsYear').textContent=st.gen*L;
    document.getElementById('gsMean').textContent=Math.round(st.meanV);
    document.getElementById('gsTot').textContent=Math.round(st.meanV-BASE);
    document.getElementById('gsPerGen').textContent=R.toFixed(1);
    document.getElementById('gsPerYr').textContent=(R/L).toFixed(1);
    document.getElementById('gsEq').innerHTML='<b>R = i &times; r &times; &sigma;<sub>A</sub></b> &nbsp;=&nbsp; '+p.i.toFixed(2)+' &times; '+r.toFixed(2)+' &times; '+sA.toFixed(1)+' &nbsp;=&nbsp; <b>'+R.toFixed(1)+' kg / generation</b><br><span style="color:#5f6b62">i = selection intensity ('+prop+'% kept) &middot; r = accuracy ('+METH[meth].name+') &middot; &sigma;<sub>A</sub> = genetic SD &middot; interval = '+L+' yr</span>';
  }

  // ---- wire controls ----
  document.getElementById('gsH2').addEventListener('input',function(){h2=parseFloat(this.value);document.getElementById('gsH2v').textContent=h2.toFixed(2);st.Va=bulmer?st.Va:Va0();if(st.gen===0)st.Va=Va0();draw();});
  document.getElementById('gsProp').addEventListener('click',function(e){if(e.target.dataset.p){prop=parseInt(e.target.dataset.p);[].forEach.call(this.children,function(b){b.classList.toggle('on',b===e.target);});draw();}});
  document.getElementById('gsMeth').addEventListener('click',function(e){if(e.target.dataset.m){meth=e.target.dataset.m;[].forEach.call(this.children,function(b){b.classList.toggle('on',b===e.target);});draw();}});
  document.getElementById('gsBulmer').addEventListener('change',function(){bulmer=this.checked;});
  document.getElementById('gsStep').addEventListener('click',step);
  document.getElementById('gsRun').addEventListener('click',run10);
  document.getElementById('gsReset').addEventListener('click',function(){reset(true);});
  reset(false);
})();
</script>

<section class="alt"><div class="wrap">
  <!-- B6 -->
  <div class="module" id="b6">
    <div class="module-head"><div class="module-num">6</div><div><h2>Genetic change, inbreeding &amp; diversity</h2><div class="module-time">~30 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Distinguish selection from drift as causes of allele-frequency change.</li>
      <li>Explain why genomic selection needs active control of inbreeding.</li></ul></div>
    <p>Selection changes allele frequencies directionally and leaves <strong>signatures of selection</strong> in the genome, detectable through statistics such as F<sub>ST</sub> (differentiation between populations), reduced heterozygosity, and haplotype-based measures (iHS, EHH) around <strong>selective sweeps</strong>. But not all change is selection: <strong>genetic drift</strong>, random change that is larger in small populations (inversely proportional to effective size N<sub>e</sub>), also shifts frequencies and erodes diversity, and must be separated from true selection signals.</p>
    <p>This matters for sustainability. Genomic selection captures close family relationships, so without care it can <strong>increase inbreeding per generation</strong> relative to progeny testing. The remedy is <strong>genomic control of inbreeding</strong>: managing matings to restrict the increase in marker-based kinship while still selecting for merit. Maintaining genetic diversity is not a side issue, it protects long-term response, adaptability and resilience, which is exactly where breeding meets <strong>biodiversity</strong>.</p>
    <div class="kc"><strong class="kclabel">Key concept · diversity is a resource</strong>Faster genetic gain is only sustainable if genetic diversity is managed. Genomic tools that accelerate selection should be paired with genomic management of inbreeding and kinship.</div>
    <details class="quiz"><summary>Check: allele frequencies shift in a small closed herd with no deliberate selection. Selection or drift?</summary><div class="ans"><strong>Drift</strong>, random change in allele frequencies, which is stronger the smaller the effective population size. It erodes diversity and can mimic or mask selection signatures, which is why distinguishing the two requires care.</div></details>
  </div>

  <!-- B7 -->
  <div class="module" id="b7">
    <div class="module-head"><div class="module-num">7</div><div><h2>Glossary</h2></div></div>
    <div class="gloss">
      <div><b>SNP chip</b>, array genotyping tens to hundreds of thousands of markers per animal.</div>
      <div><b>GEBV</b>, genomic estimated breeding value, merit predicted from markers.</div>
      <div><b>Winner's curse</b>, upward bias when keeping only significant SNP effects.</div>
      <div><b>SNP-BLUP / ridge</b>, fit all markers with equal, shrunk variance.</div>
      <div><b>BayesA / BayesB</b>, Bayesian methods allowing unequal (or zero) marker effects.</div>
      <div><b>GBLUP</b>, mixed model using the genomic relationship matrix G.</div>
      <div><b>Daetwyler equation</b>, accuracy as a function of N, h² and M<sub>e</sub>.</div>
      <div><b>Single-step</b>, joint evaluation of genotyped and non-genotyped animals.</div>
      <div><b>Bulmer effect</b>, reduction in additive variance caused by selection.</div>
      <div><b>Signatures of selection</b>, genomic patterns (F<sub>ST</sub>, iHS) left by selection.</div>
      <div><b>Genetic drift</b>, random change in allele frequency, stronger when N<sub>e</sub> is small.</div>
    </div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-genomic-selection-breeding.html", course3)


# ---------------- COURSE 4: Breeding and Genetics (Peter Sørensen) ----------------
BG="https://github.com/psoerensen/bgcourse/blob/main/"
def bglink(label, fname):
    return '<a href="'+BG+fname.replace(" ","%20")+'" target="_blank" rel="noopener">'+label+'</a>'
def matbox(title, fname):
    return ('<a class="matbox" href="'+BG+fname.replace(" ","%20")+'" target="_blank" rel="noopener">'
            '<span class="mb-ic">\U0001F4D8</span>'
            '<span class="mb-tx"><strong>Go to detailed materials →</strong>'
            '<span>'+title+' (PDF · Peter Sørensen)</span></span></a>')

course4 = head("Breeding and Genetics","knowledge.html","A self-paced ASAP-Bio course on breeding and quantitative genetics by Peter Sørensen (Aarhus University), from basic concepts to genomic breeding values, with R practicals.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Biodiversity and Breeding programs</div>
  <h1>Breeding and Genetics</h1>
  <p class="csub">The quantitative-genetics foundations of animal and plant breeding: how traits are inherited, how we estimate heritability and breeding values, and how genomic data sharpen prediction, with hands-on analyses in R.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~8 hours</span><span>🎓 MSc / advanced</span><span>📊 R practicals</span><span>🔓 CC0 open licence</span>
  </div>
</div></section>

<section><div class="wrap">
  <div class="attrib"><strong>About this course.</strong> ASAP-Bio provides the structured study path below. The full lecture notes, practicals and R solutions are by <strong>Peter Sørensen</strong> (Center for Quantitative Genetics and Genomics, Aarhus University), released under a <strong>CC0-1.0</strong> public-domain dedication. Each part of the path ends with a green box linking to the matching original material. Source repository: <a href="https://github.com/psoerensen/bgcourse" target="_blank" rel="noopener">github.com/psoerensen/bgcourse</a>.</div>

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Describe how breeding programmes turn genetic variation into genetic gain.</li>
    <li>Decompose a phenotype into genetic and environmental components and define heritability.</li>
    <li>Estimate genetic parameters (heritabilities, correlations) using mixed models.</li>
    <li>Estimate breeding values with BLUP and the animal model.</li>
    <li>Extend prediction to genomic breeding values (GBLUP and marker models).</li>
    <li>Carry out quantitative-genetic analyses in R.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#bg1">1 · Introduction to breeding</a>
    <a href="#bg2">2 · Basic quantitative genetics</a>
    <a href="#bg3">3 · Genetic parameters</a>
    <a href="#bg4">4 · Breeding values (BLUP)</a>
    <a href="#bg5">5 · Genomic breeding values</a>
    <a href="#bg6">6 · Analyses in R &amp; practicals</a>
    <a href="#bg7">7 · Glossary &amp; credits</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <div class="module" id="bg1">
    <div class="module-head"><div class="module-num">1</div><div><h2>Introduction to plant and animal breeding</h2><div class="module-time">~45 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>State what a breeding programme is and what a breeding goal does.</li>
      <li>Describe the breeder&rsquo;s cycle: variation, evaluation, selection, mating.</li></ul></div>
    <p>Breeding is the directed improvement of populations across generations. A programme starts from a <strong>breeding goal</strong> (the traits to improve and their relative economic or societal weights), then repeats a cycle: measure <strong>phenotypes</strong>, estimate each candidate&rsquo;s genetic merit, <strong>select</strong> the best as parents, and <strong>mate</strong> them to produce the next generation. Plant and animal breeding share this logic, differing mainly in reproductive biology, generation interval and how populations are structured.</p>
    <p>Genetic gain per cycle depends on how intensely we select, how accurately we rank candidates, how much genetic variation exists, and how long a generation takes, the same levers explored in the companion genomic-selection course and simulator.</p>
    <details class="quiz"><summary>Check: why is a clearly defined breeding goal the first step of any programme?</summary><div class="ans">Because every later decision, which traits to record, how to weight them in an index, which animals to select, follows from the goal. Without it, selection has no consistent direction and traits can drift or deteriorate.</div></details>
    """ + matbox("Brief Introduction to Plant and Animal Breeding","Brief-Introduction-to-Plant-and-Animal-Breeding.pdf") + """
  </div>

  <div class="module" id="bg2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Basic concepts in quantitative genetics</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Decompose phenotype into genetic and environmental parts.</li>
      <li>Define additive variance, breeding value and heritability.</li>
      <li>Explain why relatives resemble each other.</li></ul></div>
    <p>Quantitative traits (growth, milk yield, disease resistance) are shaped by many genes of small effect plus the environment, the <strong>infinitesimal model</strong>. The core decomposition is <strong>P = G + E</strong>: an individual&rsquo;s phenotype is its genotypic value plus an environmental deviation. The genotypic value splits further into <strong>additive</strong> (transmissible), dominance and epistatic parts. The additive value is the <strong>breeding value</strong>, what a parent passes on, and is the currency of selection.</p>
    <p>At the population level, variance partitions the same way: total phenotypic variance V<sub>P</sub> = V<sub>A</sub> + V<sub>D</sub> + V<sub>E</sub> (and more). <strong>Heritability</strong> in the narrow sense, h² = V<sub>A</sub>/V<sub>P</sub>, is the fraction of phenotypic variation that is additive and therefore responds to selection. Relatives resemble one another because they share alleles; the degree of resemblance (covariance between relatives) is what lets us estimate genetic parameters and breeding values.</p>
    <div class="figbox">
      <svg viewBox="0 0 620 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Phenotype equals genotype plus environment, with variance partition">
        <g font-family="Segoe UI,Arial" font-size="13" text-anchor="middle">
          <rect x="20" y="50" width="120" height="50" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="80" y="72">Phenotype</text><text x="80" y="90" font-size="11" fill="#5f6b62">P (V_P)</text>
          <text x="160" y="80" font-size="20">=</text>
          <rect x="185" y="50" width="120" height="50" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="245" y="72">Genotype</text><text x="245" y="90" font-size="11" fill="#5f6b62">G (V_A + V_D + ...)</text>
          <text x="320" y="80" font-size="20">+</text>
          <rect x="345" y="50" width="130" height="50" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="410" y="72">Environment</text><text x="410" y="90" font-size="11" fill="#5f6b62">E (V_E)</text>
          <rect x="500" y="50" width="100" height="50" rx="9" fill="#fff" stroke="#bbb"/><text x="550" y="70" font-size="12">h² =</text><text x="550" y="88" font-size="12">V_A / V_P</text>
          <text x="310" y="128" font-size="12" fill="#5f6b62">The additive part (breeding value) is what parents transmit and what selection acts on.</text>
        </g>
      </svg>
      <figcaption>The central decomposition of quantitative genetics, and heritability as the additive share of phenotypic variance.</figcaption>
    </div>
    <details class="quiz"><summary>Check: a trait has h² = 0.1. What does that tell a breeder?</summary><div class="ans">Only 10% of the phenotypic variation is additive genetic, so individual phenotypes are weak predictors of breeding value. Progress is still possible but needs more information (relatives, repeated records, genomics) and/or higher selection intensity; response per generation will be modest.</div></details>
    """ + matbox("Basic Concepts in Quantitative Genetics","Basic-Concepts-in-Quantitative-Genetics.pdf") + """
  </div>

  <div class="module" id="bg3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Estimation of genetic parameters</h2><div class="module-time">~60 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain how heritabilities and genetic correlations are estimated.</li>
      <li>Describe variance-component estimation with mixed models (REML).</li></ul></div>
    <p>Before we can predict breeding values we need the <strong>genetic parameters</strong>: heritabilities, and genetic and environmental (co)variances among traits. These are estimated from the resemblance between relatives, using <strong>mixed models</strong> that separate fixed effects (herd, year, sex) from random genetic effects. The standard estimation method is <strong>REML</strong> (restricted maximum likelihood), which estimates <strong>variance components</strong> (V<sub>A</sub>, V<sub>E</sub>, and others) from the data and pedigree or genomic relationships.</p>
    <p><strong>Genetic correlations</strong> matter because traits are not independent: selecting hard on one trait drags correlated traits along, sometimes unfavourably. Reliable parameters are the foundation of both selection-index design and BLUP evaluation.</p>
    <details class="quiz"><summary>Check: why does a breeder need genetic correlations, not just heritabilities?</summary><div class="ans">Because selection on one trait changes correlated traits too. A favourable genetic correlation gives a free bonus; an unfavourable one (for example, between yield and fertility) means single-trait selection can erode another important trait. Multi-trait indexes need the correlations to balance the goal.</div></details>
    """ + matbox("Estimation of Genetic Parameters","Estimation-of-Genetic-Parameters.pdf") + """
  </div>

  <div class="module" id="bg4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Estimation of breeding values (BLUP)</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain BLUP and the animal model.</li>
      <li>Say how the pedigree relationship matrix and information sources drive accuracy.</li></ul></div>
    <p>To rank selection candidates we estimate their breeding values. The standard tool is <strong>BLUP</strong> (best linear unbiased prediction) in the <strong>animal model</strong>, <em>y = Xb + Zu + e</em>, which simultaneously corrects for fixed effects and predicts each animal&rsquo;s additive genetic merit <em>u</em>. BLUP combines every available record, the animal&rsquo;s own, its relatives&rsquo;, across generations, weighting them by the <strong>pedigree relationship matrix A</strong> and the genetic parameters from Module 3.</p>
    <p>The prediction&rsquo;s <strong>accuracy</strong> (correlation between estimated and true breeding value) rises with heritability and with the amount of information on the animal and its relatives. BLUP&rsquo;s great strength is that it accounts for selection, non-random mating and unbalanced data, which is why it underpins national genetic evaluations.</p>
    <div class="figbox">
      <svg viewBox="0 0 700 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="From records and relationships to breeding values">
        <defs><marker id="bvar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="10" y="45" width="150" height="55" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="85" y="67">Phenotypes +</text><text x="85" y="85">fixed effects</text>
          <rect x="190" y="45" width="170" height="55" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="275" y="67">Relationships</text><text x="275" y="85" font-size="11" fill="#5f6b62">pedigree A (or genomic G)</text>
          <rect x="390" y="45" width="150" height="55" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="465" y="67">BLUP / animal</text><text x="465" y="85">model (MME)</text>
          <rect x="570" y="45" width="120" height="55" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="630" y="67">Breeding</text><text x="630" y="85">values + accuracy</text>
          <line x1="162" y1="72" x2="188" y2="72" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bvar)"/>
          <line x1="362" y1="72" x2="388" y2="72" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bvar)"/>
          <line x1="542" y1="72" x2="568" y2="72" stroke="#2E6B3E" stroke-width="2" marker-end="url(#bvar)"/>
        </g>
      </svg>
      <figcaption>BLUP combines records, fixed effects and relationships to estimate each candidate&rsquo;s breeding value.</figcaption>
    </div>
    <details class="quiz"><summary>Check: what does the relationship matrix A contribute to a BLUP evaluation?</summary><div class="ans">It tells the model how genetically similar animals are, so information flows between relatives. That lets an animal&rsquo;s breeding value borrow strength from its parents, sibs and progeny, and corrects estimates for the genetic merit of the animals it is compared with.</div></details>
    """ + matbox("Estimation of Breeding Values","Estimation-of-Breeding-Values.pdf") + """
  </div>

  <div class="module" id="bg5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Estimation of genomic breeding values</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain how genomic markers replace or augment pedigree.</li>
      <li>Describe GBLUP and marker (ridge / Bayesian) models.</li></ul></div>
    <p>Dense SNP markers let us measure relationships and gene effects directly. In <strong>GBLUP</strong>, the pedigree matrix A is replaced (or blended, single-step) with a <strong>genomic relationship matrix G</strong> built from markers, capturing the <em>realised</em> sharing of DNA between animals rather than its pedigree expectation. Equivalently, one can fit all marker effects at once with <strong>ridge regression / SNP-BLUP</strong> or <strong>Bayesian</strong> models that allow markers to differ in effect.</p>
    <p>Genomic prediction gives accurate breeding values on <strong>young animals before they have records or progeny</strong>, shortening the generation interval and accelerating genetic gain. Accuracy depends on the size and relatedness of the reference population and the trait&rsquo;s heritability. This module connects directly to the companion course <a href="course-genomic-selection-breeding.html">Breeding programs with Genomic selection</a>, which covers reference-population design and the accuracy equation in depth.</p>
    <details class="quiz"><summary>Check: what is the key practical advantage of a genomic breeding value over a pedigree-only one?</summary><div class="ans">It can be computed accurately on a young animal with no phenotype or progeny of its own, using only its DNA and a trained reference population. Selecting earlier shortens the generation interval and speeds genetic gain.</div></details>
    """ + matbox("Estimation of Genomic Breeding Values","Estimation-of-Genomic-Breeding-Values.pdf") + """
  </div>

  <div class="module" id="bg6">
    <div class="module-head"><div class="module-num">6</div><div><h2>Statistical analysis of quantitative traits in R, and practicals</h2><div class="module-time">~3 hours hands-on</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Read and explore quantitative-genetic data in R.</li>
      <li>Fit linear and mixed models, estimate variance components, and run genomic prediction.</li></ul></div>
    <p>The course is built around hands-on computing in <strong>R</strong>. The guide and practicals walk through importing data, fitting linear and mixed models, estimating heritabilities and breeding values, and carrying out genomic prediction, the methods of Modules 2 to 5 applied to real data. Work through the practicals in order; full R solutions are provided so you can check yourself.</p>
    """ + matbox("Using R for Statistical Analyses of Quantitative Traits (guide)","Using-R-for-Statistical-Analyses-of-Quantitative-Traits.pdf") + matbox("Practicals 1–4 (combined)","Practicals.pdf") + matbox("R solutions (Practicals 1–2–3)","Practicals_1_2_3_Rsolutions.pdf") + """
    <p class="matnote">Individual practicals: """ + bglink("Practical 1","Practical_1.pdf") + " · " + bglink("Practical 2","Practical_2.pdf") + " · " + bglink("Practical 3","Practicals_3.pdf") + " · " + bglink("Practical 4","Practicals_4.pdf") + " · " + bglink("R solutions (1–2)","Practicals_1_2_Rsolutions.pdf") + """.</p>
  </div>

  <div class="module" id="bg7">
    <div class="module-head"><div class="module-num">7</div><div><h2>Glossary &amp; credits</h2><div class="module-time">~5 minutes</div></div></div>
    <h3>Glossary</h3>
    <div class="gloss">
      <div><b>Phenotype (P)</b>, the observed trait value; P = G + E.</div>
      <div><b>Breeding value</b>, the additive (transmissible) genetic merit of an individual.</div>
      <div><b>Heritability (h²)</b>, the additive share of phenotypic variance, V_A / V_P.</div>
      <div><b>Genetic correlation</b>, the correlation of breeding values for two traits.</div>
      <div><b>REML</b>, restricted maximum likelihood, used to estimate variance components.</div>
      <div><b>BLUP</b>, best linear unbiased prediction of breeding values (animal model).</div>
      <div><b>Relationship matrix (A / G)</b>, pedigree-based (A) or genomic (G) genetic similarity.</div>
      <div><b>GBLUP</b>, BLUP using the genomic relationship matrix.</div>
      <div><b>Reference population</b>, genotyped and phenotyped animals used to train genomic prediction.</div>
    </div>
    <div class="attrib" style="margin-top:18px"><strong>Credit.</strong> Lecture notes, practicals and R solutions by Peter Sørensen, Center for Quantitative Genetics and Genomics, Aarhus University, released under CC0-1.0. The detailed-materials links in each module open Peter&rsquo;s original files; source repository: <a href="https://github.com/psoerensen/bgcourse" target="_blank" rel="noopener">github.com/psoerensen/bgcourse</a>.</div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-breeding-genetics.html", course4)


print("Generated pages:", [f for f,_ in NAV])

# ================= HULUNIM COURSES (Debre Berhan University) =================
HUL_CREDIT = ('<div class="attrib"><strong>About this course.</strong> This self-paced course was '
  'developed by ASAP-Bio from the teaching materials of <strong>Hulunim Gatew Tariku</strong>, '
  'Department of Animal Sciences, College of Agriculture and Natural Resource Sciences, '
  '<strong>Debre Berhan University</strong>, Ethiopia. It is open-access and free to use for study.</div>')

# ---------------- COURSE 5: Foundations of Animal Genetics ----------------
course5 = head("Foundations of Animal Genetics","knowledge.html","A self-paced ASAP-Bio course on the foundations of animal genetics: cells and chromosomes, mitosis and meiosis, Mendelian inheritance, gene interactions and epistasis. Developed from the teaching materials of Hulunim Gatew Tariku, Debre Berhan University.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Biodiversity and Breeding programs</div>
  <h1>Foundations of Animal Genetics</h1>
  <p class="csub">How traits pass from one generation to the next: the cell and its chromosomes, mitosis and meiosis, Mendel&rsquo;s laws, and the ways genes interact to shape the animals we breed. This is the entry point to the ASAP-Bio breeding track.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~6 hours</span><span>🎓 BSc / early MSc</span><span>🧬 Foundational</span><span>🔓 Open access</span>
  </div>
</div></section>

<section><div class="wrap">
  """ + HUL_CREDIT + """

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Use the core vocabulary of genetics correctly: gene, allele, locus, genotype, phenotype, homozygous, heterozygous, dominant and recessive.</li>
    <li>Explain how cells divide by mitosis and meiosis, and why meiosis is the engine of genetic variation.</li>
    <li>Trace how gametes form and how fertilisation recombines genetic material.</li>
    <li>Predict the outcome of monohybrid and dihybrid crosses using Mendel&rsquo;s two laws and the Punnett square.</li>
    <li>Recognise departures from simple dominance: incomplete dominance, codominance, multiple alleles, lethal alleles and epistasis.</li>
    <li>See how single-gene logic scales up to the quantitative traits that breeding programmes select on.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#g1">1 · Genetics and its language</a>
    <a href="#g2">2 · Cells, chromosomes &amp; cell division</a>
    <a href="#g3">3 · Gametogenesis &amp; fertilisation</a>
    <a href="#g4">4 · Mendelian inheritance</a>
    <a href="#g5">5 · Gene &amp; allele interactions</a>
    <a href="#g6">6 · From genes to breeding</a>
    <a href="#g7">7 · Glossary &amp; credits</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <div class="module" id="g1">
    <div class="module-head"><div class="module-num">1</div><div><h2>Genetics and its language</h2><div class="module-time">~35 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define genetics and name its main branches.</li>
      <li>Use the basic terms of inheritance precisely.</li></ul></div>
    <p><strong>Genetics</strong> is the science of heredity and variation: how characteristics are transmitted from parents to offspring, and why individuals differ. For animal scientists it is the foundation of breeding, because we can only improve what is inherited. The field has several branches, including <strong>transmission (Mendelian) genetics</strong>, <strong>molecular genetics</strong>, <strong>population genetics</strong> and <strong>quantitative genetics</strong>, the last two being the bridge into animal breeding.</p>
    <p>A small, exact vocabulary carries the whole subject. A <strong>gene</strong> is a unit of heredity occupying a fixed position, its <strong>locus</strong>, on a chromosome. Alternative forms of a gene are <strong>alleles</strong>. An animal&rsquo;s genetic make-up is its <strong>genotype</strong>; the observable result is its <strong>phenotype</strong>. When the two alleles at a locus are identical the animal is <strong>homozygous</strong>; when they differ it is <strong>heterozygous</strong>. An allele whose effect is seen in the heterozygote is <strong>dominant</strong>; one whose effect is masked is <strong>recessive</strong>.</p>
    <details class="quiz"><summary>Check: an animal is heterozygous (Bb) at a coat-colour locus and looks black. What does that tell you about the B allele?</summary><div class="ans">B (black) is dominant to b: a single copy is enough to produce the black phenotype, so the recessive b allele is masked in the heterozygote. The animal still carries and can transmit b.</div></details>
  </div>

  <div class="module" id="g2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Cells, chromosomes and cell division</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Describe chromosomes and the diploid and haploid states.</li>
      <li>Walk through the stages of mitosis and meiosis.</li>
      <li>Explain why meiosis generates variation while mitosis does not.</li></ul></div>
    <p>Genes are carried on <strong>chromosomes</strong>. Body (somatic) cells are <strong>diploid (2n)</strong>: chromosomes come in homologous pairs, one from each parent. Gametes are <strong>haploid (n)</strong>, carrying a single set. Cattle, for example, have 2n = 60; sheep 2n = 54; goats 2n = 60. Two kinds of division maintain and reshuffle this material.</p>
    <p><strong>Mitosis</strong> divides a somatic cell into two genetically identical daughter cells, used for growth and tissue repair. After DNA replication, the cell passes through <strong>prophase, metaphase, anaphase and telophase</strong>: chromosomes condense, line up on the cell&rsquo;s equator, sister chromatids separate, and two identical nuclei form. The chromosome number is conserved (2n &rarr; 2n).</p>
    <p><strong>Meiosis</strong> produces gametes and halves the chromosome number (2n &rarr; n) over two successive divisions. It is the source of genetic variation through two mechanisms. In <strong>prophase I</strong>, homologous chromosomes pair and exchange segments by <strong>crossing over (recombination)</strong>. At <strong>metaphase I / anaphase I</strong>, the homologous pairs line up and separate <strong>independently</strong> of one another, so maternal and paternal chromosomes are dealt into gametes in new combinations. The result is four haploid cells, each genetically unique.</p>
    <div class="figbox">
      <svg viewBox="0 0 660 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mitosis versus meiosis outcomes">
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="20" y="60" width="90" height="48" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="65" y="80">Parent cell</text><text x="65" y="97" font-size="11" fill="#5f6b62">2n</text>
          <text x="150" y="35" font-size="12" fill="#2E6B3E">Mitosis</text>
          <line x1="112" y1="75" x2="200" y2="50" stroke="#2E6B3E" stroke-width="1.6"/>
          <line x1="112" y1="92" x2="200" y2="118" stroke="#2E6B3E" stroke-width="1.6"/>
          <rect x="205" y="34" width="120" height="40" rx="8" fill="#E3EEF6" stroke="#3E7CB1"/><text x="265" y="50">2 identical</text><text x="265" y="65" font-size="11" fill="#5f6b62">daughter cells · 2n</text>
          <rect x="205" y="100" width="120" height="40" rx="8" fill="#E3EEF6" stroke="#3E7CB1"/><text x="265" y="116">growth / repair</text><text x="265" y="131" font-size="11" fill="#5f6b62">no new variation</text>
          <rect x="370" y="60" width="90" height="48" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="415" y="80">Germ cell</text><text x="415" y="97" font-size="11" fill="#5f6b62">2n</text>
          <text x="505" y="35" font-size="12" fill="#C8962A">Meiosis</text>
          <line x1="462" y1="84" x2="545" y2="40" stroke="#C8962A" stroke-width="1.6"/>
          <line x1="462" y1="84" x2="545" y2="84" stroke="#C8962A" stroke-width="1.6"/>
          <line x1="462" y1="84" x2="545" y2="128" stroke="#C8962A" stroke-width="1.6"/>
          <rect x="548" y="24" width="100" height="34" rx="8" fill="#FBF3E3" stroke="#C8962A"/><text x="598" y="45">4 gametes · n</text>
          <rect x="548" y="67" width="100" height="34" rx="8" fill="#FBF3E3" stroke="#C8962A"/><text x="598" y="88" font-size="11">crossing over</text>
          <rect x="548" y="110" width="100" height="34" rx="8" fill="#FBF3E3" stroke="#C8962A"/><text x="598" y="131" font-size="11">independent assort.</text>
        </g>
      </svg>
      <figcaption>Mitosis copies a cell faithfully (2n &rarr; 2n); meiosis halves and reshuffles the genome (2n &rarr; n), the origin of genetic variation among offspring.</figcaption>
    </div>
    <details class="quiz"><summary>Check: two full siblings are never genetically identical (unless they are identical twins). Which two events in meiosis explain this?</summary><div class="ans">Crossing over in prophase I (which recombines alleles along a chromosome) and the independent assortment of homologous pairs at metaphase I (which combines maternal and paternal chromosomes in new ways). Together they make each gamete, and therefore each offspring, genetically unique.</div></details>
  </div>

  <div class="module" id="g3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Gametogenesis and fertilisation</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Compare spermatogenesis and oogenesis.</li>
      <li>Explain how fertilisation restores the diploid number and mixes two genomes.</li></ul></div>
    <p><strong>Gametogenesis</strong> is the formation of gametes by meiosis. In the male, <strong>spermatogenesis</strong> in the testis turns one diploid spermatogonium into <strong>four</strong> functional spermatozoa. In the female, <strong>oogenesis</strong> in the ovary yields a <strong>single</strong> large ovum per meiosis (the other products become polar bodies), because the egg retains almost all the cytoplasm and nutrients.</p>
    <p>At <strong>fertilisation</strong>, a haploid sperm (n) fuses with a haploid egg (n) to form a diploid <strong>zygote (2n)</strong>, restoring the species chromosome number and uniting the genetic contributions of both parents. The offspring&rsquo;s genotype is therefore one new sample from each parent&rsquo;s reshuffled genome, which is exactly why selection of parents changes the next generation.</p>
    <details class="quiz"><summary>Check: why does a single meiosis yield four sperm but only one functional egg?</summary><div class="ans">In oogenesis the cytoplasm is divided unequally so that one cell keeps the resources needed to support an early embryo; the other meiotic products are small polar bodies that degenerate. Spermatogenesis divides the cytoplasm equally, producing four motile sperm.</div></details>
  </div>

  <div class="module" id="g4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Mendelian inheritance</h2><div class="module-time">~75 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>State Mendel&rsquo;s law of segregation and law of independent assortment.</li>
      <li>Predict monohybrid (3:1) and dihybrid (9:3:3:1) ratios with a Punnett square.</li>
      <li>Use a test cross to reveal an unknown genotype.</li></ul></div>
    <p>Gregor Mendel (1865) deduced the rules of single-gene inheritance from pea crosses, and they apply directly to animals. The <strong>law of segregation</strong>: the two alleles at a locus separate during gamete formation, so each gamete carries only one. The <strong>law of independent assortment</strong>: alleles of different genes are distributed to gametes independently (for genes on different chromosomes).</p>
    <p>A cross of two heterozygotes for one gene, <strong>Bb &times; Bb</strong>, gives genotypes 1 BB : 2 Bb : 1 bb, and with full dominance a <strong>3:1</strong> phenotype ratio. A cross of two double heterozygotes, <strong>BbEe &times; BbEe</strong>, gives the classic <strong>9:3:3:1</strong> phenotype ratio because the two genes assort independently. A <strong>test cross</strong> (mating a dominant-looking animal to a recessive homozygote, bb) reveals the unknown genotype: any recessive offspring prove the parent was a carrier (Bb).</p>
    <div class="figbox">
      <svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Monohybrid Punnett square Bb by Bb">
        <g font-family="Segoe UI,Arial" font-size="14" text-anchor="middle">
          <text x="180" y="20" font-size="12" fill="#5f6b62">Bb &times; Bb</text>
          <text x="120" y="50">B</text><text x="240" y="50">b</text>
          <text x="40" y="115">B</text><text x="40" y="175">b</text>
          <rect x="70" y="60" width="120" height="60" fill="#EEF3EC" stroke="#2E6B3E"/><text x="130" y="95">BB</text>
          <rect x="190" y="60" width="120" height="60" fill="#E3EEF6" stroke="#3E7CB1"/><text x="250" y="95">Bb</text>
          <rect x="70" y="120" width="120" height="60" fill="#E3EEF6" stroke="#3E7CB1"/><text x="130" y="155">Bb</text>
          <rect x="190" y="120" width="120" height="60" fill="#FBF3E3" stroke="#C8962A"/><text x="250" y="155">bb</text>
        </g>
      </svg>
      <figcaption>Monohybrid cross Bb &times; Bb: genotypes 1 BB : 2 Bb : 1 bb, phenotypes 3 dominant : 1 recessive.</figcaption>
    </div>
    <details class="quiz"><summary>Check: a black bull (B_) is mated to several bb (red) cows and produces some red calves. What was the bull&rsquo;s genotype, and why?</summary><div class="ans">The bull is Bb. A red (bb) calf must receive a b allele from each parent; since it got one b from a red cow, the other b came from the bull. A homozygous BB bull could never sire a red calf, so the appearance of red offspring proves the bull is a heterozygous carrier.</div></details>
  </div>

  <div class="module" id="g5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Interactions between alleles and genes</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Distinguish incomplete dominance, codominance and multiple alleles.</li>
      <li>Recognise epistasis and read its modified dihybrid ratios.</li>
      <li>Explain lethal alleles, pleiotropy and environmental effects on expression.</li></ul></div>
    <p>Many traits depart from clean dominance. Under <strong>incomplete dominance</strong> the heterozygote is intermediate (a red &times; white cross giving roan-like blends). Under <strong>codominance</strong> both alleles are fully expressed in the heterozygote (the AB blood group; many protein and DNA markers). A locus may have <strong>multiple alleles</strong> in the population even though any one animal carries only two, as with coat-colour series and blood-group systems. Some alleles are <strong>lethal</strong>, removing a genotypic class and distorting ratios (for example a 2:1 ratio when the homozygote dies).</p>
    <p><strong>Epistasis</strong> is interaction <em>between</em> genes: one locus masks or modifies another. It changes the dihybrid 9:3:3:1 into recognisable ratios, including <strong>9:3:4</strong> (recessive epistasis), <strong>13:3</strong> (dominant suppression), <strong>9:7</strong> (duplicate recessive / complementary genes), <strong>15:1</strong> (duplicate dominant) and <strong>12:3:1</strong> (dominant epistasis). Two further ideas matter for breeders: <strong>pleiotropy</strong>, where one gene affects several traits, and the fact that the <strong>environment can control expression</strong> (temperature-sensitive coat colour; nutrition and growth genes). These complications are exactly why most economically important traits are treated quantitatively, the subject of the next course.</p>
    <details class="quiz"><summary>Check: a dihybrid cross gives a 9:3:4 ratio instead of 9:3:3:1. What does that tell you?</summary><div class="ans">The two genes are interacting (epistasis). Specifically a 9:3:4 ratio indicates recessive epistasis: when one locus is homozygous recessive it masks the second locus, merging two of the four phenotypic classes (3 + 1) into one class of 4. The genes are not acting independently.</div></details>
  </div>

  <div class="module" id="g6">
    <div class="module-head"><div class="module-num">6</div><div><h2>From single genes to breeding</h2><div class="module-time">~25 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain why most production traits are polygenic and continuous.</li>
      <li>Place this course in the ASAP-Bio breeding learning path.</li></ul></div>
    <p>Coat colour and the blood groups obey single-gene rules, but milk yield, growth rate and fertility do not fall into neat categories. They are <strong>polygenic</strong>, controlled by many genes of small effect, and strongly influenced by the environment, so they vary <strong>continuously</strong>. The Mendelian logic you have learned still holds at each locus; it simply sums over many loci. Capturing that sum statistically, through means, variances, heritability and breeding values, is the job of quantitative genetics and animal breeding.</p>
    <div class="callout green"><strong>Where to go next.</strong> Continue to <a href="course-applied-animal-breeding.html">Applied Animal Breeding</a> in this Hub to turn these foundations into selection decisions, then deepen the theory with <a href="course-breeding-genetics.html">Breeding and Genetics</a> (Peter Sørensen, with R practicals) and <a href="course-genomic-selection-breeding.html">Breeding programs with Genomic selection</a>.</div>
    <div class="faobox" style="margin-top:18px">
      <img class="faologo" src="assets/logo-fao.png" alt="FAO e-learning Academy logo" onerror="this.style.display='none'">
      <div class="faotext">
        <h3>Recommended FAO Academy courses</h3>
        <p>To see how this genetics underpins the conservation and sustainable use of livestock diversity, take the FAO course on <strong>Plant and Animal Genetic Resources (SDG indicators 2.5.1 &amp; 2.5.2)</strong>, and on managing genetic variation, <strong>Pre-breeding: Creating and Managing Variation</strong>.</p>
        <p><a class="btn green" href="https://elearning.fao.org/course/view.php?id=392" target="_blank" rel="noopener">FAO · Plant &amp; Animal Genetic Resources &#8594;</a>
        <a class="btn" href="https://elearning.fao.org/course/view.php?id=490" target="_blank" rel="noopener">FAO · Pre-breeding &#8594;</a></p>
      </div>
    </div>
  </div>

  <div class="module" id="g7">
    <div class="module-head"><div class="module-num">7</div><div><h2>Glossary &amp; credits</h2><div class="module-time">~5 minutes</div></div></div>
    <h3>Glossary</h3>
    <div class="gloss">
      <div><b>Gene / locus</b>, a unit of heredity and its fixed position on a chromosome.</div>
      <div><b>Allele</b>, an alternative form of a gene.</div>
      <div><b>Genotype / phenotype</b>, genetic make-up versus observed characteristic.</div>
      <div><b>Homozygous / heterozygous</b>, identical versus different alleles at a locus.</div>
      <div><b>Dominant / recessive</b>, expressed versus masked in the heterozygote.</div>
      <div><b>Diploid (2n) / haploid (n)</b>, paired chromosome set versus single set (gametes).</div>
      <div><b>Mitosis / meiosis</b>, identical somatic division versus reductional gamete-forming division.</div>
      <div><b>Crossing over</b>, exchange of segments between homologous chromosomes in meiosis.</div>
      <div><b>Independent assortment</b>, independent distribution of different genes to gametes.</div>
      <div><b>Epistasis</b>, interaction in which one gene masks or modifies another.</div>
      <div><b>Pleiotropy</b>, one gene affecting several traits.</div>
      <div><b>Polygenic trait</b>, a trait controlled by many genes of small effect.</div>
    </div>
    <div class="attrib" style="margin-top:18px"><strong>Credit.</strong> Course developed by ASAP-Bio from the teaching materials of Hulunim Gatew Tariku, Department of Animal Sciences, Debre Berhan University, Ethiopia. Open-access for study.</div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-foundations-animal-genetics.html", course5)
print("course5 appended")

# ---------------- COURSE 6: Applied Animal Breeding ----------------
course6 = head("Applied Animal Breeding","knowledge.html","A self-paced ASAP-Bio course on applied animal breeding: traits and variation, heritability and repeatability, the breeder's equation and selection, breeding-value estimation and BLUP, and systems of mating including inbreeding. Developed from the teaching materials of Hulunim Gatew Tariku, Debre Berhan University.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Biodiversity and Breeding programs</div>
  <h1>Applied Animal Breeding</h1>
  <p class="csub">The working toolkit of the animal breeder: how to measure traits and variation, estimate heritability, predict breeding values, select parents with the breeder&rsquo;s equation, and manage mating systems and inbreeding to deliver lasting genetic gain.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~8 hours</span><span>🎓 MSc level</span><span>🧮 Worked examples</span><span>🔓 Open access</span>
  </div>
</div></section>

<section><div class="wrap">
  """ + HUL_CREDIT + """

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>State what a breeding programme does and define a breeding goal.</li>
    <li>Classify traits and partition phenotypic variation into genetic and environmental parts.</li>
    <li>Interpret heritability and repeatability and use them to choose a selection method.</li>
    <li>Apply the breeder&rsquo;s equation, R = i&middot;r&middot;&sigma;<sub>A</sub>, and quantify the four levers of genetic gain.</li>
    <li>Estimate breeding values from own performance, relatives and progeny, build a selection index, and explain BLUP.</li>
    <li>Compute an inbreeding coefficient and manage inbreeding and effective population size.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#a1">1 · What animal breeding is</a>
    <a href="#a2">2 · Traits &amp; their measurement</a>
    <a href="#a3">3 · Variation</a>
    <a href="#a4">4 · Heritability &amp; repeatability</a>
    <a href="#a5">5 · Selection &amp; the breeder&rsquo;s equation</a>
    <a href="#a6">6 · Breeding values, index &amp; BLUP</a>
    <a href="#a7">7 · Systems of mating &amp; inbreeding</a>
    <a href="#a8">8 · Glossary &amp; credits</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <div class="module" id="a1">
    <div class="module-head"><div class="module-num">1</div><div><h2>What animal breeding is</h2><div class="module-time">~40 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>State the task of the animal breeder and the role of a breeding goal.</li>
      <li>Outline the breeder&rsquo;s cycle and a little of its history.</li></ul></div>
    <p><strong>Animal breeding</strong> is the application of genetic principles to improve farm-animal populations for the traits people value: more milk, faster or leaner growth, better fertility, disease resistance and resilience. The breeder&rsquo;s task is to identify the genetically superior animals and choose which become parents, so that each generation is, on average, better than the last. Everything starts from a clearly stated <strong>breeding goal</strong>, the traits to improve and their relative economic weights.</p>
    <p>The work then repeats a four-step <strong>breeder&rsquo;s cycle</strong>: record <strong>phenotypes</strong>, estimate each candidate&rsquo;s genetic merit, <strong>select</strong> the best as parents, and <strong>mate</strong> them to produce the next generation. Robert Bakewell pioneered systematic selection and progeny testing in the eighteenth century; Mendel (1865) supplied the genetic mechanism; and Jay Lush, from 1945, built the quantitative methods, heritability, breeding values and selection theory, that this course teaches.</p>
    <details class="quiz"><summary>Check: why is a clearly defined breeding goal the first step of any programme?</summary><div class="ans">Because every later decision, which traits to record, how to weight them, which animals to select, follows from the goal. Without it selection has no consistent direction, and traits can drift or deteriorate even as effort is spent.</div></details>
  </div>

  <div class="module" id="a2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Traits in farm animals and their measurement</h2><div class="module-time">~50 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Distinguish qualitative and quantitative traits.</li>
      <li>Name economically important traits in dairy, beef and sheep.</li>
      <li>Explain why records must be standardised before comparison.</li></ul></div>
    <p>Traits fall into two broad classes. <strong>Qualitative traits</strong> (coat colour, horned or polled) are controlled by one or a few genes, fall into distinct categories and are little affected by environment. <strong>Quantitative traits</strong> (milk yield, growth rate, litter size) are controlled by many genes plus the environment, vary continuously and are the main target of selection. A few are <strong>threshold traits</strong>: an underlying continuous liability expressed as a yes/no outcome such as calving difficulty or survival.</p>
    <p>Economically important traits differ by species and system: in <strong>dairy cattle</strong>, milk volume and composition (fat, protein), fertility, udder health (mastitis) and longevity; in <strong>beef cattle</strong>, growth rate, feed efficiency, carcass yield and calving ease; in <strong>sheep</strong>, reproduction rate, growth, and wool or meat quality. Because animals are kept in different herds, years and seasons, raw records are not comparable. They must first be <strong>standardised</strong>, corrected for fixed environmental effects such as parity, age, season and lactation length, so that the genetic signal is not confounded with management.</p>
    <details class="quiz"><summary>Check: why must lactation records be adjusted (for example to a mature-equivalent, 305-day basis) before cows are ranked?</summary><div class="ans">Because differences in age/parity and in the number of days milked are environmental, not genetic. Comparing a young cow&rsquo;s partial record with a mature cow&rsquo;s full record would rank management and circumstance rather than breeding value. Standardising removes those known effects so the comparison reflects genetic merit.</div></details>
  </div>

  <div class="module" id="a3">
    <div class="module-head"><div class="module-num">3</div><div><h2>Variation and how we partition it</h2><div class="module-time">~55 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>List the sources of phenotypic variation.</li>
      <li>Write and interpret the variance partition.</li>
      <li>Explain genotype-by-environment interaction.</li></ul></div>
    <p>Selection works only because animals vary. An individual&rsquo;s phenotype is <strong>P = G + E</strong>: a genotypic value plus an environmental deviation. The genotypic value itself splits into an <strong>additive</strong> part (the average effect of alleles, transmissible to offspring), a <strong>dominance</strong> part (interaction of alleles at a locus) and an <strong>epistatic</strong> part (interaction between loci). Only the additive part is reliably passed on, which is why it is the currency of selection.</p>
    <p>At the population level the same logic partitions variance: <strong>V<sub>P</sub> = V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>E</sub></strong>. Genetic variation arises from recombination, the independent assortment of chromosomes, mutation and chromosomal change; environmental variation comes from feeding, climate, health and management. A further complication is <strong>genotype-by-environment interaction (G&times;E)</strong>: the best genotype in one environment is not always the best in another, so an animal selected under high input may not excel under harsh tropical conditions, a central concern for African breeding programmes.</p>
    <details class="quiz"><summary>Check: a sire&rsquo;s daughters are top-ranked on a high-input European farm but only average under low-input tropical management. Which phenomenon is this, and why does it matter for ASAP-Bio partners?</summary><div class="ans">Genotype-by-environment interaction. Because genetic merit is re-ranked across environments, breeding values estimated in one production system may not transfer to another. It matters because importing genetics evaluated abroad can disappoint locally; evaluations and breeding goals should reflect the target environment.</div></details>
  </div>

  <div class="module" id="a4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Heritability and repeatability</h2><div class="module-time">~55 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define narrow-sense heritability and read its typical ranges.</li>
      <li>Define repeatability and distinguish it from heritability.</li>
      <li>Use both to decide how much to trust a single record.</li></ul></div>
    <p><strong>Heritability</strong> in the narrow sense, <strong>h&sup2; = V<sub>A</sub> / V<sub>P</sub></strong>, is the fraction of phenotypic variation that is additive genetic, and therefore the fraction that responds to selection. It runs from 0 to 1. A useful rule of thumb from the course materials: <strong>h&sup2; &lt; 0.1</strong> is very low, <strong>0.1&ndash;0.2</strong> low, <strong>0.2&ndash;0.4</strong> medium and <strong>&gt; 0.4</strong> high. Reproduction traits are usually low, growth traits moderate, and conformation or some milk-composition traits high. The higher the heritability, the more an animal&rsquo;s own phenotype reveals its breeding value.</p>
    <p><strong>Repeatability (R)</strong> applies to traits measured more than once per animal (successive lactations, litters). It is the proportion of variance due to permanent differences between animals: <strong>R = (V<sub>G</sub> + V<sub>Ep</sub>) / V<sub>P</sub></strong>, the ratio of genetic plus permanent-environmental variance to total. Repeatability is always at least as large as heritability and sets an upper limit on it. A high repeatability means one record already predicts future performance well, so few records are needed; a low one means you should average several records before judging an animal.</p>
    <div class="figbox">
      <svg viewBox="0 0 640 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Heritability ranges">
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="30" y="45" width="140" height="34" fill="#F3E9D7" stroke="#C8962A"/><text x="100" y="67">very low &lt;0.1</text>
          <rect x="170" y="45" width="140" height="34" fill="#EDE3CF" stroke="#C8962A"/><text x="240" y="67">low 0.1&ndash;0.2</text>
          <rect x="310" y="45" width="150" height="34" fill="#DCEAD7" stroke="#2E6B3E"/><text x="385" y="67">medium 0.2&ndash;0.4</text>
          <rect x="460" y="45" width="150" height="34" fill="#C7DDBF" stroke="#2E6B3E"/><text x="535" y="67">high &gt;0.4</text>
          <text x="320" y="28" font-size="12" fill="#5f6b62">h&sup2; = V_A / V_P</text>
          <text x="320" y="100" font-size="11" fill="#5f6b62">Higher h&sup2; &rarr; an animal&rsquo;s own record is a better guide to its breeding value</text>
        </g>
      </svg>
      <figcaption>Working ranges for heritability used in the course materials.</figcaption>
    </div>
    <details class="quiz"><summary>Check: a trait has h&sup2; = 0.1. What does that imply for selection?</summary><div class="ans">Only 10% of phenotypic variation is additive genetic, so an individual&rsquo;s own record is a weak guide to its breeding value. Progress is still possible but needs more information (records on relatives, repeated records, genomics) or higher selection intensity; response per generation will be modest.</div></details>
  </div>

  <div class="module" id="a5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Selection and the breeder&rsquo;s equation</h2><div class="module-time">~80 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Use the breeder&rsquo;s equation and name its four levers.</li>
      <li>Define accuracy, intensity and generation interval.</li>
      <li>Compare mass, family, progeny-test and index selection.</li></ul></div>
    <p>The expected genetic gain from one round of selection is captured by the <strong>breeder&rsquo;s equation</strong>:</p>
    <div class="formula"><strong>R = i &middot; r &middot; &sigma;<sub>A</sub></strong>&nbsp;&nbsp;per generation, or rate of gain&nbsp; &Delta;G = (i &middot; r &middot; &sigma;<sub>A</sub>) / L</div>
    <p>where <strong>R</strong> is response, <strong>i</strong> the <strong>selection intensity</strong> (how extreme the selected group is, in standard-deviation units; selecting fewer animals raises i), <strong>r</strong> the <strong>accuracy</strong> of selection (correlation between the estimated and true breeding value), <strong>&sigma;<sub>A</sub></strong> the additive genetic standard deviation (the variation available), and <strong>L</strong> the <strong>generation interval</strong> (average age of parents when their replacements are born). To breed faster you increase intensity or accuracy, preserve genetic variation, or shorten the generation interval, and these levers trade off against one another.</p>
    <div class="example"><h4>Worked example</h4>
      <p>A milk trait has phenotypic SD &sigma;<sub>P</sub> = 600 kg and heritability h&sup2; = 0.25, so &sigma;<sub>A</sub> = &radic;0.25 &times; 600 = 300 kg. Suppose we select on own records (accuracy r = h = 0.5) and keep the top 10% of cows (selection intensity i &asymp; 1.76).</p>
      <p>Response per generation: R = i &middot; r &middot; &sigma;<sub>A</sub> = 1.76 &times; 0.5 &times; 300 = <strong>&asymp; 264 kg</strong>. If the generation interval is L = 5 years, the annual gain is 264 / 5 &asymp; <strong>53 kg per year</strong>. Doubling accuracy (better evaluation) or halving the generation interval (genomic selection on young animals) roughly doubles annual gain, the central insight that motivates modern breeding.</p>
    </div>
    <p>How accurately we rank candidates depends on the <strong>information source</strong>. <strong>Mass (individual) selection</strong> uses the animal&rsquo;s own record, simple and effective for highly heritable traits expressed in both sexes. <strong>Family selection</strong> and the use of <strong>relatives&rsquo; records</strong> help for low-heritability traits. <strong>Progeny testing</strong>, judging a sire by the mean of his offspring, gives the highest accuracy for traits of low heritability or expressed in one sex (milk, egg production), but lengthens the generation interval; the materials note that as many as 30 offspring per sire may be needed for very low-heritability traits. When several traits matter at once, they are combined into a <strong>selection index</strong> rather than selected one at a time.</p>
    <details class="quiz"><summary>Check: for a low-heritability, sex-limited trait such as milk yield, why is progeny testing preferred to mass selection of bulls, despite its cost in time?</summary><div class="ans">A bull does not express milk yield himself, so his own phenotype carries no direct information (mass selection cannot work). The mean of many daughters estimates his breeding value with high accuracy, and averaging over many progeny overcomes the low heritability. The price is a longer generation interval while daughters are recorded, which is exactly what genomic selection later helps to shorten.</div></details>
  </div>

  <div class="module" id="a6">
    <div class="module-head"><div class="module-num">6</div><div><h2>Estimating breeding values: index and BLUP</h2><div class="module-time">~75 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Define a breeding value and the sources used to estimate it.</li>
      <li>Explain the selection index and its limitation.</li>
      <li>Say what BLUP adds and why national evaluations rely on it.</li></ul></div>
    <p>A <strong>breeding value (BV)</strong> is the additive genetic merit of an animal, twice the average deviation of its offspring from the population mean, because a parent passes on a sample of half its genes. We never observe a BV directly; we <strong>estimate</strong> it (an EBV) from records on the animal&rsquo;s own performance, its <strong>pedigree</strong>, its <strong>progeny</strong>, and correlated traits, weighting each source by how much information it carries.</p>
    <p>The classical tool for combining sources is the <strong>selection index</strong>: a weighted sum of records, with weights chosen to maximise the correlation between the index and the true breeding value (it is the best linear prediction, BLP). Its weakness is that it assumes the records are already corrected for environmental effects and that those effects are known without error, rarely true in field data with unbalanced herds, years and management.</p>
    <p><strong>BLUP</strong> (best linear unbiased prediction) removes that weakness. In the mixed-model equation <em>y = Xb + Zu + e</em>, it estimates the <strong>fixed environmental effects (b)</strong> and predicts the <strong>random breeding values (u)</strong> simultaneously, using the <strong>relationship matrix A</strong> so that information flows between relatives across the whole pedigree. BLUP therefore corrects for unequal environments, accounts for non-random mating and selection, and ranks all animals on one comparable scale, which is why it underpins national genetic evaluations. Each animal&rsquo;s BV also contains a <strong>Mendelian-sampling</strong> term, its deviation from the parental average, the reason full sibs differ in merit.</p>
    <div class="figbox">
      <svg viewBox="0 0 700 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Inputs to a BLUP evaluation">
        <defs><marker id="abv" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="10" y="42" width="150" height="52" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="85" y="63">Records +</text><text x="85" y="81">fixed effects</text>
          <rect x="185" y="42" width="170" height="52" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="270" y="63">Pedigree</text><text x="270" y="81" font-size="11" fill="#5f6b62">relationship matrix A</text>
          <rect x="380" y="42" width="150" height="52" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="455" y="63">BLUP / animal</text><text x="455" y="81">model (MME)</text>
          <rect x="560" y="42" width="130" height="52" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="625" y="63">EBVs +</text><text x="625" y="81">accuracy</text>
          <line x1="160" y1="68" x2="183" y2="68" stroke="#2E6B3E" stroke-width="2" marker-end="url(#abv)"/>
          <line x1="355" y1="68" x2="378" y2="68" stroke="#2E6B3E" stroke-width="2" marker-end="url(#abv)"/>
          <line x1="530" y1="68" x2="558" y2="68" stroke="#2E6B3E" stroke-width="2" marker-end="url(#abv)"/>
        </g>
      </svg>
      <figcaption>BLUP combines records, fixed effects and pedigree relationships into comparable breeding values.</figcaption>
    </div>
    <details class="quiz"><summary>Check: what does a selection index assume that BLUP does not?</summary><div class="ans">The selection index assumes records are already corrected for environmental (fixed) effects and that those corrections are exact. BLUP drops that assumption: it estimates fixed effects and breeding values at the same time from unbalanced data, using the relationship matrix, so it stays unbiased when herds, years and management differ.</div></details>
  </div>

  <div class="module" id="a7">
    <div class="module-head"><div class="module-num">7</div><div><h2>Systems of mating and inbreeding</h2><div class="module-time">~70 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Distinguish random, assortative, inbreeding and outbreeding systems.</li>
      <li>Compute an inbreeding coefficient from a simple pedigree.</li>
      <li>Link effective population size to the rate of inbreeding.</li></ul></div>
    <p>Selection decides <em>which</em> animals breed; the <strong>mating system</strong> decides <em>which with which</em>. Options range from <strong>random mating</strong>, through <strong>positive</strong> and <strong>negative assortative mating</strong> (like-with-like or unlike-with-unlike for a trait), to the two pure-breeding strategies: <strong>inbreeding</strong> (mating relatives) and <strong>outbreeding / crossbreeding</strong> (mating unrelated animals or different breeds). Crossbreeding exploits <strong>heterosis</strong> (hybrid vigour) and breed complementarity; inbreeding concentrates desired genes and exposes recessives but carries costs.</p>
    <p>The <strong>inbreeding coefficient F</strong> is the probability that the two alleles at a locus are identical by descent. From a pedigree it is computed by the path method:</p>
    <div class="formula"><strong>F<sub>X</sub> = &Sigma; (&frac12;)<sup>n&#8321;+n&#8322;+1</sup> (1 + F<sub>A</sub>)</strong></div>
    <p>summing over every common ancestor A, where n&#8321; and n&#8322; are the numbers of generations from each parent back to A, and F<sub>A</sub> is that ancestor&rsquo;s own inbreeding.</p>
    <div class="example"><h4>Worked example</h4>
      <p>Mate a half-brother and half-sister that share one common ancestor (a sire, S), each one generation away, with S non-inbred (F<sub>S</sub> = 0). There is one path through S with n&#8321; = 1 and n&#8322; = 1, so</p>
      <p>F<sub>offspring</sub> = (&frac12;)<sup>1+1+1</sup> (1 + 0) = (&frac12;)&sup3; = <strong>0.125</strong>, i.e. 12.5% inbreeding. A full-sib mating (two common parents) gives F = 0.25.</p>
    </div>
    <p>Inbreeding accumulates fastest in small populations. Its rate per generation depends on the <strong>effective population size N<sub>e</sub></strong>:</p>
    <div class="formula"><strong>&Delta;F &asymp; 1 / (2 N<sub>e</sub>)</strong></div>
    <p>so using too few sires, the usual bottleneck, drives N<sub>e</sub> down and inbreeding up, eroding fitness through <strong>inbreeding depression</strong> (lower fertility, survival and growth). Managing genetic gain and genetic diversity together, by limiting the rate of inbreeding while selecting, is essential, and is exactly the concern carried into the genomic-selection course.</p>
    <details class="quiz"><summary>Check: a breeder uses only two bulls in a herd to maximise short-term gain. What is the genetic risk, in the language of this module?</summary><div class="ans">Using very few sires drops the effective population size N<sub>e</sub>, so the rate of inbreeding &Delta;F &asymp; 1/(2N<sub>e</sub>) rises sharply. Inbreeding accumulates, recessive defects surface and inbreeding depression lowers fertility and survival, undermining the very gain the breeder sought. Genetic diversity must be managed alongside selection.</div></details>
  </div>

  <div class="module" id="a8">
    <div class="module-head"><div class="module-num">8</div><div><h2>Glossary, recommendations &amp; credits</h2><div class="module-time">~10 minutes</div></div></div>
    <h3>Glossary</h3>
    <div class="gloss">
      <div><b>Breeding goal</b>, the traits to improve and their relative economic weights.</div>
      <div><b>Heritability (h&sup2;)</b>, additive share of phenotypic variance, V_A / V_P.</div>
      <div><b>Repeatability (R)</b>, share of variance due to permanent differences between animals.</div>
      <div><b>Breeder&rsquo;s equation</b>, R = i &middot; r &middot; &sigma;_A; gain per generation.</div>
      <div><b>Selection intensity (i)</b>, how extreme the selected group is, in SD units.</div>
      <div><b>Accuracy (r)</b>, correlation between estimated and true breeding value.</div>
      <div><b>Generation interval (L)</b>, average age of parents when replacements are born.</div>
      <div><b>Breeding value (BV / EBV)</b>, additive genetic merit, estimated as an EBV.</div>
      <div><b>Selection index</b>, weighted combination of records predicting breeding value.</div>
      <div><b>BLUP</b>, best linear unbiased prediction of breeding values (animal model).</div>
      <div><b>Inbreeding coefficient (F)</b>, probability of alleles identical by descent.</div>
      <div><b>Effective population size (N_e)</b>, drives the rate of inbreeding, &Delta;F &asymp; 1/(2N_e).</div>
    </div>
    <div class="callout green" style="margin-top:18px"><strong>Where to go next.</strong> This course assumes the genetics covered in <a href="course-foundations-animal-genetics.html">Foundations of Animal Genetics</a>. To take breeding values into the genomic era, continue to <a href="course-genomic-selection-breeding.html">Breeding programs with Genomic selection</a> and <a href="course-breeding-genetics.html">Breeding and Genetics</a> (Peter Sørensen, with R practicals). To deliver genetic gain on the ground, see <a href="course-animal-reproduction-biotech.html">Animal Reproduction and Reproductive Biotechnology</a>.</div>
    <div class="faobox" style="margin-top:18px">
      <img class="faologo" src="assets/logo-fao.png" alt="FAO e-learning Academy logo" onerror="this.style.display='none'">
      <div class="faotext">
        <h3>Recommended FAO Academy course</h3>
        <p>The FAO <strong>Animal breeding</strong> course complements this one with a field-extension perspective: breeding structures and systems, management of breeding stock and, importantly for the region, <strong>community-based breeding programmes</strong>. It is a tutored course; the page explains how to join a session.</p>
        <p><a class="btn green" href="https://virtual-learning-center.fao.org/admin/tool/custompage/view.php?id=67" target="_blank" rel="noopener">FAO · Animal breeding course &#8594;</a></p>
      </div>
    </div>
    <div class="attrib" style="margin-top:18px"><strong>Credit.</strong> Course developed by ASAP-Bio from the teaching materials of Hulunim Gatew Tariku, Department of Animal Sciences, Debre Berhan University, Ethiopia. Open-access for study.</div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-applied-animal-breeding.html", course6)
print("course6 appended")

# ---------------- COURSE 7: Animal Reproduction & Reproductive Biotechnology ----------------
course7 = head("Animal Reproduction and Reproductive Biotechnology","knowledge.html","A self-paced ASAP-Bio course on animal reproduction and reproductive biotechnology: reproductive anatomy and hormones, the estrous cycle, gestation, artificial insemination, semen evaluation, estrus synchronisation and embryo transfer. Developed from the teaching materials of Hulunim Gatew Tariku, Debre Berhan University.") + """
<section class="course-hero" id="top"><div class="wrap">
  <div class="eyebrow">Knowledge Hub · Biodiversity and Breeding programs</div>
  <h1>Animal Reproduction and Reproductive Biotechnology</h1>
  <p class="csub">Reproduction is how genetic gain reaches the herd. This course covers the reproductive systems and hormones, the estrous cycle and gestation, and the biotechnologies, artificial insemination, semen processing, estrus synchronisation and embryo transfer, that multiply superior genetics across a population.</p>
  <div class="metachips">
    <span>★ Self-paced</span><span>⏱ ~7 hours</span><span>🎓 MSc level</span><span>🧬 Biotech focus</span><span>🔓 Open access</span>
  </div>
</div></section>

<section><div class="wrap">
  """ + HUL_CREDIT + """
  <div class="callout gold"><strong>One Health link.</strong> Reproductive performance sits at the animal&ndash;human&ndash;environment interface: fertility drives food security and farm income, hygienic AI reduces disease transmission, and reproductive disorders are sentinels of herd health. This course is placed under Biodiversity and Breeding programs but connects directly to the One Health theme.</div>

  <h2>What you will learn</h2>
  <div class="outcomes"><ul>
    <li>Identify the organs of the male and female reproductive systems and their functions.</li>
    <li>Explain the hormones that govern reproduction and how they are regulated.</li>
    <li>Describe the estrous cycle and its phases, and the length of gestation across species.</li>
    <li>Carry out the logic of artificial insemination: semen collection, evaluation, dilution, packaging and timing.</li>
    <li>Apply estrus-synchronisation protocols and outline embryo transfer (MOET).</li>
    <li>Connect reproductive biotechnology to the delivery of genetic gain in a breeding programme.</li>
  </ul></div>

  <h3>Course contents</h3>
  <div class="toc-chips">
    <a href="#r1">1 · Reproductive anatomy</a>
    <a href="#r2">2 · Reproductive hormones</a>
    <a href="#r3">3 · Estrous cycle, fertilisation &amp; gestation</a>
    <a href="#r4">4 · Artificial insemination &amp; semen</a>
    <a href="#r5">5 · Synchronisation &amp; embryo transfer</a>
    <a href="#r6">6 · Glossary &amp; credits</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">

  <div class="module" id="r1">
    <div class="module-head"><div class="module-num">1</div><div><h2>The reproductive systems</h2><div class="module-time">~50 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Name the male and female reproductive organs and their roles.</li></ul></div>
    <p>The <strong>male</strong> system has three jobs: produce sperm, produce hormones, and deliver semen. The <strong>testes</strong>, held outside the body in the <strong>scrotum</strong> for temperature control, produce spermatozoa and testosterone. Sperm mature and are stored in the <strong>epididymis</strong>, travel through the <strong>ductus (vas) deferens</strong>, and are mixed with fluid from the <strong>accessory sex glands</strong> (seminal vesicles, prostate, bulbourethral) to form semen, delivered through the penis.</p>
    <p>The <strong>female</strong> system produces ova, receives semen, and supports pregnancy. The <strong>ovaries</strong> produce ova and the hormones estrogen and progesterone. The <strong>oviducts (fallopian tubes)</strong> are the site of fertilisation; the <strong>uterus</strong> nourishes the developing fetus; the <strong>cervix</strong> seals the uterus and is where AI deposits semen; and the <strong>vagina</strong> receives the penis at mating. Knowing this layout is the basis for AI, pregnancy diagnosis and reproductive health.</p>
    <details class="quiz"><summary>Check: why are the testes carried in the scrotum, outside the body cavity?</summary><div class="ans">Spermatogenesis requires a temperature a few degrees below core body temperature. The scrotum, with its muscle and a counter-current blood supply, holds the testes outside the body and regulates their temperature; if they are retained inside (cryptorchidism), sperm production fails.</div></details>
  </div>

  <div class="module" id="r2">
    <div class="module-head"><div class="module-num">2</div><div><h2>Reproductive hormones and their control</h2><div class="module-time">~55 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>List the main reproductive hormones and their sources and actions.</li>
      <li>Explain the hypothalamic&ndash;pituitary&ndash;gonadal axis and feedback.</li></ul></div>
    <p>Reproduction is run by a hormonal cascade. The <strong>hypothalamus</strong> releases <strong>GnRH</strong>, which makes the <strong>anterior pituitary</strong> secrete two gonadotropins: <strong>FSH</strong> (follicle-stimulating hormone), which grows ovarian follicles, and <strong>LH</strong> (luteinizing hormone), whose surge triggers <strong>ovulation</strong> and forms the corpus luteum. The growing follicle secretes <strong>estrogen</strong>, which produces the signs of heat and, by positive feedback, the LH surge. After ovulation the <strong>corpus luteum</strong> secretes <strong>progesterone</strong>, which maintains pregnancy and, by negative feedback, blocks a new cycle.</p>
    <p>Two more hormones are pivotal in practice. <strong>Prostaglandin F2&alpha; (PGF2&alpha;)</strong> from the uterus destroys (luteolyses) the corpus luteum, ending the luteal phase and bringing the female back into heat, the basis of synchronisation. <strong>Oxytocin</strong> drives uterine contractions at birth and milk let-down. Understanding this axis explains every hormonal tool used to manage breeding.</p>
    <div class="figbox">
      <svg viewBox="0 0 620 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hypothalamic pituitary gonadal axis">
        <defs><marker id="rh" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2E6B3E"/></marker></defs>
        <g font-family="Segoe UI,Arial" font-size="12" text-anchor="middle">
          <rect x="20" y="55" width="120" height="44" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="80" y="73">Hypothalamus</text><text x="80" y="90" font-size="11" fill="#5f6b62">GnRH</text>
          <rect x="180" y="55" width="120" height="44" rx="9" fill="#E3EEF6" stroke="#3E7CB1"/><text x="240" y="73">Pituitary</text><text x="240" y="90" font-size="11" fill="#5f6b62">FSH · LH</text>
          <rect x="340" y="55" width="120" height="44" rx="9" fill="#FBF3E3" stroke="#C8962A"/><text x="400" y="73">Ovary / testis</text><text x="400" y="90" font-size="11" fill="#5f6b62">follicle · CL</text>
          <rect x="500" y="55" width="100" height="44" rx="9" fill="#EEF3EC" stroke="#2E6B3E"/><text x="550" y="73">Estrogen</text><text x="550" y="90" font-size="11" fill="#5f6b62">progesterone</text>
          <line x1="140" y1="77" x2="178" y2="77" stroke="#2E6B3E" stroke-width="2" marker-end="url(#rh)"/>
          <line x1="300" y1="77" x2="338" y2="77" stroke="#2E6B3E" stroke-width="2" marker-end="url(#rh)"/>
          <line x1="460" y1="77" x2="498" y2="77" stroke="#2E6B3E" stroke-width="2" marker-end="url(#rh)"/>
          <path d="M550,100 C550,130 80,130 80,101" fill="none" stroke="#b06" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#rh)"/>
          <text x="315" y="128" font-size="11" fill="#b06">feedback (negative / positive)</text>
        </g>
      </svg>
      <figcaption>The hypothalamic&ndash;pituitary&ndash;gonadal axis; steroid feedback closes the loop and PGF2&alpha; resets it by luteolysis.</figcaption>
    </div>
    <details class="quiz"><summary>Check: an injection of PGF2&alpha; brings a cow into heat a few days later. What did it do, hormonally?</summary><div class="ans">PGF2&alpha; caused luteolysis: it destroyed the corpus luteum, so progesterone fell. With progesterone&rsquo;s negative feedback removed, FSH/LH rise, a follicle matures, estrogen climbs and the cow returns to estrus. This is why PGF2&alpha; is the workhorse of estrus synchronisation, but only in cows that have a responsive corpus luteum.</div></details>
  </div>

  <div class="module" id="r3">
    <div class="module-head"><div class="module-num">3</div><div><h2>The estrous cycle, fertilisation and gestation</h2><div class="module-time">~65 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Describe the four phases of the estrous cycle.</li>
      <li>Quote cycle and gestation lengths for the main species.</li>
      <li>Outline fertilisation and the stages of pregnancy.</li></ul></div>
    <p><strong>Puberty</strong> marks the start of reproductive life; thereafter non-pregnant females cycle. The <strong>estrous cycle</strong> has four phases: <strong>proestrus</strong> (follicle growth), <strong>estrus</strong> (standing heat, when the female accepts mating and ovulation is near), <strong>metestrus</strong> (corpus luteum forms) and <strong>diestrus</strong> (active corpus luteum, high progesterone). If no pregnancy occurs, PGF2&alpha; ends diestrus and the cycle repeats. Cattle and many species are <strong>polyestrous</strong> (cycle year-round); sheep and goats are typically <strong>seasonal</strong>.</p>
    <div class="tablewrap"><table class="t">
      <tr><th>Species</th><th>Estrous cycle</th><th>Duration of estrus (heat)</th><th>Gestation (avg, range)</th></tr>
      <tr><td>Cattle</td><td>21 days (16&ndash;24)</td><td>18&ndash;19 h (range to ~24)</td><td>285 d (278&ndash;290)</td></tr>
      <tr><td>Sheep</td><td>16&ndash;17 days</td><td>24&ndash;36 h</td><td>148 d (140&ndash;159)</td></tr>
      <tr><td>Goat</td><td>21 days</td><td>24&ndash;36 h</td><td>150 d</td></tr>
      <tr><td>Swine</td><td>21 days</td><td>2&ndash;3 days</td><td>114 d (102&ndash;128)</td></tr>
      <tr><td>Horse</td><td>21&ndash;22 days</td><td>4&ndash;8 days</td><td>338 d (301&ndash;365)</td></tr>
    </table></div>
    <p class="matnote">Cycle and gestation lengths from the course materials; ranges reflect breed and environment.</p>
    <p>At mating or AI, sperm travel to the oviduct and one fertilises the ovum, restoring the diploid zygote. Pregnancy then proceeds through <strong>cleavage</strong> (the early dividing ovum, roughly days 0&ndash;13), <strong>differentiation / embryo</strong> (germ layers, membranes and organs form, about days 14&ndash;45) and <strong>growth</strong> (day 46 to birth). <strong>Parturition</strong> (birth) is triggered by a fetal&ndash;maternal hormonal cascade and assisted by oxytocin-driven contractions. Knowing normal gestation length lets a manager predict calving dates and flag problems early.</p>
    <details class="quiz"><summary>Check: a cattle breeder wants calves born in a tight window next spring. Using the table, roughly when should AI take place, and why does cycle knowledge help?</summary><div class="ans">With ~285-day gestation, AI should occur about 9.5 months before the target calving window (so early-to-mid summer for spring calving). Because cows cycle about every 21 days with only ~18 hours of standing heat, accurate heat detection or synchronisation is needed to place AI at the right point of the cycle and hit the window.</div></details>
  </div>

  <div class="module" id="r4">
    <div class="module-head"><div class="module-num">4</div><div><h2>Artificial insemination and semen technology</h2><div class="module-time">~80 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain why AI is the main vehicle for disseminating genetic gain.</li>
      <li>Evaluate semen and outline its dilution, packaging and storage.</li>
      <li>Detect heat and time insemination correctly.</li></ul></div>
    <p><strong>Artificial insemination (AI)</strong> places semen in the female&rsquo;s reproductive tract by instrument rather than natural mating. It is the single most important reproductive technology in breeding because one superior, progeny-tested sire can produce hundreds of thousands of doses, spreading proven genetics widely while avoiding the cost, risk and disease transmission of keeping bulls. AI is what turns a high breeding value into population-wide gain.</p>
    <p><strong>Semen collection</strong> is usually by <strong>artificial vagina</strong> (or electro-ejaculation). The ejaculate is then <strong>evaluated</strong>: gross measures (volume, colour, pH), <strong>concentration</strong> (sperm per mL), and microscopic assessment of <strong>motility</strong> (the proportion of progressively motile sperm) and <strong>morphology</strong> (the proportion of normal versus abnormal heads, midpieces and tails). Only semen meeting thresholds is processed.</p>
    <p>Good semen is then <strong>diluted</strong> in an <strong>extender</strong>, a buffered medium with energy source, protectants and antibiotics, which increases the number of doses, nourishes and protects the sperm, and controls bacteria. A good extender is iso-osmotic, buffers pH, protects against cold shock (egg-yolk or milk) and contains a cryoprotectant (glycerol) for freezing. Semen is <strong>packaged</strong> (commonly in 0.25 or 0.5 mL straws), frozen in liquid nitrogen and stored at &minus;196&deg;C, where it remains viable for years.</p>
    <p>Success then hinges on <strong>timing</strong>. Because standing heat is short and ovulation follows it, the classic <strong>a.m./p.m. rule</strong> applies: cows seen in heat in the morning are bred that evening, and those seen in the evening are bred the next morning, placing capacitated sperm in the tract before ovulation. Heat is detected by direct observation (standing to be mounted is the definitive sign), aided by <strong>KAMAR mount detectors</strong>, tail paint, teaser animals or activity sensors.</p>
    <details class="quiz"><summary>Check: a technician thaws a straw and finds 25% progressive motility and many bent tails. Should it be used, and what two evaluations produced that judgement?</summary><div class="ans">No, it should be rejected: low progressive motility (well below the usual minimum) and a high share of morphological abnormalities both predict poor fertility. The judgement comes from the motility assessment and the morphology (normal-versus-abnormal) evaluation, the two core microscopic checks in semen evaluation.</div></details>
  </div>

  <div class="module" id="r5">
    <div class="module-head"><div class="module-num">5</div><div><h2>Estrus synchronisation and embryo transfer</h2><div class="module-time">~60 minutes</div></div></div>
    <div class="outcomes"><h4>By the end you can</h4><ul>
      <li>Explain estrus synchronisation and a PGF2&alpha; protocol.</li>
      <li>Outline MOET (multiple ovulation and embryo transfer) and its purpose.</li>
      <li>Place these tools in a breeding programme.</li></ul></div>
    <p><strong>Estrus synchronisation</strong> brings a group of females into heat together so they can be inseminated at one planned time (fixed-time AI), concentrating calving, easing management and making AI practical on large numbers. The commonest approach uses <strong>PGF2&alpha;</strong>: a widely used protocol gives <strong>two injections 14 days apart</strong>, so that whatever stage each cow started in, all have a responsive corpus luteum at the second injection and come into heat together a few days later. Progesterone devices (CIDR/PRID) achieve the same by mimicking then withdrawing the luteal phase, and are useful in non-cycling animals where PGF2&alpha; alone will not work.</p>
    <p><strong>Embryo transfer</strong>, in its programme form <strong>MOET</strong>, multiplies the female side of the pedigree. A genetically valuable <strong>donor</strong> is <strong>superovulated</strong> with FSH (the materials note repeated injections over about four days) to release many ova, inseminated, and her early embryos are recovered about a week later and transferred, fresh or frozen, into synchronised <strong>recipient</strong> cows that carry the pregnancies. Donor and recipients must be on the same cycle stage, again synchronised with PGF2&alpha;. MOET lets an elite cow produce many more offspring than the one calf a year of natural reproduction, raising selection intensity on the dam side and shortening the generation interval, the reproductive complement to genomic selection.</p>
    <div class="callout green"><strong>Why this matters for breeding.</strong> Selection and BLUP (see <a href="course-applied-animal-breeding.html">Applied Animal Breeding</a>) decide which animals are genetically best; AI, synchronisation and MOET are how that superiority is <em>multiplied and delivered</em> to the population. The two halves together are what produce genetic gain on the ground.</div>
    <details class="quiz"><summary>Check: how do AI and MOET each raise the rate of genetic gain, in terms of the breeder&rsquo;s equation?</summary><div class="ans">AI raises selection intensity on the sire side (one top bull breeds enormous numbers, so only the very best males are used) and helps shorten the generation interval. MOET raises selection intensity on the dam side (an elite cow yields many offspring instead of one a year) and can shorten the generation interval too. Both increase the i term, and reduce L, in &Delta;G = (i &middot; r &middot; &sigma;_A)/L.</div></details>
  </div>

  <div class="module" id="r6">
    <div class="module-head"><div class="module-num">6</div><div><h2>Glossary, recommendations &amp; credits</h2><div class="module-time">~10 minutes</div></div></div>
    <h3>Glossary</h3>
    <div class="gloss">
      <div><b>Estrous cycle</b>, the recurring reproductive cycle: proestrus, estrus, metestrus, diestrus.</div>
      <div><b>Estrus (heat)</b>, the period when the female accepts mating; ovulation is near.</div>
      <div><b>GnRH / FSH / LH</b>, the hypothalamic and pituitary hormones driving follicle growth and ovulation.</div>
      <div><b>Estrogen / progesterone</b>, ovarian steroids of heat and of pregnancy maintenance.</div>
      <div><b>PGF2&alpha;</b>, uterine prostaglandin that lyses the corpus luteum; used to synchronise estrus.</div>
      <div><b>Corpus luteum (CL)</b>, progesterone-secreting structure formed after ovulation.</div>
      <div><b>Artificial insemination (AI)</b>, instrumental deposition of semen in the tract.</div>
      <div><b>Extender / diluent</b>, medium that increases, nourishes and protects semen doses.</div>
      <div><b>Motility / morphology</b>, the two core microscopic measures of semen quality.</div>
      <div><b>Superovulation</b>, FSH-induced release of many ova from a donor.</div>
      <div><b>MOET</b>, multiple ovulation and embryo transfer.</div>
      <div><b>Gestation</b>, the pregnancy period; e.g. ~285 days in cattle.</div>
    </div>
    <div class="callout green" style="margin-top:18px"><strong>Where to go next.</strong> Pair this course with <a href="course-applied-animal-breeding.html">Applied Animal Breeding</a> (which decides <em>which</em> animals to breed) and, for the genomic acceleration of gain, <a href="course-genomic-selection-breeding.html">Breeding programs with Genomic selection</a>. The genetics foundation is in <a href="course-foundations-animal-genetics.html">Foundations of Animal Genetics</a>.</div>
    <div class="attrib" style="margin-top:18px"><strong>Credit.</strong> Course developed by ASAP-Bio from the teaching materials of Hulunim Gatew Tariku, Department of Animal Sciences, Debre Berhan University, Ethiopia. Open-access for study.</div>
    <div class="coursenav">
      <a class="btn green" href="knowledge.html">← Back to the Knowledge Hub</a>
      <a class="btn" href="#top">↑ Back to top</a>
    </div>
  </div>

</div></section>
""" + FOOT
write("course-animal-reproduction-biotech.html", course7)
print("course7 appended")
