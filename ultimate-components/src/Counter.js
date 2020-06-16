import React, { useState } from "react";
import InteractiveView from "./InteractiveView";

const Counter = () => {
  const [count, setCount] = useState(0);

  const onClickHandler = () => {
    setCount((count) => count + 1);
  };

  return (
    <>
      <InteractiveView
        value={count}
        onAction={onClickHandler}
        actionText="Increment"
      />
    </>
  );
};

export default Counter;
