function personInfo(firstName, lastName, age) {
    let obj = {};
    obj.firstName = firstName;
    obj.lastName = lastName;
    obj.age = age;

    return obj
}

console.log(personInfo("Peter", "Pan", "20"))