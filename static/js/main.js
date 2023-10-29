const content = "파일을 업로드하세요.";
const text = document.querySelector(".text");
let index = 0;

function typing() {
    let txt = content[index++];
    text.innerHTML += txt === "\n" ? "<br/>":txt;
    if ( index > content.length) {
        text.textContent = "";
        index = 0;
    }
}
setInterval(typing, 120)