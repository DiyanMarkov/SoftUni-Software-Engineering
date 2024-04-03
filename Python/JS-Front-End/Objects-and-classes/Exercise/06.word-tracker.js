function wordTracker(array) {
    let list = array.shift().split(' ')
    
    let occurrences = {};

    for (const word of list) {
        occurrences[word] = 0

        for (const string of array) {
            if (word === string) {
                occurrences[word] += 1;
            }
        }
   
    }

    let entries = Object.entries(occurrences).sort((a,b) => b[1] - a[1]);

    for (const [key, value] of entries) {
        console.log(`${key} - ${value}`);
    }
}   

wordTracker([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
    ]);