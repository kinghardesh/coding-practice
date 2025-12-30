
class person{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
}
const john = new person("John", 30);
console.log(john);
console.log(john.name);
console.log(john.age);

const jane = new person("Jane", 25);
console.log(jane.name);
console.log(jane.age);




for (let i = 1; i < 11; i++) {
    console.log(i);
}   

for (let i = 10; i > 0; i--) {
    let sum = 0;
    sum += i;
    console.log(i);
}
for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        console.log("even number: ");
        console.log(i);
    }
    else {
        console.log("odd number: ");
        console.log(i);
    }
}
arr1=[1,2,3,4,5,6,7,8,9,10];
rev=[];
for (let i = arr1.length - 1; i >= 0; i--) {
    rev.push(arr1[i]);
}
arr2=[12,34,56,7,89,90,23,45,67];
let max=arr2[0];
for (let i = 1; i < arr2.length; i++) {
    if (arr2[i]>max){
        max=arr2[i];
    }
}
console.log("maximum number is: ");
console.log(max);

let square=arr1.map(num => num * num);
console.log("squared array is: ");
console.log(square);

let evenNumbers=arr1.filter(num => num %2==0);
console.log("even numbers are: ");
console.log(evenNumbers);
