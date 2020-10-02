// This is how functions returning functions are done in JS

function greetingMaker(salutation) {
    function greeting(name) {
        return `${salutation}, ${name}`
    }
    return greeting;
}

let hello = greetingMaker('Hello');
console.log(hello('World')); // => 'Hello, World'
console.log(hello("Ari")) // => 'Hello, Ari'