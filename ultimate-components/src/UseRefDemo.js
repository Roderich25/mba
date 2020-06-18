import React, { useState, useEffect, useRef } from "react";

const UseRefDemo = () => {
  const [name, setName] = useState("");

  const previousName = useRef("");

  useEffect(() => {
    previousName.current = name;
  }, [name]);

  return (
    <>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <div>
        My name is {name} and it is used to be {previousName.current}
      </div>
    </>
  );
};

export default UseRefDemo;
