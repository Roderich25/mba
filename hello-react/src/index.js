import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import PostsUsersComments from "./PostsUsersComments";
import WindowWidth from "./WindowWidth";
import Phrases from "./Phrases.js";
import Github from "./Github.js";

ReactDOM.render(<App />, document.getElementById("root"));
ReactDOM.render(
  <PostsUsersComments />,
  document.getElementById("posts-users-comments")
);
ReactDOM.render(<WindowWidth />, document.getElementById("window-width"));
ReactDOM.render(<Phrases />, document.getElementById("phrases"));
ReactDOM.render(
  <Github user="roderich25" />,
  document.getElementById("github")
);
