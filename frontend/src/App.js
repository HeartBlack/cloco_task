import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import PrivateRoutes from './utils/privateroute'
import Dashboard from './pages/dashboard';
import Login from './pages/login';
import NotFound from './pages/404';
import Home from './pages/home';
import Signup from './pages/signup';
import CreateNewSong from './components/create_song';

function App() {

  return (
    <div className="App">
      <Router>
          <Routes>
            <Route element={<PrivateRoutes />}>
                <Route element={<Dashboard/>} path="/dashboard" />
                <Route element={<CreateNewSong/>} path="/create/new/song" />

            </Route>
            <Route element={<Login/>} path="/login"/>
            <Route element={<Signup/>} path="/signup"/>
            <Route element={<Home/>} path="/" exact/>
            <Route path='*' element={<NotFound/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
