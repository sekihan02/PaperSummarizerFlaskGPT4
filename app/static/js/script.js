document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const fileInput = document.getElementById('fileInput');
    const dropArea = document.getElementById('dropArea');
    const fileNameDisplay = document.getElementById('fileName');

    // ドロップエリアのイベント
    dropArea.addEventListener('dragover', (event) => {
        event.stopPropagation();
        event.preventDefault();
        event.dataTransfer.dropEffect = 'copy';
    });

    dropArea.addEventListener('drop', (event) => {
        event.stopPropagation();
        event.preventDefault();
        const files = event.dataTransfer.files;
        handleFiles(files);
    });

    dropArea.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', () => {
        handleFiles(fileInput.files);
    });

    form.addEventListener('submit', function(e) {
        // デフォルトのフォーム送信を防止
        e.preventDefault();

        // ロード画面を表示
        showLoadingScreen();

        // フォームのデータを送信
        const formData = new FormData(this);
        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            // ロード画面を非表示にする
            hideLoadingScreen();
        });
    });
    
    function handleFiles(files) {
        if (files.length > 0) {
            const file = files[0];
            if (file.type === 'application/pdf') {
                // ファイル名を表示
                fileNameDisplay.textContent = `選択されたファイル: ${file.name}`;
                fileInput.files = files;
            } else {
                // PDF以外のファイルが選択された場合のエラー処理
                alert('PDFファイルを選択してください。');
            }
        }
    }
});



function showLoadingScreen() {
    // ロード画面を表示するコード
    const loadingScreen = document.createElement('div');
    loadingScreen.id = 'loadingScreen';
    // loadingScreen.innerHTML = '<div class="loader">Loading...</div>';
    loadingScreen.innerHTML = '<div class="loader"></div>';
    document.body.appendChild(loadingScreen);
}

function hideLoadingScreen() {
    // ロード画面を非表示にするコード
    const loadingScreen = document.getElementById('loadingScreen');
    if (loadingScreen) {
        loadingScreen.remove();
    }
}

