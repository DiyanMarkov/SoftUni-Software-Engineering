function playlist(array) {

    class Song {
        constructor(type, name, time) {
            this.type = type
            this.name = name
            this.time = time
        }
    }

    let songs = [];
    let numberOfSongs = array.shift();
    let typeSong = array.pop();

    for (let index = 0; index < numberOfSongs; index++) {
        let [type, name, time] = array[index].split('_');
        let currentSong = new Song(type, name, time);
        songs.push(currentSong);
        
    }

    if (typeSong === 'all') {
        for (const song of songs) {
            console.log(song.name);
        }
    } else {
        let filteredSongs = songs.filter((item) => item.type === typeSong);
        filteredSongs.forEach((item) => console.log(item.name));
    }

    
}

playlist([3, 'favourite_DownTown_3:14', 'favourite_Kiss_4:16', 'favourite_Smooth Criminal_4:01', 'favourite'])