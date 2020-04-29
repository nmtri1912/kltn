import React from 'react';
import './App.css';
import TextareaAutosize from 'react-textarea-autosize';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      output: '',
    };
  }
  render() {
    return (
      <>
        <form>
          <div className="col-xl-10 container">
            <div>
              <div className="text-center">
                <h1>Demo Mô Hình Dịch Máy Từ Tiếng Anh Sang Tiếng Việt</h1>
              </div>
            </div>
            <div className="row mt-5 text-center">
              <div className="col" style={{ fontSize: '28px' }}>
                Tiếng Anh
              </div>
              <div className="col" style={{ fontSize: '28px' }}>
                Tiếng Việt
              </div>
            </div>
            <div className="row mt-2 text-center">
              <div
                className="col"
                style={{ minHeight: '200px', height: 'auto' }}
              >
                <TextareaAutosize
                  style={{
                    minHeight: '100%',
                    minWidth: '100%',
                    height: 'auto',
                    resize: 'vertical',
                  }}
                  name="input"
                  placeholder="Enter text"
                  autoCapitalize="off"
                  autoComplete="off"
                  autoCorrect="off"
                  spellCheck="false"
                ></TextareaAutosize>
              </div>

              <div className="col" style={{ minHeight: '200px' }}>
                <TextareaAutosize
                  style={{ minHeight: '100%', minWidth: '100%' }}
                ></TextareaAutosize>
              </div>
            </div>
            <div className="text-center mt-3">
              <button type="submit" className="btn btn-secondary">
                Dịch
              </button>
            </div>
          </div>
        </form>
      </>
    );
  }
}

export default App;
