function log(message){
    console.log(message)
}

let message = 'Hello world'

log(message)


//Different types in typescript:

let count = 5; //type is number

// if you do not know the value of a variable ahead of time, thats when you use type annotation 
let a: number ; // to specify that this declared variable must a  number
let b : boolean;// to specify that this declared variable must be boolean
let c : string;// to specify that this declared variable must be string
let d: any; // to specify that this declared variable can be any datatype
let e: number[]; // to specify that this declared variable must be an array of numbers
let f: any[]= [1,true,'a', false] // to specify that this declared variable can be an array of any datatype

//ENUM
const ColorRed = 0
const ColorGreen = 1
const ColorBlue = 2

enum Color {Red = 0, Green = 1, Blue = 2};
let backgroundColor = Color.Red

// Type assertions.
let msg;
msg = 'abc'
let endWithC = (<string>msg).endsWith('c') //One way to create assertions
let alternativeWay = (msg as string).endsWith('c') // Another way to create assortions


interface Point{
    x:number,
    y: number
}

let drawpoint = (point : Point)=>{
    // ...
}
