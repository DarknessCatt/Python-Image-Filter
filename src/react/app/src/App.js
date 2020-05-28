import React from 'react';
import NoImage from './Images/NoImage.png';
import ErrorImage from './Images/ErrorImage.png';
import './App.css';

const base_image_url = 'http://127.0.0.1:5000/image?'

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
        <img onError={this.handleError} src={this.state.url} className="App-logo" alt="File to be Filtered"/>
      )
    }

    return(
      <img src={ErrorImage} className="App-logo" alt="No file loaded from URL"/>
    )
  }
}

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {url: '', blur: 0, image: ''};

    this.handleURL = this.handleURL.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleURL(event) {
    this.setState({url: event.target.value});
  }

  handleBlur(event) {
    this.setState({blur: event.target.value});
  }

  handleSubmit(event) {
    this.setState({image: base_image_url + "url=" + this.state.url + "&radius=" + this.state.blur})
    event.preventDefault();
  }

  handleReset(event) {
    this.setState({url: '', blur: 0, image: ''})
    event.preventDefault();
  }

  render() {
    return (
      <>
      {this.state.image === ''
      ?
        <form onSubmit={this.handleSubmit}>
          {this.state.url === ''
            ? <img src={NoImage} className="App-logo" alt="No file loaded from URL"/>
            : <Image key={this.state.url} url={this.state.url}/>
          }
          <br/><br/>
          
          <label>
            Image URL: <space/>
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
      : 
        <form onSubmit={this.handleReset}>
          <Image url={this.state.image}/>
          <br/>
          <input type="submit" value="Filter a new image!" />
        </form>
      }
      </>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Blur an Image from URL! </h1>
        <Form />
      </header>
    </div>
  );
}

export default App;
