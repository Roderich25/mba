import React, { useState, Fragment } from "react";

const sourceObj = {
  id1: "Value1",
  id2: "Value2",
  id3: "Value3",
  id4: "Value4",
  id5: "Value5",
};
const UltimateHolidayList = () => {
  return (
    <section>
      <h1>Holiday Destinations</h1>
      <ol>
        {Object.keys(sourceObj).map((k) => (
          <li key={k}>{sourceObj[k]}</li>
        ))}
      </ol>
    </section>
  );
};

export default UltimateHolidayList;
