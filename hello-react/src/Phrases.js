import React, { useState, useEffect } from "react";
import "./App.css";

function Phrases() {
  const [val, setVal] = useState("");
  const [val2, setVal2] = useState("");

  useEffect(() => {
    console.log(`field 1: ${val}`);
  }, [val]);
  useEffect(() => {
    console.log(`field 2: ${val2}`);
  }, [val2]);

  return (
    <div align="center">
      <label>
        Favorite Phrase:{" "}
        <input value={val} onChange={(e) => setVal(e.target.value)} />
      </label>
      <br />
      <label>
        Second Favorite Phrase:{" "}
        <input value={val2} onChange={(e) => setVal2(e.target.value)} />
      </label>
    </div>
  );
}

export default Phrases;
