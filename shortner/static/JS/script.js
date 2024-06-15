let copyText = document.getElementById('copyText');
let copybtn = document.getElementById('copybtn');

copybtn.addEventListener('click', () => {
    let text = copyText.textContent
    navigator.clipboard.writeText(text)
    alert('Text copied to clipboard')
})