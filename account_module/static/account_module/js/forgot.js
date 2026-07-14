/**
 * پروژه مسیر - مدیریت رفتارهای صفحه فراموشی رمز عبور
 */
document.addEventListener('DOMContentLoaded', function() {
    const forgotPasswordForm = document.getElementById('forgotPasswordForm');

    if (forgotPasswordForm) {
        forgotPasswordForm.addEventListener('submit', function(e) {
            // در حال حاضر اجازه می‌دهیم فرم به طور طبیعی سابمیت شود تا به جنگو برسد.
            // در صورتی که نیاز به ولیدیشن‌های سمت فرانت داشته باشید، کدهای آن اینجا قرار می‌گیرند.

            const emailInput = forgotPasswordForm.querySelector('input[type="email"]');
            const captchaInput = forgotPasswordForm.querySelector('input[name="captcha_code"]');

            if (!emailInput.value || !captchaInput.value) {
                e.preventDefault();
                alert('لطفاً تمامی فیلدها را به درستی تکمیل کنید.');
            }
        });
    }
});