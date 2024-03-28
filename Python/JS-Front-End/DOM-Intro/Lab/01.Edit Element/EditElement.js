function editElement(reference, match, replacer) {
    let text = reference.textContent;
    let editedText = text.replace(new RegExp(match, 'g'), replacer);
    reference.textContent = editedText;
}