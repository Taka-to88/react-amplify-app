import "./App.css";
import ApiFetch from "./components/ApiFetch";
import logo from "./logo.svg";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ApiFetch />
      </header>
    </div>
  );
}

export default App;
