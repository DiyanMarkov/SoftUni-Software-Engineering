function colorize() {
    const rows = document.querySelectorAll('tr:nth-child(even)')

    for (let index = 0; index < rows.length; index++) {
        rows[index].style.background = 'Teal';
    }
}