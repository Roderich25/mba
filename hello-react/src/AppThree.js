import React, { useState, useEffect } from "react";
import "./App.css";

function AppThree() {
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  const handleWindowResize = () => setWindowWidth(window.innerWidth);

  useEffect(() => window.addEventListener("resize", handleWindowResize), []);
  return (
    <div align="center">
      <h1>Window Width:{windowWidth}</h1>
    </div>
  );
}

export default AppThree;
