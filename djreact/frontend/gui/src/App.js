import React from "react";
import "./App.css";
import "antd/dist/antd.css";
import CustomLayout from "./containers/Layout";

function App() {
  return (
    <div className="App">
      <CustomLayout>Content</CustomLayout>
    </div>
  );
}

export default App;
