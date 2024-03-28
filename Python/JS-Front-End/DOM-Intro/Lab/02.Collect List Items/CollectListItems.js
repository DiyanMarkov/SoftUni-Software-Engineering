function extractText() {
    elements = document.getElementsByTagName('li');
    
    let text = []

    for (const el of Array.from(elements)) {
        text.push(el.textContent)
    }

    textArea = document.getElementById('result');
    textArea.textContent = text.join('\n');

}