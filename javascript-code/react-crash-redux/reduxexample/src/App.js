import React from "react";
//import logo from "./logo.svg";
import "./App.css";
import { Provider } from "react-redux";
import store from "./store";
import Posts from "./components/Posts";
import PostForm from "./components/PostForm";
import "materialize-css";
import "materialize-css/dist/css/materialize.min.css";

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <PostForm />
        <Posts />
      </div>
    </Provider>
  );
}

export default App;
