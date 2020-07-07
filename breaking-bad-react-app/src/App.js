import React, { useState, useEffect, useReducer } from "react";
import axios from "axios";
import Header from "./components/ui/Header";
import Search from "./components/ui/Search";
import CharacterGrid from "./components/characters/CharacterGrid";
import "./App.css";

export const MyContext = React.createContext();

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { count: state.count++ };
    case "decrement":
      return { count: state.count-- };
    default:
      return state;
  }
}

const App = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  const [items, setItems] = useState([]);
  const [theme, setTheme] = useState(true);
  const [isLoading, setIsLoading] = useState(true);
  const [query, setQuery] = useState("");

  const increment = () => {
    dispatch({ type: "increment" });
  };

  const decrement = () => {
    dispatch({ type: "decrement" });
  };

  useEffect(() => {
    const fetchItems = async () => {
      const result = await axios(
        `https://www.breakingbadapi.com/api/characters?name=${query}`
      );
      console.log(result.data);

      setItems(result.data);
      setIsLoading(false);
    };

    fetchItems();
  }, [query]);

  function toggleTheme() {
    setTheme((theme) => !theme);
    console.log(theme);
  }

  return (
    <React.Fragment>
      <button onClick={decrement}>-</button>
      <span>{state.count}</span>
      <button onClick={increment}>+</button>
      <div className="container">
        <MyContext.Provider value={theme}>
          <button onClick={toggleTheme}>Toggle</button>
          <Header />
          <Search getQuery={(q) => setQuery(q)} />
        </MyContext.Provider>
        <CharacterGrid isLoading={isLoading} items={items} />
      </div>
    </React.Fragment>
  );
};

export default App;
