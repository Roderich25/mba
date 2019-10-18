const items = [
    {name:'Bike', price: 100},
    {name:'TV', price: 200},
    {name:'Album', price: 10},
    {name:'Book', price: 5},
    {name:'Phone', price: 500},
    {name:'Computer', price: 1000},
    {name:'Keyboard', price: 25},
    {name:'Watch', price: 60},    
]

const filteredItems = items.filter(
    (item) => {
        return item.price <= 100;
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
        return item.price <= 100;
    }
)

console.log(hasInexpensiveItems)

const allInexpensiveItems = items.every(
    (item) => {
        return item.price <= 100;
    }
)

console.log(allInexpensiveItems);

const total = items.reduce(
    (currentTotal, item) => {
        return item.price + currentTotal;
    }, 0
)

console.log(total);

const integers = [1, 2, 3, 4, 5]
const includesTwo = integers.includes(2)
console.log(includesTwo);