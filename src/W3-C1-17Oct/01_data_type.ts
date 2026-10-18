const hostpitalName: string = "City Hospital";
const totalBeds: number = 500;
const isMultiSpeciality: boolean = true;
const isEmergency: boolean = false;

let age: number = 45;
//bigint should end with samll n or use BigInt()
let balanceAmount: bigint = 1000000000000000000n;
let balanceAmount1: bigint = BigInt("1000000000000000000");


let patientName: null = null;
let doctorName: undefined = undefined;
let browserName: string | undefined = undefined;
let browser: "Chrome" | "Firefox" | "Safari" | "Edge";
let apiResponse: [number, string];

// 1. Concatenate the values
// Expected output format: "City Hospital has 500 beds and is a Multi Speciality hospital."
const result = hostpitalName + " has " + totalBeds + " beds and is a " + isMultiSpeciality + " hospital.";

// 2. Use console.log to display the output
console.log(hostpitalName);
console.log(totalBeds);
console.log(isMultiSpeciality);
console.log(isEmergency);
console.log(age);
console.log(balanceAmount);

console.log("String : " + typeof hostpitalName);
console.log("Number : " + typeof totalBeds);
console.log("Boolean : " + typeof isMultiSpeciality);
console.log("Boolean : " + typeof isEmergency);
console.log("Number : " + typeof age);

// age = "50"; 