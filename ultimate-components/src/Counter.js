import React, { useState, useEffect } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count is ${count}|React`;
    console.log("Title Set");
  }, [count]);

  useEffect(() => {
    const savedCounterValue = localStorage.getItem("counter");
    if (savedCounterValue != null) {
      setCount(parseInt(savedCounterValue, 10));
    }
  }, []);

  const onCountClickHandler = () => {
    setCount((c) => c + 1);
  };

  const onSaveClickHandler = () => {
    localStorage.setItem("counter", count);
  };

  console.log("MAIN Rendered");
  return (
    <div align="center">
      <h1>Counter</h1>
      <p>{count}</p>
      <button onClick={onCountClickHandler} type="button">
        Increment
      </button>
      <button onClick={onSaveClickHandler} type="button">
        Local Storage
      </button>
    </div>
  );
};

export default Counter;
