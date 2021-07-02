function log(message) {
    console.log(message);
}
var message = 'Hello world';
log(message);
//Different types in typescript:
var count = 5; //type is number
// if you do not know the value of a variable ahead of time, thats when you use type annotation 
var a; // to specify that this declared variable must a  number
var b; // to specify that this declared variable must be boolean
var c; // to specify that this declared variable must be string
var d; // to specify that this declared variable can be any datatype
var e; // to specify that this declared variable must be an array of numbers
var f = [1, true, 'a', false]; // to specify that this declared variable can be an array of any datatype
//ENUM
var ColorRed = 0;
var ColorGreen = 1;
var ColorBlue = 2;
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var backgroundColor = Color.Red;
