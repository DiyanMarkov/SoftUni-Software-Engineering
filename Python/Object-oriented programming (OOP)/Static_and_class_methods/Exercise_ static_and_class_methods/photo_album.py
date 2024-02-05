import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__initialize_photos()
        self.index = 0

    def __initialize_photos(self):
        matrix = []
        for i in range(self.pages):
            matrix.append([])

        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label:str):
        if len(self.photos[self.index]) == 4:
            self.index += 1

        try:
            self.photos[self.index].append(label)

            return f"{label} photo added successfully on page {self.index + 1} slot {len(self.photos[self.index])}"

        except IndexError:
            return "No more free slots"


    def display(self):
        res = "-" * 11 + "\n"

        for page in self.photos:
            res += ' '.join(["[]" for photo_name in page]) + "\n"
            res += "-" * 11 + "\n"

        return res

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())