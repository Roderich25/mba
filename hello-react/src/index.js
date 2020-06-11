import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import AppTwo from "./AppTwo";
import AppThree from "./AppThree";

ReactDOM.render(<App />, document.getElementById("root2"));
ReactDOM.render(<AppTwo />, document.getElementById("root3"));
ReactDOM.render(<AppThree />, document.getElementById("root"));
