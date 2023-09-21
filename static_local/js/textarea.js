// Bardにより生成
// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', function() {
  // classがdynamic-textareaであるtextareaを取得
  const textareas = document.querySelectorAll('.dynamic-textarea');

  // textareaの縦の大きさを調整
  textareas.forEach(textarea => {
    autoResizeTextArea(textarea);
    console.log("textarea")
  });
});

// 入力時に実行
document.addEventListener('input', function(event) {
  // 対象要素がtextareaタグであり、かつclass属性に"dynamic-textarea"が含まれている場合
  if (event.target.tagName.toLowerCase() === 'textarea' && event.target.classList.contains('dynamic-textarea')) {
    // textareaの縦の大きさを調整
    autoResizeTextArea(event.target);
    console.log("textarea")
  }
});

// textareaの高さを調整する関数
function autoResizeTextArea(textArea) {
  // textareaのheight属性を取得
  const height = textArea.scrollHeight + 'px';

  // textareaのheight属性を設定
  textArea.style.height = height;
}

// // ウィンドウサイズ変更時のイベントハンドラ
// window.addEventListener("resize", function() {
//   // classがdynamic-textareaであるtextareaを取得
//   const textareas = document.querySelectorAll('.dynamic-textarea');
//
//   // textareaの縦の大きさを調整
//   textareas.forEach(textarea => {
//     autoResizeTextArea(textarea);
//   });
// });
