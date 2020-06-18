import React, { useState, useEffect } from "react";

import "./stopwatch.css";

const StopWatch = () => {
  const [time, setTime] = useState(0);
  const [counterActive, setCounterActive] = useState(true);

  useEffect(() => {
    let interval = null;

    if (counterActive) {
      interval = setInterval(() => {
        setTime((time) => time + 1);
      }, 1000);
    }

    return () => {
      clearInterval(interval);
    };
  }, [counterActive]);

  const onClickHandler = () => {
    setCounterActive((c) => !c);
  };

  const formattedTime = new Date(time * 1000).toISOString().substr(11, 8);

  return (
    <section className="stopwatch-frame">
      <h1>StopWatch</h1>
      <span>{formattedTime}</span>
      <button
        type="button"
        aria-pressed={!counterActive}
        onClick={onClickHandler}
      >
        Start/Stop
      </button>
    </section>
  );
};

export default StopWatch;
