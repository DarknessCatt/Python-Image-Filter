import React from 'react';
import logo from './logo.svg';
import './App.css';

class Image extends React.Component{
  constructor(props) {
    super(props);
    this.state = {error: false, url: props.url};

    this.handleError = this.handleError.bind(this);
  }

  handleError(event){
    this.setState({error: true});
  }

  render(){

    if(!this.state.error){
      return(
        <img onError={this.handleError} src={this.state.url} className="App-logo" alt="Image"/>
      )
    }

    return(
      "Error!"
    )

  }
}

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {url: '', blur: 0};

    this.handleURL = this.handleURL.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleURL(event) {
    this.setState({url: event.target.value});
    if(this.state.url != ''){}
  }

  handleBlur(event) {
    this.setState({blur: event.target.value});
  }

  handleSubmit(event) {
    alert('URL: ' + this.state.url + '\nBlur: ' + this.state.blur);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
          {this.state.url != '' &&
            <Image key={this.state.url} url={this.state.url}/>
          }
          <br/>
          Image URL: <space/>
        <label>
          <input type="text" value={this.state.url} onChange={this.handleURL} size="70"/>
        </label>
        <br/>
        <label>
          Blurriness: <space/>
          <input type="number" value={this.state.blur} onChange={this.handleBlur} style={{width: "4em"}}/>
        </label>
        <br/>
        <input type="submit" value="Filter!" />
      </form>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Form />
      </header>
    </div>
  );
}

export default App;
