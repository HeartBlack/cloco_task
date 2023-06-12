import axios from 'axios';
import { Outlet, Navigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
export const setToken = (token) => {
    localStorage.setItem('access_token', token);
};

export const fetchToken = async () => {
    var authData = localStorage.getItem('access_token');
    console.log(authData)
    if (authData != null) {
        try {
            const response = await axios.post(
                'http://localhost:8000/api/v1/verify_user',
                {
                    token: authData,
                },
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                }
            );

            if (response.status === 200) {
                return { token: true };
            } else {
                return { token: false };
            }
        } catch (error) {
            return { token: false };
        }
    } else {
        localStorage.clear("access_token")
        return { token: false };
    }
};

function PrivateRoutes() {
    const [auth, setAuth] = useState(null);

    useEffect(() => {
        const fetchAuth = async () => {
            const tokenData = await fetchToken();
            setAuth(tokenData.token);
        };

        fetchAuth();
    }, []);

    console.log(auth);

    if (auth === null) {
        return null; // or render a loading state if desired
    }

    return auth ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoutes;
