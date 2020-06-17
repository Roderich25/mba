import React, { useState, Fragment } from "react";

const list = [
  { id: 1, name: "The beach", top: true },
  { id: 2, name: "The mountains", top: false },
  { id: 3, name: "Old cities", top: true },
  { id: 4, name: "Boring city", top: false },
  { id: 5, name: "Carnival city", top: true },
];

const UltimateHolidayList = () => {
  const [showAll, setShowAll] = useState(true);

  return (
    <section>
      <h1>Holiday Destinations</h1>
      {list
        .filter((item) => (showAll ? true : item.top))
        .map((item, index) => (
          <li key={index}>{item.name}</li>
        ))}
      <button
        type="button"
        onClick={() => {
          setShowAll(true);
        }}
      >
        Show all
      </button>
      <button
        type="button"
        onClick={() => {
          setShowAll(false);
        }}
      >
        Show only top
      </button>
    </section>
  );
};

export default UltimateHolidayList;
