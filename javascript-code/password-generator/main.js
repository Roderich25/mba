
const resultEl = document.getElementById('result');
const lengthEl = document.getElementById('length');
const uppercaseEl = document.getElementById('uppercase');
const lowercaseEl = document.getElementById('lowercase');
const numbersEl = document.getElementById('numbers');
const symbolsEl = document.getElementById('symbols');
const generateEl = document.getElementById('generate');
const clipboardEl = document.getElementById('clipboard');

const randomFunc = {
    lower: getRandomLower,
    upper: getRandomUpper,
    number: getRandomNumber,
    symbol: getRandomSymbol
};

//copy password to clipboard
clipboardEl.addEventListener('click', () => {
    const textArea = document.createElement('textArea');
    const password = resultEl.innerText;

    if(!password){
        return;
    }
    
    textArea.value = password;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    textArea.remove();
    alert('Password copied to clipboard!');
});

//generate event listener
generateEl.addEventListener('click', () => {
   const length = +lengthEl.value;
   const hasLower = lowercaseEl.checked;
   const hasUpper = uppercaseEl.checked;
   const hasNumber = numbersEl.checked;
   const hasSymbol = symbolsEl.checked;
   resultEl.innerHTML=generatePassword(length, hasLower, hasUpper, hasNumber, hasSymbol);

});

//generate password function
function generatePassword(len, lower, upper, number, symbol){
    let pwd = '';
    const typesCount = lower + upper + number + symbol;
    const typesArray = [{lower}, {upper}, {number}, {symbol}]
                        .filter(item => Object.values(item)[0]);
    if(typesCount===0){
        return '';
    }
    for(let i = 0; i<len; i += typesCount){
        typesArray.forEach(type => {
            const funcName = Object.keys(type)[0];
            pwd += randomFunc[funcName]();
        });
    }

    return randomSort(pwd).slice(0,len);

}

//generator functions

function randomSort(string){
    let temp = '';
    let length = string.length;
    for(let i=0; i<length; i++){
        
        temp += string[Math.floor(Math.random()*length)];
    }
    return temp;
}


function getRandomLower(){
    randomNumber = Math.floor(Math.random() * 26) + 97;
    return String.fromCharCode(randomNumber);
};

function getRandomUpper(){
    randomNumber = Math.floor(Math.random() * 26) + 65;
    return String.fromCharCode(randomNumber);
};

function getRandomNumber(){
    randomNumber = Math.floor(Math.random() * 10) + 48;
    return String.fromCharCode(randomNumber);
};

function getRandomSymbol(){
    const symbols = '!"#$%&/()[]{},.-_@*';
    randomNumber = Math.floor(Math.random()*symbols.length);
    return symbols[randomNumber];
};