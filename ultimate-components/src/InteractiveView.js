import React from "react";

const InteractiveView = ({ value, onAction, actionText }) => (
  <>
    <p>{value}</p>
    <button type="button" onClick={onAction}>
      {actionText}
    </button>
  </>
);

export default InteractiveView;
