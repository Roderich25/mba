import React, { useState, useEffect } from "react";
import "./App.css";

function initialCount() {
  //console.log("Running once");
  return 0;
}

function App() {
  const [count, setCount] = useState(() => initialCount());
  const [team, setTeam] = useState(() => "");
  const [temp, setTemp] = useState("");

  function decrementCount() {
    setCount((previous) => previous - 1);
    setCount((previous) => previous - 1);
  }
  function incrementCount() {
    setCount((previous) => previous + 1);
    setCount((previous) => previous + 1);
  }

  function handleChange(e) {
    setTemp(e.target.value);
  }

  function handleClick() {
    setTeam((previous) => {
      if (previous === temp) {
        return previous;
      } else {
        setCount(0);
        return temp;
      }
    });
  }

  useEffect(() => console.log("Count or team changed"), [team, count]);

  return (
    <div align="center">
      <div>
        <h1>Team: {team}</h1>
        <input type="text" id="team-choice" onChange={handleChange} />
        <button onClick={handleClick}>Add team</button>
      </div>
      <button onClick={decrementCount}>-</button>
      <span>{count}</span>
      <button onClick={incrementCount}>+</button>
    </div>
  );
}

export default App;
