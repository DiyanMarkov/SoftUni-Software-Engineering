function cats(array) {

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }   

    for (const cat of array) {
        const [name, age] = cat.split(' ');
        const newCat = new Cat(name, age);
        newCat.meow();

    }

}

cats(['Mellow 2', 'Tom 5'])