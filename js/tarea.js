// Retorne un array con los números pares del 1 al n.tomados de un array
const numeros=[1,20,33,46,50,4,7,9,66,11,44]
let pares = [];
for(let i= 0;i<numeros.length;i++){
    if(i % 2 ==0){
        pares.push(numeros[i]);
    }

}
console.log("Los numeros pares son " + pares);