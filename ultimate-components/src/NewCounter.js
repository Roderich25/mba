import React, { useState, useEffect } from "react";

const subscribe = (c) => {
  console.log(`Suscribed for ${c}.`);
};

const unsubscribe = (c) => {
  console.log(`Unsuscribed for ${c}.`);
};

const NewCounter = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count is ${count}|React`;
    console.log("Title Set");
  }, [count]);

  useEffect(() => {
    subscribe(count);

    return () => {
      unsubscribe(count);
    };
  }, [count]);

  const onClickHandler = () => {
    setCount((c) => c + 1);
  };

  console.log("MAIN Rendered");
  return (
    <div align="center">
      <h1>Counter</h1>
      <p>{count}</p>
      <button onClick={onClickHandler} type="button">
        Increment
      </button>
    </div>
  );
};

export default NewCounter;
