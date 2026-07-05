const items = document.querySelectorAll('.plan-card .item');
  const xpFill = document.getElementById('xpFill');
  const xpTargets = [8, 35, 68];
  let i = 0;

  function cycle(){
    if(i > 0){
      items[i-1].classList.remove('checked');
      void items[i-1].offsetWidth;
    }
    if(i >= items.length){
      items.forEach(it => it.classList.remove('checked'));
      xpFill.style.width = '8%';
      i = 0;
      void document.body.offsetWidth;
    }
    const current = items[i];
    setTimeout(() => {
      current.classList.add('checked');
      xpFill.style.width = xpTargets[i] + '%';
    }, 500);
    i++;
    setTimeout(cycle, 1700);
  }

  if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    setTimeout(cycle, 500);
  } else {
    items.forEach(it => it.classList.add('checked'));
    xpFill.style.width = '68%';
  }

  document.getElementById('signupForm').addEventListener('submit', function(e){
    e.preventDefault();
    if(this.checkValidity()){
      alert(currentLang === 'fa' ? 'بعدی: انتخاب مقطع تحصیلی و تنظیم برنامه روزانه' : 'Next: choose your grade level and set up your daily plan');
    } else {
      this.reportValidity();
    }
  });

  document.getElementById('googleBtn').addEventListener('click', () => alert('اتصال به گوگل بعداً وصل می‌شود.'));
  document.getElementById('facebookBtn').addEventListener('click', () => alert('اتصال به فیسبوک بعداً وصل می‌شود.'));

  // ---- language switch ----
  let currentLang = 'fa';
  function applyLang(lang){
    currentLang = lang;
    document.documentElement.setAttribute('lang', lang === 'fa' ? 'fa' : 'en');
    document.documentElement.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');

    document.querySelectorAll('[data-fa-html]').forEach(el => {
      el.innerHTML = lang === 'fa' ? el.dataset.faHtml : el.dataset.enHtml;
    });
    document.querySelectorAll('[data-fa]:not([data-fa-html])').forEach(el => {
      const val = lang === 'fa' ? el.dataset.fa : el.dataset.en;
      if(val !== undefined && val !== '') el.textContent = val;
    });
    document.querySelectorAll('[data-fa-ph]').forEach(el => {
      el.setAttribute('placeholder', lang === 'fa' ? el.dataset.faPh : el.dataset.enPh);
    });
    document.querySelectorAll('.lang-switch button').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  }
  document.querySelectorAll('.lang-switch button').forEach(btn => {
    btn.addEventListener('click', () => applyLang(btn.dataset.lang));
  });
