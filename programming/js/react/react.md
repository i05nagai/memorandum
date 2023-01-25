---
title: React
---

## React

## New app
https://reactjs.org/docs/create-a-new-react-app.html

- If you’re learning React or creating a new single-page app, use Create React App.
- If you’re building a server-rendered website with Node.js, try Next.js.
- If you’re building a static content-oriented website, try Gatsby.
- If you’re building a component library or integrating with an existing codebase, try More Flexible Toolchains.

## Properties

#### key
key is a special and reserved property in React (along with ref, a more advanced feature). When an element is created, React extracts the key property and stores the key directly on the returned element. Even though key may look like it belongs in props, key cannot be referenced using this.props.key. React automatically uses key to decide which components to update. A component cannot inquire about its key.

```
<li key={user.id}>{user.name}: {user.taskCount} tasks left</li>
```

It’s strongly recommended that you assign proper keys whenever you build dynamic lists.

#### ref

## Lifecycles

- `componentDidMount`
    - The method runs after the component output has been rendered to the DOM.
- `componentWillUnmount`
    - If the component is ever removed from the DOM, React calls the componentWillUnmount() lifecycle method

```
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
  }

  componentWillUnmount() {
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

## States
- State Updates May Be Asynchronous
    - React may batch multiple setState() calls into a single update for performance.

```
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});
// Correct
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

- State Updates are Merged
    - When you call setState(), React merges the object you provide into the current state.

## Events
- synthetic events
    - https://reactjs.org/docs/events.html

```
function Form() {
// e is synthetic event
// prevent default form behaviour of submitting
// https://www.w3.org/TR/DOM-Level-3-Events/
  function handleSubmit(e) {
    e.preventDefault();
    console.log('You clicked submit.');
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Submit</button>
    </form>
  );
}
```


- event handler
    - You have to be careful about the meaning of this in JSX callbacks. In JavaScript, class methods are not bound by default. If you forget to bind this.handleClick and pass it to onClick, this will be undefined when the function is actually called.

## Hook

#### useState

```

```


## API
- React.Component
    - https://reactjs.org/docs/react-component.html#constructor
    - `this.state`

## Reference
* [pinglinh/simple\_webpack\_boilerplate: 🕸📦Ever wondered how you could set up a React project from scratch? This is the repo for you\! I have also written up a blog tutorial to follow along\.](https://github.com/pinglinh/simple_webpack_boilerplate)
