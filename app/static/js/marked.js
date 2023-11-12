document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    form.addEventListener("submit", function(e) {
        // ロード画面を表示
        showLoadingScreen();

        // フォームのデータを送信
        const formData = new FormData(this);
        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(text => {
            // MarkdownをHTMLに変換
            const html = marked(text);  // ここでmarkedを使用
            // 現在のページの内容を更新
            document.body.innerHTML = html;
        })
        .catch(error => {
            console.error('Error:', error);
            hideLoadingScreen();
        });

        // デフォルトのフォーム送信を防止
        e.preventDefault();
    });
});

// showLoadingScreen と hideLoadingScreen 関数は省略
