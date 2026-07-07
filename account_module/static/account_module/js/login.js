// ==========================================
// 1. CYCLE ANIMATION (برنامه‌ریز درسی هوشمند)
// ==========================================
const items = document.querySelectorAll('.plan-card .item');
const xpFill = document.getElementById('xpFill');
const xpTargets = [8, 35, 68];
let i = 0;

function cycle() {
  if (!items.length || !xpFill) return;

  if (i > 0) {
    items[i - 1].classList.remove('checked');
    void items[i - 1].offsetWidth; // Trigger reflow
  }

  if (i >= items.length) {
    items.forEach(it => it.classList.remove('checked'));
    xpFill.style.width = '8%';
    i = 0;
    void document.body.offsetWidth;
  }

  const current = items[i];

  setTimeout(() => {
    if (current) {
      current.classList.add('checked');
      xpFill.style.width = xpTargets[i] + '%';
    }
  }, 500);

  i++;
  setTimeout(cycle, 1700);
}

// بررسی ترجیحات انیمیشن کاربر (Accessibility)
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  setTimeout(cycle, 500);
} else {
  items.forEach(it => it.classList.add('checked'));
  if (xpFill) xpFill.style.width = '68%';
}


// ==========================================
// 2. SOCIAL BUTTONS HANDLERS
// ==========================================


const facebookBtn = document.getElementById('facebookBtn');
if (facebookBtn) {
  facebookBtn.addEventListener('click', () =>
    alert('اتصال به فیسبوک بعداً وصل می‌شود.')
  );
}


// ==========================================
// 3. PASSWORD TOGGLE (اصلاح شده و داینامیک)
// ==========================================
const pwToggle = document.getElementById('pwToggle');
if (pwToggle) {
  pwToggle.addEventListener('click', function () {
    // پیدا کردن اینپوت پسورد از طریق والد مشترک برای جلوگیری از تداخل با IDهای جنگو
    const pwContainer = this.closest('.pw-wrap');
    const pw = pwContainer ? pwContainer.querySelector('input') : null;

    const show = document.getElementById('pwIconShow');
    const hide = document.getElementById('pwIconHide');

    if (!pw) return;

    const isHidden = pw.type === 'password';
    pw.type = isHidden ? 'text' : 'password';

    if (show && hide) {
      show.style.display = isHidden ? 'none' : 'block';
      hide.style.display = isHidden ? 'block' : 'none';
    }

    this.setAttribute(
      'aria-label',
      isHidden ? 'پنهان کردن رمز عبور' : 'نمایش رمز عبور'
    );
  });
}


// ==========================================
// 4. LOGIN & SIGNUP FORM SUBMIT
// ==========================================
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', function (e) {
    console.log("FORM SUBMITTED TO DJANGO");

    // مدیریت اعتبارسنجی اولیه مرورگر قبل از ارسال به جنگو
    if (!this.checkValidity()) {
      e.preventDefault();
      this.reportValidity();
    }
  });
}


// ==========================================
// 5. LANGUAGE SWITCHER (FA / EN)
// ==========================================
let currentLang = 'fa';

function applyLang(lang) {
  currentLang = lang;

  document.documentElement.setAttribute('lang', lang === 'fa' ? 'fa' : 'en');
  document.documentElement.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');

  // تغییر محتوای HTML عناصر دارای دیتاسِت
  document.querySelectorAll('[data-fa-html]').forEach(el => {
    el.innerHTML = lang === 'fa' ? el.dataset.faHtml : el.dataset.enHtml;
  });

  // تغییر متون متنی ساده
  document.querySelectorAll('[data-fa]:not([data-fa-html])').forEach(el => {
    const val = lang === 'fa' ? el.dataset.fa : el.dataset.en;
    if (val !== undefined && val !== '') el.textContent = val;
  });

  // تغییر پلیس‌هولدرهای اینپوت‌ها
  document.querySelectorAll('[data-fa-ph]').forEach(el => {
    el.setAttribute(
      'placeholder',
      lang === 'fa' ? el.dataset.faPh : el.dataset.enPh
    );
  });

  // تغییر وضعیت اکتیو دکمه‌های سوئیچ زبان
  document.querySelectorAll('.lang-switch button').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
}

// اتصال رویداد کلیک به دکمه‌های تغییر زبان
document.querySelectorAll('.lang-switch button').forEach(btn => {
  btn.addEventListener('click', () => applyLang(btn.dataset.lang));
});