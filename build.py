NAV=[("index.html","Home"),("about.html","About"),("contact.html","Contact")]
def page(fn,title,desc,main):
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#0b0b0b">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="wrap nav"><a class="brand" href="index.html"><img src="logo.svg" alt="" width="40" height="40">CKardinal Solutions, LLC</a><nav aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main">
{main}
</main>
<footer><div class="wrap foot"><p>&copy; 2026 CKardinal Solutions, LLC. All rights reserved.</p><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms</a></li><li><a href="contact.html">Contact</a></li></ul></div></footer>
</body>
</html>
'''
EMAIL='<a href="mailto:carlos.matos@ckardinal.com">carlos.matos@ckardinal.com</a>'
home=f'''<section class="hero"><div class="wrap hero-grid"><div>
<span class="eyebrow">CKardinal Solutions, LLC</span>
<h1>Practical solutions for everyday business.</h1>
<p class="lead">CKardinal Solutions, LLC is a general-purpose business company. We take on well-defined work, plan it clearly and deliver it with care.</p>
<a class="btn" href="contact.html">Get in touch</a>
</div><div class="crest-wrap"><img class="crest" src="crest.png" alt="CKardinal Solutions, LLC crest" width="534" height="720"></div>
</div></section>
<section class="soft"><div class="wrap">
<div class="head"><span class="eyebrow">What we do</span><h2>Services and capabilities</h2><p>Our work spans a few core areas, scoped to fit each engagement.</p></div>
<div class="grid">
<div class="card"><span class="num">01</span><h3>Business services</h3><p>Planning, organization and operational support for projects of different shapes and sizes.</p></div>
<div class="card"><span class="num">02</span><h3>Consulting</h3><p>Clear, practical advice to help define goals, weigh options and decide on next steps.</p></div>
<div class="card"><span class="num">03</span><h3>Software and digital products</h3><p>Designing and publishing software, including applications offered to the public.</p></div>
</div></div></section>
<section><div class="wrap split">
<div><span class="eyebrow">How we work</span><h2>Straightforward and accountable</h2></div>
<div><p>We agree on scope up front, communicate plainly along the way and stand behind what we deliver.</p><p>Every engagement starts with a conversation about what you need.</p></div>
</div></section>
<section class="soft"><div class="wrap cta">
<div><h2>Let&rsquo;s talk.</h2><p>Questions or project inquiries: {EMAIL}</p></div>
<a class="btn btn-dark" href="contact.html">Contact us</a>
</div></section>'''
about=f'''<div class="page"><div class="wrap prose">
<span class="eyebrow">About</span><h1>About CKardinal Solutions, LLC</h1>
<p class="lead">CKardinal Solutions, LLC is a limited liability company founded and led by Carlos Matos.</p>
<h2>What we do</h2>
<p>CKardinal operates as a general-purpose business. Our work includes business services, consulting, and the development and publishing of software and digital products.</p>
<h2>Our approach</h2>
<ul><li>Clear scope and honest expectations.</li><li>Plain, direct communication.</li><li>Careful, quality work.</li><li>Respect for the privacy of the people we work with and the people who use our products.</li></ul>
<h2>Contact</h2>
<p>To reach us, email {EMAIL}.</p>
</div></div>'''
contact=f'''<div class="page"><div class="wrap prose">
<span class="eyebrow">Contact</span><h1>Contact us</h1>
<p class="lead">For business inquiries, product support or privacy questions, email us and we&rsquo;ll reply as soon as we can.</p>
<div class="contact-box"><h2 style="margin-top:0">Email</h2><p>{EMAIL}</p></div>
</div></div>'''
privacy=f'''<div class="page"><div class="wrap prose">
<span class="eyebrow">Legal</span><h1>Privacy Policy</h1>
<p class="meta">Last updated: October 12, 2026</p>
<p>This Privacy Policy explains how CKardinal Solutions, LLC (&ldquo;CKardinal,&rdquo; &ldquo;we,&rdquo; &ldquo;us&rdquo;) handles information in connection with this website, our business services and our software products, including mobile apps (together, the &ldquo;Services&rdquo;). Where a product has its own privacy notice, that notice also applies.</p>
<h2>Information we collect</h2>
<ul><li><strong>Information you send us.</strong> If you email us, we receive your email address and whatever you choose to include.</li>
<li><strong>Business information.</strong> If you work with us, we keep the contact and project details needed to do that work.</li>
<li><strong>Purchases.</strong> In-app purchases are processed by the app store (for example, Apple). We do not receive your full payment card details.</li></ul>
<h2>Information we do not collect</h2>
<p>This website does not use cookies, analytics or advertising trackers. We do not sell personal information, and we do not use it for targeted advertising.</p>
<h2>Data in our apps</h2>
<p>Our apps are designed to keep your content on your device where possible. If an app asks for access to features such as the camera, microphone or files, that access is used only to provide the feature you are using, and you can change it at any time in your device settings. Each app&rsquo;s App Store listing describes its data practices.</p>
<h2>How we use information</h2>
<ul><li>To respond to you and provide support.</li><li>To provide, maintain and improve the Services.</li><li>To meet legal, accounting and security obligations.</li></ul>
<h2>Sharing</h2>
<p>We share information only with service providers who help us operate (such as email hosting or app stores), when required by law, or as part of a business transfer. We do not sell it.</p>
<h2>Retention and security</h2>
<p>We keep information only as long as needed for the purposes above or as required by law, and we use reasonable measures to protect it. No method of transmission or storage is completely secure.</p>
<h2>Your choices and rights</h2>
<p>You may ask to access, correct or delete personal information we hold about you by emailing us. Depending on where you live, you may have additional rights under local law.</p>
<h2>Children</h2>
<p>Our Services are not directed to children under 13, and we do not knowingly collect their personal information.</p>
<h2>Changes</h2>
<p>We may update this policy. The date above shows when it last changed.</p>
<h2>Contact</h2>
<p>Privacy questions: {EMAIL}</p>
</div></div>'''
terms=f'''<div class="page"><div class="wrap prose">
<span class="eyebrow">Legal</span><h1>Terms of Use</h1>
<p class="meta">Last updated: October 12, 2026</p>
<p>These Terms govern your use of this website and the software products of CKardinal Solutions, LLC (&ldquo;CKardinal,&rdquo; &ldquo;we,&rdquo; &ldquo;us&rdquo;). By using them, you agree to these Terms.</p>
<h2>Use of the website</h2>
<p>You may use this website for lawful purposes only. Content on this site is provided for general information.</p>
<h2>Software products</h2>
<p>Apps distributed through an app store are licensed, not sold, and are also subject to that store&rsquo;s terms, including Apple&rsquo;s Licensed Application End User License Agreement where applicable. Purchases and refunds are handled by the app store.</p>
<h2>Services engagements</h2>
<p>Business or consulting work is governed by the separate agreement made for that engagement.</p>
<h2>Intellectual property</h2>
<p>The CKardinal name, this website and our products are owned by CKardinal Solutions, LLC and protected by applicable law.</p>
<h2>Disclaimer</h2>
<p>The website and products are provided &ldquo;as is&rdquo; without warranties of any kind, to the extent permitted by law.</p>
<h2>Limitation of liability</h2>
<p>To the extent permitted by law, CKardinal Solutions, LLC is not liable for indirect, incidental or consequential damages arising from use of the website or products.</p>
<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Florida, without regard to its conflict-of-law rules.</p>
<h2>Changes</h2>
<p>We may update these Terms. Continued use after changes means you accept them.</p>
<h2>Contact</h2>
<p>Questions about these Terms: {EMAIL}</p>
</div></div>'''
P=[("index.html","CKardinal Solutions, LLC","CKardinal Solutions, LLC is a general-purpose business company offering business services, consulting and software.",home),
("about.html","About | CKardinal Solutions, LLC","About CKardinal Solutions, LLC.",about),
("contact.html","Contact | CKardinal Solutions, LLC","Contact CKardinal Solutions, LLC.",contact),
("privacy.html","Privacy Policy | CKardinal Solutions, LLC","Privacy Policy for CKardinal Solutions, LLC.",privacy),
("terms.html","Terms of Use | CKardinal Solutions, LLC","Terms of Use for CKardinal Solutions, LLC.",terms)]
for fn,t,d,m in P: open(fn,"w").write(page(fn,t,d,m))
