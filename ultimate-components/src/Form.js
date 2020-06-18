import React, { useState } from "react";

const initialState = { firstName: "", lastName: "" };

const Form = () => {
  const [formState, setFormState] = useState(initialState);

  const onChangeHandler = (e) => {
    setFormState({ ...formState, [e.target.name]: e.target.value });
  };

  const onSubmitHandler = (e) => {
    e.preventDefault();
    console.log(formState);
  };

  const onClickHandler = () => {
    setFormState(initialState);
  };

  return (
    <form onSubmit={onSubmitHandler}>
      <br />
      <label htmlFor="firstName">First name:</label>
      <input
        id="firstName"
        name="firstName"
        onChange={onChangeHandler}
        value={formState.firstName}
      />
      <label htmlFor="lastName">Last name:</label>
      <input
        id="lastName"
        name="lastName"
        onChange={onChangeHandler}
        value={formState.lastName}
      />
      <button type="submit">Save</button>
      <button type="button" onClick={onClickHandler}>
        Clear
      </button>
    </form>
  );
};

export default Form;
