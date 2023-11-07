import logo from './logo.png';
import './App.css';
import SearchForm from './SearchForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className='inner-header desktop-width'>
          <a href="#"><img src={logo} /></a>
        </div>
      </header>
      <main className='desktop-width landing-page-hero'>
        <section>
          <h1>Why browse endlessly for your car</h1>
          <p className='hero-subheadline'>Experience a smarter way to find your next car. By prioritizing your preferences and budget, our platform does the searching for you, ensuring you're only presented with options that truly resonate.</p>
        </section>
        <section className='form-column'>
          <SearchForm />
        </section>
      </main>
    </div>
  );
}

export default App;
