import React, { useContext } from "react";
import logo from "../../img/logo.png";
import { MyContext } from "../../App";

const Header = () => {
  const theme = useContext(MyContext);

  const hs = theme ? "center" : "left";
  return (
    <header className={hs}>
      <img src={logo} alt="" />
    </header>
  );
};

export default Header;
