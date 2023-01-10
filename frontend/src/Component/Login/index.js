import React, { useState } from "react";
import Typography from '@mui/material/Typography';
import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import { Box } from "@mui/system";


function LoginForm(){
    // const history = useHistory();

    const [Username, setEmail] = useState('');
    const [Password, setPassword] = useState('');

  // State for the error message
    const [error, setError] = useState('');
    
  // Function to handle the login form submission
    const handleSubmit = async (e) => {
        e.preventDefault();

    // Send a POST request to the login route with the email and password
    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ Username, Password })
    });

    // Get the JSON data from the response
    const data = await response.json(); debugger

    // If there is an error, display it
        if (data.error) {
          setError(data.error);
        }

    // If there is a token, store it in the browser's local storage and redirect to the dashboard
        else if (data.access_token) { debugger
            localStorage.setItem('token', data.access_token);
            // window.location.href = '/dashboard';
            window.location.replace("dashboard");                    
        // console.log(data)
        }
    };

    return (
        <Box align="center" sx={{width: 300,
            height: 300,
            backgroundColor: 'primary.dark',
            '&:hover': {
            backgroundColor: 'primary.main',
            opacity: [0.9, 0.8, 0.7]
            },
        }}
        >
            <Typography variant="h6" component="h6">
               Login
            </Typography>
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Username"
                    type="text"
                    name="Username"
                    value={Username}
                    onChange={(e) => setEmail(e.target.value)}
                    margin="normal"
                />
                <TextField
                    label="Password"
                    type="password"
                    name="password"
                    value={Password}
                    onChange={(e) => setPassword(e.target.value)}
                    margin="normal"
                />
                {error && <p>{error}</p>}
                <Button type="submit" variant="contained" color="primary">
                    Log In
                </Button>
            </form>
        </Box>
    );
}

export default LoginForm;
