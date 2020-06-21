import React, { useState } from "react";

const initialState = {
  firstName: "",
  lastName: "",
  biography: "",
  transport: "",
  agree: false,
  breakfast: false,
  lunch: false,
  dinner: false,
};

const Form = () => {
  const [formState, setFormState] = useState(initialState);

  const onChangeHandler = (e) => {
    const value =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setFormState({ ...formState, [e.target.name]: value });
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
      <label htmlFor="biography">Biography:</label>
      <textarea
        id="biography"
        name="biography"
        onChange={onChangeHandler}
        value={formState.biography}
        rows="10"
      />
      <label htmlFor="transport">Preferred Transport:</label>
      <select
        id="transport"
        name="transport"
        onChange={onChangeHandler}
        value={formState.transport}
      >
        <option>---Select---</option>
        <option value="planes">Planes</option>
        <option value="trains">Trains</option>
        <option value="cars">Cars</option>
        <option value="boats">Boats</option>
      </select>
      <fieldset>
        <legend>Select your meals</legend>
        <input
          type="checkbox"
          id="breakfast"
          name="breakfast"
          onChange={onChangeHandler}
          checked={formState.breakfast}
        />
        <label htmlFor="breakfast">Breakfast</label>
        <input
          type="checkbox"
          id="lunch"
          name="lunch"
          onChange={onChangeHandler}
          checked={formState.lunch}
        />
        <label htmlFor="lunch">Lunch</label>
        <input
          type="checkbox"
          id="dinner"
          name="dinner"
          onChange={onChangeHandler}
          checked={formState.dinner}
        />
        <label htmlFor="dinner">Dinner</label>
      </fieldset>
      <label htmlFor="agree">Agree?</label>
      <input
        type="checkbox"
        id="agree"
        name="agree"
        onChange={onChangeHandler}
        checked={formState.agree}
      />
      <button type="submit">Save</button>
      <button type="button" onClick={onClickHandler}>
        Clear
      </button>
    </form>
  );
};

export default Form;
