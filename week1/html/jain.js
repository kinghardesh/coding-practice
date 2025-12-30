arr1=[1,2,3,4,5,6,7,8,9,10];
rev=[];
for (let i=0;i<arr1.length;i++){
    rev.push(arr1[i]);
}
console.log("reversed array is: ");
console.log(rev);
max=arr1[0];
for (let i=1;i<arr1.length;i++){
    if (arr1[i]>max){
        max=arr1[i];
    }
}
console.log("maximum number is: ");
console.log(max);
min=arr1[0];
for (let i=0;i<arr1.length;i++){
    arr1[i]<min){
        min=arr1[i];
    }   
}
console.log("minimum number is: ");
console.log(min);
for (let i=0;i<arr1.length;i++){
    let sum=0;
    sum+=arr1[i];
    console.log("sum is: ");
    console.log(sum);
}
for (let i=0;i<arr1.length;i++){
    if (arr1[i]%2==0){
        console.log("even number: ");
        console.log(arr1[i]);
    }
    else{
        console.log("odd number: ");
        console.log(arr1[i]);
    }
}
for (let i=0;i<arr1.length;i++){
    let square=arr1[i]*arr1[i];
    console.log("square is: ");
    console.log(square);
}
let multipleof3=arr1.filter(num => num%3==0);
console.log("multiple of 3 are: ");
console.log(multipleof3);
class Person{
    constructor(name,marks){
        this.name=name;
        this.marks=marks;
    }
}
const jain=new Person("A",80);
console.log(jain);
const raj=new Person("B",60);
console.log(raj);
const simran=new Person("C",90);
console.log(simran);

let students = [
  {name:"A", marks:80},
  {name:"B", marks:60},
  {name:"C", marks:90}
];
let top = students.reduce((a,b)=>a.marks>b.marks?a:b);
console.log(top.name);
console.log(top.marks);
