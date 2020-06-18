import React from "react";

const InteractiveView = ({ value, onAction, actionText, title }) => (
  <>
    <h1>{title}</h1>
    <p>{value}</p>
    <button type="button" onClick={onAction}>
      {actionText}
    </button>
  </>
);

export default InteractiveView;
