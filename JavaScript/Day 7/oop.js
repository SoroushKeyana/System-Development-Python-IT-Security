
class person {

    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    getName = () => {
        return this.name
    }
    getAge = () => {
        return this.age
    }
}
class House {
    constructor(address, rent, residents){
        this.address = address;
        this.rent = rent;
        this.resident = residents;
    }
    getAddress = () =>{
        return this.address
    }
    getRent = () =>{
        return this.rent
    }
    getResidents = () =>{
        return this.residents
    }
    addResident = (resident) =>{
        this.residents.push(resident);
    }
}

let person1 = new person('Soroush',28);
let person2 = new person('Someyeh',27);
let person3 = new person('Barsam', 1);
let house = new House('Gustavavagen 121', 7995, [person1, person2]);

console.log(house.addResident(person3.name));
console.log(house.getResidents());