import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "./components/ui/Header";
import Search from "./components/ui/Search";
import CharacterGrid from "./components/characters/CharacterGrid";
import "./App.css";

export const MyContext = React.createContext();

const App = () => {
  const [items, setItems] = useState([]);
  const [theme, setTheme] = useState(true);
  const [isLoading, setIsLoading] = useState(true);
  const [query, setQuery] = useState("");

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
    <div className="container">
      <MyContext.Provider value={theme}>
        <button onClick={toggleTheme}>Toggle</button>
        <Header />
        <Search getQuery={(q) => setQuery(q)} />
      </MyContext.Provider>
      <CharacterGrid isLoading={isLoading} items={items} />
    </div>
  );
};

export default App;
