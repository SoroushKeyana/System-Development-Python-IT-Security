class Person {
    static instances = [];

    constructor(firstName, lastName, age, email){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = email;
        Person.instances.push(this);
    }
    getInstances() {
        return Person.instances;
    }
}

let person1 = new Person("Maria", "Peterson", 21, "mp@gmail.com");
let person2 = new Person("Lexicon");
let person3 = new Person("Stefan", "Larsson", 25);
let person4 = new Person("Peter", "Jansson", 24, "ptr@gmail.com");

console.log(Person.instances);