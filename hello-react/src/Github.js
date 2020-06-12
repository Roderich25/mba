import React, { useState, useEffect, useReducer } from "react";
import "./App.css";

function Checkbox() {
  const [checked, toggle] = useReducer((checked) => !checked, false);

  return (
    <>
      <input type="checkbox" value={checked} onChange={toggle} />
      {checked ? "Checked" : "Disabled"}
    </>
  );
}

function Github({ user }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`https://api.github.com/users/${user}`)
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  }, []);

  if (data) {
    return (
      <div align="center">
        <h4>Github/{data.login}</h4>
        <img src={data.avatar_url} width={100} alt="user avatar" />
        <br />
        <Checkbox />
      </div>
    );
  }
  return null;
}

export default Github;
