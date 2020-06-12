import React, { useState, useEffect } from "react";
import "./App.css";

function PostsUsersComments() {
  const [resource, setResource] = useState("posts");
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/${resource}`)
      .then((response) => response.json())
      .then((json) => setItems(json));
  }, [resource]);

  return (
    <div align="center">
      <div>
        <br />
        <button onClick={() => setResource("posts")}>Posts</button>
        <button onClick={() => setResource("users")}>Users</button>
        <button onClick={() => setResource("comments")}>Comments</button>
      </div>
      <h1>{resource}</h1>
      {items.map((item, index) => (
        <pre key={index}>{JSON.stringify(item)}</pre>
      ))}
    </div>
  );
}

export default PostsUsersComments;
