const companies = [
  {name: "Company One", category: "Finance", start: 1981, end: 2003},
  {name: "Company Two", category: "Retail", start: 1992, end: 2008},
  {name: "Company Three", category: "Auto", start: 1999, end: 2007},
  {name: "Company Four", category: "Retail", start: 1989, end: 2010},
  {name: "Company Five", category: "Technology", start: 2009, end: 2014},
  {name: "Company Six", category: "Finance", start: 1987, end: 2010},
  {name: "Company Seven", category: "Auto", start: 1986, end: 1996},
  {name: "Company Eight", category: "Technology", start: 2011, end: 2016},
  {name: "Company Nine", category: "Retail", start: 1981, end: 1989}
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

for(let i = 0; i < companies.length; i++){
    //console.log(companies[i]);
}

//forEach
companies.forEach(function(company) {
    //console.log(company.name);
})

//filter
let canDrink = [];
for(let i = 0; i < ages.length; i++){
    if(ages[i]>=21){
        canDrink.push(ages[i]);
    }
}
//console.log(canDrink);
//console.log( ages.filter( function(age){ if(age>=21){ return true; } } ) );
//console.log( ages.filter(age => age>=21) );
//console.log( companies.filter(companies => companies.category==='Retail') );

//map
//console.log( companies.map((company)=> { return company.name}) );
//console.log( companies.map((company,idx) => `${idx+1}.- ${company.name} Inc.`) );
//console.log( ages.map(age => Math.sqrt(age)).map(age => age*2.5) );

//sort
//console.log( companies.sort(function(c1, c2){ return c1.start>c2.start ? -1 : 1;  }) );
//console.log(ages.sort( (a, b) => b-a ));

//reduce
let ageSum = 0;
for(let i=0; i<ages.length; i++){
    ageSum += ages[i];
}
//console.log(ageSum);
//console.log( ages.reduce( (total, age) => total+age, 40) );
//console.log( companies.reduce( (total, company) => total + (company.end-company.start) ,0) );

//filter map reduce
console.log( ages.filter(age => age>=21).map(age => age*12).reduce((total, age)=>total+age, 0) );