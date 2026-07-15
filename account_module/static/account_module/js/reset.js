document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("resetForm");
    const pass1 = document.getElementById("password");
    const pass2 = document.getElementById("confirm_password");
    const errorMsg = document.getElementById("errorMsg");

    if (form) {
        form.addEventListener("submit", function(e) {
            // در کنار ولیدیشن سمت سرور جنگو، این کار در فرانت‌اند خطای سریع‌تری به کاربر نمایش می‌دهد
            if (pass1.value !== pass2.value) {
                e.preventDefault();
                errorMsg.style.display = "block";
                pass2.style.borderColor = "#ff4d4d";
            } else {
                errorMsg.style.display = "none";
                pass2.style.borderColor = "var(--line)";
            }
        });

        pass2.addEventListener("input", function() {
            errorMsg.style.display = "none";
            pass2.style.borderColor = "var(--line)";
        });
    }
});