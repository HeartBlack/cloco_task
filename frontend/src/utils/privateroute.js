import axios from 'axios';
import { Outlet, Navigate } from 'react-router-dom';

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

async function PrivateRoutes() {
    const tokenData = await fetchToken();
    console.log("tokenData", tokenData)
    let auth = tokenData.token;
    console.log("auth", auth);

    return auth ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoutes;
