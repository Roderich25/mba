import React, { useState, Fragment, useEffect } from "react";

const initialState = {
  firstName: "",
  lastName: "",
  biography: "",
  transport: "",
  agree: false,
  breakfast: false,
  lunch: false,
  dinner: false,
  shirtSize: "",
};

const loadState = {
  firstName: "Rodrigo",
  lastName: "Avila",
  biography: "I'm a developer",
  transport: "planes",
  agree: true,
  breakfast: false,
  lunch: true,
  dinner: false,
  shirtSize: "M",
};

const FormContainer = () => {
  const [data, setData] = useState(initialState);
  const onSubmitHandler = (formState) => {
    console.log(formState);
  };

  const onClickHandler = () => {
    setData(loadState);
  };

  return (
    <Fragment>
      <Form onSubmit={onSubmitHandler} data={data} />{" "}
      <button type="button" onClick={onClickHandler}>
        Load data
      </button>
    </Fragment>
  );
};

const Form = ({ onSubmit, data }) => {
  const [formState, setFormState] = useState(initialState);

  useEffect(() => {
    setFormState(data);
  }, [data]);

  const onChangeHandler = (e) => {
    const value =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setFormState({ ...formState, [e.target.name]: value });
  };

  const onClickHandler = () => {
    setFormState(loadState);
  };

  const onSubmitHandler = (e) => {
    e.preventDefault();
    onSubmit(formState);
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
      <fieldset>
        <legend>T-Shirt size</legend>
        <input
          type="radio"
          id="sizeS"
          name="shirtSize"
          value="S"
          onChange={onChangeHandler}
          checked={formState.shirtSize === "S"}
        />
        <label htmlFor="sizeS">Small</label>
        <input
          type="radio"
          id="sizeM"
          name="shirtSize"
          value="M"
          onChange={onChangeHandler}
          checked={formState.shirtSize === "M"}
        />
        <label htmlFor="sizeM">Medium</label>
        <input
          type="radio"
          id="sizeL"
          name="shirtSize"
          value="L"
          onChange={onChangeHandler}
          checked={formState.shirtSize === "L"}
        />
        <label htmlFor="sizeL">Large</label>
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
    </form>
  );
};

export default FormContainer;
