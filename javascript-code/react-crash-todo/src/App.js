import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import Todos from "./components/Todos";
import Header from "./components/layout/Header";
import AddToDo from "./components/AddToDo";
import About from "./components/pages/About";
//import uuid from "uuid";
import axios from "axios";

class App extends Component {
  state = {
    todos: []
  };

  componentDidMount(){
    axios.get('https://jsonplaceholder.typicode.com/todos?_limit=5')
    .then(res => this.setState({todos: res.data.map(todo => {todo.completed=false; return todo;}) }) );
    

  }

  //Toggle Complete
  markComplete = id => {
    this.setState({
      todos: this.state.todos.map(todo => {
        if (todo.id === id) {
          todo.completed = !todo.completed;
        }
        return todo;
      })
    });
  };

  //Delete
  deleteToDo = id => {

    axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
    .then(res => this.setState({todos: [...this.state.todos.filter(todo => todo.id !== id)]}) );
  };

  addToDo = title => {
    /*
    const newToDo = {
      id: uuid.v4(),
      title,
      completed: false
    };
    */
   axios.post('https://jsonplaceholder.typicode.com/todos', {title, completed: false})
   .then(res => this.setState({ todos: [...this.state.todos, res.data] }) )

  };

  render() {
    //console.log(this.state.todos);
    return (
      <Router>
        <div className="App">
          <div className="container">
            <Header />
            <Route
              exact
              path="/"
              render={props => (
                <React.Fragment>
                  <AddToDo addToDo={this.addToDo} />
                  <Todos
                    todos={this.state.todos}
                    markComplete={this.markComplete}
                    deleteToDo={this.deleteToDo}
                  />
                </React.Fragment>
              )}
            />
            <Route path="/about" component={About} />
          </div>
        </div>
      </Router>
    );
  }
}

export default App;
