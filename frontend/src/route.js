import { BrowserRouter as Router, Route } from 'react-router-dom';
import Login from "./Component/Login";
import Dashboard from "./Component/dashboard";

function App() {
  return (
    <Router>
      <div>
        {/* Home route */}
        <Route exact path="/">
          <Login />
        </Route>

        {/* Dashboard route */}
        <Route path="/dashboard">
          <Dashboard />
        </Route>

        {/* Profile route */}
        {/* <Route path="/profile">
          <Profile />
        </Route> */}
      </div>
    </Router>
  );
}

export default App;