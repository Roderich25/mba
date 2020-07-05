import React, { useState, useContext } from "react";
import { MyContext } from "../../App";

const Search = ({ getQuery }) => {
  const theme = useContext(MyContext);
  const placeholder = theme ? "SEARCH CHARACTERS" : "Search Characters";
  const [text, setText] = useState("");
  const onChange = (q) => {
    setText(q);
    getQuery(q);
  };

  return (
    <section className="search">
      <form>
        <input
          type="text"
          className="form-control"
          placeholder={placeholder}
          value={text}
          onChange={(e) => onChange(e.target.value)}
          autoFocus
        />
      </form>
    </section>
  );
};

export default Search;
