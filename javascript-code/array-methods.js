const items = [
    {name:'Album', prices: 10},
    {name:'Bike', prices: 100},
    {name:'Book', prices: 5},
    {name:'Computer', prices: 1000},
    {name:'Keyboard', prices: 25},
    {name:'Phone', prices: 500},
    {name:'TV', prices: 200},
    {name:'Watch', prices: 60},    
]

const filteredItems = items.filter(
    (item) => {
        return item.prices <= 100;
    }
)

const itemNames = items.map(
    (item) => {
        return item.name;
    }
)

const foundItem = items.find(
    (item) => {
        return item.name === 'Book';
    }
)

console.log(filteredItems);
console.log(itemNames);
console.log(foundItem);

items.forEach(
    (item) => {
        console.log(item.name+'<>'+item.name);
    }
)

const hasInexpensiveItems = items.some(
    (item) => {
        return item.prices <= 100;
    }
)

console.log(hasInexpensiveItems)

const allInexpensiveItems = items.every(
    (item) => {
        return item.prices <= 100;
    }
)

console.log(allInexpensiveItems);

const total = items.reduce(
    (currentTotal, item) => {
        return item.prices + currentTotal;
    }, 0
)

console.log(total);

const integers = [1, 2, 3, 4, 5]
const includesTwo = integers.includes(2)
console.log(includesTwo);